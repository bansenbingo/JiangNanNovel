江南写作技能安装器 (JiangNanSkills) — macOS 版

============================================
快速开始
============================================

方式一（推荐）: 双击「江南技能安装.app」
  1. 将「江南技能安装.app」拖入「应用程序」文件夹
  2. 双击运行（首次打开如提示未验证开发者，请右键 → 打开）
  3. 在打开的终端窗口中，按提示输入项目路径即可激活技能

方式二: 命令行
  将本 DMG 中的 jiangnan-skills 复制到任意目录（如 /usr/local/bin）：
      sudo cp jiangnan-skills /usr/local/bin/
      jiangnan-skills --project ~/你的小说项目
  常用参数：
      jiangnan-skills                交互模式
      jiangnan-skills --project DIR  安装到指定项目
      jiangnan-skills --uninstall    停用
      jiangnan-skills --list         查看技能清单

============================================
说明
============================================
- 技能来源: 远程仓库（GitHub bansenbingo/JiangNanNovel），自动拉取更新
- 项目隔离: 只在指定的项目内激活，其他项目不受影响
- 内容不入库: 技能实体仅存于 ~/Library/Caches/JiangNanSkills，项目内为符号链接
- 若本机无任何 Agent CLI（claude/codex/opencode），安装器会优先自动安装 opencode
