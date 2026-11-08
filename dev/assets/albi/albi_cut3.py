# 1.3.0.91 — Albi: slide and roll (sheet 10, captions ignored); stored for a later move, not in the bundle yet
exec(open('albi_cut.py').read().split('H0=131')[0])
import json
a,fg=load('s10.jpg'); R=rows(boxes(fg)); figs=R[0]+R[2]
k=124/figs[7].shape[0] if False else None
fr=[frame(a,fg,b) for b in (R[0][:2]+[(280,635,1480,1970)]+R[0][3:]+R[2])]
k=124/fr[7].shape[0]
names=['slide0','slide1','slide2','slide3','roll0','roll1','roll2','roll3']
for n,f in zip(names,fr): put('albi_n_'+n,f,k)
A=json.load(open('albi_assets.json')); M=json.load(open('albi_meta.json')); A.update(OUT_A); M.update(OUT_M)
json.dump(A,open('albi_assets.json','w')); json.dump(M,open('albi_meta.json','w'))
ims=[Image.open(io.BytesIO(base64.b64decode(v.split(',')[1]))) for v in OUT_A.values()]
sh=Image.new('RGB',(sum(i.width+10 for i in ims),max(i.height for i in ims)),(70,78,90)); x=0
for i in ims: sh.paste(i,(x,sh.height-i.height),i); x+=i.width+10
sh.save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/albi_slide.png'); print({k_:v for k_,v in OUT_M.items()})
