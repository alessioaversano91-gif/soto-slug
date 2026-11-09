# 1.3.0.95 — Albi running while aiming straight up (8) and diagonally up (8)
exec(open('albi_cut.py').read().split('H0=131')[0])
import json
a,fg=load('s14.jpg'); R=rows(boxes(fg))
up=[frame(a,fg,b) for b in R[0]]; dg=[frame(a,fg,b) for b in R[1]]
k=124/np.median([f.shape[0] for f in dg])          # same height as the walk/run cycle
for i,f in enumerate(up): put(f'albi_n_rup{i}',f,k,'u')
for i,f in enumerate(dg):
    put(f'albi_n_rdiag{i}',f,k)
    m=(f[...,3]>0)&(f[...,:3].max(2)<90); ys,xs=np.where(m[:int(f.shape[0]*.55)])
    j=np.argmax(xs-ys); OUT_M[f'albi_n_rdiag{i}'][1:]=[round(xs[j]/f.shape[1],3),round(ys[j]/f.shape[0],3)]   # up-right tip of the barrel
A0=json.load(open('albi_assets.json')); M0=json.load(open('albi_meta.json')); A0.update(OUT_A); M0.update(OUT_M)
json.dump(A0,open('albi_assets.json','w')); json.dump(M0,open('albi_meta.json','w'))
from PIL import ImageDraw
ims=[(k_,Image.open(io.BytesIO(base64.b64decode(v.split(',')[1])))) for k_,v in OUT_A.items()]
S=Image.new('RGB',(8*110,2*190),(70,78,90)); d=ImageDraw.Draw(S)
for n,(k_,im) in enumerate(ims):
    x=(n%8)*110; y=(n//8)*190+180-im.height; S.paste(im,(x,y),im); m=OUT_M[k_]; d.ellipse([x+m[1]*im.width-3,y+m[2]*im.height-3,x+m[1]*im.width+3,y+m[2]*im.height+3],outline=(0,255,0))
S.save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/albi_rup.png'); print({k_:(im.size,OUT_M[k_]) for k_,im in ims[:2]+ims[8:10]})
