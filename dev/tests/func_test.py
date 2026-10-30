# End-to-end functional journey (1.3.0.61): real clicks/keys where possible, logic shortcuts only to skip long play
from playwright.sync_api import sync_playwright
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
OK=[]; BAD=[]
def chk(name,cond,info=''):
    (OK if cond else BAD).append(name+('' if cond else ' -> '+str(info))); print(('PASS ' if cond else 'FAIL ')+name,'' if cond else info,flush=True)
with sync_playwright() as p:
    b=p.chromium.launch()
    # ---------- PC ----------
    pg=b.new_page(viewport={'width':1280,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1200)
    v=pg.evaluate("()=>[getComputedStyle(document.getElementById('pad')).display,document.getElementById('cv').getBoundingClientRect().height,document.getElementById('startBtn').textContent]")
    chk('PC: pulsantiera nascosta, schermo piu grande',v[0]=='none' and v[1]>700,v)
    chk('PC: titolo PREMI INVIO',v[2]=='PREMI INVIO',v[2])
    pg.evaluate("()=>{PROG.tut=true;saveProg()}")
    # title -> select -> stage -> map -> play
    pg.keyboard.press('Enter'); pg.wait_for_timeout(300); chk('Titolo -> scelta personaggio',pg.evaluate("()=>ST.mode")=='charselect',pg.evaluate("()=>ST.mode"))
    pg.click('#cc0'); pg.click('#toStage'); pg.wait_for_timeout(200); chk('Scelta stage',pg.evaluate("()=>document.getElementById('pls').classList.contains('on')"))
    pg.click('#lc1'); pg.click('#goBtn'); pg.wait_for_timeout(400); chk('Mappa del viaggio',pg.evaluate("()=>ST.mode")=='map',pg.evaluate("()=>ST.mode"))
    pg.keyboard.press('Enter'); pg.wait_for_timeout(200); pg.keyboard.press('Enter'); pg.wait_for_timeout(800)
    chk('Partita avviata (Genova)',pg.evaluate("()=>[ST.mode,ST.stage]")==['playing',2],pg.evaluate("()=>[ST.mode,ST.stage]"))
    # movement / shoot / jump / bomb via keyboard
    pg.wait_for_timeout(2500); x0=pg.evaluate("()=>PL.x"); pg.keyboard.down('ArrowRight'); pg.wait_for_timeout(700); pg.keyboard.up('ArrowRight')
    chk('Tastiera: muovi',pg.evaluate("()=>PL.x")>x0+20)
    s0=pg.evaluate("()=>PROG.st.shots"); pg.keyboard.down('z'); pg.wait_for_timeout(400); pg.keyboard.up('z'); chk('Tastiera: spara',pg.evaluate("()=>PROG.st.shots")>s0)
    pg.keyboard.press('ArrowUp'); pg.wait_for_timeout(120); chk('Tastiera: salta',pg.evaluate("()=>PL.air||PL.jy<0"))
    pg.wait_for_timeout(900); pg.evaluate("()=>{ST.god=false;ST.bombs=5;updBombs()}"); pg.keyboard.press('c'); pg.wait_for_timeout(150); chk('Tastiera: bomba',pg.evaluate("()=>ST.bombs")==4,pg.evaluate("()=>ST.bombs")); pg.evaluate("()=>setGod(true)")
    # pause, settings, back
    pg.keyboard.press('p'); pg.wait_for_timeout(200); chk('Pausa',pg.evaluate("()=>ST.mode")=='paused')
    pg.click('#pauseSetBtn'); pg.wait_for_timeout(200); chk('Impostazioni dalla pausa',pg.evaluate("()=>document.getElementById('pset').classList.contains('on')"))
    pg.click('#bigBtn'); chk('Testo grande',pg.evaluate("()=>SET.big&&document.body.classList.contains('bigtxt')")); pg.click('#bigBtn')
    pg.click('#setBackBtn'); pg.wait_for_timeout(150); chk('Ritorno alla pausa',pg.evaluate("()=>document.getElementById('ppause').classList.contains('on')"))
    pg.click('#resumeBtn'); pg.wait_for_timeout(150); chk('Riprendi',pg.evaluate("()=>ST.mode")=='playing')
    # god toggle G
    pg.keyboard.press('g'); g1=pg.evaluate("()=>ST.god"); pg.keyboard.press('g'); chk('Tasto G: God/Life',g1!=pg.evaluate("()=>ST.god"))
    # checkpoint save + resume
    pg.evaluate("()=>{setGod(false);ST.wavePlan=[];ST.carPlan=[];ST.lockCam=false;PL.chute=false;PL.air=false;PL.jy=0;ST.scrollX=ST.maxScroll*.5+5;PL.x=ST.scrollX+200;}"); pg.wait_for_timeout(600)
    chk('Checkpoint salvato',pg.evaluate("()=>!!PROG.save"),pg.evaluate("()=>JSON.stringify(PROG.save)"))
    # win -> next city on the map
    pg.evaluate("()=>{ for(const e of enemies) e.hp=0; ST.bossDead=true; doWin(); }"); pg.wait_for_timeout(500)
    chk('Vittoria stage',pg.evaluate("()=>ST.mode")=='win',pg.evaluate("()=>ST.mode"))
    if pg.is_visible('#nextBtn'):
        pg.click('#nextBtn'); pg.wait_for_timeout(500); chk('Prossima citta: mappa',pg.evaluate("()=>[ST.mode,MAP.to]")==['map',1],pg.evaluate("()=>[ST.mode,MAP.to]"))
    else: chk('Pulsante prossima citta',False,'nextBtn non visibile')
    # game over -> retry
    pg.evaluate("()=>{ mapStart(); }"); pg.wait_for_timeout(600)
    pg.evaluate("()=>{ setGod(false); ST.lives=1; PL.chute=false; PL.inv=0; PL.hp=1; hurtPlayer('tankshot',PL.x,PL.y); for(let i=0;i<200&&ST.mode==='playing';i++){ update(); if(!PL.dead&&ST.mode==='playing'){PL.inv=0;PL.hp=1;hurtPlayer('tankshot',PL.x,PL.y);} } }"); pg.wait_for_timeout(300)
    chk('Game over',pg.evaluate("()=>ST.mode")=='gameover',pg.evaluate("()=>[ST.mode,ST.lives]"))
    pg.click('#retryBtn'); pg.wait_for_timeout(400); chk('Riprova',pg.evaluate("()=>[ST.mode,ST.lives]")==['playing',3],pg.evaluate("()=>[ST.mode,ST.lives]"))
    # back to title, medals, ranking, boss rush
    pg.evaluate("()=>{togglePause()}"); pg.click('#pauseTitleBtn'); pg.wait_for_timeout(300); chk('Torna al titolo',pg.evaluate("()=>ST.mode")=='title')
    chk('Pulsante RIPRENDI dal checkpoint',pg.evaluate("()=>getComputedStyle(document.getElementById('contBtn')).display!=='none'"))
    pg.click('#medBtn'); pg.wait_for_timeout(200); m=pg.evaluate("()=>{const l=document.getElementById('medl');return [l.children.length,l.scrollHeight<=l.clientHeight+1]}"); chk('Medaglie: 13 visibili',m==[13,True],m)
    pg.keyboard.press('Escape'); pg.wait_for_timeout(200)
    pg.click('#rankBtn'); pg.wait_for_timeout(200); chk('Classifica',pg.evaluate("()=>document.getElementById('prank').classList.contains('on')")); pg.keyboard.press('Escape'); pg.wait_for_timeout(200)
    pg.click('#rushBtn'); pg.wait_for_timeout(300)
    rush=pg.evaluate("()=>[ST.mode,!!ST.rush||!!ST.rushPending]"); chk('Boss Rush avviabile',rush[1] or rush[0]=='charselect',rush)
    chk('PC: nessun errore JS',not errs,errs[:3])
    # touch on a PC brings the deck back
    pg.evaluate("()=>window.dispatchEvent(new TouchEvent('touchstart'))"); pg.wait_for_timeout(200)
    chk('PC con touch: pulsantiera ricompare',pg.evaluate("()=>getComputedStyle(document.getElementById('pad')).display")!='none')
    pg.close()
    # ---------- phone ----------
    ctx=b.new_context(viewport={'width':390,'height':844},is_mobile=True,has_touch=True,device_scale_factor=3); pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1200)
    v=pg.evaluate("()=>[innerWidth,document.documentElement.scrollWidth,document.getElementById('startBtn').textContent,getComputedStyle(document.querySelector('.keys')).display]")
    chk('Telefono: niente sbordo laterale',v[0]==390 and v[1]==390,v); chk('Telefono: TOCCA PER GIOCARE e niente legenda',v[2]=='TOCCA PER GIOCARE' and v[3]=='none',v)
    pg.evaluate("()=>{PROG.tut=true}"); pg.tap('#startBtn'); pg.wait_for_timeout(300); pg.tap('#cc2'); pg.tap('#toStage'); pg.tap('#lc0'); pg.tap('#goBtn'); pg.wait_for_timeout(300)
    pg.evaluate("()=>mapStart()"); pg.wait_for_timeout(3500)
    chk('Telefono: partita (Lollo, Lione)',pg.evaluate("()=>[ST.mode,ST.stage,ST.char]")==['playing',1,2],pg.evaluate("()=>[ST.mode,ST.stage,ST.char]"))
    box=pg.evaluate("()=>{const r=document.querySelector('.dz[data-k=\"r\"]').getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]}")
    x0=pg.evaluate("()=>PL.x"); cdp=ctx.new_cdp_session(pg)
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':box[0],'y':box[1]}]}); pg.wait_for_timeout(700); cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    chk('Touch: croce destra muove',pg.evaluate("()=>PL.x")>x0+20,[x0,pg.evaluate("()=>PL.x")])
    fb=pg.evaluate("()=>{const r=document.querySelector('.ab.fire').getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]}"); s0=pg.evaluate("()=>PROG.st.shots")
    cdp.send('Input.dispatchTouchEvent',{'type':'touchStart','touchPoints':[{'x':fb[0],'y':fb[1]}]}); pg.wait_for_timeout(500); cdp.send('Input.dispatchTouchEvent',{'type':'touchEnd','touchPoints':[]})
    chk('Touch: FIRE',pg.evaluate("()=>PROG.st.shots+PL.melee+(PL.fireAnim||0)")>s0,'')
    chk('Telefono: nessun errore JS',not errs,errs[:3])
    ctx.close(); b.close()
print('\nRIEPILOGO',len(OK),'ok,',len(BAD),'falliti'); [print(' -',x) for x in BAD]
