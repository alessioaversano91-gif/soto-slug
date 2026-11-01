# Rebuild kit from a published build: pulls every generated block (sprites, metas, font) out of the HTML
import json,re,sys
src=sys.argv[1] if len(sys.argv)>1 else '/mnt/user-data/outputs/soto_slug_tex_edition.html'
h=open(src).read(); D=json.JSONDecoder(); B={}
for ph,var in [('__ASSETS__','ASSET_SRC'),('__FRMETA__','FR'),('__GENDMETA__','GD'),('__CARMETA__','CM'),('__DOGMETA__','DM'),('__TANKMETA__','TK'),('__CIVMETA__','CVM')]:
    tag='const %s='%var; i=h.index(tag)+len(tag); v,end=D.raw_decode(h[i:]); B[ph]=h[i:i+end]
m=re.search(r"base64,([A-Za-z0-9+/=]+)\) format\('woff2'\)",h); B['__FONT__']=m.group(1)
for k,rel in [('__ICON64__','icon'),('__ICON180__','apple-touch-icon')]:
    m2=re.search(r'<link rel="%s"[^>]*href="([^"]+)"'%rel,h)
    if m2: B[k]=m2.group(1)
json.dump(B,open('build_bundle.json','w')); print({k:len(v)//1024 for k,v in B.items()},'KB')
