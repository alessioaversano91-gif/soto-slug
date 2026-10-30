# measures average render() time per city (ms), with the 4x CPU throttle a mid-range phone roughly has
from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':900}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    cdp=pg.context.new_cdp_session(pg); cdp.send('Emulation.setCPUThrottlingRate',{'rate':4})
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(1500)
    pg.evaluate("()=>{PROG.tut=true;gTitle()}"); pg.keyboard.press('Enter'); pg.click('#cc0'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(800)
    res={}
    for c in (2,1,4,3):
        r=pg.evaluate("""(c)=>{ST.stage=c;ST.part=1;resetRun(1);PL.chute=false;PL.air=false;PL.jy=0;setGod(true);ST.scrollX=ST.maxScroll*.4;PL.x=ST.scrollX+200;ST.wavePlan=[];
          for(let i=0;i<60;i++){update();}  // warm up
          const t=[];for(let i=0;i<120;i++){update();const a=performance.now();render();t.push(performance.now()-a);}
          t.sort((a,b)=>a-b);return [Math.round(t.reduce((a,b)=>a+b)/t.length*100)/100, Math.round(t[Math.floor(t.length*.95)]*100)/100]}""",c)
        res[c]=r
    print('avg / p95 render ms (CPU x4):',res,'ERR',errs); b.close()
