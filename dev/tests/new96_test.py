# 1.3.0.96-97: Seba (with the UZI) runs while aiming up at a flyer: 3-frame running pose, shots leave the raised barrel and hit
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
START=open('new86_test.py').read().split('START="')[1].split('"\n')[0]
ok=True
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    pg.evaluate(START,[1,2]); pg.evaluate("()=>{PL.hasUzi=true;}")
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    r=pg.evaluate("""()=>{ enemies.length=0; setGod(true); const s=S.bottle_s, dx=150, dy=-300;
      enemies.push({type:2,key:'bottle_s',x:PL.x+dx,y:GROUND+dy,w:s.w,h:s.h,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:999,hoverY:GROUND+dy});
      K.r=1; K.s=1; const poses=new Set(); let hit=0, mz=[];
      for(let i=0;i<90;i++){ const e=enemies[0]; e.y=GROUND+dy; e.vx=0; const h0=e.hp; update(); const p=gunPose(CHARS[1]); if(p) poses.add(p[0]); if(e.hp<h0) hit++; if(i>=30&&!mz.length){ const m=muzzle(); if(gunPose(CHARS[1])[0].includes('rup')) mz=[Math.round(m[0]-PL.x),Math.round(m[1]-GROUND)]; render(); } }
      K.r=0; K.s=0; return {poses:[...poses].filter(k=>k.includes('rup')), hit, mz}; }""")
    print(r); ok&= len(r['poses'])==3 and r['hit']>0 and r['mz'][1]<-120
    # diagonal: flyer further ahead -> 6-frame diagonal running pose, hits
    pg.evaluate(START,[1,2]); pg.evaluate("()=>{PL.hasUzi=true;}")
    r=pg.evaluate("""()=>{ enemies.length=0; setGod(true); const s=S.bottle_s, dx=330, dy=-260;
      enemies.push({type:2,key:'bottle_s',x:PL.x+dx,y:GROUND+dy,w:s.w,h:s.h,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:999,hoverY:GROUND+dy});
      K.r=1; K.s=1; const poses=new Set(); let hit=0;
      for(let i=0;i<90;i++){ const e=enemies[0]; e.y=GROUND+dy; e.vx=0; const h0=e.hp; update(); const p=gunPose(CHARS[1]); if(p) poses.add(p[0]); if(e.hp<h0) hit++; }
      K.r=0; K.s=0; return {poses:[...poses].filter(k=>k.includes('rdiag')), hit}; }""")
    print('diag',r); ok&= len(r['poses'])>=5 and r['hit']>0
    pg.screenshot(path=SP+'seba96.png',clip={'x':0,'y':oy+180,'width':480,'height':320})
    print('ERR',errs); ok&=not errs; b.close()
print('PASS' if ok else 'FAIL')
