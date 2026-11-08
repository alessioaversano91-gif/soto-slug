# 1.3.0.86 — new Albi sheets: model, idle, walk, run, fire (straight/diagonal/up), jump, crouch, throw, hurt, defeat, victory.
# Every sheet gets one scale from a standing reference frame, frames sit on the feet, muzzle flashes are trimmed (the game draws its own).
from albi_common import *
OUT_A={}; OUT_M={}
def frame(a,fg,b):
    y0,y1,x0,x1=b; m=fg[y0:y1,x0:x1]; ys,xs=np.where(m)
    c=a[y0:y1,x0:x1][ys.min():ys.max()+1,xs.min():xs.max()+1]; m=m[ys.min():ys.max()+1,xs.min():xs.max()+1]
    return np.dstack([np.clip(c,0,255),m*255]).astype(np.uint8)
def feet_x(f):
    m=f[...,3]>0; h=m.shape[0]; lo=m[int(h*.82):]; xs=np.where(lo.any(0))[0]; return (xs.min()+xs.max())/2
def _dark_only(f,mask):                              # in the muzzle zone keep only the dark gun metal: flash and smoke go
    f=f.copy(); rgb=f[...,:3].astype(int); dark=rgb.max(2)<125; f[...,3]=np.where(mask&~dark,0,f[...,3]); return f
def trim_right(f,limit):
    m=np.zeros(f.shape[:2],bool); m[:,max(0,int(limit)-30):]=True; f=_dark_only(f,m); f[:,int(limit)+6:,3]=0; return tight(f)
def trim_top(f,limit):
    m=np.zeros(f.shape[:2],bool); m[:max(0,int(limit)+30),:]=True; f=_dark_only(f,m); return tight(f)
def tight(f):
    ys,xs=np.where(f[...,3]>0); return f[ys.min():ys.max()+1,xs.min():xs.max()+1]
def tip_right(f):                                       # rightmost pixel in the upper 60% = gun muzzle
    m=f[...,3]>0; h=m.shape[0]; up=m[:int(h*.62)]; cols=np.where(up.any(0))[0]; x=cols.max(); ys=np.where(up[:,max(0,x-5):x+1].any(1))[0]; return x,ys.mean()
def tip_up(f):
    m=f[...,3]>0; ys=np.where(m.any(1))[0]; y=ys.min(); xs=np.where(m[y:y+6].any(0))[0]; return xs.mean(),y
def put(key,f,k,gun=None):
    im=Image.fromarray(f,'RGBA'); fx=feet_x(f); W,H=im.size
    im=im.resize((max(1,round(W*k)),max(1,round(H*k))),Image.LANCZOS)
    arr=np.array(im); arr[...,3]=np.where(arr[...,3]>110,255,0); im=Image.fromarray(arr,'RGBA')
    b=io.BytesIO(); im.save(b,'WEBP',quality=92,alpha_quality=100); OUT_A[key]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
    meta=[round(fx/W,3),1.0,0.35]
    if gun=='r': x,y=tip_right(f); meta=[round(fx/W,3),round(x/W,3),round(y/H,3)]
    if gun=='u': x,y=tip_up(f); meta=[round(fx/W,3),round(x/W,3),round(y/H,3)]
    OUT_M[key]=meta
def sheet(i):
    a,fg=load(f's{i}.jpg'); R=rows(boxes(fg)); return [[frame(a,fg,b) for b in r] for r in R]
