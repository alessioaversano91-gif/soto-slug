# Assemble from build_bundle.json (generated data) + game_template.html (engine). Used since the 1.3.0.63 beta.
import json
import os; os.chdir(os.path.dirname(os.path.abspath(__file__))); B=json.load(open('build_bundle.json')); t=open('game_template.html').read()
for k,v in B.items(): assert t.count(k)==1,k; t=t.replace(k,v)
open('/mnt/user-data/outputs/soto_slug_tex_edition.html','w').write(t); print(len(t)//1024,'KB')
