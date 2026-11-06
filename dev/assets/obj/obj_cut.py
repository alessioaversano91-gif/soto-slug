# 1.3.0.82 — cut the level-object sheets (explosive barrel, mystery crate, hostages, market stalls).
# Magenta keyed with a fringe cleanup that only touches pixels next to the background, so lilac hair and lavender survive.
import numpy as np, json, base64, io
from PIL import Image
from scipy import ndimage as nd
MAG=np.array([255,0,255])
def load(f): return np.array(Image.open(f).convert('RGB')).astype(int)
def boxes(a,ymin=0,area=1500):
    fg=np.abs(a-MAG).sum(2)>140
    lab,_=nd.label(nd.binary_dilation(fg,iterations=12)); out=[]
    for s in nd.find_objects(lab):
        y0,y1,x0,x1=s[0].start,s[0].stop,s[1].start,s[1].stop
        if fg[s].sum()>area and y0>=ymin: out.append((y0,y1,x0,x1))
    return out
def cut(a,b):
    y0,y1,x0,x1=b; c=a[y0:y1,x0:x1]
    fg=np.abs(c-MAG).sum(2)>140
    fg=nd.binary_opening(fg,iterations=1)
    lab,n=nd.label(fg); sz=nd.sum(fg,lab,range(1,n+1)); keep=np.isin(lab,1+np.where(sz>=40)[0])
    edge=keep&~nd.binary_erosion(keep,iterations=2)
    pink=(np.minimum(c[...,0],c[...,2])-c[...,1])>60
    keep=keep&~(edge&pink)                                   # magenta fringe on the outline only
    ys,xs=np.where(keep); c=c[ys.min():ys.max()+1,xs.min():xs.max()+1]; keep=keep[ys.min():ys.max()+1,xs.min():xs.max()+1]
    return np.dstack([np.clip(c,0,255),keep*255]).astype(np.uint8)
def base_x(rgba):                                            # center of the lowest quarter: feet / bottom of the object
    m=rgba[...,3]>0; h=m.shape[0]; lo=m[int(h*.75):]; xs=np.where(lo.any(0))[0]; return (xs.min()+xs.max())/2
A={};M={}
def put(key,rgba,k):
    im=Image.fromarray(rgba,'RGBA'); bx=base_x(rgba)
    im=im.resize((max(1,round(im.width*k)),max(1,round(im.height*k))),Image.LANCZOS)
    al=np.array(im)[...,3]; al=np.where(al>110,255,0).astype(np.uint8); arr=np.array(im); arr[...,3]=al; im=Image.fromarray(arr,'RGBA')
    b=io.BytesIO(); im.save(b,'WEBP',quality=92,alpha_quality=100); A[key]='data:image/webp;base64,'+base64.b64encode(b.getvalue()).decode()
    M[key]={'w':im.width,'h':im.height,'ax':round(bx*k),'gy':im.height,'bw':im.width}
def rows(bs,breaks):
    R=[[] for _ in range(len(breaks)+1)]
    for b in bs: R[sum(b[0]>=y for y in breaks)].append(b)
    return [sorted(r,key=lambda b:b[2]) for r in R]
# explosive barrel: one row, 4 states (the blurred ghosts above are skipped)
a=load('barrel.jpg'); bs=sorted(boxes(a,ymin=440),key=lambda b:b[2]); fr=[cut(a,b) for b in bs]; k=66/fr[0].shape[0]
for i,f in enumerate(fr): put(f'obj_barrel{i}',f,k)
# mystery crate: one row, 4 states
a=load('crate.jpg'); bs=sorted(boxes(a,ymin=440),key=lambda b:b[2]); fr=[cut(a,b) for b in bs]; k=62/fr[0].shape[0]
for i,f in enumerate(fr): put(f'obj_crate{i}',f,k)
# hostages: rows tied(2) / freed(4) / give(2) / run(4), standing frame = 128 px
for city,src in [('g','host_genova.jpg'),('l','host_lione.jpg'),('m','host_mantova.jpg'),('s','host_marsiglia.jpg')]:
    a=load(src); R=rows(boxes(a),[300,1150,1805]); R[0]=R[0][:2]
    fr={'tie':[cut(a,b) for b in R[0]],'free':[cut(a,b) for b in R[1]],'give':[cut(a,b) for b in R[2]],'run':[cut(a,b) for b in R[3]]}
    k=128/fr['free'][2].shape[0]
    for kind,L in fr.items():
        for i,f in enumerate(L): put(f'obj_h{city}_{kind}{i}',f,k)
# market stalls: 3 states + loose goods (first four: food), stall 150 px tall
for city,src in [('g','stall_genova.jpg'),('l','stall_lione.jpg'),('m','stall_mantova.jpg'),('s','stall_marsiglia.jpg')]:
    a=load(src); bs=boxes(a,area=5000); big=sorted([b for b in bs if b[1]-b[0]>300],key=lambda b:b[0]); small=sorted([b for b in bs if b[1]-b[0]<=300],key=lambda b:b[2])
    fr=[cut(a,b) for b in big]; k=150/fr[0].shape[0]
    for i,f in enumerate(fr): put(f'obj_st{city}{i}',f,k)
    for i,b in enumerate(small[:4]): put(f'obj_gd{city}{i}',cut(a,b),k)
json.dump(A,open('obj_assets.json','w')); json.dump(M,open('obj_meta.json','w'))
print(len(A),'frames',sum(len(v) for v in A.values())//1024,'KB')
# contact sheet for a visual check
keys=list(A); W=1800; x=y=0; rowh=0; sheet=Image.new('RGB',(W,1400),(80,88,98))
for kk in keys:
    im=Image.open(io.BytesIO(base64.b64decode(A[kk].split(',')[1])))
    if x+im.width>W: x=0; y+=rowh+8; rowh=0
    sheet.paste(im,(x,y),im); x+=im.width+8; rowh=max(rowh,im.height)
sheet.crop((0,0,W,y+rowh+4)).save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/obj_prev.png')
