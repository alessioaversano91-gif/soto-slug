# 1.3.0.69: white car in every Genova level, passing traffic (both ways, not hittable), Carabinieri frames all the same size
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return civs.map(c=>c.col).join('');}"
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300)
    sets=[pg.evaluate(START,[0,2,1+i%3]) for i in range(15)]; print('white in every level',all('w' in x for x in sets),sets[:6])
    print('carabinieri body widths',pg.evaluate("()=>Object.entries(CVM).filter(([k])=>k.startsWith('civc_')&&!/boom/.test(k)).map(([k,m])=>k.slice(5)+':'+m.bw+'/'+m.h).join(' ')"))
    r=pg.evaluate("""()=>{ ST.trafT=1; const dirs=new Set(); let n=0; for(let i=0;i<3000;i++){ update(); for(const v of traffic) dirs.add(v.dir); n=Math.max(n,traffic.length); if(i%500===0) render(); }
      // a bullet fired straight through a passing vehicle keeps flying
      civs=[]; obs=[]; enemies=[]; cars=[]; traffic=[{col:'v',dir:-1,v:-4,x:PL.x+80,t:0}]; shots=[]; PL.shootCd=0; PL.dir=1; doShoot(); const s=shots[0]; for(let i=0;i<6;i++) updateShots(); return {dirs:[...dirs],max:n,bulletAlive:shots.includes(s)}; }""")
    print('traffic',r)
    pg.evaluate("()=>{ traffic=[{col:'c',dir:-1,v:-4,x:ST.scrollX+250,t:0},{col:'w',dir:1,v:4,x:ST.scrollX-60,t:0}]; civs=[{col:'c',x:ST.scrollX+150,st:'alarm',hp:14,max:14,t:0,stT:0,calm:999,flash:0,vx:0},{col:'c',x:ST.scrollX-160,st:'park',hp:14,max:14,t:0,stT:0,calm:999,flash:0,vx:0}]; PL.x=ST.scrollX+60; render(); }")
    pg.screenshot(path=SP+'traffic.png',clip={'x':0,'y':300,'width':480,'height':300})
    print('ERR',errs); b.close()
