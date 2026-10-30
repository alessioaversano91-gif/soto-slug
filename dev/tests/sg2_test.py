from playwright.sync_api import sync_playwright
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(300); pg.evaluate("()=>{PL.chute=false;PL.air=false;PL.jy=0;spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];falls=[];ST.dropT=99999;PL.inv=0;setGod(false);PL.x=ST.scrollX+150}")
    mk="(dx)=>{const s=S.bottle;return {type:0,key:'bottle',x:PL.x+dx,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:3,max:3,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0}}"
    print('streak 5:',pg.evaluate("()=>{const mk="+mk+";for(let i=0;i<5;i++){const e=mk(200);enemies=[e];killEnemy(e);} return [ST.streak,document.getElementById('hsg').className,parts.filter(q=>q.t==='spark').length]}"))
    pg.wait_for_timeout(200); pg.screenshot(path=OUT+'sg2_near.png',clip={'x':0,'y':oy+250,'width':480,'height':390})
    r=pg.evaluate("()=>{const mk="+mk+";corpses=[];enemies=[mk(70)];setSG(true);PL.sgAmmo=20;PL.dir=1;shots=[];fireSG(PL.x+30,enemies[0].y+enemies[0].h*.5,1);for(let t=0;t<30;t++)updateShots();const c=corpses[0];const x0=c.x;return [x0,c.vx]}")
    pg.wait_for_timeout(600); print('corpse knockback start/vx',r,'-> now x',pg.evaluate("()=>corpses[0]&&Math.round(corpses[0].x)"))
    pg.screenshot(path=OUT+'sg2_push.png',clip={'x':0,'y':oy+250,'width':480,'height':390})
    print('ERR',errs); b.close()
