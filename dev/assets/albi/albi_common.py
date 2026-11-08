import numpy as np, json, base64, io
from PIL import Image
from scipy import ndimage as nd
MAG=np.array([255,0,255])
def load(f):
    a=np.array(Image.open(f).convert('RGB')).astype(int)
    fg=np.abs(a-MAG).sum(2)>150
    pink=(np.minimum(a[...,0],a[...,2])-a[...,1])>45          # breath puffs, smoke, grid lines, magenta fringe
    fg&=~pink; fg=nd.binary_opening(fg,iterations=1)
    lab,n=nd.label(fg); sz=nd.sum(fg,lab,range(1,n+1)); fg=np.isin(lab,1+np.where(sz>=30)[0])
    return a,fg
def boxes(fg,minarea=3000,dil=14):
    lab,_=nd.label(nd.binary_dilation(fg,iterations=dil)); out=[]
    for s in nd.find_objects(lab):
        if fg[s].sum()>minarea: out.append((s[0].start,s[0].stop,s[1].start,s[1].stop))
    return out
def rows(bs,gap=180):
    bs=sorted([b for b in bs if b[3]-b[2]>60 and b[1]-b[0]>60],key=lambda b:(b[0]+b[1])/2); R=[]
    for b in bs:
        c=(b[0]+b[1])/2
        if R and c-R[-1][-1][4]<gap: R[-1].append(b+(c,))
        else: R.append([b+(c,)])
    R=[[x[:4] for x in r] for r in R]
    return [sorted(r,key=lambda b:b[2]) for r in R]
