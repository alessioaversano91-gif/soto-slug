from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc2'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()")
    pg.wait_for_timeout(300); pg.evaluate("()=>{PL.chute=false;PL.air=false;PL.jy=0;spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];falls=[];ST.dropT=99999;PL.inv=0;setGod(false)}")
    mk="(dx,t)=>{const s=S.bottle;return {type:t||0,key:'bottle',x:PL.x+dx,y:GROUND-(s.h+12),w:s.w,h:s.h+12,hp:3,max:3,dir:-1,vx:0,t:0,shootT:9999,flash:0,keep:0,hoverY:0}}"
    # streak: 7 kills, hit, then 8 kills
    r=pg.evaluate("()=>{const mk="+mk+";const o=[];for(let i=0;i<7;i++){const e=mk(200);enemies=[e];killEnemy(e);} o.push(ST.streak,document.getElementById('hsg').textContent);PL.inv=0;hurtPlayer('drop',PL.x,GROUND-80);o.push(ST.streak);for(let i=0;i<8;i++){const e=mk(200);enemies=[e];killEnemy(e);} o.push(ST.streak,items.map(i=>i.kind));return o}")
    print('streak 7 / after hit / after 8 ->',r)
    pg.evaluate("()=>{const u=items.find(i=>i.kind==='sg');u.y=GROUND;u.land=true;PL.x=u.x}"); pg.wait_for_timeout(200)
    print('picked:',pg.evaluate("()=>[sgOn(),PL.sgAmmo,document.getElementById('hsg').textContent,document.getElementById('flash').textContent,getComputedStyle(document.getElementById('hwpn')).visibility]"))
    pg.wait_for_timeout(900)
    # damage rules: bottle 1, gendarme 2, tank 10
    def shots_to_kill(js):
        return pg.evaluate("""()=>{"""+js+"""; const e=enemies[0]; let n=0; PL.sgAmmo=20; PL.dir=1;
          while(e.hp>0&&n<30){ shots=[]; PL.shootCd=0;PL.melee=0; const [mx,my]=[PL.x+30,e.y+e.h*.5]; fireSG(mx,my,1); n++; for(let t=0;t<30&&shots.length;t++) updateShots(); if(e.type===5) e.hitT=0; }
          return [n,Math.round(e.hp*100)/100]}""")
    print('bottle',shots_to_kill("const mk="+mk+";enemies=[mk(80)]"))
    print('gendarme',shots_to_kill("enemies=[];spawnGend?0:0;spawnGendAt?0:0; {const x=PL.x+90; enemies.push({type:6,key:'gend',x,y:GROUND-GEND_H,w:GEND_W,h:GEND_H,hp:10,max:10,dir:-1,vx:0,t:0,st:'idle',stT:0,cd:50,gcd:140,pcd:0,flash:0,jy:0,vy:0,lvx:0,dying:false,dieT:0,taunted:false,combo:0});}"))
    print('tank',shots_to_kill("enemies=[]; spawnTank(); const tk=enemies.find(e=>e.type===5); tk.x=PL.x+60; enemies=[tk]"))
    # pierce: 3 bottles in a row, one blast
    print('row of 3, one blast kills',pg.evaluate("()=>{const mk="+mk+";enemies=[mk(60),mk(110),mk(160)];shots=[];PL.sgAmmo=20;fireSG(PL.x+30,enemies[0].y+enemies[0].h*.5,1);for(let t=0;t<30;t++)updateShots();return enemies.filter(e=>e.hp<=0).length}"))
    # ammo runs out -> back to fists (no rifle yet)
    print('empty ->',pg.evaluate("()=>{enemies=[];PL.sgAmmo=2;fireSG(PL.x+30,GROUND-80,1);const a=[PL.sgAmmo,document.getElementById('flash').textContent];fireSG(PL.x+30,GROUND-80,1);return a.concat([sgOn(),gunOn(CHARS[ST.char]),PL.hasUzi])}"))
    # rifle then shotgun then empty -> rifle
    print('rifle+sg ->',pg.evaluate("()=>{PL.hasUzi=true;setSG(true);PL.sgAmmo=1;fireSG(PL.x+30,GROUND-80,1);return [sgOn(),gunOn(CHARS[ST.char]),CHARS[ST.char].gun.unlock]}"))
    # real key fire with shotgun
    pg.evaluate("()=>{enemies=[];shots=[];setSG(true);PL.sgAmmo=20;updSG();PL.shootCd=0}"); pg.keyboard.down('z'); pg.wait_for_timeout(700); pg.keyboard.up('z')
    print('held fire 0.7s: ammo',pg.evaluate("()=>PL.sgAmmo"))
    pg.evaluate('()=>updWpnIcon()');pg.screenshot(path=OUT+'sg_hud.png',clip={'x':0,'y':oy+560,'width':480,'height':80})
    # death drops shotgun
    print('death ->',pg.evaluate("()=>{playerDie();return [sgOn(),PL.sgAmmo,ST.streak]}"))
    pg.wait_for_timeout(2500)
    pg.evaluate("()=>{showPanel(null);document.getElementById('scr').classList.add('off');resetRun(1);PL.chute=false;PL.air=false;PL.dead=false;setSG(true);PL.sgAmmo=20;updWpnIcon();ST.mode='paused';PL.x=ST.scrollX+300;lights=[];parts=[];corpses=[];items=[];AMB.birds=[];shots=[];enemies=[]}")
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.pickT=0;PL.bombT=0;PL.stunT=0;PL.landT=0;PL.apT=0;PL.aimUpT=0;PL.aimDnT=0;PL.idleLong=0;PL.dead=false;ST.bossDead=false;PL.dir=1;PL.meleeLow=false;PL.back=false;PL.inv=0;PL.hitT=0;"
    sh=[]
    for js in ["PL.t=0","PL.fireAnim=22","PL.fireAnim=8","PL.walking=true;PL.t=0","PL.walking=true;PL.t=10","PL.walking=true;PL.fireAnim=22","PL.crouch=true","PL.crouch=true;PL.fireAnim=20;ST.frame=3",
               "PL.air=true;PL.jy=-80;PL.vy=-3","PL.air=true;PL.jy=-80;PL.vy=2","PL.air=true;PL.jy=-80;PL.fireAnim=20","PL.aimUpT=8;PL.fireAnim=20","PL.aimDnT=8;PL.air=true;PL.jy=-90;PL.fireAnim=20",
               "PL.bombMax=16;PL.bombT=8","PL.crouch=true;PL.bombMax=16;PL.bombT=8","PL.air=true;PL.jy=-80;PL.bombMax=16;PL.bombT=8","PL.meleeKind='punch';PL.meleeMax=18;PL.melee=14","PL.meleeKind='punch';PL.meleeMax=18;PL.melee=8","PL.hurtT=6","PL.dir=-1;PL.fireAnim=22"]:
        pg.evaluate("()=>{"+R+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210}))); c=im.crop((int(x)-110,0,int(x)+150,210))
        for yy in range(0,210,2): c.putpixel((110,yy),(255,0,0))
        sh.append(c)
    o=Image.new('RGB',(260*10,420)); [o.paste(s,((i%10)*260,(i//10)*210)) for i,s in enumerate(sh)]; o.save(OUT+'sg_states.png')
    print('ERR',errs); b.close()
