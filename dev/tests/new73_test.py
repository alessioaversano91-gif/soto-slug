# 1.3.0.73: tram in the Lione traffic only (both ways, not hittable, never parked)
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; ST.wavePlan=[]; ST.dogPlan=[]; ST.ev=null; enemies=[]; return civs.map(c=>c.col).join('');}"
RUN="""()=>{ const cols={},dirs=new Set(); for(let i=0;i<9000;i++){ if(ST.trafT>60) ST.trafT=60; update(); for(const v of traffic){ cols[v.col]=1; if(v.col==='t') dirs.add(v.dir);} if(ST.bossIn) break; } return {cols:Object.keys(cols).sort().join(''),busDirs:[...dirs]}; }"""
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1300); print('version',pg.evaluate("VERSION"))
    parked=''.join(pg.evaluate(START,[0,1+2*(i%2),1]) for i in range(20)); print('bus never parked','t' not in parked)
    pg.evaluate(START,[0,2,1]); print('Genova traffic',pg.evaluate(RUN))
    pg.evaluate(START,[0,1,1]); print('Lione traffic',pg.evaluate(RUN))
    pg.evaluate(START,[0,1,1])
    r=pg.evaluate("""()=>{ civs=[]; obs=[]; cars=[]; traffic=[{col:'t',dir:-1,v:-3,x:PL.x+40,t:0}]; shots=[]; PL.shootCd=0; PL.dir=1; doShoot(); const s=shots[0]; for(let i=0;i<6;i++) updateShots(); return shots.includes(s); }"""); print('bullets pass through',r)
    pg.evaluate("()=>{ traffic=[{col:'t',dir:1,v:3,x:ST.scrollX+20,t:7}]; PL.x=ST.scrollX+120; render(); }")
    pg.screenshot(path=SP+'tram73.png',clip={'x':0,'y':300,'width':480,'height':500})
    print('bell',pg.evaluate("()=>{ const got=[]; const o=window.sfx; window.sfx=n=>got.push(n); try{ sfx=window.sfx; }catch(e){} traffic=[{col:'t',dir:-1,v:-3,x:ST.scrollX+W+10,t:0}]; for(let i=0;i<260;i++) updateTraffic(); return got.filter(n=>n==='trambell'); }"))
    print('ERR',errs); b.close()
