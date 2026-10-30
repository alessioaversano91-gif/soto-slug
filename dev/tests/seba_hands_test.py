from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(250)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];falls=[];ST.dropT=99999;PL.inv=0}")
    # combo sequence
    seq=pg.evaluate("""()=>{const out=[];for(let i=0;i<4;i++){const s=S.bottle;enemies=[{type:0,key:'bottle',x:PL.x+30,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0}];PL.melee=0;PL.shootCd=0;PL.dir=1;doShoot();out.push(PL.meleeKind);const h0=enemies[0].hp;for(let t=0;t<30;t++)updatePlayer();out.push(h0-enemies[0].hp);}return out}""")
    print('combo kinds/damage',seq)
    # jump punch vs flying bottle
    r=pg.evaluate("""()=>{const s=S.bottle_s;enemies=[{type:2,key:'bottle_s',x:PL.x+30,y:GROUND-150,w:s.w,h:s.h,hp:99,max:99,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:GROUND-150}];
      PL.air=true;PL.jy=-60;PL.vy=-1;PL.shootCd=0;PL.melee=0;doShoot();const a=PL.apT;for(let t=0;t<8;t++){PL.apT>0&&(PL.apT===10&&airPunchImpact(),PL.apT--);} return [a,99-enemies[0].hp]}""")
    print('jump punch apT,damage to flying bottle',r)
    pg.evaluate("()=>{enemies=[];PL.air=false;PL.jy=0;PL.vy=0;PL.apT=0}")
    pg.evaluate("()=>{ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];AMB.birds=[];document.getElementById('scr').classList.add('off')}")
    shots=[]
    R="PL.fireAnim=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.reloadT=0;PL.pickT=0;PL.bombT=0;PL.stunT=0;PL.landT=0;PL.apT=0;PL.dead=false;ST.bossDead=false;PL.dir=1;PL.hasUzi=false;PL.meleeLow=false;"
    for js in ("PL.bombMax=16;PL.bombT=14","PL.bombMax=16;PL.bombT=4","PL.crouch=true;PL.bombMax=16;PL.bombT=4","PL.air=true;PL.jy=-80;PL.bombMax=16;PL.bombT=8",
               "PL.air=true;PL.jy=-80;PL.apT=14","PL.air=true;PL.jy=-80;PL.apT=6","PL.meleeKind='upper';PL.meleeMax=22;PL.melee=12","PL.meleeKind='finish';PL.meleeMax=24;PL.melee=6",
               "PL.stunT=20","PL.landT=5","ST.bossDead=true;ST.frame=16","PL.dead=true;PL.lastHurt='drop';PL.deadT=10","PL.dead=true;PL.deadT=60",
               "PL.dead=true;PL.lastHurt='tankshot';PL.deadT=20","PL.dead=true;PL.lastHurt='tankshot';PL.deadT=50",
               "PL.hasUzi=true;PL.pickT=40","PL.hasUzi=true;PL.pickT=26","PL.hasUzi=true;PL.pickT=6"):
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))); c=im.crop((int(x)-110,0,int(x)+150,210))
        for yy in range(0,210,2): c.putpixel((110,yy),(255,0,0))
        shots.append(c)
    o=Image.new('RGB',(260*6,630)); [o.paste(s,((i%6)*260,(i//6)*210)) for i,s in enumerate(shots)]; o.save(OUT+'seba_hands_states.png')
    print('ERR',errs); b.close()
