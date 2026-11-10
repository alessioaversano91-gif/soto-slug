# 1.3.0.93: Alecio's new AK sheets in every pose + slide; parachute descent can't be steered, shot or bombed
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START=open('new86_test.py').read().split('START="')[1].split('"\n')[0]
RST="Object.assign(PL,{walking:false,fireAnim:0,crouch:false,air:false,chute:false,paraLand:false,landT:0,jy:0,vy:0,aimUpT:0,aimDnT:0,bombT:0,hurtT:0,stunT:0,heavyT:0,slideT:0,t:7});"
ST_={'idle':"",'run':"PL.walking=true;PL.t=11;",'walk+fire':"PL.walking=true;PL.fireAnim=20;",'fire':"PL.fireAnim=10;",'crouch':"PL.crouch=true;",
 'diag':"PL.aimUpT=14;PL.upA=-.8;",'up':"PL.aimUpT=14;PL.upA=-1.3;",'throw':"PL.bombT=8;PL.bombMax=16;",'cthrow':"PL.crouch=true;PL.bombT=8;PL.bombMax=16;",
 'hurt':"PL.hurtT=8;",'knock':"PL.stunT=36;",'win':"ST.bossDead=true;",'slide':"PL.slideT=20;"}
ok=True
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"),'select',pg.evaluate("()=>menuIdle(CHARS[3],0)"))
    ci=pg.evaluate("CHARS.findIndex(c=>c.name==='ALECIO')"); pg.evaluate(START,[ci,2])
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    from PIL import Image; ims=[]
    for nm,js in ST_.items():
        k=pg.evaluate("(ci)=>{ "+RST+" ST.bossDead=false; "+js+" const p=gunPose(CHARS[ci]); const m=muzzle(); render(); return [p&&p[0],Math.round(m[0]-PL.x),Math.round(m[1]-GROUND)]; }",ci)
        good=bool(k[0]) and k[0].startswith('alecio_n_'); ok&=good; print(nm,k,'OK' if good else 'FAIL')
        pg.screenshot(path=SP+'_a_%d.png'%__import__('os').getpid(),clip={'x':0,'y':oy+300,'width':240,'height':200}); ims.append(Image.open(SP+'_a_%d.png'%__import__('os').getpid()).copy())
    o=Image.new('RGB',(240*7,400))
    for i,im in enumerate(ims): o.paste(im,((i%7)*240,(i//7)*200))
    o.save(SP+'alecio93.png')
    # every frame key exists
    miss=pg.evaluate("(ci)=>{const g=CHARS[ci].gun, out=[]; for(const v of Object.values(g)){ for(const k of [].concat(v)) if(typeof k==='string'&&k.startsWith('alecio')&&!S[k]) out.push(k);} return out;}",ci)
    print('missing',miss); ok&=not miss
    # parachute: inputs ignored until landing, then control comes back
    for who in [0,ci]:
        pg.evaluate("(c)=>{selChar=c; ST.char=c; ST.stage=2; ST.startPart=1; MAP={from:null,to:2,t:0,fire:false}; mapStart(); setGod(true);}",who)
        r=pg.evaluate("""()=>{ const x0=PL.x, b0=ST.bombs, s0=shots.length; let moved=false, shot=false, chuteF=0;
          K.r=1; K.s=1; let n=0; while(PL.chute&&n<600){ update(); if(!PL.chute) break; chuteF++; if(Math.abs(PL.x-x0)>1) moved=true; if(shots.some(s=>s.k!=='bomb')&&shots.length>s0) shot=true; n++; if(n===30) doBomb(); }
          const bombed=ST.bombs<b0||shots.some(s=>s.k==='bomb'); for(let i=0;i<60;i++) update(); const after=PL.x-x0; K.r=0; K.s=0;
          return {chuteF,moved,shot,bombed,after:Math.round(after)}; }""")
        print('chute',who,r); ok&= r['chuteF']>20 and not r['moved'] and not r['shot'] and not r['bombed'] and r['after']>20
    print('ERR',errs); ok&=not errs; b.close()
print('PASS' if ok else 'FAIL')
