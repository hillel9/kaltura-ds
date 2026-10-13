#!/usr/bin/env python3
"""
Maintainer helper (NOT needed to use the DS): refreshes the generated parts of DS-GUIDE.md.

    python3 tools/build-guide.py                                   # source files in the repo root -> ./DS-GUIDE.md
    python3 tools/build-guide.py --src releases/v1.0 --out releases/v1.0/DS-GUIDE.md

It reads styles.css, ds.js and ds-icons.js from --src and rewrites ONLY the regions of the --out file
that sit between these markers (everything else in the guide is hand-written and is left alone):

    <!-- BEGIN GENERATED: version -->  ...  <!-- END GENERATED: version -->
    <!-- BEGIN GENERATED: tokens -->   ...  <!-- END GENERATED: tokens -->
    <!-- BEGIN GENERATED: icons -->    ...  <!-- END GENERATED: icons -->

When component markup, events or the DS API change, edit the hand-written sections of DS-GUIDE.md too.
"""
import argparse, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def block(css, selector):
    m = re.search(re.escape(selector) + r'\s*\{(.*?)\n\}', css, re.S)
    if not m:
        sys.exit(f'build-guide: no "{selector}" block in styles.css')
    return m.group(1)


def parse_dark(css):
    out = {}
    for name, value in re.findall(r'(--ds-[a-z0-9-]+)\s*:\s*([^;]+);', block(css, '[data-theme="dark"]')):
        out[name] = value.strip()
    return out


def tokens_block(css):
    dark = parse_dark(css)
    lines = []
    for raw in block(css, ':root').split('\n'):
        line = raw.strip()
        if not line:
            continue
        c = re.fullmatch(r'/\*\s*(.*?)\s*\*/', line)
        if c:
            if lines:
                lines.append('')
            lines.append(f'/* {c.group(1)} */')
            continue
        m = re.match(r'(--ds-[a-z0-9-]+)\s*:\s*([^;]+);', line)
        if m:
            name, value = m.group(1), m.group(2).strip()
            note = f'   /* dark: {dark[name]} */' if name in dark else ''
            lines.append(f'{name}: {value};{note}')
    missing = [n for n in dark if not any(l.startswith(n + ':') for l in lines)]
    if missing:  # dark-only tokens (not in :root)
        lines += ['', '/* Dark theme only */'] + [f'{n}: {dark[n]};' for n in missing]
    return '```css\n' + '\n'.join(lines) + '\n```'


def icon_names(js):
    names = {'16': [], '24': []}
    size = None
    for line in js.split('\n'):
        m = re.match(r'\s*icons\[(16|24)\]\s*=', line)
        if m:
            size = m.group(1)
            continue
        m = re.match(r'\s{4}"([a-z0-9]+(?:-[a-z0-9]+)*)":', line)
        if m and size:
            names[size].append(m.group(1))
    return names


def icons_block(js):
    n = icon_names(js)
    only16 = sorted(set(n['16']) - set(n['24']))
    out = [
        f"**24px ({len(n['24'])}):**",
        ', '.join(n['24']),
        '',
        f"**16px ({len(n['16'])}):**",
        ', '.join(n['16']),
        '',
        '**16px-only icons (no 24px version, so ALWAYS write `size="16"` for them):** '
        + (', '.join(only16) if only16 else 'none'),
    ]
    return '\n'.join(out)


def version_block(js):
    m = re.search(r"version:\s*'([^']+)'", js)
    if not m:
        sys.exit('build-guide: no version in ds.js')
    return f'DS version: **{m.group(1)}**'


def replace_region(text, name, body):
    pat = re.compile(
        r'(<!-- BEGIN GENERATED: ' + name + r' -->\n).*?(\n<!-- END GENERATED: ' + name + r' -->)', re.S)
    if not pat.search(text):
        sys.exit(f'build-guide: markers for "{name}" not found in the guide')
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text, count=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', default=ROOT, help='folder holding styles.css, ds.js, ds-icons.js (default: repo root)')
    ap.add_argument('--out', default=os.path.join(ROOT, 'DS-GUIDE.md'), help='guide file to refresh')
    a = ap.parse_args()

    css = read(os.path.join(a.src, 'styles.css'))
    js = read(os.path.join(a.src, 'ds.js'))
    icons = read(os.path.join(a.src, 'ds-icons.js'))

    text = read(a.out)
    text = replace_region(text, 'version', version_block(js))
    text = replace_region(text, 'tokens', tokens_block(css))
    text = replace_region(text, 'icons', icons_block(icons))
    with open(a.out, 'w', encoding='utf-8') as fh:
        fh.write(text)
    print(f'refreshed generated regions of {a.out} from {a.src}')


if __name__ == '__main__':
    main()
