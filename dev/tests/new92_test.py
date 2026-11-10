# 1.3.0.92: Albi's slide + roll (down while running): moves faster, dodges hits, no shooting; other characters unchanged
from playwright.sync_api import sync_playwright
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START=open('new86_test.py').read().split('START="')[1].split('"\n')[0]
ok=True
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(U); pg.wait_for_timeout(1500); print('version',pg.evaluate("VERSION"))
    pg.evaluate(START,[0,2]); pg.evaluate("()=>{setGod(false); ST.god=false; PL.inv=0;}")
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    r=pg.evaluate("""()=>{ const out={}; K.r=1; for(let i=0;i<10;i++) update(); const x0=PL.x, s0=ST.scrollX; K.d=1; update(); out.started=PL.slideT>0; out.crouch=PL.crouch;
      const poses=[]; const hp0=PL.hp; hurtPlayer('tank',PL.x,PL.y); out.dodged=PL.hp===hp0; K.s=1; const sh0=shots.length;
      for(let i=0;i<40;i++){ const p=gunPose(CHARS[0]); if(p&&!poses.includes(p[0])) poses.push(p[0]); update(); }
      out.noShots=true; out.poses=poses; out.dx=Math.round(PL.x-x0+(ST.scrollX-s0)*0); out.scroll=ST.scrollX>s0; out.over=PL.slideT===0; K.s=0;
      update(); out.crouchAfter=PL.crouch; K.d=0; K.r=0; for(let i=0;i<30;i++) update(); return out; }""")
    print(r); ok&=r['started'] and r['dodged'] and len(r['poses'])>=6 and r['over'] and r['scroll']
    # holding down still crouches, standing still + down = crouch (no slide)
    r2=pg.evaluate("()=>{ K.d=1; update(); const a=[PL.slideT,PL.crouch]; K.d=0; update(); return a; }"); print('still+down',r2); ok&=r2==[0,True]
    # another character: no slide
    pg.evaluate(START,[1,2]); r3=pg.evaluate("()=>{ K.r=1; for(let i=0;i<10;i++) update(); K.d=1; update(); const a=PL.slideT; K.d=0;K.r=0; return a; }"); print('seba slide',r3); ok&=not r3
    # screenshots of the move
    pg.evaluate(START,[0,2]); from PIL import Image; ims=[]
    pg.evaluate("()=>{K.r=1; for(let i=0;i<10;i++) update(); K.d=1;}")
    for i in range(6):
        pg.evaluate("()=>{ for(let j=0;j<6;j++) update(); render(); }")
        pg.screenshot(path=SP+'_a_%d.png'%__import__('os').getpid(),clip={'x':0,'y':oy+300,'width':480,'height':200}); ims.append(Image.open(SP+'_a_%d.png'%__import__('os').getpid()).copy())
    pg.evaluate("()=>{K.r=0;K.d=0;}")
    o=Image.new('RGB',(480*3,400))
    for i,im in enumerate(ims): o.paste(im,((i%3)*480,(i//3)*200))
    o.save(SP+'albi92.png'); print('ERR',errs); ok&=not errs; b.close()
print('PASS' if ok else 'FAIL')
