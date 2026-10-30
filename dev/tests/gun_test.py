from playwright.sync_api import sync_playwright
from PIL import Image
import io
OUT='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
def start(pg,ch,city=1):
    pg.evaluate("()=>{gTitle()}"); pg.keyboard.press('Enter'); pg.click(f'#cc{ch}'); pg.click('#toStage'); pg.click(f'#lc{city-1}'); pg.click('#goBtn'); pg.evaluate("()=>{if(ST.mode==='map')mapStart()}"); pg.wait_for_timeout(250)
    pg.evaluate("()=>{spawnEnemy=()=>{};enemies=[];obs=[];ST.carPlan=[];ST.dogPlan=[];eshots=[];ST.frame=400;PL.x=ST.scrollX+330;lights=[]}")
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'}"); oy=pg.evaluate("()=>document.getElementById('cv').getBoundingClientRect().top")
    rows=[]
    for ch in (0,3,1,2):
        start(pg,ch); shots=[]
        def snap(state):
            pg.evaluate("()=>{ST.mode='paused';PL.inv=0;document.getElementById('scr').classList.add('off')}"); pg.evaluate(state); pg.wait_for_timeout(60)
            x=pg.evaluate("()=>PL.x-ST.scrollX"); im=Image.open(io.BytesIO(pg.screenshot(clip={'x':0,'y':oy+270,'width':480,'height':230})))
            shots.append(im.crop((int(x)-100,0,int(x)+120,230)))
        freeze="ST.mode='paused';"
        snap("()=>{PL.dir=1;PL.walking=false;PL.fireAnim=0;PL.t=0;render()}")                              # idle
        snap("()=>{PL.fireAnim=10;PL.flashT=3;ST.frame=3;render()}")                                                          # fire
        snap("()=>{PL.fireAnim=10;PL.flashT=3;PL.walking=true;PL.t=12;ST.frame=3;render()}")                                   # walk fire R
        snap("()=>{PL.fireAnim=10;PL.flashT=3;PL.walking=true;PL.dir=-1;PL.t=12;ST.frame=3;render()}")                         # walk fire L
        snap("()=>{PL.dir=1;PL.walking=false;PL.crouch=true;PL.fireAnim=10;PL.flashT=3;ST.frame=3;render()}")                  # crouch fire
        snap("()=>{PL.crouch=false;PL.air=true;PL.jy=-80;PL.vy=-3;PL.fireAnim=10;PL.flashT=3;render()}")                       # jump fire
        snap("()=>{PL.fireAnim=0;PL.flashT=0;PL.vy=3;render()}")                                                              # fall
        snap("()=>{PL.air=false;PL.jy=0;PL.vy=0;PL.landT=5;render()}")                                                         # land
        snap("()=>{PL.landT=0;PL.bombMax=16;PL.bombT=9;render()}")                                                             # throw
        snap("()=>{PL.bombT=0;PL.stunT=20;render()}")                                                                          # stun
        snap("()=>{PL.stunT=0;ST.bossDead=true;render()}")                                                                     # win
        snap("()=>{ST.bossDead=false;PL.dead=true;PL.deadT=20;render()}")                                                      # dying
        snap("()=>{PL.deadT=60;render()}")                                                                                     # dead
        snap("()=>{PL.lastHurt='tankshot';PL.deadT=30;render()}")                                                              # burned
        pg.evaluate("()=>{PL.dead=false;PL.lastHurt=''}")
        r=Image.new('RGB',(220*len(shots),230))
        for i,s in enumerate(shots): r.paste(s,(i*220,0))
        rows.append(r)
    out=Image.new('RGB',(rows[0].width,230*len(rows)))
    for i,r in enumerate(rows): out.paste(r,(0,i*230))
    out.save(OUT+'gun_states.png')
    print('ERR',errs); b.close()
