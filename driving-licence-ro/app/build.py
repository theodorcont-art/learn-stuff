"""Bundle content/chNN.json + content/signs.json into app/content.js (window.COURSE)."""
import json, glob, os, sys
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(root, 'content')
chapters = []
for p in sorted(glob.glob(os.path.join(src, 'ch*.json'))):
    with open(p, encoding='utf-8') as f:
        d = json.load(f)
    d.pop('uncertain', None)
    chapters.append(d)
signs = {}
sp = os.path.join(src, 'signs.json')
if os.path.exists(sp):
    with open(sp, encoding='utf-8') as f:
        signs = json.load(f)
out = os.path.join(root, 'app', 'content.js')
with open(out, 'w', encoding='utf-8') as f:
    f.write('window.COURSE = ' + json.dumps({'chapters': chapters, 'signs': signs}, ensure_ascii=False, separators=(',', ':')) + ';\n')
print(len(chapters), 'chapters,', sum(len(c.get('questions', [])) for c in chapters), 'questions,', len(signs), 'signs ->', out)
