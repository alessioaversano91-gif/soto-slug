from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(1500); pg.screenshot(path=OUT+'lollo_chute.png',clip={'x':0,'y':oy+40,'width':480,'height':480})
    while pg.evaluate("()=>PL.air"): pg.wait_for_timeout(40)
    pg.wait_for_timeout(100); pg.screenshot(path=OUT+'lollo_land.png',clip={'x':0,'y':oy+250,'width':480,'height':260})
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];falls=[];ST.dropT=99999;PL.inv=0}")
    print('start: armed?',pg.evaluate("()=>[!!PL.hasUzi,getComputedStyle(document.getElementById('hwpn')).visibility]"))
    seq=pg.evaluate("""()=>{const out=[];for(let i=0;i<4;i++){const s=S.bottle;enemies=[{type:0,key:'bottle',x:PL.x+30,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0}];PL.melee=0;PL.shootCd=0;PL.dir=1;doShoot();out.push(PL.meleeKind);for(let t=0;t<30;t++)updatePlayer();}return out}""")
    print('bare combo',seq,'bullets',pg.evaluate("()=>shots.filter(s=>s.k==='bul').length"))
    pg.evaluate("()=>{enemies=[];items=[];spawnDog(1);const d=enemies.find(e=>e.type===7);d.x=PL.x+120;killEnemy(d)}"); pg.wait_for_timeout(200)
    it=pg.evaluate("()=>items.map(i=>i.kind)"); pg.evaluate("()=>{const u=items.find(i=>i.kind==='uzi');if(u)PL.x=u.x}"); pg.wait_for_timeout(300)
    print('dog drop',it,'| armed',pg.evaluate("()=>[PL.hasUzi,document.getElementById('flash').textContent]"))
    pg.wait_for_timeout(1200); pg.evaluate("()=>{enemies=[];shots=[];PL.shootCd=0}"); pg.keyboard.down('z'); pg.wait_for_timeout(300); pg.keyboard.up('z')
    print('bullets with rifle',pg.evaluate("()=>shots.filter(s=>s.k==='bul').length"))
    pg.screenshot(path=OUT+'lollo_hud.png',clip={'x':0,'y':oy+580,'width':480,'height':60})
    pg.evaluate("()=>{ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];corpses=[];items=[];AMB.birds=[];document.getElementById('scr').classList.add('off')}")
    shots=[]
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.pickT=0;PL.bombT=0;PL.stunT=0;PL.landT=0;PL.apT=0;PL.aimUpT=0;PL.aimDnT=0;PL.idleLong=0;PL.dead=false;ST.bossDead=false;PL.dir=1;PL.meleeLow=false;"
    A="PL.hasUzi=true;"; N="PL.hasUzi=false;"
    for js in (N+"PL.t=0",N+"PL.bombMax=16;PL.bombT=8",N+"PL.crouch=true;PL.bombMax=16;PL.bombT=4",N+"PL.air=true;PL.jy=-80;PL.apT=6",N+"PL.crouch=true;PL.meleeKind='kick';PL.meleeLow=true;PL.meleeMax=20;PL.melee=6",N+"PL.meleeKind='finish';PL.meleeMax=24;PL.melee=12",
               N+"PL.stunT=20",N+"ST.bossDead=true;ST.frame=16",N+"PL.dead=true;PL.lastHurt='drop';PL.deadT=10",N+"PL.dead=true;PL.lastHurt='tankshot';PL.deadT=20",
               A+"PL.t=0",A+"PL.fireAnim=10;PL.flashT=3",A+"PL.walking=true;PL.t=10;PL.fireAnim=10;PL.flashT=3",A+"PL.walking=true;PL.t=5",A+"PL.crouch=true;PL.fireAnim=10;PL.flashT=3;ST.frame=3",
               A+"PL.air=true;PL.jy=-80;PL.vy=-3",A+"PL.aimUpT=8;PL.fireAnim=10;PL.flashT=3",A+"PL.aimDnT=8;PL.air=true;PL.jy=-90;PL.fireAnim=10;PL.flashT=3",A+"PL.meleeKind='punch';PL.meleeMax=18;PL.melee=8",
               A+"PL.bombMax=16;PL.bombT=8",A+"PL.hurtT=6",A+"PL.idleLong=60",A+"PL.pickMax=44;PL.pickT=20",A+"ST.bossDead=true",A+"PL.dead=true;PL.lastHurt='drop';PL.deadT=60"):
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))); c=im.crop((int(x)-100,0,int(x)+130,210))
        for yy in range(0,210,2): c.putpixel((100,yy),(255,0,0))
        shots.append(c)
    o=Image.new('RGB',(230*9,630)); [o.paste(s,((i%9)*230,(i//9)*210)) for i,s in enumerate(shots)]; o.save(OUT+'lollo_states.png')
    print('ERR',errs); b.close()
