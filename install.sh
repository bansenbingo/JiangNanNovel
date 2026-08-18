#!/usr/bin/env bash

set -eu

INSTALLER_VERSION="1.3.0"
SKILL_NAME="JiangNanNovel"
SKILL_SUBDIR="skills"
DEFAULT_REPO_URL="https://github.com/bansenbingo/JiangNanNovel.git"
REPO_URL="${JIANGNANNOVEL_REPO_URL:-$DEFAULT_REPO_URL}"
MARKER_FILE=".jiangnannovel-revision"

usage() {
  cat <<'EOF'
Install or update the complete JiangNanNovel skill bundle for a local agent CLI.

Usage:
  install.sh [--agent AGENT]
  install.sh --list
  install.sh --version

Options:
  --agent AGENT  Install for codex, claude, gemini, opencode, cursor, or copilot.
  --list         List compatible agent CLIs found on PATH.
  --version      Print the installer version.
  -h, --help     Show this help.

Without --agent, the script scans PATH and prompts when multiple agents exist.
Run the same command again to check for and install bundle updates.
EOF
}

die() {
  printf 'Error: %s\n' "$*" >&2
  exit 1
}

command_exists() {
  command -v "$1" >/dev/null 2>&1
}

AGENT_IDS=()
AGENT_LABELS=()
AGENT_ROOTS=()

add_agent() {
  if command_exists "$2"; then
    AGENT_IDS+=("$1")
    AGENT_LABELS+=("$3")
    AGENT_ROOTS+=("$4")
  fi
}

scan_agents() {
  add_agent "codex" "codex" "Codex" "$HOME/.agents/skills"
  add_agent "claude" "claude" "Claude Code" "$HOME/.claude/skills"
  add_agent "gemini" "gemini" "Gemini CLI" "$HOME/.gemini/skills"
  add_agent "opencode" "opencode" "OpenCode" "$HOME/.config/opencode/skills"
  add_agent "cursor" "cursor-agent" "Cursor Agent" "$HOME/.cursor/skills"
  add_agent "copilot" "copilot" "GitHub Copilot CLI" "$HOME/.copilot/skills"
}

