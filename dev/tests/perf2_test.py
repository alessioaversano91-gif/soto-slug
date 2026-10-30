from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900})
    cdp=pg.context.new_cdp_session(pg); cdp.send('Emulation.setCPUThrottlingRate',{'rate':4})
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1500)
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(800)
    for c in (1,4):
        r=pg.evaluate("""(c)=>{ST.stage=c;ST.part=1;resetRun(1);PL.chute=false;PL.air=false;PL.jy=0;setGod(true);ST.scrollX=ST.maxScroll*.4;PL.x=ST.scrollX+200;ST.wavePlan=[];
          for(let i=0;i<60;i++)update();
          const C=CanvasRenderingContext2D.prototype, cnt={rad:0,lin:0,draw:0,fill:0}; const o={r:C.createRadialGradient,l:C.createLinearGradient,d:C.drawImage,f:C.fillRect};
          C.createRadialGradient=function(){cnt.rad++;return o.r.apply(this,arguments)}; C.createLinearGradient=function(){cnt.lin++;return o.l.apply(this,arguments)};
          C.drawImage=function(){cnt.draw++;return o.d.apply(this,arguments)}; C.fillRect=function(){cnt.fill++;return o.f.apply(this,arguments)};
          let tu=0; for(let i=0;i<60;i++){const a=performance.now();update();tu+=performance.now()-a;render();}
          C.createRadialGradient=o.r;C.createLinearGradient=o.l;C.drawImage=o.d;C.fillRect=o.f;
          return {perFrame:Object.fromEntries(Object.entries(cnt).map(([k,v])=>[k,Math.round(v/60)])),updMs:Math.round(tu/60*100)/100,parts:parts.length,lights:lights.length}}""",c)
        print(c,r)
    b.close()
