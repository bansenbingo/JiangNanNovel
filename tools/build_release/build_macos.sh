#!/usr/bin/env bash
# 构建 macOS Release：CLI 二进制（PyInstaller）+ 安装器 .app + DMG
# 在 macOS 上运行（本地或 GitHub Actions macos runner）
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

CONTENT="$ROOT/dist/dmg-content"
DMG="$ROOT/dist/JiangNanSkills-macOS.dmg"
APP_NAME="江南技能安装.app"
APP="$CONTENT/$APP_NAME"
VERSION="${VERSION:-1.0.0}"

echo "==> 1/4 构建 CLI 二进制（PyInstaller）"
if ! python3 -m PyInstaller --version >/dev/null 2>&1; then
    echo "  安装 PyInstaller ..."
    python3 -m pip install --quiet pyinstaller
fi
python3 -m PyInstaller --onefile --console \
    --name jiangnan-skills \
    tools/install_jiangnan_skills.py >/dev/null

echo "==> 2/4 组装 .app 应用包"
rm -rf "$CONTENT"
mkdir -p "$APP/Contents/MacOS"
cp "dist/jiangnan-skills" "$APP/Contents/MacOS/jiangnan-skills"
chmod +x "$APP/Contents/MacOS/jiangnan-skills"
cp "tools/build_release/app_launcher.sh" "$APP/Contents/MacOS/launcher"
chmod +x "$APP/Contents/MacOS/launcher"
cp "tools/build_release/Info.plist" "$APP/Contents/Info.plist"
codesign --force --deep -s - "$APP" 2>/dev/null || true

echo "==> 3/4 添加 CLI 与说明文件"
cp "dist/jiangnan-skills" "$CONTENT/jiangnan-skills"
chmod +x "$CONTENT/jiangnan-skills"
cp "tools/build_release/README_macos.txt" "$CONTENT/README.txt"

echo "==> 4/4 生成 DMG"
rm -f "$DMG"
hdiutil create -volname "JiangNanSkills" -srcfolder "$CONTENT" -ov -format UDZO "$DMG" >/dev/null

echo ""
echo "构建完成: $DMG"
ls -lh "$DMG"
