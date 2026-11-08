# 1.3.0.93 — new Alecio sheets (AK): model, idle, walk, run, fire 3 directions, jump, crouch, throw, hurt/knockdown, defeat, victory, slide/roll
import sys; sys.path.insert(0,'../albi')
exec(open('../albi/albi_cut.py').read().split('H0=131')[0])
from scipy import ndimage as nd
import json
def split(fg,b,n):                     # cut a merged box into n frames at the emptiest columns near the even split points
    y0,y1,x0,x1=b; col=fg[y0:y1,x0:x1].sum(0); w=x1-x0; cuts=[0]
    for i in range(1,n):
        c=int(w*i/n); r=int(w/n*.22); seg=col[c-r:c+r]; cuts.append(c-r+int(np.argmin(seg)))
    cuts.append(w); return [(y0,y1,x0+cuts[i],x0+cuts[i+1]) for i in range(n)]
def clean(fg,b,keep=.04):              # keep the main figure (and big pieces like a grenade), drop slivers of the neighbours
    y0,y1,x0,x1=b; m=fg[y0:y1,x0:x1]; lab,n=nd.label(m)
    if n<=1: return
    sz=nd.sum(m,lab,range(1,n+1)); big=sz.max(); bad=[i+1 for i,s in enumerate(sz) if s<big*keep]
    # slivers touching the left/right cut edge are neighbours' parts
    for i,s in enumerate(sz):
        if s<big*.25:
            ys,xs=np.where(lab==i+1)
            if xs.min()==0 or xs.max()==m.shape[1]-1: bad.append(i+1)
    m[np.isin(lab,bad)]=False
def grab(a,fg,b,keep=.04): clean(fg,b,keep); return frame(a,fg,b)
def row(a,fg,R,spec):                  # spec: frames per detected box
    out=[]
    for b,n in zip(R,spec): out+= [grab(a,fg,c) for c in (split(fg,b,n) if n>1 else [b])]
    return out
H0=130; P='alecio_n_'
def sh(i): a,fg=load(f's{i}.jpg'); return a,fg,rows(boxes(fg))
# 1 model
a,fg,R=sh(1); f=row(a,fg,R[0],[1,1,1]); k=H0/f[0].shape[0]; put(P+'sel',f[0],k); put(P+'front',f[1],k)
# 2 idle (5) + walk with the gun (6)
a,fg,R=sh(2); idle=row(a,fg,R[0],[3,1,1]); walk=row(a,fg,R[1],[6]); k=H0/idle[0].shape[0]
for i,f in enumerate(idle): put(P+f'idle{i}',f,k,'r')
kw=H0/np.median([f.shape[0] for f in walk])
for i,f in enumerate(walk): put(P+f'walk{i}',f,kw,'r')
# 3 run (17)
a,fg,R=sh(3); rr=[row(a,fg,R[0],[1,1,3]),row(a,fg,R[1],[1]*5),row(a,fg,R[2],[1]*5),row(a,fg,R[3],[1,1])]
ref=np.median([f.shape[0] for f in rr[2]]); i=0     # every row of this sheet is drawn at its own size: each one is matched to row 3
for r in rr:
    k=H0/ref*(ref/np.median([f.shape[0] for f in r])) if r is not rr[1] else H0/ref*(ref/np.median([f.shape[0] for f in r]))*.97
    for f in r: put(P+f'run{i}',f,k,'r'); i+=1
# 4 fire straight / diagonal / up (aim, shot without flash)
a,fg,R=sh(4); k=H0/grab(a,fg,R[0][0]).shape[0]
for r,name,mode in [(0,'fire','r'),(1,'diag','r'),(2,'up','u')]:
    aim=grab(a,fg,R[r][0]); shot=grab(a,fg,R[r][1])
    if mode=='r': tx,_=tip_right(aim); shot=trim_right(shot,feet_x(shot)+(tx-feet_x(aim))+4)
    else: _,ty=tip_up(aim); shot=trim_top(shot,shot.shape[0]-(aim.shape[0]-ty)-4)
    put(P+name+'0',aim,k,mode); put(P+name+'1',shot,k,mode)

