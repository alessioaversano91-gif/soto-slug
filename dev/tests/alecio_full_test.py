from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc3'); pg.click('#toStage'); pg.click('#lc1'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(250)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];ST.frame=400;PL.x=ST.scrollX+300;lights=[];ST.mode='paused';PL.inv=0;document.getElementById('scr').classList.add('off')}")
    shots=[]; labels=[]
    def snap(lbl,js):
        pg.evaluate("()=>{"+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210})))
        c=im.crop((int(x)-100,0,int(x)+120,210))
        for yy in range(0,210,2): c.putpixel((100,yy),(255,0,0))
        shots.append(c); labels.append(lbl)
    R="PL.fireAnim=0;PL.flashT=0;PL.walking=false;PL.crouch=false;PL.air=false;PL.jy=0;PL.vy=0;PL.melee=0;PL.hurtT=0;PL.stunT=0;PL.landT=0;PL.bombT=0;PL.dead=false;ST.bossDead=false;PL.dir=1;"
    snap('idle',R+"PL.t=0"); snap('idle breath',R+"PL.t=26")
    snap('fire',R+"PL.fireAnim=10;PL.flashT=3;ST.frame=0"); snap('fire2',R+"PL.fireAnim=10;PL.flashT=3;ST.frame=3")
    for i in range(5): snap(f'runR{i}',R+f"PL.walking=true;PL.fireAnim=10;PL.flashT=3;PL.t={i*5}")
    for i in range(4): snap(f'runL{i}',R+f"PL.dir=-1;PL.walking=true;PL.fireAnim=10;PL.flashT=3;PL.t={i*6}")
    snap('crouch',R+"PL.crouch=true"); snap('cfire',R+"PL.crouch=true;PL.fireAnim=10;PL.flashT=3;ST.frame=3")
    snap('jump up',R+"PL.air=true;PL.jy=-80;PL.vy=-3"); snap('jump fire',R+"PL.air=true;PL.jy=-80;PL.vy=-3;PL.fireAnim=10;PL.flashT=3"); snap('fall',R+"PL.air=true;PL.jy=-60;PL.vy=3")
    snap('land',R+"PL.landT=5")
    for el in (2,6,11): snap(f'melee{el}',R+f"PL.meleeKind='punch';PL.meleeLow=false;PL.meleeMax=18;PL.melee=18-{el}")
    for el in (2,6,11): snap(f'cmelee{el}',R+f"PL.crouch=true;PL.meleeKind='lpunch';PL.meleeLow=true;PL.meleeMax=14;PL.melee=14-{el}")
    snap('throw0',R+"PL.bombMax=16;PL.bombT=14"); snap('throw1',R+"PL.bombMax=16;PL.bombT=4"); snap('jthrow',R+"PL.air=true;PL.jy=-80;PL.bombMax=16;PL.bombT=8")
    snap('hurt',R+"PL.hurtT=6"); snap('stun0',R+"PL.stunT=20"); snap('stun1',R+"PL.stunT=10")
    snap('win0',R+"ST.bossDead=true;ST.frame=0"); snap('win1',R+"ST.bossDead=true;ST.frame=24")
    snap('fall0',R+"PL.dead=true;PL.lastHurt='drop';PL.deadT=4"); snap('fall1',R+"PL.dead=true;PL.deadT=14"); snap('dead',R+"PL.dead=true;PL.deadT=60")
    snap('burn',R+"PL.dead=true;PL.lastHurt='tankshot';PL.deadT=30")
    pg.evaluate("()=>{PL.dead=false;PL.lastHurt=''}")
    per=12; rows=(len(shots)+per-1)//per
    out=Image.new('RGB',(220*per,210*rows))
    for i,s in enumerate(shots): out.paste(s,((i%per)*220,(i//per)*210))
    out.save(OUT+'alecio_full_states.png'); print(labels); print('ERR',errs); b.close()
