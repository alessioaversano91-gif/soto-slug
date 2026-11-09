# 1.3.0.96 — Seba running while aiming the UZI straight up (3 frames)
import sys; sys.path.insert(0,'../albi')
exec(open('../albi/albi_cut.py').read().split('H0=131')[0])
import json
a,fg=load('s1.png')
c=a.astype(int); fg&=~(((c[...,0]-c[...,1])>45)&((c[...,2]-c[...,1])>45))     # small soft image: drop the magenta halo too
from scipy import ndimage as nd
lab,n=nd.label(fg); sz=nd.sum(fg,lab,range(1,n+1)); fg=np.isin(lab,1+np.where(sz>=25)[0])
W=a.shape[1]; fr=[]
for i in range(3):
    x0,x1=i*W//3,(i+1)*W//3; ys,xs=np.where(fg[:,x0:x1]); fr.append(frame(a,fg,(ys.min(),ys.max()+1,x0+xs.min(),x0+xs.max()+1)))
A=json.loads(json.load(open('../../build_bundle.json'))['__ASSETS__'])
ref=Image.open(io.BytesIO(base64.b64decode(A['seba_guup1'].split(',')[1])))
def hat_top(f):                      # first row with the beige hat (under the gun)
    c=f[...,:3].astype(int); m=(f[...,3]>0)&(c[...,0]>150)&(c[...,1]>120)&(c[...,2]<150)&(c[...,0]-c[...,2]>25)
    return np.where(m.any(1))[0][0]
def unpink(f):                        # magenta spill on edges and shoes -> neutral grey
    f=f.copy(); c=f[...,:3].astype(int); m=(c[...,0]-c[...,1]>18)&(c[...,2]-c[...,1]>18)
    g=(c[...,0]+c[...,1]+c[...,2])//3; 
    for ch in range(3): f[...,ch]=np.where(m,g,f[...,ch])
    return f
fr=[unpink(f) for f in fr]
body=np.median([f.shape[0]-hat_top(f) for f in fr]); k=126/body     # hat-to-feet a little taller than his running frames: this sheet draws him slimmer, so the same height looked smaller
for i,f in enumerate(fr): put(f'seba_n_rup{i}',f,k,'u')
json.dump(OUT_A,open('seba_assets.json','w')); json.dump(OUT_M,open('seba_meta.json','w'))
ims=[ref]+[Image.open(io.BytesIO(base64.b64decode(v.split(',')[1]))) for v in OUT_A.values()]
S=Image.new('RGB',(sum(i.width+10 for i in ims),150),(70,78,90)); x=0
for i in ims: S.paste(i,(x,145-i.height),i.convert('RGBA')); x+=i.width+10
S.resize((S.width*2,300),Image.NEAREST).save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/seba_rup.png'); print(k,OUT_M)
