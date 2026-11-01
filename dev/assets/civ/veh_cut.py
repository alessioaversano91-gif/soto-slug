# Vehicles for the Genova levels (1.3.0.68): van (v) and Carabinieri car (c). Same pipeline as civ_build.py.
# Rows are cut with fixed slots; the sheet titles (top-left of each row) are masked out.
import numpy as np, json, base64, io, cv2
from PIL import Image
V={
 'v':{'src':'van.jpg','target':280,'hp':16,'rows':{
   'r1':(82,196,[[27,262],[279,516],[530,766],[776,1013]],None),
   'r2':(205,386,[[20,272],[276,520],[522,770],[776,1014]],(250,270)),
   'r3':(390,575,[[12,270],[270,520],[520,772],[772,1020]],(434,215)),
   'r4':(586,762,[[90,560],[590,880]],(636,420))},
   'use':{'idle':['r1:0'],'drive':['r1:1','r1:2','r1:3'],'dmg':['r2:0'],'burn':['r2:1'],'boom':['r2:2'],'wreck':['r2:3'],
          'alarm':['r3:0','r3:1','r3:2','r3:3'],'peel':['r4:0'],'warn':['r4:1']}},
 'c':{'src':'carab.jpg','target':250,'hp':14,'rows':{
   'r1':(165,392,[[45,625],[665,1215],[1222,1772],[1780,2330]],None),
   'r2':(450,850,[[25,645],[648,1240],[1240,1792],[1792,2344]],(592,660)),
   'r3':(885,1322,[[22,790],[800,1580]],(1000,520)),
   'r4':(1365,1785,[[90,1230],[1440,2260]],(1482,900))},
   'use':{'idle':['r1:0'],'drive':['r1:1','r1:2','r1:3'],'dmg':['r2:0'],'burn':['r2:1'],'boom':['r2:2'],'wreck':['r2:3'],
          'alarm':['r3:0','r3:1'],'peel':['r4:0'],'warn':['r4:1']}}}
def frame(a,bg,y0,y1,x0,x1,title):
    c=a[y0:y1,x0:x1].copy()
    d=np.abs(c-bg).sum(2); mag=(np.minimum(c[...,0],c[...,2])-c[...,1])>80
    m=((d>110)&~mag).astype(np.uint8)
    if title: ty,tx=title; m[:max(0,ty-y0),:max(0,tx-x0)]=0
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(m,8); keep=np.zeros_like(m)
    for i in range(1,n):
        if st[i,4]>=18: keep[lab==i]=1
    pink=(np.minimum(c[...,0],c[...,2])-c[...,1])>28; g=c.mean(2,keepdims=True).repeat(3,2)*.85; c=np.where(pink[...,None],g,c)   # magenta cast -> grey
    ys,xs=np.where(keep); c=c[ys.min():ys.max()+1,xs.min():xs.max()+1]; keep=keep[ys.min():ys.max()+1,xs.min():xs.max()+1]
    colh=keep.sum(0); body=np.where(colh>=colh.max()*.55)[0]; bl,br=int(body.min()),int(body.max())
    gy=int(np.where(keep[:,bl:br+1].any(1))[0].max())
    return np.dstack([np.clip(c,0,255),keep*255]).astype(np.uint8),bl,br,gy
A={};M={};INFO={}
for vid,cfg in V.items():
    a=np.array(Image.open(cfg['src']).convert('RGB')).astype(int)
    bg=np.median(np.concatenate([a[:,:4].reshape(-1,3),a[:,-4:].reshape(-1,3)]),axis=0)
    cut={}
    for rn,(y0,y1,slots,title) in cfg['rows'].items():
        for i,(x0,x1) in enumerate(slots): cut[f'{rn}:{i}']=frame(a,bg,y0,y1,x0,x1,title)
    _,bl,br,_=cut['r1:0']; k=cfg['target']/(br-bl); INFO[vid]={'hp':cfg['hp']}
    for kind,frames in cfg['use'].items():
        for i,fr in enumerate(frames):
            rgba,bl,br,gy=cut[fr]; im=Image.fromarray(rgba,'RGBA')
            im=im.resize((max(1,round(im.width*k)),max(1,round(im.height*k))),Image.LANCZOS if k<1 else Image.NEAREST)
            x=np.array(im); x[...,3]=np.where(x[...,3]>127,255,0); im=Image.fromarray(x,'RGBA')
            key=f'civ{vid}_{kind}'+(str(i) if len(frames)>1 else '')
            b=io.BytesIO(); im.save(b,'WEBP',quality=92,alpha_quality=100); A[key]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
            if kind in ('peel','warn'): M[key]={'w':im.width,'h':im.height,'ax':round(br*k)-cfg['target'],'gy':round(gy*k),'bw':cfg['target']}   # smoke trails behind: anchor on the front bumper
            else: M[key]={'w':im.width,'h':im.height,'ax':round(bl*k),'gy':round(gy*k),'bw':round((br-bl)*k)}
json.dump(A,open('veh_assets.json','w')); json.dump(M,open('veh_meta.json','w')); json.dump(INFO,open('veh_info.json','w'))
print(len(A),'frames',sum(len(v) for v in A.values())//1024,'KB'); [print(k,M[k]) for k in ['civv_idle','civc_idle','civv_boom','civc_peel']]
# preview
ks=list(A); cols=6; cw=330; ch=230
o=Image.new('RGB',(cols*cw,((len(ks)+cols-1)//cols)*ch),(90,96,104))
from PIL import ImageDraw; d=ImageDraw.Draw(o)
for i,kk in enumerate(ks):
    im=Image.open(io.BytesIO(base64.b64decode(A[kk].split(',')[1]))); x=(i%cols)*cw+5; y=(i//cols)*ch+ch-12
    if im.width>cw-10: im=im.resize((cw-10,int(im.height*(cw-10)/im.width)))
    o.paste(im,(x,y-im.height),im); d.line([(x,y),(x+cw-15,y)],fill=(255,255,0)); d.text((x,(i//cols)*ch+3),kk,fill=(255,255,255))
o.save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/veh_prev.png')
