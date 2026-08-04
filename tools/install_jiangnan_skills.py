#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""江南写作技能安装器（项目级，内容不落本地项目）

从远程仓库拉取江南写作技能（.claude/skills/ 中的 4 个人格），
以符号链接方式安装到指定项目，供 Claude Code / opencode / codex 使用。

设计原则：
- 项目隔离：只在运行脚本时指定的项目内激活，其他项目不受影响
- 内容不入库：技能实体只存在于系统缓存（从远程拉取），项目内只有符号链接
- 关闭即停用：卸载（--uninstall）或删除链接后，Agent 不再加载该技能

用法示例：
    python3 tools/install_jiangnan_skills.py                     # 安装到当前目录
    python3 tools/install_jiangnan_skills.py --project ~/novels  # 安装到指定项目
    python3 tools/install_jiangnan_skills.py --uninstall         # 卸载
    python3 tools/install_jiangnan_skills.py --list              # 查看技能列表
    python3 tools/install_jiangnan_skills.py --repo ./           # 指定来源（本地仓库或 URL）
"""

import argparse
import os
import shutil
import subprocess
import sys

SKILLS = [
    "author-jiang-nan-master",       # 总人格：自动识别世界观（龙族/九州/天之炽），首选
    "author-jiang-nan",              # 九州缥缈录专项
    "author-jiang-nan-longzu",       # 龙族专项
    "author-jiang-nan-tianzhichi",   # 天之炽专项
]

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


def cache_root() -> str:
    """技能缓存根目录（实体内容只存在这里，不写入项目）。"""
    if sys.platform == "darwin":
        base = os.path.expanduser("~/Library/Caches")
    else:
        base = os.environ.get("XDG_CACHE_HOME") or os.path.expanduser("~/.cache")
    return os.path.join(base, "JiangNanSkills")


def repo_dir() -> str:
    return os.path.join(cache_root(), "repo")


def run_git(args: list, cwd: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)


def fetch_source(repo: str, branch: str, offline: bool) -> str:
    """拉取/更新远程仓库到缓存，返回技能源目录路径。"""
    rdir = repo_dir()
    git_dir = os.path.join(rdir, ".git")

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
    else:
        if offline:
            print("[offline] 无本地缓存且处于离线模式，无法获取技能")
            raise SystemExit(1)
        print(f"[fetch] 从来源仓库拉取技能: {repo}")
        shutil.rmtree(rdir, ignore_errors=True)
        os.makedirs(os.path.dirname(rdir), exist_ok=True)
        r = run_git(["clone", "--depth", "1", "--branch", branch, repo, rdir])
        if r.returncode != 0:
            raise SystemExit(f"[错误] 拉取失败: {r.stderr.strip() or '网络错误'}")

    src = os.path.join(rdir, SKILL_SOURCE_DIR)
    if not os.path.isdir(src):
        raise SystemExit(f"[错误] 仓库中未找到 {SKILL_SOURCE_DIR}/ 目录（{src}）")
    return src


def is_managed_link(path: str) -> bool:
    """判断路径是否为指向技能缓存的符号链接（本脚本管理的）。"""
    return os.path.islink(path) and os.path.realpath(path).startswith(os.path.realpath(cache_root()))


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
            if os.path.islink(dst):
                if force:
                    os.unlink(dst)
                else:
                    print(f"  ! {rel}/{name} 是指向其他位置的链接，跳过（--force 覆盖）")
                    continue
            if os.path.exists(dst):
                print(f"  ! {rel}/{name} 已存在真实目录，跳过（不覆盖本地内容）")
                continue
            os.symlink(skill_src, dst)
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
            elif os.path.islink(dst):
                print(f"  ! {rel}/{name} 不是本脚本创建的链接，保留")
            elif os.path.exists(dst):
                print(f"  ! {rel}/{name} 是真实目录，保留")
        if os.path.isdir(target_dir) and not os.listdir(target_dir):
            os.rmdir(target_dir)
            print(f"  - 已清理空目录: {rel}/")
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


def main() -> None:
    parser = argparse.ArgumentParser(
        description="从远程仓库拉取江南写作技能，以符号链接方式安装到指定项目（内容不入库、项目隔离）。"
    )
    parser.add_argument("--project", default=None, help="目标项目目录（默认: 当前目录）")
    parser.add_argument("--repo", default=DEFAULT_REPO, help=f"技能来源仓库（URL 或本地路径，默认: {DEFAULT_REPO}）")
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help=f"来源分支（默认: {DEFAULT_BRANCH}）")
    parser.add_argument("--offline", action="store_true", help="离线模式，仅使用已有缓存")
    parser.add_argument("--force", action="store_true", help="覆盖指向其他位置的已有链接")
    parser.add_argument("--no-gitignore", action="store_true", help="不修改项目的 .gitignore")
    parser.add_argument("--uninstall", action="store_true", help="卸载（移除本脚本创建的链接并清理 .gitignore）")
    parser.add_argument("--list", action="store_true", help="列出技能并退出")
    args = parser.parse_args()

    if args.list:
        print_skills()
        return

    project = os.path.abspath(args.project or os.getcwd())
    if not os.path.isdir(project):
        raise SystemExit(f"[错误] 项目目录不存在: {project}")

    if args.uninstall:
        uninstall(project)
        print("\n完成。已停用项目中的江南技能；关闭 Agent 后不再加载。")
        return

    src = fetch_source(args.repo, args.branch, args.offline)
    made = install(project, src, args.force)
    if not args.no_gitignore and made:
        add_gitignore_lines(project)

    print("\n[完成] 江南写作技能已激活，支持以下 Agent：")
    print("  - Claude Code:  技能可斜杠调用（/author-jiang-nan-master 等）")
    print("  - opencode:     skill 工具自动列出可用技能")
    print("  - codex:        自动发现 .codex/skills 技能")
    print(f"  技能实体仅存于缓存（{repo_dir()}），项目内仅为链接；")
    print("  重新运行脚本即更新，--uninstall 即停用。")


if __name__ == "__main__":
    main()
