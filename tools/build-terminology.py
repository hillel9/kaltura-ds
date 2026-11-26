#!/usr/bin/env python3
"""
Maintainer helper (NOT needed to use the DS): writes the terminology index into the docs.

    python3 tools/build-terminology.py

Reads tools/terminology.json (the one source of truth: Figma name, KEP UI name and kaltura-ds
classes for every component and property) and rewrites the regions between

    <!-- BEGIN GENERATED: terminology -->  ...  <!-- END GENERATED: terminology -->

in index.html (HTML tables) and DS-GUIDE.md (markdown tables). Edit the JSON whenever a
component is added, renamed or fixed, then run this script.
"""
import html, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
BEGIN, END = '<!-- BEGIN GENERATED: terminology -->', '<!-- END GENERATED: terminology -->'


def code_list(text):
    """Wrap class names, tokens and attributes in <code>, leave words alone."""
    out = html.escape(text)
    return re.sub(r'(&lt;ds-icon[^&]*?&gt;|--ds-[a-z0-9{}-]+|ds-[a-z0-9-]+(?:\(\))?|DS\.[a-zA-Z]+\(\)|aria-[a-z]+=&quot;[a-z]+&quot;|\.?-(?:sm|md|lg|xl|info|error|success|warning|white|black|secondary|danger|darker|brighter|green|orange|red|grey|on|off|2|3)\b)',
                  r'<code>\1</code>', out)


def html_table(rows, cols):
    head = ''.join(f'<th>{h}</th>' for _, h in cols)
    body = []
    for r in rows:
        cells = []
        for key, _ in cols:
            v = r.get(key, '')
            if key == 'ds':
                cell = code_list(v)
                if r.get('was'):
                    cell += f'<br><span style="color:var(--ds-tone-3);">was {code_list(r["was"])}</span>'
            elif key == 'name':
                cell = f'<strong>{html.escape(v)}</strong>'
                if r.get('anchor'):
                    cell = f'<a href="#{r["anchor"]}" style="color:inherit;">{cell}</a>'
            else:
                cell = html.escape(v)
            cells.append(f'<td>{cell}</td>')
        body.append('        <tr>' + ''.join(cells) + '</tr>')
    return ('    <table class="token-table">\n      <thead><tr>' + head + '</tr></thead>\n      <tbody>\n'
            + '\n'.join(body) + '\n      </tbody>\n    </table>\n')


def md_cell(v):
    return v.replace('|', '\\|')


def md_table(rows, cols):
    lines = ['| ' + ' | '.join(h for _, h in cols) + ' |', '|' + '---|' * len(cols)]
    for r in rows:
        cells = []
        for key, _ in cols:
            v = r.get(key, '')
            if key == 'ds' and r.get('was'):
                v += f' (was {r["was"]})'
            cells.append(md_cell(v))
        lines.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(lines) + '\n'


def replace_region(path, content):
    text = open(path, encoding='utf-8').read()
    if BEGIN not in text or END not in text:
        sys.exit(f'build-terminology: markers missing in {path}')
    pre, rest = text.split(BEGIN, 1)
    _, post = rest.split(END, 1)
    open(path, 'w', encoding='utf-8').write(pre + BEGIN + '\n' + content + END + post)


def check(d):
    """Fail if the index names a class, token or page section that does not exist."""
    css = open(os.path.join(ROOT, 'styles.css'), encoding='utf-8').read()
    page = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()
    classes = set(re.findall(r'\.(ds-[a-z0-9-]+)', css)) | {'ds-icon', 'ds-toast-active'}
    tokens = set(re.findall(r'(--ds-[a-z0-9-]+)\s*:', css))
    errors = []
    for section in ('components', 'properties'):
        for r in d[section]:
            for field in ('ds', 'was'):
                text = r.get(field, '')
                for c in re.findall(r'(?<![-\w])(ds-[a-z0-9-]+)', text):
                    if c not in classes:
                        errors.append(f'{r["name"]}: class {c} is not in styles.css')
                for t in re.findall(r'(--ds-[a-z0-9-]+)', text):
                    placeholder = t.endswith('-') or '-x-' in t
                    if not placeholder and t not in tokens:
                        errors.append(f'{r["name"]}: token {t} is not in styles.css')
            if r.get('anchor') and f'id="{r["anchor"]}"' not in page:
                errors.append(f'{r["name"]}: index.html has no section id="{r["anchor"]}"')
    if errors:
        sys.exit('build-terminology: fix tools/terminology.json:\n  ' + '\n  '.join(errors))


def main():
    d = json.load(open(os.path.join(ROOT, 'tools', 'terminology.json'), encoding='utf-8'))
    check(d)
    comp_cols = [('name', 'Component'), ('figma', 'Figma (Platform DS)'), ('kep', 'KEP UI (ds-react-components)'), ('ds', 'kaltura-ds'), ('notes', 'Notes')]
    prop_cols = [('name', 'Concept'), ('figma', 'Figma'), ('kep', 'KEP UI'), ('ds', 'kaltura-ds'), ('notes', 'Notes')]
    miss_cols = [('name', 'Component'), ('figma', 'Figma'), ('kep', 'KEP UI')]

    sub = '    <h3 style="font-size:var(--ds-font-size-4); font-weight:var(--ds-font-weight-bold); margin:var(--ds-space-6) 0 var(--ds-space-3);">{}</h3>\n'
    page = (sub.format('Components') + html_table(d['components'], comp_cols)
            + sub.format('Properties, states and tokens') + html_table(d['properties'], prop_cols)
            + sub.format('In Figma or KEP UI, not in kaltura-ds yet') + html_table(d['missing'], miss_cols))
    replace_region(os.path.join(ROOT, 'index.html'), page)

    guide = ('**Components**\n\n' + md_table(d['components'], comp_cols)
             + '\n**Properties, states and tokens**\n\n' + md_table(d['properties'], prop_cols)
             + '\n**In Figma or KEP UI, not in kaltura-ds yet** (build these yourself from tokens)\n\n' + md_table(d['missing'], miss_cols))
    replace_region(os.path.join(ROOT, 'DS-GUIDE.md'), guide)
    print(f"terminology: {len(d['components'])} components, {len(d['properties'])} properties, {len(d['missing'])} missing -> index.html, DS-GUIDE.md")


if __name__ == '__main__':
    main()
