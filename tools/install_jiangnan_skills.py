#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""江南写作技能安装器（项目级，内容不落本地项目，跨平台）

从远程仓库拉取江南写作技能（.claude/skills/ 中的 4 个人格），
以符号链接方式安装到指定项目，供 Claude Code / opencode / codex 使用。

设计原则：
- 项目隔离：只在运行脚本时指定的项目内激活，其他项目不受影响
- 内容不入库：技能实体只存在于系统缓存（从远程拉取），项目内只有链接
- 关闭即停用：卸载（--uninstall）或删除链接后，Agent 不再加载该技能
- 开箱即用：双击（无参数运行）进入交互模式，自动检测 Agent CLI，
  本机无任何 Agent 时优先自动安装 opencode；Windows 无 git 时自动改用 ZIP 下载

用法示例：
    install_jiangnan_skills.py                      # 交互模式（Windows 双击 / macOS 双击）
    install_jiangnan_skills.py --project ~/novels   # 安装到指定项目
    install_jiangnan_skills.py --uninstall          # 卸载
    install_jiangnan_skills.py --list               # 查看技能清单
    install_jiangnan_skills.py --repo ./            # 指定来源（本地仓库或 URL）
"""

import argparse
import io
import os
import re
import shutil
import subprocess
import sys
import urllib.request
import zipfile

SKILLS = [
    "author-jiang-nan-master",       # 总人格：自动识别世界观（龙族/九州/天之炽），首选
    "author-jiang-nan",              # 九州缥缈录专项
    "author-jiang-nan-longzu",       # 龙族专项
    "author-jiang-nan-tianzhichi",   # 天之炽专项
]

AGENTS = ["claude", "codex", "opencode"]

DEFAULT_REPO = "https://github.com/bansenbingo/JiangNanNovel.git"
DEFAULT_BRANCH = "main"
SKILL_SOURCE_DIR = ".claude/skills"

# 各 Agent 的项目级技能目录：(相对项目路径, 说明)
PROJECT_TARGETS = [
    (".claude/skills", "Claude Code / opencode"),
    (".codex/skills", "codex"),
]

GITIGNORE_LINES = [
    "# 江南写作技能（install_jiangnan_skills.py 自动管理，删除此行以下两行即可清理）",
    ".claude/skills/",
    ".codex/skills/",
]

BANNER = r"""
   ____  _                      ____         _   _  ____
  / __ \\(_)_  __ ___ _ __      / ___| __ _ _(_)_(_)/ ___|  _ __ __ _
 / / _` | \\ \\/ / _ \\ '_ \\ ____| |  _ / _` |_ _| \\___ \\ | '_ \\ / _` |
