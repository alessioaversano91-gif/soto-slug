# Civilian car 1 -> sprites for the engine: civw_* (white), civg_* (green). Scaled so the car body is ~200 px wide.
import numpy as np, json, base64, io, cv2
from PIL import Image
J=json.load(open('civ_cut.json'))
TARGET_W=220   # 1.3.0.74: +10%
USE={  # engine key : (sheet frame, ...)
 'w':{'idle':['white_idle0'],'drive':['white_idle1','white_idle2','white_idle3','white_idle4'],'alarm':['wx_alarm0','wx_alarm1','wx_alarm2','wx_alarm3'],
      'dmg':['white_boom0'],'burn':['white_boom1'],'boom':['white_boom2'],'wreck':['white_boom3'],'peel':['wx_peel0','wx_peel1','wx_peel2','wx_peel3'],'warn':['white_flee2'],'driver':['white_flee0']},
 'g':{'idle':['green_idle0'],'drive':['green_idle1','green_idle2','green_idle3','green_idle4'],'alarm':['green_alarm0','green_alarm1','green_alarm2','green_alarm3','green_alarm4','green_alarm5'],
      'dmg':['green_boom0'],'burn':['green_boom1'],'boom':['green_boom2'],'wreck':['green_boom3'],'peel':['green_flee0','green_flee1'],'warn':['green_flee2'],'driver':['green_flee0']}}
cache={}
def sheet(f):
    if f not in cache:
        a=np.array(Image.open(f).convert('RGB')).astype(int)
        bg=np.median(np.concatenate([a[:,:4].reshape(-1,3),a[:,-4:].reshape(-1,3)]),axis=0); cache[f]=(a,bg)
    return cache[f]
def cut(fr):
    v=J[fr]; a,bg=sheet(v['src']); x0,y0,x1,y1=v['box']; c=a[y0:y1,x0:x1].copy()
    d=np.abs(c-bg).sum(2); green=bg[1]>200
    tint=(c[...,1]-np.maximum(c[...,0],c[...,2])>60) if green else (np.minimum(c[...,0],c[...,2])-c[...,1]>80)
    m=((d>110)&~tint).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((2,2),np.uint8))
    n,lab,st,_=cv2.connectedComponentsWithStats(m,8)          # drop specks
    keep=np.zeros_like(m)
    for i in range(1,n):
        if st[i,4]>=12: keep[lab==i]=1
    edge=(cv2.dilate(keep,np.ones((3,3),np.uint8))-cv2.erode(keep,np.ones((3,3),np.uint8)))>0
    if green: c[...,1]=np.where(edge,np.minimum(c[...,1],np.maximum(c[...,0],c[...,2])+10),c[...,1])   # de-spill
    else:
        lo=np.minimum(c[...,0],c[...,2]); c[...,0]=np.where(edge&(lo>c[...,1]+30),np.minimum(c[...,0],c[...,1]+30),c[...,0]); c[...,2]=np.where(edge&(lo>c[...,1]+30),np.minimum(c[...,2],c[...,1]+30),c[...,2])
    if not green:      # magenta sheet: glass and smoke picked up a pink cast -> neutral grey
        mag=(np.minimum(c[...,0],c[...,2])-c[...,1])>28; g=c.mean(2,keepdims=True).repeat(3,2)*.85; c=np.where(mag[...,None],g,c)
    rgba=np.dstack([np.clip(c,0,255),keep*255]).astype(np.uint8)
    # car body: columns where the mask is tall -> rear edge (left) and width; ground: lowest pixel under the body
    colh=keep.sum(0); body=np.where(colh>=colh.max()*.55)[0]; bl,br=int(body.min()),int(body.max())
    rows=np.where(keep[:,bl:br+1].any(1))[0]; gy=int(rows.max())
    return rgba,bl,br,gy
A={};M={}
for col,U in USE.items():
    ref=None
    for kind,frames in U.items():
        for i,fr in enumerate(frames):
            rgba,bl,br,gy=cut(fr)
            src='wx' if fr.startswith('wx') else 'ab'
            k=TARGET_W/(150 if src=='ab' else 214)      # body widths measured on the idle frames of each sheet
            im=Image.fromarray(rgba,'RGBA'); w,h=im.size; im=im.resize((max(1,round(w*k)),max(1,round(h*k))),Image.NEAREST if k>1 else Image.LANCZOS)
            a=np.array(im); a[...,3]=np.where(a[...,3]>127,255,0); im=Image.fromarray(a,'RGBA')
            key=f'civ{col}_{kind}'+(str(i) if len(frames)>1 else '')
            b=io.BytesIO(); im.save(b,'WEBP',quality=94,alpha_quality=100); A[key]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
            M[key]={'w':im.width,'h':im.height,'ax':round(bl*k),'gy':round(gy*k),'bw':round((br-bl)*k)}
json.dump(A,open('civ_assets.json','w')); json.dump(M,open('civ_meta.json','w'))
print(len(A),'frames', sum(len(v) for v in A.values())//1024,'KB')
for k in ['civw_idle','civw_alarm1','civw_peel1','civw_boom','civg_idle','civg_alarm3','civg_peel1']: print(k,M[k])
