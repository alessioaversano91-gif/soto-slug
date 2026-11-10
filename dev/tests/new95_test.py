# 1.3.0.95: Albi runs while aiming up / diagonally up (automatic aim at flyers): legs keep moving, shots leave the raised barrel and hit
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
START=open('new86_test.py').read().split('START="')[1].split('"\n')[0]
ok=True
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    pg.evaluate(START,[0,2])
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    from PIL import Image; ims=[]
    for name,dx,dy in [('up',30,-300),('diag',190,-230)]:
        r=pg.evaluate("""([dx,dy])=>{ enemies.length=0; setGod(true); const s=S.bottle_s;
          enemies.push({type:2,key:'bottle_s',x:PL.x+dx,y:GROUND+dy,w:s.w,h:s.h,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:999,hoverY:GROUND+dy,frozen:true});
          K.r=1; K.s=1; const poses=new Set(); let hit=0, mz=[];
          for(let i=0;i<90;i++){ const e=enemies[0]; e.x=PL.x+dx; e.y=GROUND+dy; const h0=e.hp; update(); const p=gunPose(CHARS[0]); if(p) poses.add(p[0]); if(e.hp<h0) hit++; if(i===20){ const m=muzzle(); mz=[Math.round(m[0]-PL.x),Math.round(m[1]-GROUND)]; render(); } }
          K.r=0; K.s=0; return {poses:[...poses].filter(k=>k.includes('rup')||k.includes('rdiag')), hit, mz, walking:PL.walking}; }""",[dx,dy])
        print(name,r); want='rup' if name=='up' else 'rdiag'; ok&= sum(want in k for k in r['poses'])>=4 and r['hit']>0
        pg.screenshot(path=SP+'_a_%d.png'%__import__('os').getpid(),clip={'x':0,'y':oy+180,'width':480,'height':320}); ims.append(Image.open(SP+'_a_%d.png'%__import__('os').getpid()).copy())
    o=Image.new('RGB',(960,320)); o.paste(ims[0],(0,0)); o.paste(ims[1],(480,0)); o.save(SP+'albi95.png')
    # other characters unchanged (Alecio: no running aim-up sheet yet -> old single frame)
    ci=pg.evaluate("CHARS.findIndex(c=>c.name==='ALECIO')"); pg.evaluate(START,[ci,2])
    r=pg.evaluate("(ci)=>{PL.walking=true; PL.aimUpT=10; PL.upA=-1.3; return gunPose(CHARS[ci])[0];}",ci); print('alecio',r); ok&= r=='alecio_n_up0'
    print('ERR',errs); ok&=not errs; b.close()
print('PASS' if ok else 'FAIL')
