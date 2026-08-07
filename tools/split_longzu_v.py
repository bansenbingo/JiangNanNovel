from pathlib import Path
import re

SRC = Path('原著素材/龙族/龙族Ⅴ·悼亡者归来.txt')
OUT = Path('原著素材/龙族/分卷/龙族V_分卷')
TARGET = 20000
MIN = 16000
MAX = 24000

s = SRC.read_text(encoding='utf-8-sig', errors='replace').replace('\r\n','\n').replace('\r','\n')
# Remove common web-publishing noise while retaining chapter/title text.
lines = []
for raw in s.split('\n'):
    x = raw.replace('\ufeff','').replace('\ufffd','').strip()
    if not x:
        continue
    if re.search(r'https?://|www\.|\.com\b|\.cn\b|扫码|二维码|公众号|关注作者|打赏|月票|推荐票|收藏本章|广告|订阅本章|加入书签|投推荐票|章节错误|举报', x, re.I):
        continue
    # Divider-only lines, including repeated punctuation.
    if not re.search(r'[\u4e00-\u9fffA-Za-z0-9]', x):
        continue
    if re.fullmatch(r'[\-—_=*~·•.。！!？?，,、/\\|#]{2,}', x):
        continue
    # Strip ornamental divider runs at line edges.
    x = re.sub(r'^[\-—_=*~·•.。！!？?，,、/\\|#]{2,}', '', x)
    x = re.sub(r'[\-—_=*~·•.。！!？?，,、/\\|#]{2,}$', '', x).strip()
    if x:
        lines.append(x)

# Chapter/title lines are retained and used as safe split points.
heading = re.compile(r'^(?:第[一二三四五六七八九十百千万零〇0-9]+章|第[一二三四五六七八九十百千万零〇0-9]+节|楔子|序章|尾声|后记|番外|龙族[Ⅴ五Vv])')
blocks, cur = [], []
for x in lines:
    if heading.match(x) and cur:
        blocks.append('\n'.join(cur)); cur = []
    cur.append(x)
if cur:
    blocks.append('\n'.join(cur))

# Merge chapter blocks toward ~20k chars, never split a chapter unless one chapter itself exceeds MAX.
chunks, cur, n = [], [], 0
for block in blocks:
    b_n = len(block)
    if cur and n + b_n > TARGET and n >= MIN:
        chunks.append('\n\n'.join(cur)); cur, n = [], 0
    if b_n <= MAX:
        cur.append(block); n += b_n
    else:
        # Very long chapter: split only on paragraph boundaries.
        paras = block.split('\n')
        for para in paras:
            if cur and n + len(para) + 1 > TARGET and n >= MIN:
                chunks.append('\n\n'.join(cur)); cur, n = [], 0
            cur.append(para); n += len(para) + 1
if cur:
    chunks.append('\n\n'.join(cur))

OUT.mkdir(parents=True, exist_ok=True)
for p in OUT.glob('*.txt'):
    p.unlink()
for i, chunk in enumerate(chunks, 1):
    (OUT / f'龙族V_{i:02d}.txt').write_text(chunk + '\n', encoding='utf-8')

print(f'源文件字符数: {len(s)}')
print(f'清洗后正文字符数: {sum(len(x) for x in chunks)}')
print(f'输出分卷数: {len(chunks)}')
for i, c in enumerate(chunks, 1):
    print(f'{i:02d}\t{len(c)}')