list_agents() {
  if [ "${#AGENT_IDS[@]}" -eq 0 ]; then
    printf 'No compatible agent CLI was found on PATH.\n'
    return
  fi

  printf 'Compatible agent CLIs found on PATH:\n'
  local i
  for ((i = 0; i < ${#AGENT_IDS[@]}; i++)); do
    printf '  %d. %-20s %s\n' "$((i + 1))" "${AGENT_LABELS[$i]}" "${AGENT_ROOTS[$i]}"
  done
}

select_agent() {
  local requested="$1"
  local i choice

  [ "${#AGENT_IDS[@]}" -gt 0 ] || die "No compatible agent CLI was found on PATH."

  if [ -n "$requested" ]; then
    for ((i = 0; i < ${#AGENT_IDS[@]}; i++)); do
      if [ "${AGENT_IDS[$i]}" = "$requested" ]; then
        SELECTED_INDEX="$i"
        return
      fi
    done
    die "Agent '$requested' is not installed or is not on PATH. Run with --list to inspect detected agents."
  fi

  if [ "${#AGENT_IDS[@]}" -eq 1 ]; then
    SELECTED_INDEX=0
    return
  fi

  list_agents
  printf 'Select an agent [1-%d]: ' "${#AGENT_IDS[@]}" >/dev/tty
  IFS= read -r choice </dev/tty || die "Unable to read a selection. Use --agent AGENT instead."
  case "$choice" in
    ''|*[!0-9]*) die "Invalid selection: $choice" ;;
  esac
  [ "$choice" -ge 1 ] && [ "$choice" -le "${#AGENT_IDS[@]}" ] || die "Selection is out of range."
  SELECTED_INDEX="$((choice - 1))"
}

same_tree() {
  local source_dir="$1"
  local target_dir="$2"
  local source_list="$TMP_DIR/source-files"
  local target_list="$TMP_DIR/target-files"
  local relative

  [ -d "$target_dir" ] || return 1
  (cd "$source_dir" && find . -type f ! -name "$MARKER_FILE" -print | LC_ALL=C sort) >"$source_list"
  (cd "$target_dir" && find . -type f ! -name "$MARKER_FILE" -print | LC_ALL=C sort) >"$target_list"
  cmp -s "$source_list" "$target_list" || return 1

  while IFS= read -r relative; do
    cmp -s "$source_dir/$relative" "$target_dir/$relative" || return 1
  done <"$source_list"
}

install_skill() {
  local source_dir="$1"
  local revision="$2"
  local skills_root="$3"
  local destination="$skills_root/$SKILL_NAME"
  local stage="$skills_root/.$SKILL_NAME.stage.$$"
  local backup="$skills_root/.$SKILL_NAME.backup.$$"

  mkdir -p "$skills_root"
  [ ! -e "$stage" ] || die "Temporary path already exists: $stage"
  [ ! -e "$backup" ] || die "Temporary path already exists: $backup"

  if same_tree "$source_dir" "$destination"; then
    printf '%s\n' "$revision" >"$destination/$MARKER_FILE"
    printf '%s is already up to date in %s\n' "$SKILL_NAME" "$destination"
    return
  fi

  cp -R "$source_dir" "$stage"
  printf '%s\n' "$revision" >"$stage/$MARKER_FILE"

  if [ ! -e "$destination" ]; then
    mv "$stage" "$destination"
    printf '%s installed for %s at %s\n' "$SKILL_NAME" "${AGENT_LABELS[$SELECTED_INDEX]}" "$destination"
    return
  fi

  mv "$destination" "$backup"
  if mv "$stage" "$destination"; then
    rm -rf "$backup"
    printf '%s updated for %s at %s\n' "$SKILL_NAME" "${AGENT_LABELS[$SELECTED_INDEX]}" "$destination"
  else
    mv "$backup" "$destination"
    die "Update failed; the previous installation was restored."
  fi
}

REQUESTED_AGENT="${JIANGNANNOVEL_AGENT:-}"
LIST_ONLY=0

while [ "$#" -gt 0 ]; do
  case "$1" in
    --agent)
      [ "$#" -ge 2 ] || die "--agent requires a value."
      REQUESTED_AGENT="$2"
      shift 2
      ;;
    --list)
      LIST_ONLY=1
      shift
      ;;
    --version)
      printf '%s\n' "$INSTALLER_VERSION"
      exit 0
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      die "Unknown option: $1"
      ;;
  esac
done

scan_agents
if [ "$LIST_ONLY" -eq 1 ]; then
  list_agents
  exit 0
fi

select_agent "$REQUESTED_AGENT"
command_exists git || die "Git 2.25 or newer is required."

TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/jiangnannovel.XXXXXX")"
trap 'rm -rf "$TMP_DIR"' EXIT HUP INT TERM

printf 'Checking the latest %s skill bundle...\n' "$SKILL_NAME"
git clone --quiet --depth 1 --filter=blob:none --sparse "$REPO_URL" "$TMP_DIR/repo" || die "Unable to clone $REPO_URL"
git -C "$TMP_DIR/repo" sparse-checkout set "$SKILL_SUBDIR" || die "Unable to fetch $SKILL_SUBDIR"

SOURCE_DIR="$TMP_DIR/repo/$SKILL_SUBDIR"
[ -f "$SOURCE_DIR/SKILL.md" ] || die "The downloaded bundle does not contain its root SKILL.md."
[ -f "$SOURCE_DIR/novel-source-compressor/SKILL.md" ] || die "The downloaded bundle does not contain the source compressor Skill."
[ -f "$SOURCE_DIR/novel-continuation-outline/SKILL.md" ] || die "The downloaded bundle does not contain the outline planning Skill."
[ -f "$SOURCE_DIR/JiangNanNovel/SKILL.md" ] || die "The downloaded bundle does not contain the author Skill."
[ -f "$SOURCE_DIR/characters/lu_mingfei/SKILL.md" ] || die "The downloaded bundle does not contain its character Skills."
REVISION="$(git -C "$TMP_DIR/repo" rev-parse HEAD)"

install_skill "$SOURCE_DIR" "$REVISION" "${AGENT_ROOTS[$SELECTED_INDEX]}"
printf 'Restart %s if the skill is not immediately visible.\n' "${AGENT_LABELS[$SELECTED_INDEX]}"
