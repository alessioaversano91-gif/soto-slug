from playwright.sync_api import sync_playwright
from PIL import Image
import io
def start(pg,ch=0,city=1,god=False):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{city-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(250)
    pg.evaluate("(g)=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];eshots=[];PL.inv=0;setGod(g);}",god)
with sync_playwright() as p:
    b=p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    print('version',pg.evaluate("()=>VERSION"))
    # music: title -> map -> stage -> boss -> pause hold -> win null
    pg.mouse.click(240,500); pg.wait_for_timeout(400)
    mu=lambda: pg.evaluate("()=>({cur:MU.cur,step:MU.step,ctx:AU.ctx&&AU.ctx.state})")
    print('1 title music',mu())
    pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.wait_for_timeout(500); print('  map music',mu())
    pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(600); a=mu(); print('  stage music (Genova)',a)
    pg.keyboard.press('p'); pg.wait_for_timeout(500); h=mu(); pg.keyboard.press('p'); pg.wait_for_timeout(300); print('  paused keeps position',h,'-> resumed',mu())
    pg.keyboard.press('n'); pg.wait_for_timeout(200); print('  N = music off',mu(),pg.evaluate("()=>MU.on")); pg.keyboard.press('n')
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];ST.scrollX=ST.maxScroll;}"); pg.wait_for_timeout(700); print('  boss music',mu(),'bossIn',pg.evaluate("()=>ST.bossIn"))
    # pickups heal in LIFE mode
    for city,name in ((1,'croissant'),(2,'focaccia'),(3,'baguette'),(4,'sbrisolona')):
        start(pg,0,city)
        pg.evaluate("()=>{PL.hp=8;updEnergy();dropItem(PL.x+140,GROUND-60,true);dropItem(PL.x+70,GROUND-60,false);}")
        pg.wait_for_timeout(700)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200})))
        im.crop((int(x)-40,60,int(x)+200,200)).save(f'item_{name}.png')
        k=pg.evaluate("()=>items.map(i=>i.kind+(i.land?':landed':':air'))")
        pg.evaluate("()=>{PL.x+=70}"); pg.wait_for_timeout(100); h1=pg.evaluate("()=>PL.hp")
        pg.evaluate("()=>{PL.x+=70}"); pg.wait_for_timeout(100); h2=pg.evaluate("()=>[PL.hp,items.length,ST.score]")
        print('2 city',city,k,'| hp 8 -> coffee',h1,'-> specialty',h2)
    # drops from kills
    start(pg,0,1)
    n=pg.evaluate("()=>{let d=0;for(let i=0;i<140;i++){items=[];const e={type:0,x:PL.x+100,y:GROUND-80,w:30,h:80,dir:-1,hp:1};killEnemy(e);d+=items.length;}return d}")
    print('3 drops from 140 bottle kills:',n,'(expect ~10+6%)')
    # GOD: score only
    start(pg,0,2,True); sc=pg.evaluate("()=>ST.score"); pg.evaluate("()=>{dropItem(PL.x,GROUND-10,true)}"); pg.wait_for_timeout(300); print('4 GOD pickup: hp',pg.evaluate("()=>PL.hp"),'score +',pg.evaluate("()=>ST.score")-sc)
    # boss parachute
    start(pg,0,1); pg.evaluate("()=>{ST.scrollX=ST.maxScroll;PL.hp=10}"); pg.wait_for_timeout(4200)
    ch=pg.evaluate("()=>items.map(i=>({k:i.kind,chute:i.chute,y:Math.round(i.y)}))"); print('5 boss parachute:',ch)
    pg.evaluate("()=>{enemies.forEach(e=>e.shootT=9999);}")
    x=pg.evaluate("()=>(items[0]?items[0].x:PL.x)-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy,'width':480,'height':640}))); im.save('boss_chute.png')
    # Pinuccia blood death
    shots=[]
    for blood in (True,False):
        start(pg,4,1); pg.evaluate("(b)=>{setBlood(b);PL.hp=1;hurtPlayer('drop',PL.x,300)}",blood)
        for w in (230,300,1000):
            pg.wait_for_timeout(w); x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))); shots.append(im.crop((max(0,int(x)-110),0,max(0,int(x)-110)+220,200)))
    out=Image.new('RGB',(220*3,400))
    for i,s in enumerate(shots): out.paste(s,((i%3)*220,(i//3)*200))
    out.save('pin_blood.png')
    pg.keyboard.press('p'); pg.wait_for_timeout(200); pg.screenshot(path='pause127.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.keyboard.press('b'); print('6 blood toggle (B in pause):',pg.evaluate("()=>[ST.blood,document.getElementById('pauseBloodBtn').textContent,document.getElementById('pauseMusicBtn').textContent]"))
    print('ERR',errs); b.close()
