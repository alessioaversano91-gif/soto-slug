from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(250)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];ST.frame=400;PL.x=ST.scrollX+330;lights=[];ST.mode='paused';PL.inv=0;document.getElementById('scr').classList.add('off')}")
    shots=[]
    def snap(js):
        pg.evaluate("()=>{"+js+";render()}"); pg.wait_for_timeout(40)
        x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+290,'width':480,'height':210})))
        c=im.crop((int(x)-100,0,int(x)+120,210)); 
        for yy in range(210): c.putpixel((100,yy),(255,0,0))   # PL.x reference line
        shots.append(c)
    snap("PL.dir=1")
    for el in (2,6,12): snap(f"PL.meleeKind='punch';PL.meleeLow=false;PL.meleeMax=18;PL.melee=18-{el}")
    snap("PL.melee=0;PL.hurtT=5")
    snap("PL.hurtT=0;PL.stunT=20"); snap("PL.stunT=10")
    snap("PL.stunT=0;ST.bossDead=true;ST.frame=0"); snap("ST.frame=24")
    snap("ST.bossDead=false;PL.dead=true;PL.lastHurt='tankshot';PL.deadT=20"); snap("PL.deadT=55")
    snap("PL.dead=false;PL.lastHurt='';PL.dir=-1;PL.meleeKind='punch';PL.meleeLow=false;PL.meleeMax=18;PL.melee=6")
    out=Image.new('RGB',(220*len(shots),210))
    for i,s in enumerate(shots): out.paste(s,(i*220,0))
    out.save(OUT+'albi2_states.png'); print('ERR',errs); b.close()