# 5 jump bare (5) + standing shots row (aim, shot, recover)
a,fg,R=sh(5); jb=row(a,fg,R[0],[1]*5); k5=H0/grab(a,fg,R[1][0]).shape[0]


# 6 crouch: bare (2), with the gun (aim, shot) + crouched walk (6)
a,fg,R=sh(6); c0=row(a,fg,R[0],[1,1,1,1]); k6=k5*0+H0/grab(a,fg,split(fg,R[1][0],6)[0]).shape[0]*0.0+ (H0/c0[2].shape[0])*(c0[2].shape[0]/c0[2].shape[0])
aim=c0[2]; tx,_=tip_right(aim); c0[3]=trim_right(c0[3],feet_x(c0[3])+(tx-feet_x(aim))+4)
k6=H0/c0[2].shape[0]   # standing aim frame = standing height
for i,f in enumerate(c0): put(P+f'crouch{i}',f,k6*(1.0),'r' if i>=2 else None)
for i,f in enumerate(row(a,fg,R[1],[6])): put(P+f'cwalk{i}',f,k6,'r')
# 7 throw standing (4) + low (3)
a,fg,R=sh(7); t=row(a,fg,R[0],[1]*4); ct=row(a,fg,R[2],[1]*3); k7=H0/t[0].shape[0]
for i,f in enumerate(t): put(P+f'throw{i}',f,k7)
for i,f in enumerate(ct): put(P+f'cthrow{i}',f,k7)
# 8 hurt + knockdown / getting up
a,fg,R=sh(8); h=row(a,fg,R[0],[1]*4); g=row(a,fg,R[1],[1]*4); k8=H0/g[2].shape[0]
for i,f in enumerate(h): put(P+f'hurt{i}',f,k8)
for i,f in enumerate(g): put(P+f'getup{i}',f,k8)
# 9 defeat + victory
a,fg,R=sh(9); d=row(a,fg,R[0],[1]*4); w=row(a,fg,R[1],[1]*4); k9=H0/w[0].shape[0]
for i,f in enumerate(d): put(P+f'die{i}',f,k9)
def no_light(f,beige=False):         # drop the bright flash / dust pixels (the game draws its own)
    f=f.copy(); c=f[...,:3].astype(int)
    m=(c.min(2)>150)|((c[...,0]>200)&(c[...,1]>170)&(c[...,2]<170)) if not beige else ((c[...,0]>140)&(c[...,1]>115)&(c[...,2]>95)&(c[...,0]-c[...,2]<90))
    f[...,3]=np.where(m,0,f[...,3]); return tight(f)
w[3]=no_light(w[3])
for i,f in enumerate(w): put(P+f'win{i}',f,k9)
# 10 slide + roll
a,fg,R=sh(10); s=row(a,fg,R[0],[1]*4); r=row(a,fg,R[1],[1]*4); k10=(H0*.95)/r[3].shape[0]
b=R[0][2]; s[2]=no_light(grab(a,fg,(b[0],b[1],b[2]+int((b[3]-b[2])*.30),b[3])),True)   # dust cloud on the left goes
for i,f in enumerate(s): put(P+f'slide{i}',f,k10)
for i,f in enumerate(r): put(P+f'roll{i}',f,k10)
json.dump(OUT_A,open('alecio_assets.json','w')); json.dump(OUT_M,open('alecio_meta.json','w'))
ims=[(k_,Image.open(io.BytesIO(base64.b64decode(v.split(',')[1])))) for k_,v in OUT_A.items()]
from PIL import ImageDraw
Wd=1900; x=0; y=0; rowh=175; S=Image.new('RGB',(Wd,1800),(70,78,90)); d_=ImageDraw.Draw(S)
for k_,im in ims:
    if x+im.width+10>Wd: x=0; y+=rowh
    S.paste(im,(x,y+150-im.height),im); m=OUT_M[k_]
    if m[1]<1: d_.ellipse([x+m[1]*im.width-3,y+150-im.height+m[2]*im.height-3,x+m[1]*im.width+3,y+150-im.height+m[2]*im.height+3],outline=(0,255,0))
    d_.text((x,y+156),k_[9:],fill=(255,255,160)); x+=im.width+12
S.crop((0,0,Wd,y+rowh)).save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/alecio_new.png'); print(len(OUT_A))
