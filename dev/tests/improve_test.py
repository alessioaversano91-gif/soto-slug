from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
def start(pg,ch=0,city=1,god=False):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{city-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(250)
    pg.evaluate("(g)=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];eshots=[];PL.inv=0;setGod(g);}",god)
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    print('version',pg.evaluate("()=>VERSION"))
    pg.screenshot(path=OUT+'t_title.png',clip={'x':0,'y':oy,'width':480,'height':640})
    # 2 Enter: repeat ignored, one step per press
    seq=[pg.evaluate("()=>ST.mode")]
    pg.evaluate("()=>document.dispatchEvent(new KeyboardEvent('keydown',{key:'Enter',repeat:true}))"); seq.append(pg.evaluate("()=>ST.mode"))
    pg.click('#startBtn'); seq.append(pg.evaluate("()=>ST.mode"))
    pg.click('#cc0'); pg.keyboard.press('Enter'); seq.append(pg.evaluate("()=>ST.mode"))
    pg.keyboard.press('Enter'); seq.append(pg.evaluate("()=>ST.mode"))
    print('2 Enter sequence (expect title,title,charselect,levelselect,map):',seq)
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.wait_for_timeout(300)
    pg.screenshot(path=OUT+'t_cards.png',clip={'x':0,'y':oy,'width':480,'height':640})
    # 1 off-screen enemies don't shoot
    start(pg,0,1,True)
    r=pg.evaluate("""()=>{const s=S.chartreuse||S[Object.keys(S).find(k=>k==='bottle'||k==='chartreuse')];
      const mk=(x)=>({type:0,key:'bottle',x,y:GROUND-90,w:30,h:90,hp:9,max:9,dir:1,vx:0,t:0,shootT:1,flash:0,keep:300,hoverY:0});
      enemies=[mk(ST.scrollX-70)]; eshots=[]; for(let i=0;i<3;i++) updateEnemies(); const off=eshots.length;
      enemies=[mk(ST.scrollX+380)]; eshots=[]; for(let i=0;i<3;i++) updateEnemies(); const on=eshots.length; enemies=[]; eshots=[]; return {offscreen:off,onscreen:on}}""")
    print('1 shots fired:',r)
    # 4 traits
    t=pg.evaluate("""()=>CHARS.map(c=>({n:c.name,cd:c.cd||WPN[c.wpn].cd,pow:c.pow||1,bombs:c.bombs,spd:c.spd,label:c.label}))"""); print('4 traits',t)
    start(pg,3,1); pg.evaluate("()=>{PL.shootCd=0;doShoot()}"); print('  Alecio cooldown after a shot:',pg.evaluate("()=>PL.shootCd"))
    # 5 bombs
    start(pg,0,1); b0=pg.evaluate("()=>[ST.bombs,document.getElementById('hbombs').textContent]")
    pg.evaluate("()=>{for(let i=0;i<12;i++){doBomb()}}"); b1=pg.evaluate("()=>[ST.bombs,document.getElementById('hbombs').textContent,shots.filter(s=>s.k==='bomb').length]")
    pg.evaluate("()=>{dropItem(PL.x,GROUND-5,'bombs')}"); pg.wait_for_timeout(300); b2=pg.evaluate("()=>ST.bombs")
    pg.evaluate("()=>{ST.bombs=0;PL.hp=1;hurtPlayer('drop',PL.x,300)}"); pg.wait_for_timeout(2300); b3=pg.evaluate("()=>[PL.dead,ST.bombs]")
    print('5 bombs: start',b0,'| after 12 throws',b1,'| crate ->',b2,'| after respawn',b3)
    start(pg,1,1); print('  Seba starts with',pg.evaluate("()=>ST.bombs"))
    start(pg,0,1,True); pg.evaluate("()=>{for(let i=0;i<15;i++){doBomb()}}"); print('  GOD:',pg.evaluate("()=>[ST.bombs,document.getElementById('hbombs').textContent,shots.filter(s=>s.k==='bomb').length]"))
    # 6 progress + GO
    start(pg,0,2); pg.evaluate("()=>{ST.scrollX=ST.maxScroll*.45;PL.x=ST.scrollX+180;ST.frame=400}"); pg.wait_for_timeout(3200)
    print('6 GO counter',pg.evaluate("()=>ST.goT"))
    pg.evaluate("()=>{dropItem(PL.x+120,GROUND-5,'bombs')}"); pg.wait_for_timeout(400)
    for i in range(6):
        pg.wait_for_timeout(100); pg.screenshot(path=OUT+f't_go{i}.png',clip={'x':0,'y':oy,'width':480,'height':640})
    # 7 summary
    start(pg,0,1); pg.evaluate("()=>{ST.score=10000;ST.kills=23;ST.itemsGot=4;ST.dmgTaken=6;ST.playT=60*135;doWin()}"); pg.wait_for_timeout(300)
    print('7 summary score',pg.evaluate("()=>[ST.score,document.getElementById('winsc').textContent]"))
    pg.screenshot(path=OUT+'t_win.png',clip={'x':0,'y':oy,'width':480,'height':640})
    # 9 caps
    start(pg,0,1); print('9 caps',pg.evaluate("()=>{for(let i=0;i<3000;i++)P({t:'spark',x:300,y:300,life:200,col:'#fff'});for(let i=0;i<100;i++)light(300,300,40,'255,255,255',200);return [parts.length,lights.length,MAX_PARTS,MAX_LIGHTS]}"))
    print('ERR',errs); b.close()
