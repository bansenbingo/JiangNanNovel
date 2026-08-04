#!/bin/bash
# 江南技能安装器（macOS .app 启动器）
# 双击 .app 时打开终端，运行 CLI 安装器
DIR="$(cd "$(dirname "$0")" && pwd)"
BIN="$DIR/jiangnan-skills"

osascript <<EOF
tell application "Terminal"
    do script "cd '$DIR' && '$BIN'"
    activate
end tell
EOF
