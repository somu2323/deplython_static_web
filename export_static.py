#!/usr/bin/env python3
"""Export this Django-based static site to a plain static `dist/` folder.

This script performs a minimal conversion of Django's `{% static %}` tags into
relative paths and copies the `personal/static/` assets into `dist/static/`.
It's intentionally small and does not require Django to be installed.
"""

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / 'personal' / 'templates' / 'home.html'
STATIC_SRC = ROOT / 'personal' / 'static'
DIST = ROOT / 'dist'


def main():
    if not TEMPLATE.exists():
        print(f"Template not found: {TEMPLATE}")
        return 2

    html = TEMPLATE.read_text(encoding='utf-8')

    # Remove the load static tag (we'll replace static references ourselves)
    html = re.sub(r"\{%\s*load\s+static\s*%\}", "", html)

    # Replace {% static 'path' %} with static/path
    html = re.sub(r"\{%\s*static\s+'([^']+)'\s*%\}", r"static/\1", html)

    # Ensure output dir
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    (DIST / 'index.html').write_text(html, encoding='utf-8')

    # Copy static files
    if STATIC_SRC.exists():
        shutil.copytree(STATIC_SRC, DIST / 'static')
    else:
        print(f"Warning: static source not found: {STATIC_SRC}")

    print(f"Export complete: {DIST}")
    print("Files written:\n")
    for p in sorted(DIST.rglob('*')):
        print('-', p.relative_to(DIST))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