H0=131
# 1 model sheet: side view = character select
R=sheet(1); k=H0/R[0][0].shape[0]; put('albi_n_sel',R[0][0],k); put('albi_n_front',R[0][1],k)
# 2 idle (4) + walk with the gun raised (8)
R=sheet(2); k=H0/R[0][0].shape[0]
for i,f in enumerate(R[0]): put(f'albi_n_idle{i}',f,k,'r')
for i,f in enumerate(R[1]+R[2]): put(f'albi_n_walk{i}',f,k,'r')
# 3 run (8)
R=sheet(3); k=126/R[0][3].shape[0]
for i,f in enumerate(R[0]+R[1]): put(f'albi_n_run{i}',f,k,'r')
# 4 fire straight / diagonal / up: aim, shot (flash trimmed), recover (smoke trimmed)
R=sheet(4); k=H0/R[0][0].shape[0]
for row,name,mode in [(0,'fire','r'),(1,'diag','r'),(2,'up','u')]:
    aim=R[row][0]; ax=feet_x(aim)
    if mode=='r': tx,_=tip_right(aim); lim=lambda f: feet_x(f)+(tx-ax)+4
    else: _,ty=tip_up(aim)
    for i,f in enumerate(R[row]):
        if i>0 and mode=='r': f=trim_right(f,lim(f))
        if i>0 and mode=='u': f=trim_top(f,f.shape[0]-(aim.shape[0]-ty)-4)
        put(f'albi_n_{name}{i}',f,k,mode)
# 5 jump: bare-handed arc (5, kept for later) + mid-air with the gun: aim, shot, recover
R=sheet(5); k=H0/R[0][3].shape[0]
for i,f in enumerate(R[0]): put(f'albi_n_jumpb{i}',f,k)
aim=R[1][0]; tx,_=tip_right(aim); ax=feet_x(aim)
for i,f in enumerate(R[1]):
    if i>0: f=trim_right(f,feet_x(f)+(tx-ax)+4)
    put(f'albi_n_jump{i}',f,k,'r')
# 6 crouch: bare (2), with the gun (2, second with a shot)
R=sheet(6); k=H0/R[1][1].shape[0]
for i,f in enumerate(R[0]):
    if i==3: aim=R[0][2]; tx,_=tip_right(aim); f=trim_right(f,feet_x(f)+(tx-feet_x(aim))+4)
    put(f'albi_n_crouch{i}',f,k,'r' if i>=2 else None)
# 7 grenade throw: standing (4), low (3)
R=sheet(7); k=H0/R[0][0].shape[0]
for i,f in enumerate(R[0]): put(f'albi_n_throw{i}',f,k)
for i,f in enumerate(R[1]): put(f'albi_n_cthrow{i}',f,k)
# 8 hurt and getting up
R=sheet(8); k=128/R[1][3].shape[0]
for i,f in enumerate(R[0]): put(f'albi_n_hurt{i}',f,k)
for i,f in enumerate(R[1]): put(f'albi_n_getup{i}',f,k)
# 9 defeat and victory
R=sheet(9); k=H0/R[1][0].shape[0]
for i,f in enumerate(R[0]): put(f'albi_n_die{i}',f,k)
for i,f in enumerate(R[1]): put(f'albi_n_win{i}',f,k)
json.dump(OUT_A,open('albi_assets.json','w')); json.dump(OUT_M,open('albi_meta.json','w'))
print(len(OUT_A),'frames',sum(len(v) for v in OUT_A.values())//1024,'KB')
# contact sheet on the feet line
ims=[(k_,Image.open(io.BytesIO(base64.b64decode(v.split(',')[1])))) for k_,v in OUT_A.items()]
Wd=1900; x=0; y=0; rowh=170; sh=Image.new('RGB',(Wd,1400),(70,78,90))
from PIL import ImageDraw; d=ImageDraw.Draw(sh)
for k_,im in ims:
    if x+im.width+10>Wd: x=0; y+=rowh
    sh.paste(im,(x,y+150-im.height),im); m=OUT_M[k_]; d.line([(x+int(m[0]*im.width),y+150),(x+int(m[0]*im.width),y+156)],fill=(255,0,0))
    if m[1]<1 or k_.startswith(('albi_n_fire','albi_n_walk','albi_n_run','albi_n_up','albi_n_jump','albi_n_idle')): d.ellipse([x+m[1]*im.width-2,y+150-im.height+m[2]*im.height-2,x+m[1]*im.width+2,y+150-im.height+m[2]*im.height+2],outline=(0,255,0))
    d.text((x,y+156),k_[7:],fill=(255,255,160)); x+=im.width+14
sh.crop((0,0,Wd,y+rowh)).save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/albi_new.png')
