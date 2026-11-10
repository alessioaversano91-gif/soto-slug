# 1.3.0.91: Albi knocked down by a big hit (fall, ground, get up) and down on one knee
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START=open('new86_test.py').read().split('START="')[1].split('"\n')[0]
RST="Object.assign(PL,{walking:false,fireAnim:0,crouch:false,air:false,chute:false,paraLand:false,landT:0,jy:0,vy:0,aimUpT:0,aimDnT:0,bombT:0,hurtT:0,stunT:0,heavyT:0,t:7});"
STATES={'k0':"PL.stunT=40;PL.heavyT=28;",'k1':"PL.stunT=31;PL.heavyT=20;",'k2':"PL.stunT=24;PL.heavyT=12;",'k3':"PL.stunT=17;",'k4':"PL.stunT=10;",'k5':"PL.stunT=2;",'heavy':"PL.heavyT=20;",'hurt':"PL.hurtT=8;"}
EXP={'k0':'albi_n_hurt2','k1':'albi_n_hurt3','k2':'albi_n_getup0','k3':'albi_n_getup1','k4':'albi_n_getup2','k5':'albi_n_getup3','heavy':'albi_n_getup1','hurt':'albi_n_hurt0'}
ok=True
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    pg.evaluate(START,[0,2])
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    from PIL import Image; ims=[]
    for nm,js in STATES.items():
        k=pg.evaluate("()=>{ "+RST+" ST.bossDead=false; "+js+" const p=gunPose(CHARS[0]); const m=muzzle(); render(); return [p&&p[0],Math.round(m[0]-PL.x),Math.round(m[1]-(GROUND+PL.jy))]; }")
        good=bool(k[0]) and k[0].startswith(EXP[nm]); ok&=good; print(nm,k,'OK' if good else 'FAIL')
        pg.screenshot(path=SP+'_a_%d.png'%__import__('os').getpid(),clip={'x':0,'y':oy+180,'width':300,'height':320}); ims.append(Image.open(SP+'_a_%d.png'%__import__('os').getpid()).copy())
    o=Image.new('RGB',(300*4,640))
    for i,im in enumerate(ims): o.paste(im,((i%4)*300,(i//4)*320))
    o.save(SP+'albi91.png')
    print('ERR',errs); ok&=not errs; b.close()
print('PASS' if ok else 'FAIL')
