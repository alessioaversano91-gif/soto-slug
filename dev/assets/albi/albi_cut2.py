# 1.3.0.90 — Albi: parachute (descent, firing, landing), mid-air shot down and mid-air grenade throw
exec(open('albi_cut.py').read().split('H0=131')[0])
import json
from scipy import ndimage as nd
def load_raw(f):                                   # keep the 1-2 px parachute lines (no opening)
    a=np.array(Image.open(f).convert('RGB')).astype(int); fg=np.abs(a-MAG).sum(2)>150
    pink=(np.minimum(a[...,0],a[...,2])-a[...,1])>45; fg&=~pink
    lab,n=nd.label(fg); sz=nd.sum(fg,lab,range(1,n+1)); fg=np.isin(lab,1+np.where(sz>=30)[0]); return a,fg
def flash_off(f,x0):                              # keep only dark gun metal right of x0 (muzzle flash out)
    f=f.copy(); dark=f[...,:3].max(2)<125; f[:,int(x0):,3]=np.where(dark[:,int(x0):],f[:,int(x0):,3],0); return tight(f)
cur=json.load(open('albi_meta.json')); A0=json.load(open('albi_assets.json'))
def h_of(key): return Image.open(io.BytesIO(base64.b64decode(A0[key].split(',')[1]))).height
# sheet 11: hanging, landing (canopy collapsing), standing next to the folded chute
a,fg=load_raw('s11.jpg')
stand=frame(a,fg,(951,1335,1272,1539)); stand[-50:,:28,3]=0; stand=tight(stand)
k=131/stand.shape[0]
put('albi_n_para0',frame(a,fg,(400,1219,28,555)),k); put('albi_n_paraland',frame(a,fg,(749,1333,571,1025)),k); put('albi_n_paraready',stand,k,'r')
# sheet 12: firing while hanging (straight; the second, aimed down, is skipped)
a,fg=load_raw('s12.jpg'); f=frame(a,fg,(280,1225,59,741)); x=np.where((f[...,3]>0)&(f[...,:3].max(2)<125))[1]
# muzzle: rightmost dark pixel in the gun band; the flash beyond it goes
band=f[int(f.shape[0]*.62):int(f.shape[0]*.78)]; dk=np.where(((band[...,3]>0)&(band[...,:3].max(2)<125)).any(0))[0]
f=flash_off(f,dk.max()+2); w0=frame(*load_raw('s11.jpg'),(400,1219,28,555)).shape[1]
can=lambda g: np.where((g[...,3]>0)[:int(g.shape[0]*.3)].any(0))[0]
f0=frame(*load_raw('s11.jpg'),(400,1219,28,555)); k2=k*(np.ptp(can(f0))/np.ptp(can(f)))
put('albi_n_parafire',f,k2,'r')
# sheet 13: in the air - gun pointing down (2), grenade throw (3); same height as the new jump pose
a,fg=load('s13.png'); R=rows(boxes(fg)); k3=h_of('albi_n_jump0')/R[1][0].shape[0] if False else None
fr=[[frame(a,fg,b) for b in r] for r in R]; k3=h_of('albi_n_jump0')/fr[1][1].shape[0]
for i,g in enumerate(fr[0]): put(f'albi_n_jdn{i}',g,k3,'d')
for i,g in enumerate(fr[1]): put(f'albi_n_jthrow{i}',g,k3)
# 'd' frames: muzzle = lowest dark pixel of the gun
for i,g in enumerate(fr[0]):
    m=(g[...,3]>0)&(g[...,:3].max(2)<90); ys,xs=np.where(m[:, int(g.shape[1]*.5):]); y=ys.max(); x=xs[ys==y].mean()+int(g.shape[1]*.5)
    OUT_M[f'albi_n_jdn{i}']=[OUT_M[f'albi_n_jdn{i}'][0],round(x/g.shape[1],3),round(y/g.shape[0],3)]
A0.update(OUT_A); cur.update(OUT_M); json.dump(A0,open('albi_assets.json','w')); json.dump(cur,open('albi_meta.json','w'))
print({k_:(Image.open(io.BytesIO(base64.b64decode(v.split(',')[1]))).size,OUT_M[k_]) for k_,v in OUT_A.items()})
ims=[Image.open(io.BytesIO(base64.b64decode(v.split(',')[1]))) for v in OUT_A.values()]
sh=Image.new('RGB',(sum(i.width+10 for i in ims),max(i.height for i in ims)),(70,78,90)); x=0
for i in ims: sh.paste(i,(x,sh.height-i.height),i); x+=i.width+10
sh.save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/albi_new2.png')
