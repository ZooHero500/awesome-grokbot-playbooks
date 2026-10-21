#!/usr/bin/env python3
"""Render README banner and GitHub social card from assets/banner/banner.html.

Numbers come from README.md (the "为什么看这个仓库" table), so the banner always
matches the README. Needs Google Chrome (or Chromium) installed locally.

    python3 scripts/banner.py           # writes assets/social-preview.png and assets/social-card.png
    python3 scripts/banner.py --check   # exit 1 if the PNG is out of date with README numbers
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
HTML = ROOT / 'assets/banner/banner.html'
STAMP = ROOT / 'assets/banner/numbers.txt'
OUT = {'readme': ROOT / 'assets/social-preview.png', 'card': ROOT / 'assets/social-card.png'}
CHROME = [
    os.environ.get('CHROME', ''),
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/Applications/Chromium.app/Contents/MacOS/Chromium',
    shutil.which('google-chrome') or '', shutil.which('chromium') or '', shutil.which('chromium-browser') or '',
]


def numbers():
    t = (ROOT / 'README.md').read_text(encoding='utf-8')
    get = lambda pat: re.search(r'\| \*\*(\d+)\*\* \| ' + pat, t).group(1)
    return {'entries': get('个条目'), 'recipes': get('个可抄配方'), 'tutorials': get('篇社区教程')}


def render(query, out):
    chrome = next(c for c in CHROME if c and os.path.exists(c))
    url = HTML.as_uri() + '?' + urllib.parse.urlencode(query)
    with tempfile.TemporaryDirectory() as profile:
        subprocess.run([chrome, '--headless=new', '--disable-gpu', '--hide-scrollbars', '--no-first-run',
                        f'--user-data-dir={profile}', '--force-device-scale-factor=1', '--window-size=1280,640',
                        '--virtual-time-budget=2000', f'--screenshot={out}', url],
                       check=True, capture_output=True)


def main():
    n = numbers()
    stamp = '{entries} / {recipes} / {tutorials}'.format(**n)
    if '--check' in sys.argv:
        old = STAMP.read_text().strip() if STAMP.exists() else ''
        print('banner', 'up to date' if old == stamp else f'stale: {old or "none"} -> {stamp}')
        sys.exit(0 if old == stamp else 1)
    render(n, OUT['readme'])
    render({'mode': 'card'}, OUT['card'])
    STAMP.write_text(stamp + '\n')
    print('rendered', stamp)


if __name__ == '__main__':
    main()
