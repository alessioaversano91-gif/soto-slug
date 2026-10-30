# Albi & Alecio after removing the old bare-hand frames: every pose must still find a sprite
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1500)
    r=pg.evaluate("""()=>{ window.__M={}; const df=drawFrame; window.drawFrame=function(ctx,key){ if(!S[key]) __M[key]=(__M[key]||0)+1; return df.apply(this,arguments); };
      const out={};
      for(const ci of [0,3]){
        PROG.tut=true; selChar=ci; ST.char=ci; ST.stage=2; MAP={from:null,to:2,t:0,fire:false}; mapStart(); setGod(true);
        for(let i=0;i<260;i++) update(); PL.chute=false;
        const states=[()=>{},()=>{PL.crouch=true},()=>{PL.crouch=false;PL.air=true;PL.vy=-3},()=>{PL.vy=3},()=>{PL.air=false;PL.walking=true},()=>{PL.dir=-1},()=>{PL.walking=false;PL.melee=8;PL.meleeMax=12},()=>{PL.melee=0;PL.hurtT=8},()=>{PL.hurtT=0;PL.heavyT=20},()=>{PL.heavyT=0;PL.stunT=30},()=>{PL.stunT=0;ST.bossDead=true},()=>{ST.bossDead=false;PL.fireAnim=6},()=>{PL.fireAnim=0;PL.bombT=10;PL.bombMax=20},()=>{PL.bombT=0;PL.idleLong=60}];
        for(const f of states){ f(); for(let k=0;k<6;k++){ render(); PL.t++; ST.frame++; } }
        PL.dead=true; for(let t=0;t<120;t+=5){ PL.deadT=t; ST.deadT=t; render(); } PL.dead=false;
        gTitle(); for(let i=0;i<5;i++) render();
      }
      return __M; }""")
    print('missing keys:',r); print('ERR',errs); b.close()
