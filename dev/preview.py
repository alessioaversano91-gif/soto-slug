# Release preview: one frame per city/level with a parked vehicle and a passing vehicle, side by side (sent at every release)
import sys
from playwright.sync_api import sync_playwright
from PIL import Image
SP='/tmp/claude-0/-home-claude/cd384b70-471e-5c72-87e8-917c6f304069/scratchpad/ui/'
U='file:///mnt/user-data/outputs/soto_slug_tex_edition.html'
START="(a)=>{PROG.tut=true; selChar=a[0]; ST.char=a[0]; ST.stage=a[1]; ST.startPart=a[2]||1; MAP={from:null,to:a[1],t:0,fire:false}; mapStart(); setGod(true); for(let i=0;i<200;i++) update(); PL.chute=false; PL.air=false; PL.jy=0; enemies=[]; document.getElementById('flash').classList.remove('on');}"
SHOTS=[(2,1,'b',0),(2,3,'p',0),(1,1,'t',-200),(3,1,'s',60),(4,1,None,0)]
out=sys.argv[1] if len(sys.argv)>1 else SP+'preview.png'
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={'width':480,'height':800}); pg.goto(U); pg.wait_for_timeout(1300)
    oy=pg.evaluate("()=>{document.getElementById('cab').style.cssText+=';position:relative;left:0;top:0;transform:none'; return document.getElementById('cv').getBoundingClientRect().top}")
    ims=[]
    for st,pt,tr,dx in SHOTS:
        pg.evaluate(START,[0,st,pt])
        pg.evaluate("([tr,dx])=>{ traffic=tr?[{col:tr,dir:1,v:3,x:ST.scrollX+dx-20,t:7}]:[]; if(civs[0]) civs[0].x=ST.scrollX+250; PL.x=ST.scrollX+120; PL.dir=1; if(ST.stage===3&&typeof stunt!=='undefined'){ civs=[]; stunt={dir:-1,x:ST.scrollX+220,v:0,t:20,say:60,said:true,txt:'TROP LENT!'}; } render(); }",[tr,dx])
        f=SP+'_pv.png'; pg.screenshot(path=f,clip={'x':0,'y':oy,'width':480,'height':640}); ims.append(Image.open(f).copy())
    b.close()
o=Image.new('RGB',(490*len(ims)-10,640),(0,0,0))
for i,im in enumerate(ims): o.paste(im,(i*490,0))
o.resize((o.width*2//3,o.height*2//3)).save(out); print(out)
