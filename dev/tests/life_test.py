from playwright.sync_api import sync_playwright
from PIL import Image
import io
def start(pg,ch=0,city=1):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{city-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(250)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];eshots=[];PL.inv=0;setGod(false);}")
with sync_playwright() as p:
    b=p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required']); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.evaluate("()=>{document.body.classList.remove('kb');fit()}"); pg.wait_for_timeout(100); pg.wait_for_timeout(1000)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}")
    oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    hud=lambda: pg.evaluate("()=>({hp:PL.hp,lives:ST.lives,ef:document.getElementById('ef').style.width,hl:document.getElementById('hlives').textContent,god:getComputedStyle(document.getElementById('godmode')).display})")
    start(pg,0)
    print('1 start:',hud())
    pg.evaluate("()=>hurtPlayer('gaxe',PL.x,300)"); a=hud(); pg.evaluate("()=>hurtPlayer('gaxe',PL.x,300)"); b2=hud()
    print('2 one axe hit:',a,'| immediate second hit (i-frames):',b2['hp'])
    # death + respawn
    pg.wait_for_timeout(800); pg.evaluate("()=>{PL.hp=1;hurtPlayer('drop',PL.x,300)}")
    d=pg.evaluate("()=>({dead:PL.dead,lives:ST.lives})")
    shots=[]
    for w in (130,900):
        pg.wait_for_timeout(w); x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))); shots.append(im.crop((max(0,int(x)-110),0,max(0,int(x)-110)+220,200)))
    pg.wait_for_timeout(1300); r=pg.evaluate("()=>({dead:PL.dead,hp:PL.hp,lives:ST.lives,inv:PL.inv>0})")
    print('3 death:',d,'| after respawn:',r)
    # death pose of every character
    for ch in (1,2,3,4):
        start(pg,ch); pg.evaluate("()=>{PL.hp=1;hurtPlayer('drop',PL.x,300)}"); pg.wait_for_timeout(1400 if ch==4 else 1100)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))); shots.append(im.crop((max(0,int(x)-110),0,max(0,int(x)-110)+220,200)))
    # game over + retry
    start(pg,0); pg.evaluate("()=>{ST.score=5000;ST.stageScore=1200;ST.lives=1;PL.hp=1;hurtPlayer('drop',PL.x,300)}"); pg.wait_for_timeout(2400)
    go=pg.evaluate("()=>({mode:ST.mode,panel:document.getElementById('pgo').classList.contains('on'),score:document.getElementById('gosc').textContent})")
    pg.screenshot(path='gameover.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.click('#retryBtn'); pg.wait_for_timeout(200); rt=pg.evaluate("()=>({mode:ST.mode,lives:ST.lives,score:ST.score,hp:PL.hp})")
    print('4 game over:',go,'| retry:',rt)
    # god mode
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.evaluate("()=>setGod(false)"); pg.click('#godBtn')
    gl=pg.evaluate("()=>document.getElementById('godBtn').textContent"); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(200)
    pg.evaluate("()=>{for(let i=0;i<30;i++){PL.inv=0;hurtPlayer('gdown',PL.x,300)}}")
    print('5 god mode:',gl,hud(),'dead?',pg.evaluate("()=>PL.dead"))
    pg.evaluate("()=>setGod(false)")
    # pause
    f0=pg.evaluate("()=>ST.frame"); pg.keyboard.press('p'); pg.wait_for_timeout(500); f1=pg.evaluate("()=>[ST.mode,ST.frame]")
    pg.screenshot(path='pause.png',clip={'x':0,'y':oy,'width':480,'height':640})
    pg.keyboard.press('p'); pg.wait_for_timeout(200); f2=pg.evaluate("()=>[ST.mode,ST.frame]")
    bb=pg.locator('#pauseBtn').bounding_box(); pg.mouse.move(bb['x']+10,bb['y']+10); pg.mouse.down(); pg.mouse.up(); pg.wait_for_timeout(100); f3=pg.evaluate("()=>ST.mode")
    pg.click('#resumeBtn'); pg.wait_for_timeout(100)
    pg.evaluate("()=>window.dispatchEvent(new Event('blur'))"); f4=pg.evaluate("()=>ST.mode"); pg.click('#resumeBtn')
    print('6 pause: frame',f0,'-> paused',f1,'-> resumed',f2,'| deck button ->',f3,'| window blur ->',f4)
    # audio
    pg.keyboard.press('m'); m1=pg.evaluate("()=>[AU.muted,document.getElementById('muteBtn').textContent]"); pg.keyboard.press('m'); m2=pg.evaluate("()=>AU.muted")
    au=pg.evaluate("()=>{auInit();const ok=[];for(const k in SFX){try{AU.last={};sfx(k);ok.push(k)}catch(e){}}return {ctx:!!AU.ctx,state:AU.ctx&&AU.ctx.state,played:ok.length,total:Object.keys(SFX).length}}")
    print('7 mute toggle:',m1,'->',m2,'| audio:',au)
    # beer bottle in game
    pg.evaluate("()=>{const s=S.beer;enemies.push({type:3,key:'beer',x:PL.x+120,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0});}"); pg.wait_for_timeout(200)
    ex=pg.evaluate("()=>enemies[0].x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))); beer=im.crop((int(ex)-20,40,int(ex)+70,200)).resize((180,320),Image.NEAREST)
    out=Image.new('RGB',(220*len(shots)+190,200))
    for i,s in enumerate(shots): out.paste(s,(i*220,0))
    out.paste(beer.resize((110,196)),(220*len(shots)+5,0)); out.save('life_strip.png')
    print('ERR',errs); b.close()
