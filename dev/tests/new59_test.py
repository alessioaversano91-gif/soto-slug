from playwright.sync_api import sync_playwright
import json,os
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/'
with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':480,'height':900},accept_downloads=True); pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///mnt/user-data/outputs/soto_slug_tex_edition.html'); pg.wait_for_timeout(900)
    pg.evaluate("()=>{PROG.tut=true;PROG.kills=777;PROG.med={first:1};SET.mus=3;SET.big=true;ST.hi=12345;saveProg();saveSet();gTitle();openSettings()}")
    with pg.expect_download() as d: pg.click('#expBtn')
    f=SP+'exp.json'; d.value.save_as(f); o=json.load(open(f)); print('export',d.value.suggested_filename,o['app'],o['prog']['kills'],o['set']['mus'],o['hi'])
    pg.evaluate("()=>{PROG.kills=1;PROG.med={};SET.mus=9;SET.big=false;ST.hi=0;saveProg();saveSet()}")
    pg.set_input_files('#impFile',f); pg.wait_for_timeout(400)
    print('import',pg.evaluate("()=>[PROG.kills,Object.keys(PROG.med).length,SET.mus,SET.big,ST.hi,document.getElementById('toast').textContent,Array.isArray(PROG.board),document.body.classList.contains('bigtxt')]"))
    open(SP+'bad.json','w').write('{"hello":1}'); pg.set_input_files('#impFile',SP+'bad.json'); pg.wait_for_timeout(300)
    print('bad',pg.evaluate("()=>[document.getElementById('toast').textContent,PROG.kills]"))
    # quiet gendarmerie car: no lights while arriving/braking, lights on 10 ticks after stopping
    pg.evaluate("()=>{closeSettings();PROG.tut=true;}"); pg.keyboard.press('Enter'); pg.click('#cc1'); pg.click('#toStage'); pg.click('#lc0'); pg.click('#goBtn'); pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(1200)
    r=pg.evaluate("""()=>{ ST.carN=5; const R=Math.random; Math.random=()=>.1; spawnCar(1); Math.random=R; const c=cars[cars.length-1], seen=[]; 
       for(let i=0;i<200&&!(c.st==='park'&&c.stT>14);i++){ updateCars(); const k=carKey(c); if(seen[seen.length-1]!==k) seen.push(k); render(); }
       return [c.quiet,seen.join(' '),!!S[c.bk+'0']]; }""")
    print('quiet car',r)
    # Seba: first stride after landing uses seba_gbstep
    ci=pg.evaluate("()=>CHARS.findIndex(c=>c.bare&&c.bare.step)"); print('seba idx',ci)
    r=pg.evaluate(f"""()=>{{ const c=CHARS[{ci}]; PL.air=false; PL.chute=false; PL.paraLand=false; PL.landT=0; PL.stepT=14; PL.walking=true; PL.crouch=false; PL.fireAnim=0; const a=barePose(c); PL.stepT=0; const b=barePose(c); return [a&&a[0],b&&b[0]]; }}""")
    print('seba step',r)
    print('ERR',errs); b.close()
