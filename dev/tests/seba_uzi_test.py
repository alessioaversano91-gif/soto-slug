from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
def start(pg,ch,city):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{city-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(250)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];eshots=[];PL.inv=0;falls=[];ST.dropT=99999;}")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    start(pg,1,2)
    print('start: hasUzi',pg.evaluate("()=>[!!PL.hasUzi,getComputedStyle(document.getElementById('hwpn')).visibility]"))
    pg.keyboard.down('z'); pg.wait_for_timeout(500); pg.keyboard.up('z')
    print('fire with fists: bullets',pg.evaluate("()=>shots.filter(s=>s.k==='bul').length"),'punching',pg.evaluate("()=>PL.melee>0||PL.shootCd>0"))
    # punch an enemy with no projectile
    pg.evaluate("()=>{const s=S.bottle;enemies.push({type:0,key:'bottle',x:PL.x+30,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:3,max:3,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0});PL.dir=1;PL.shootCd=0}")
    pg.keyboard.down('z'); pg.wait_for_timeout(700); pg.keyboard.up('z'); print('bottle punched to death:',pg.evaluate("()=>enemies.length===0||enemies[0].hp<=0"))
    # dog kill -> uzi drop
    pg.evaluate("()=>{enemies=[];items=[];spawnDog(1);const d=enemies.find(e=>e.type===7);d.x=PL.x+120;killEnemy(d)}"); pg.wait_for_timeout(300)
    it=pg.evaluate("()=>items.map(i=>i.kind)"); pg.evaluate("()=>{const u=items.find(i=>i.kind==='uzi');if(u)PL.x=u.x}"); pg.wait_for_timeout(300)
    print('dog -> items',it,'| after pickup hasUzi',pg.evaluate("()=>[PL.hasUzi,PL.reloadT>0,getComputedStyle(document.getElementById('hwpn')).visibility]"))
    pg.wait_for_timeout(800); pg.evaluate("()=>{enemies=[];shots=[];PL.shootCd=0}"); pg.keyboard.down('z'); pg.wait_for_timeout(300); pg.keyboard.up('z')
    print('fire with uzi: bullets',pg.evaluate("()=>shots.filter(s=>s.k==='bul').length"))
    # kill-count drop in Lyon
    start(pg,1,1); print('Lyon start hasUzi',pg.evaluate("()=>!!PL.hasUzi"))
    pg.evaluate("()=>{for(let i=0;i<12;i++){killEnemy({type:0,x:PL.x+150,y:GROUND-90,w:30,h:90,dir:-1,hp:1})}}"); pg.wait_for_timeout(100)
    print('after 12 kills items',pg.evaluate("()=>items.map(i=>i.kind)"))
    # poses
    pg.evaluate("()=>{PL.hasUzi=true;ST.mode='paused';PL.x=ST.scrollX+300;lights=[];AMB.rain=[];items=[];parts=[];corpses=[];enemies=[];document.getElementById('scr').classList.add('off')}")
    shots=[]
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.reloadT=0;PL.dir=1;"
    for js in ("PL.t=0","PL.fireAnim=10;PL.flashT=3;ST.frame=0","PL.walking=true;PL.t=5;PL.fireAnim=10;PL.flashT=3","PL.dir=-1;PL.walking=true;PL.t=10;PL.fireAnim=10;PL.flashT=3",
               "PL.crouch=true","PL.crouch=true;PL.fireAnim=10;PL.flashT=3;ST.frame=3","PL.air=true;PL.jy=-80;PL.vy=-3","PL.air=true;PL.jy=-80;PL.vy=-3;PL.fireAnim=10;PL.flashT=3","PL.reloadT=30","PL.reloadT=5","PL.hurtT=6",
               "PL.hasUzi=false","PL.hasUzi=false;PL.meleeKind='punch';PL.meleeMax=18;PL.melee=8"):
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+300,'width':480,'height':200}))); c=im.crop((int(x)-100,0,int(x)+120,200))
        for yy in range(0,200,2): c.putpixel((100,yy),(255,0,0))
        shots.append(c)
    o=Image.new('RGB',(220*7,400)); [o.paste(s,((i%7)*220,(i//7)*200)) for i,s in enumerate(shots)]; o.save(OUT+'seba_states.png')
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.wait_for_timeout(300); pg.screenshot(path=OUT+'seba_card.png',clip={'x':0,'y':oy,'width':480,'height':330})
    print('ERR',errs); b.close()
