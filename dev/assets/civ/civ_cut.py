# Civilian car 1 (white / green): cut the sheets into frames. Titles on the sheets are ignored.
import numpy as np, json, sys
from PIL import Image
SHEETS={
 'white':('civ1_white.jpg',[('idle',42,140,5),('boom',145,282,4),('alarm',286,428,6),('flee',438,566,3)]),
 'green':('civ1_green.jpg',[('idle',42,140,5),('boom',145,282,4),('alarm',286,428,6),('flee',438,566,3)]),
 'wx':   ('civ1_white_extra.jpg',[('soto',70,210,3),('alarm',266,438,4),('peel',505,662,4)])}
TITLE_X=330
# fixed slots where effects (smoke, sound waves) touch the next frame
SLOTS={('ab','alarm'):[[22,184],[188,351],[354,519],[522,683],[686,848],[852,1014]],
       ('ab','flee'):[[38,198],[199,352],[353,512]],
       ('wx','alarm'):[[26,268],[272,522],[524,770],[772,1014]],
       ('wx','peel'):[[42,282],[283,532],[533,774],[775,1020]]}
def fgmask(a,bg):
    d=np.abs(a-bg).sum(2)
    # green screen / magenta screen: also drop strongly bg-tinted pixels
    if bg[1]>200: tint=(a[...,1]-np.maximum(a[...,0],a[...,2]))>70
    else: tint=(np.minimum(a[...,0],a[...,2])-a[...,1])>90
    return (d>110)&~tint
def segments(m,want):
    col=m.sum(0)>0; segs=[]; on=False
    for x in range(len(col)):
        if col[x] and not on: on=True; x0=x
        if not col[x] and on: on=False; segs.append([x0,x])
    if on: segs.append([x0,len(col)])
    segs=[s for s in segs if s[1]-s[0]>=3]
    # merge until the expected count: always join the narrowest piece with its closest neighbour
    while len(segs)>want:
        i=min(range(len(segs)),key=lambda k:segs[k][1]-segs[k][0])
        if i==0: j=1
        elif i==len(segs)-1: j=i-1
        else: j=i-1 if segs[i][0]-segs[i-1][1]<=segs[i+1][0]-segs[i][1] else i+1
        a,b=sorted([i,j]); segs[a]=[segs[a][0],segs[b][1]]; del segs[b]
    return segs
out={}
for name,(f,rows) in SHEETS.items():
    im=Image.open(f).convert('RGB'); a=np.array(im).astype(int)
    bg=np.median(np.concatenate([a[:,:4].reshape(-1,3),a[:,-4:].reshape(-1,3)]),axis=0)
    M=fgmask(a,bg)
    for (rn,y0,y1,n) in rows:
        m=M[y0:y1].copy()
        # titles sit at the top-left of each row band
        tb=min(36,y1-y0); m[:tb,:TITLE_X]=False if rn!='idle' and rn!='soto' else m[:tb,:TITLE_X]
        segs=SLOTS.get((name if name=='wx' else 'ab',rn)) or segments(m,n)
        for i,(x0,x1) in enumerate(segs):
            sub=m[:,x0:x1]; ys=np.where(sub.any(1))[0]; ty0,ty1=ys.min(),ys.max()+1
            out[f'{name}_{rn}{i}']={'src':f,'box':[int(x0),int(y0+ty0),int(x1),int(y0+ty1)]}
        print(name,rn,[(s[0],s[1]) for s in segs])
json.dump(out,open('civ_cut.json','w'),indent=0)
