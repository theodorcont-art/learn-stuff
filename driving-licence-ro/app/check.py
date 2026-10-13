"""Validate chapter JSON files; fix cedilla diacritics in place. Usage: check.py <content dir>"""
import json, glob, os, re, sys
src = sys.argv[1]
signs = {}
if os.path.exists(os.path.join(src, 'signs.json')):
    signs = json.load(open(os.path.join(src, 'signs.json'), encoding='utf-8'))
ARMS = {'n', 's', 'e', 'w'}
LAYOUTS = {'cross', 't-north', 't-south', 't-east', 't-west', 'roundabout', 'straight'}
TAGS = re.compile(r'</?([a-zA-Z0-9]+)')
OK_TAGS = {'p', 'b', 'i', 'ul', 'ol', 'li', 'br', 'strong', 'em'}
problems, used = [], set()
def vis(v, where):
    if not v: return
    if 'sign' in v: used.add(v['sign'])
    for s in v.get('signs', []): used.add(s)
    sc = v.get('scene')
    if sc:
        if sc.get('layout') not in LAYOUTS: problems.append(f'{where}: bad layout {sc.get("layout")}')
        for ve in sc.get('vehicles', []):
            if ve.get('arm') not in ARMS: problems.append(f'{where}: bad arm {ve}')
        for g in sc.get('signs', []): used.add(g.get('sign'))
for p in sorted(glob.glob(os.path.join(src, 'ch*.json'))):
    raw = open(p, encoding='utf-8').read()
    fixed = raw.replace('ş', 'ș').replace('ţ', 'ț').replace('Ş', 'Ș').replace('Ţ', 'Ț')
    if fixed != raw:
        open(p, 'w', encoding='utf-8').write(fixed); print('fixed cedillas in', os.path.basename(p))
    d = json.loads(fixed); n = os.path.basename(p)
    for k in ('id', 'title', 'tagline', 'minutes', 'intro', 'cards', 'summary', 'questions'):
        if k not in d: problems.append(f'{n}: missing {k}')
    for i, c in enumerate(d.get('cards', [])):
        if c.get('kind') not in ('idea', 'rule', 'trap', 'memo', 'example'): problems.append(f'{n} card {i}: kind {c.get("kind")}')
        bad = {t.lower() for t in TAGS.findall(c.get('body', ''))} - OK_TAGS
        if bad: problems.append(f'{n} card {i}: tags {bad}')
        vis(c.get('visual'), f'{n} card {i}')
    for i, q in enumerate(d.get('questions', [])):
        if len(q.get('o', [])) != 3: problems.append(f'{n} q{i}: {len(q.get("o", []))} options')
        if not q.get('c') or any(x not in (0, 1, 2) for x in q['c']) or len(set(q['c'])) != len(q['c']): problems.append(f'{n} q{i}: bad c {q.get("c")}')
        vis(q.get('visual'), f'{n} q{i}')
    cs = [len(q['c']) for q in d.get('questions', [])]
    print(f"{n}: {len(d.get('cards', []))} cards, {len(cs)} q (1:{cs.count(1)} 2:{cs.count(2)} 3:{cs.count(3)}), uncertain {len(d.get('uncertain', []))}")
missing = sorted(u for u in used if u and u not in signs)
print('signs used', len(used), 'missing', missing)
print('\n'.join(problems) or 'no structural problems')
