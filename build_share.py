"""Claude用の index.html から、外部に置ける版（share/index.html）を作る。

Claude の上ではフローチャートが自動で描かれるが、外部では描かれないため、
描画用のライブラリ（mermaid）を読み込む行を足す。検索に出ないよう noindex も付ける。
index.html を直したら、このファイルを実行して share/index.html を作り直す:
    python3 build_share.py
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "index.html").read_text(encoding="utf-8")
body_start = src.index('<div class="wrap">')
head_part = src[:body_start].replace('<meta charset="utf-8">\n', "")
body_part = src[body_start:]

html = (
    '<!doctype html>\n<html lang="ja">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<meta name="robots" content="noindex, nofollow">\n'
    + head_part
    + "<style>body { margin: 0; } img { max-width: 100%; }</style>\n"
    + "</head>\n<body>\n"
    + body_part
    + '\n<script src="https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.min.js"></script>\n'
    + "<script>mermaid.initialize({ startOnLoad: true });</script>\n"
    + "</body>\n</html>\n"
)
out = here / "share" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print("wrote", out)
