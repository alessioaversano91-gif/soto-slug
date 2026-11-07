# 1.3.0.84 — second batch: pickups, city specialties, gas cylinders, hydrant, hanging sign, harbor container.
exec(open('obj_cut.py').read().split('A={};M={}')[0])
A={};M={}
exec(open('obj_cut.py').read().split('A={};M={}')[1].split('# explosive barrel')[0])   # put() and rows()
def cut_merge(a,bs):                                   # one frame made of several detected boxes
    y0=min(b[0] for b in bs); y1=max(b[1] for b in bs); x0=min(b[2] for b in bs); x1=max(b[3] for b in bs); return cut(a,(y0,y1,x0,x1))
def cut_centroid(a,y0,y1,edges):                       # frames split by component centroid x (for overlapping explosions)
    fg=np.abs(a-MAG).sum(2)>140; sub=fg[y0:y1]; lab,n=nd.label(nd.binary_dilation(sub,iterations=3)); out=[]
    cs=nd.center_of_mass(sub,lab,range(1,n+1)); sz=nd.sum(sub,lab,range(1,n+1))
    for i in range(len(edges)-1):
        ids=[j+1 for j,(c,s) in enumerate(zip(cs,sz)) if s>60 and edges[i]<=c[1]<edges[i+1]]
        m=np.isin(lab,ids); ys,xs=np.where(m); c=a[y0:y1].copy(); c[~m]=MAG
        out.append(cut(c,(ys.min(),ys.max()+1,xs.min(),xs.max()+1)))
    return out
# pickups: grenade box, ammo box, first-aid kit, coin, medal (+ shine frames)
a=load('premi.jpg'); bs=boxes(a,area=800); r1=sorted([b for b in bs if b[0]<800],key=lambda b:b[2]); r2=sorted([b for b in bs if b[0]>=800],key=lambda b:b[2])
k=38/(r1[0][1]-r1[0][0])
for i,(b1,b2) in enumerate(zip(r1,r2)): put(f'obj_it{i}',cut(a,b1),k); put(f'obj_it{i}s',cut(a,b2),k)
# city specialties: row 1 plain, row 2 with shine
for city,src in [('g','spec_genova.jpg'),('l','spec_lione.jpg'),('s','spec_marsiglia.jpg'),('m','spec_mantova.jpg')]:
    a=load(src); bs=boxes(a,area=800); ys=sorted(set(b[0]//300 for b in bs)); R=[sorted([b for b in bs if b[0]//300==y],key=lambda b:b[2]) for y in ys]
    R=[r for r in R if len(r)==3][:2]; k=40/max(b[1]-b[0] for b in R[0])
    for i in range(3): put(f'obj_sp{city}{i}',cut(a,R[0][i]),k); put(f'obj_sp{city}{i}s',cut(a,R[1][i]),k)
# gas cylinders: 5 frames, split by centroid because flames and debris overlap
a=load('gas.jpg'); fr=cut_centroid(a,140,1130,[0,520,990,1450,2100,2528]); k=72/fr[0].shape[0]
for i,f in enumerate(fr): put(f'obj_gas{i}',f,k)
# hydrant: intact, cap off (with the cap), broken, 4 jet frames
a=load('hydrant.jpg'); k=56/(778-242)
put('obj_hyd0',cut(a,(242,778,133,452)),k); put('obj_hyd1',cut_merge(a,[(257,778,734,1051),(42,274,966,1193)]),k); put('obj_hyd2',cut(a,(228,778,1332,1672)),k)
for i,(x0,x1) in enumerate([(55,385),(500,845),(950,1285),(1390,1755)]): put(f'obj_hydj{i}',cut(a,(900,2390,x0,x1)),k)
# hanging sign: bracket+board, snapped, bracket alone, falling board, crashed board
a=load('sign.jpg'); k=150/(609-68)
put('obj_sign0',cut(a,(34,640,60,615)),k); put('obj_sign1',cut(a,(34,745,750,1312)),k); put('obj_signb',cut(a,(30,345,2125,2680)),k)
put('obj_signf',cut(a,(285,790,1530,2035)),k); put('obj_signc',cut(a,(460,780,2160,2690)),k)
for i,(x0,x1) in enumerate([(105,580),(795,1270),(1480,1960),(2170,2645)]): put(f'obj_signp{i}',cut(a,(935,1412,x0,x1)),k)
# harbor container: hanging, snapping, falling, crashed, ground shadow
a=load('container.jpg'); k=270/(704-113)
put('obj_cont0',cut(a,(0,935,105,710)),k); put('obj_cont1',cut(a,(0,1000,770,1390)),k); put('obj_cont2',cut(a,(315,1100,1410,2015)),k)
put('obj_cont3',cut(a,(975,1300,1925,2735)),k); put('obj_conts',cut(a,(1250,1340,140,680)),k)
json.dump(A,open('obj2_assets.json','w')); json.dump(M,open('obj2_meta.json','w'))
print(len(A),'frames',sum(len(v) for v in A.values())//1024,'KB')
keys=list(A); Wd=1800; x=y=0; rowh=0; sheet=Image.new('RGB',(Wd,1400),(80,88,98))
for kk in keys:
    im=Image.open(io.BytesIO(base64.b64decode(A[kk].split(',')[1])))
    if x+im.width>Wd: x=0; y+=rowh+8; rowh=0
    sheet.paste(im,(x,y),im); x+=im.width+8; rowh=max(rowh,im.height)
sheet.crop((0,0,Wd,y+rowh+4)).save('/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/obj2_prev.png')
