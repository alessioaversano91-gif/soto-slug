from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    ims=[]
    for t in (900,1700):
        pg.wait_for_timeout(t-(0 if t==900 else 900)); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+60,'width':480,'height':440}))))
    while pg.evaluate("()=>PL.air"): pg.wait_for_timeout(30)
    pg.wait_for_timeout(150); ims.append(Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+60,'width':480,'height':440}))))
    o=Image.new('RGB',(1440,440)); [o.paste(im,(i*480,0)) for i,im in enumerate(ims)]; o.save(OUT+'l2_chute.png')
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];falls=[];ST.dropT=99999;PL.inv=0}")
    r=pg.evaluate("""()=>{const mk=(dx)=>{const s=S.bottle;return {type:0,key:'bottle',x:PL.x+dx-s.w/2,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0}};
      const out=[];for(const full of [true,false]){PL.hp=full?PL_MAXHP:PL_MAXHP-10;PL.meleeN=3;enemies=[mk(40),mk(-40)];PL.melee=0;PL.shootCd=0;PL.dir=1;doShoot();const k=PL.meleeKind;for(let t=0;t<30;t++)updatePlayer();out.push([k,enemies.map(e=>99-e.hp)]);}return out}""")
    print('finisher full/not full ->',r)
    pg.evaluate("()=>{enemies=[];PL.hasUzi=true;PL.dir=1;PL.x=ST.scrollX+300}")
    pg.keyboard.down('z'); pg.keyboard.down('ArrowLeft'); pg.wait_for_timeout(500)
    print('back walk: dir',pg.evaluate("()=>[PL.dir,PL.back,PL.walking,Math.round(PL.vx*10)/10]"))
    pg.keyboard.up('z'); pg.wait_for_timeout(200); print('release fire: dir',pg.evaluate("()=>[PL.dir,PL.back]")); pg.keyboard.up('ArrowLeft')
    pg.evaluate("()=>{ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];corpses=[];items=[];AMB.birds=[];shots=[]}")
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.pickT=0;PL.bombT=0;PL.stunT=0;PL.landT=0;PL.apT=0;PL.aimUpT=0;PL.aimDnT=0;PL.idleLong=0;PL.dead=false;ST.bossDead=false;PL.dir=1;PL.meleeLow=false;PL.back=false;"
    sh=[]
    for js in ["PL.hasUzi=false;PL.meleeKind='spin';PL.meleeMax=28;PL.melee=26","PL.hasUzi=false;PL.meleeKind='spin';PL.meleeMax=28;PL.melee=16","PL.hasUzi=false;PL.meleeKind='spin';PL.meleeMax=28;PL.melee=4",
               "PL.hasUzi=true;PL.walking=true;PL.back=true;PL.t=0","PL.hasUzi=true;PL.walking=true;PL.back=true;PL.t=6","PL.hasUzi=true;PL.walking=true;PL.back=true;PL.t=12;PL.dir=-1",
               "PL.hasUzi=true;PL.dead=true;PL.lastHurt='tankshot';PL.deadT=20","PL.hasUzi=true;PL.dead=true;PL.lastHurt='tankshot';PL.deadT=50"]:
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))); c=im.crop((int(x)-130,0,int(x)+130,210))
        for yy in range(0,210,2): c.putpixel((130,yy),(255,0,0))
        sh.append(c)
    o=Image.new('RGB',(260*8,210)); [o.paste(s,(i*260,0)) for i,s in enumerate(sh)]; o.save(OUT+'l2_states.png')
    print('ERR',errs); b.close()