| | (_| | |>  <  __/ | | |_____| |_| | (_| | | |  |___) || | | | (_| |
 \\ \\__,_|_/_/\\_\\___|_| |_|      \\____|\\__,_|___|_|____/ |_| |_|\\__, |
  \\____/                                                        |___/
"""


# ---------- 基础工具 ----------


def cache_root() -> str:
    """技能缓存根目录（实体内容只存在这里，不写入项目）。"""
    if os.name == "nt":
        base = os.environ.get("LOCALAPPDATA") or os.path.expanduser("~\\AppData\\Local")
        return os.path.join(base, "JiangNanSkills")
    if sys.platform == "darwin":
        return os.path.expanduser("~/Library/Caches/JiangNanSkills")
    base = os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache")
    return os.path.join(base, "JiangNanSkills")


def repo_dir() -> str:
    return os.path.join(cache_root(), "repo")


def run_git(args: list, cwd: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def _is_junction(path: str) -> bool:
    """Windows 目录联接（junction）检测，Python 3.12+ 原生支持。"""
    f = getattr(os.path, "isjunction", None)
    return bool(f and f(path))


def link_target(path: str) -> str | None:
    """读取符号链接/联接的目标路径（规范化），非链接返回 None。"""
    if os.path.islink(path) or _is_junction(path):
        try:
            target = os.readlink(path)
        except OSError:
            return None
        if not os.path.isabs(target):
            target = os.path.join(os.path.dirname(path), target)
        return os.path.realpath(target)
    return None


def is_managed_link(path: str) -> bool:
    """判断路径是否为指向技能缓存的链接（本脚本管理的）。"""
    target = link_target(path)
    return target is not None and target.startswith(os.path.realpath(cache_root()))


def make_link(src: str, dst: str) -> None:
    """创建目录链接：macOS/Linux 用符号链接；Windows 优先 junction（无需管理员权限）。"""
    if os.name == "nt":
        r = subprocess.run(
            ["cmd", "/c", "mklink", "/J", dst, src], capture_output=True, text=True
        )
        if r.returncode != 0:
            raise OSError(r.stderr.strip() or r.stdout.strip() or "mklink /J 失败")
        return
    os.symlink(src, dst, target_is_directory=True)


# ---------- 来源获取（git clone，兜底 ZIP 下载） ----------


def parse_github_repo(repo: str):
    m = re.match(r"^https?://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", repo)
    return (m.group(1), m.group(2)) if m else None


def download_github_zip(owner: str, repo_name: str, branch: str, dest: str) -> None:
    url = f"https://codeload.github.com/{owner}/{repo_name}/zip/refs/heads/{branch}"
    print(f"[fetch] 下载 ZIP: {url}")
    try:
        with urllib.request.urlopen(url, timeout=120) as resp:
            data = resp.read()
    except Exception as e:
        raise SystemExit(f"[错误] 下载失败: {e}")
    os.makedirs(dest, exist_ok=True)
    with zipfile.ZipFile(io.BytesIO(data)) as zf:
        for member in zf.infolist():
            parts = member.filename.split("/", 1)
            if len(parts) < 2 or not parts[1]:
                continue
            target = os.path.join(dest, parts[1])
            if member.is_dir():
                os.makedirs(target, exist_ok=True)
            else:
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with zf.open(member) as fsrc, open(target, "wb") as fdst:
                    shutil.copyfileobj(fsrc, fdst)


def fetch_source(repo: str, branch: str, offline: bool) -> str:
    """拉取/更新远程仓库到缓存，返回技能源目录路径。"""
    rdir = repo_dir()
    git_dir = os.path.join(rdir, ".git")
    gh = parse_github_repo(repo)

    if os.path.isdir(git_dir):
        if not offline:
            print(f"[cache] 更新缓存仓库: {rdir}")
            r = run_git(["fetch", "--depth", "1", "origin", branch], cwd=rdir)
            if r.returncode == 0:
                run_git(["reset", "--hard", f"origin/{branch}"], cwd=rdir)
                run_git(["clean", "-fd"], cwd=rdir)  # 清除缓存中残留的未跟踪文件
            else:
                print(f"  ! 更新失败（{r.stderr.strip()[:120]}），使用已有缓存")
        else:
            print("[cache] 离线模式，使用已有缓存")
        src = os.path.join(rdir, SKILL_SOURCE_DIR)
        if not os.path.isdir(src):
            raise SystemExit(f"[错误] 缓存中未找到 {SKILL_SOURCE_DIR}/ 目录（{src}）")
        return src

    if offline:
        raise SystemExit("[offline] 无本地缓存且处于离线模式，无法获取技能")

    if shutil.which("git") and not gh:
        # 非 GitHub URL 或本地路径：只能走 git
        print(f"[fetch] 从来源仓库拉取技能: {repo}")
        shutil.rmtree(rdir, ignore_errors=True)
        os.makedirs(os.path.dirname(rdir), exist_ok=True)
        r = run_git(["clone", "--depth", "1", "--branch", branch, repo, rdir])
        if r.returncode != 0:
            raise SystemExit(f"[错误] 拉取失败: {r.stderr.strip() or '网络错误'}")
    elif gh:
        if shutil.which("git"):
            print(f"[fetch] 从 GitHub 仓库拉取技能: {repo}")
            shutil.rmtree(rdir, ignore_errors=True)
            os.makedirs(os.path.dirname(rdir), exist_ok=True)
            r = run_git(["clone", "--depth", "1", "--branch", branch, repo, rdir])
            if r.returncode != 0:
                print(f"  ! git 克隆失败（{r.stderr.strip()[:120]}），改用 ZIP 下载")
                shutil.rmtree(rdir, ignore_errors=True)
                download_github_zip(*gh, branch, rdir)
        else:
            print("[fetch] 未检测到 git，改用 ZIP 下载")
            download_github_zip(*gh, branch, rdir)
    else:
        raise SystemExit("[错误] 系统缺少 git 且来源不是 GitHub 仓库")

    src = os.path.join(rdir, SKILL_SOURCE_DIR)
    if not os.path.isdir(src):
        raise SystemExit(f"[错误] 仓库中未找到 {SKILL_SOURCE_DIR}/ 目录（{src}）")
    return src


# ---------- 安装 / 卸载 ----------


def install(project: str, src: str, force: bool) -> list:
    print(f"[install] 目标项目: {project}")
    made: list[str] = []
    for rel, label in PROJECT_TARGETS:
        target_dir = os.path.join(project, rel)
        os.makedirs(target_dir, exist_ok=True)
        for name in SKILLS:
            skill_src = os.path.join(src, name)
            dst = os.path.join(target_dir, name)
            if not os.path.isdir(skill_src):
                print(f"  ! 来源缺少技能 {name}，跳过")
                continue
            if is_managed_link(dst):
                print(f"  = 已链接: {rel}/{name}")
                continue
            if link_target(dst) is not None:
                if force:
                    os.unlink(dst)
                else:
                    print(f"  ! {rel}/{name} 是指向其他位置的链接，跳过（--force 覆盖）")
                    continue
            if os.path.exists(dst):
                print(f"  ! {rel}/{name} 已存在真实目录，跳过（不覆盖本地内容）")
                continue
            try:
                make_link(skill_src, dst)
            except OSError as e:
                print(f"  ! 无法创建链接（{e}），改用复制（占用空间较大）")
                shutil.copytree(skill_src, dst)
            made.append(dst)
            print(f"  + {rel}/{name} -> {skill_src}")
    if not made:
        print("  （本次未创建新链接）")
    return made


def uninstall(project: str) -> None:
    print(f"[uninstall] 目标项目: {project}")
    removed = 0
    for rel, _ in PROJECT_TARGETS:
        target_dir = os.path.join(project, rel)
        if not os.path.isdir(target_dir):
            continue
        for name in SKILLS:
            dst = os.path.join(target_dir, name)
            if is_managed_link(dst):
                os.unlink(dst)
                removed += 1
                print(f"  - 已移除: {rel}/{name}")
            elif link_target(dst) is not None:
                print(f"  ! {rel}/{name} 不是本脚本创建的链接，保留")
            elif os.path.exists(dst):
                print(f"  ! {rel}/{name} 是真实目录，保留")
        if os.path.isdir(target_dir) and not os.listdir(target_dir):
            os.rmdir(target_dir)
            print(f"  - 已清理空目录: {rel}/")
        parent = os.path.dirname(target_dir)
        while (
            parent
            and os.path.normpath(parent) != os.path.normpath(project)
            and os.path.isdir(parent)
            and not os.listdir(parent)
        ):
            os.rmdir(parent)
            print(f"  - 已清理空目录: {os.path.basename(parent)}/")
            parent = os.path.dirname(parent)
    if not removed:
        print("  （未找到本脚本安装的技能）")
    remove_gitignore_lines(project)


def add_gitignore_lines(project: str) -> None:
    """在项目 .gitignore 中忽略技能链接，避免误提交。"""
    gitignore = os.path.join(project, ".gitignore")
    if not os.path.isfile(gitignore):
        return
    with open(gitignore, "r", encoding="utf-8") as f:
        content = f.read()
    missing = [line for line in GITIGNORE_LINES if line not in content]
    if missing:
        with open(gitignore, "a", encoding="utf-8") as f:
            if not content.endswith("\n"):
                f.write("\n")
            f.write("\n".join(missing) + "\n")
        print(f"[gitignore] 已在 {gitignore} 追加忽略规则")


def remove_gitignore_lines(project: str) -> None:
    gitignore = os.path.join(project, ".gitignore")
    if not os.path.isfile(gitignore):
        return
    with open(gitignore, "r", encoding="utf-8") as f:
        lines = f.readlines()
    kept = [ln for ln in lines if ln.rstrip("\n") not in GITIGNORE_LINES]
    if len(kept) != len(lines):
        with open(gitignore, "w", encoding="utf-8") as f:
            f.writelines(kept)
        print(f"[gitignore] 已从 {gitignore} 移除忽略规则")


# ---------- Agent 检测与自动安装 ----------


def detect_agents() -> list:
    return [name for name in AGENTS if shutil.which(name)]


def install_opencode() -> bool:
    print("\n[agent] 未检测到任何 Agent CLI，开始安装 opencode ...")
    ok = False
    if os.name == "nt":
        npm = shutil.which("npm")
        if npm:
            print("  方式: npm install -g opencode-ai")
            r = subprocess.run([npm, "install", "-g", "opencode-ai"], capture_output=True, text=True)
            ok = r.returncode == 0
            if not ok:
                print(f"  ! npm 安装失败: {(r.stderr or r.stdout).strip()[:200]}")
        if not ok:
            print("  方式: 官方 PowerShell 安装脚本")
            ps = "irm https://opencode.ai/install | iex"
            r = subprocess.run(
                ["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-Command", ps],
                capture_output=True, text=True,
            )
            ok = r.returncode == 0
            if not ok:
                print(f"  ! 官方脚本安装失败: {(r.stderr or r.stdout).strip()[:200]}")
    else:
        print("  方式: 官方安装脚本 (curl | bash)")
        try:
            curl = subprocess.run(["curl", "-fsSL", "https://opencode.ai/install"], capture_output=True, timeout=120)
            if curl.returncode == 0:
                r = subprocess.run(["bash"], input=curl.stdout, capture_output=True, timeout=300)
                ok = r.returncode == 0
                if not ok:
                    print(f"  ! 安装失败: {(r.stderr.decode(errors='replace') if r.stderr else '').strip()[:200]}")
            else:
                print("  ! 下载安装脚本失败（网络问题）")
        except Exception as e:
            print(f"  ! 安装失败: {e}")
    if ok:
        print("[agent] opencode 安装完成。请重新打开终端后，在项目中运行本工具。")
    else:
        print("[agent] opencode 安装失败，可稍后手动安装：https://opencode.ai/install")
    return ok


# ---------- 交互模式（双击即用） ----------


def ask_yes_no(prompt: str, default: bool = True) -> bool:
    hint = "[Y/n]" if default else "[y/N]"
    try:
        ans = input(f"{prompt} {hint} ").strip().lower()
    except EOFError:
        return default
    if not ans:
        return default
    return ans in ("y", "yes", "是", "1")


def ask_path(prompt: str, default: str) -> str:
    try:
        ans = input(f"{prompt} [默认: {default}] ").strip()
    except EOFError:
        ans = ""
    return os.path.abspath(ans or default)


def run_interactive(args) -> None:
    print(BANNER)
    print("江南写作技能安装器 v1.0.0")
    print("-" * 56)

    agents = detect_agents()
    if not agents:
        print("[检查] 未检测到 Agent CLI（claude / codex / opencode）。")
        if ask_yes_no("[安装] 是否立即安装 opencode？", True):
            install_opencode()
    else:
        print("[检查] 已检测到 Agent CLI: " + "、".join(agents))

    project = ask_path("\n请输入要激活技能的项目路径（回车使用当前目录）", os.getcwd())
    if not os.path.isdir(project):
        raise SystemExit(f"[错误] 项目目录不存在: {project}")

    src = fetch_source(args.repo, args.branch, args.offline)
    made = install(project, src, args.force)
    if not args.no_gitignore and made:
        add_gitignore_lines(project)
    print_summary()

    try:
        input("\n按回车键退出...")
    except EOFError:
        pass


def print_summary() -> None:
    print("\n[完成] 江南写作技能已激活，支持以下 Agent：")
    print("  - Claude Code:  技能可斜杠调用（/author-jiang-nan-master 等）")
    print("  - opencode:     skill 工具自动列出可用技能")
    print("  - codex:        自动发现 .codex/skills 技能")
    print(f"  技能实体仅存于缓存（{repo_dir()}），项目内仅为链接；")
    print("  重新运行本工具即更新，--uninstall 即停用。")


def print_skills() -> None:
    print("江南写作技能（来源: 远程仓库 .claude/skills/）：")
    print(f"  {'技能名':<28} 适用场景")
    print("  " + "-" * 60)
    desc = {
        "author-jiang-nan-master": "★ 总人格（自动识别龙族/九州/天之炽）",
        "author-jiang-nan": "九州缥缈录专项",
        "author-jiang-nan-longzu": "龙族专项",
        "author-jiang-nan-tianzhichi": "天之炽专项",
    }
    for name in SKILLS:
        print(f"  {name:<28} {desc[name]}")
    print(f"\n缓存位置: {repo_dir()}")


# ---------- 入口 ----------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="从远程仓库拉取江南写作技能，以链接方式安装到指定项目（内容不入库、项目隔离、跨平台）。"
    )
    parser.add_argument("--project", default=None, help="目标项目目录（默认: 当前目录）")
    parser.add_argument("--repo", default=DEFAULT_REPO, help=f"技能来源仓库（URL 或本地路径，默认: {DEFAULT_REPO}）")
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help=f"来源分支（默认: {DEFAULT_BRANCH}）")
    parser.add_argument("--offline", action="store_true", help="离线模式，仅使用已有缓存")
    parser.add_argument("--force", action="store_true", help="覆盖指向其他位置的已有链接")
    parser.add_argument("--no-gitignore", action="store_true", help="不修改项目的 .gitignore")
    parser.add_argument("--uninstall", action="store_true", help="卸载（移除本脚本创建的链接并清理 .gitignore）")
    parser.add_argument("--list", action="store_true", help="列出技能并退出")
    parser.add_argument("--interactive", action="store_true", help="强制进入交互模式（默认无参数时自动进入）")
    args = parser.parse_args()

    if args.list:
        print_skills()
        return

    if args.uninstall:
        project = os.path.abspath(args.project or os.getcwd())
        if not os.path.isdir(project):
            raise SystemExit(f"[错误] 项目目录不存在: {project}")
        uninstall(project)
        print("\n完成。已停用项目中的江南技能；关闭 Agent 后不再加载。")
        return

    if args.interactive or not args.project:
        run_interactive(args)
        return

    project = os.path.abspath(args.project)
    if not os.path.isdir(project):
        raise SystemExit(f"[错误] 项目目录不存在: {project}")

    if not detect_agents():
        print("[提示] 未检测到 Agent CLI（claude/codex/opencode），安装技能后仍需安装 Agent 才能使用。")

    src = fetch_source(args.repo, args.branch, args.offline)
    made = install(project, src, args.force)
    if not args.no_gitignore and made:
        add_gitignore_lines(project)
    print_summary()


if __name__ == "__main__":
    main()
