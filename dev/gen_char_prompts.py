# Generates prompt_personaggi.md: analysis of the current character sprites + complete prompts per character and sheet.
HEAD="Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline."
STYLE="STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing)."
RULES="CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another."
BG="BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient."
AVOID="Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur."
CH={
 'ALBI':dict(look="ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.",
   wpn="a compact black assault rifle / submachine gun held with both hands",bare=False),
 'SEBA':dict(look="SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.",
   wpn="a black UZI submachine gun held with one hand",bare=True),
 'LOLLO':dict(look="LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.",
   wpn="a black pump-action shotgun held with both hands",bare=True),
 'ALECIO':dict(look="ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.",
   wpn="a black and wood AK-style assault rifle held with both hands",bare=False),
 'PINUCCIA':dict(look="PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.",
   wpn="a big steel battle axe with a long wooden handle",bare=False),
}
def sheet(title,body):
    return f"""### {title}
```
{HEAD}

SUBJECT: {{LOOK}}

{body}

{RULES}

{STYLE}

{BG}

{AVOID}
```
"""
def sheets(name,c):
    W=c['wpn']; out=[]
    out.append(("0. Scheda modello (da fare per prima)","LAYOUT: one row of 3 frames, standing still, arms relaxed: (1) strict side view facing right; (2) front view; (3) strict side view facing right holding "+W+". This is the reference model sheet for all the other sheets: the cleanest, most detailed version of the character."))
    if c['bare']:
        out.append(("1. A mani nude: fermo e camminata","LAYOUT: 2 rows. Row 1 (4 frames): idle breathing loop, fists up in a light boxing guard, the chest rising and falling slightly. Row 2 (8 frames): walk cycle with fists up, contact - down - passing - up for each leg, smooth and even steps."))
        out.append(("2. A mani nude: colpi","LAYOUT: 2 rows. Row 1 (6 frames): punch combo - jab (wind-up, hit, recover) then cross (wind-up, hit, recover). Row 2 (6 frames): "+("a strong straight kick and a spinning roundhouse kick, 3 frames each (wind-up, hit, recover)." if name=='LOLLO' else "a hook punch and an uppercut, 3 frames each (wind-up, hit, recover).")))
        out.append(("3. Raccoglie l'arma","LAYOUT: one row of 5 frames: bending down to the ground, grabbing "+W+", standing up, checking the weapon, ready pose with the weapon pointing right."))
    else:
        out.append(("1. Fermo e camminata con l'arma","LAYOUT: 2 rows. Row 1 (4 frames): idle breathing loop holding "+W+" low and ready. Row 2 (8 frames): walk cycle holding "+W+" pointed right, contact - down - passing - up for each leg, the weapon steady at the same height in every frame."))
    if name=='PINUCCIA':
        out.append(("2. Corsa con l'ascia","LAYOUT: one row of 8 frames: run cycle carrying the axe on the right shoulder, body leaning forward, long strides, both feet off the ground in frames 3 and 7."))
        out.append(("3. Colpi d'ascia","LAYOUT: 2 rows. Row 1 (5 frames): overhead axe strike - axe raised behind the head, swinging over, impact in front at ground level, follow-through, recovery. Row 2 (5 frames): horizontal sweep - wind-up behind, swing, impact at waist height, follow-through, recovery."))
        out.append(("4. Lancio e ripresa dell'ascia","LAYOUT: 2 rows. Row 1 (5 frames): throwing the axe forward - wind-up behind, step forward, release with the arm extended, empty-handed follow-through, empty-handed ready pose. Row 2 (3 frames): catching the spinning axe back - hand open, catch, back to ready. Separate small row: the axe alone spinning in the air, 4 frames (0, 90, 180, 270 degrees)."))
    else:
        out.append(("4. Corsa con l'arma (8 fotogrammi)" if c['bare'] else "2. Corsa con l'arma (8 fotogrammi)","LAYOUT: one row of 8 frames: run cycle holding "+W+" pointed forward, body leaning forward, long strides, both feet off the ground in frames 3 and 7, the weapon and the arms stay in the same position in every frame (only the legs and a light body bob move)."))
        out.append(("5. Sparo in tutte le direzioni" if c['bare'] else "3. Sparo in tutte le direzioni","LAYOUT: 3 rows of 3 frames. Row 1: standing, firing "+W+" straight right - aim, muzzle flash with recoil, recover. Row 2: standing, firing diagonally up at 45 degrees - aim, flash, recover. Row 3: firing straight up - aim, flash, recover. Bright yellow-white muzzle flashes, ejected brass casings."))
    n=len(out)
    out.append((f"{n}. Salto (5 fotogrammi) e sparo in volo","LAYOUT: 2 rows. Row 1 (5 frames): jump - crouched take-off, rising with knees up, apex tucked, falling with legs stretched down, landing crouch. Row 2 (3 frames): in mid-air "+("swinging the axe down" if name=='PINUCCIA' else "firing "+W+" straight down")+" - aim, attack, recover."))
    out.append((f"{n+1}. Accovacciato: fermo, camminata, attacco","LAYOUT: 2 rows. Row 1 (4 frames): crouched idle (2 frames) and crouched attack with "+W+" (2 frames). Row 2 (6 frames): crouch-walk cycle, low and steady, the head at the same height in every frame."))
    out.append((f"{n+2}. Lancio della bomba","LAYOUT: 2 rows. Row 1 (4 frames): standing grenade throw - reaching to the belt, arm back with a round black grenade, throwing forward, follow-through. Row 2 (3 frames): the same throw while crouched."))
    out.append((f"{n+3}. Colpito, a terra e di nuovo in piedi","LAYOUT: 2 rows. Row 1 (4 frames): hurt reaction - hit flinch, stagger back, knocked off the feet in the air, lying on the back. Row 2 (4 frames): getting up - rolling to the side, on one knee, standing up, shaking the head."))
    out.append((f"{n+4}. Sconfitta e vittoria","LAYOUT: 2 rows. Row 1 (4 frames): defeat - knees giving way, falling forward, on the ground, lying still. Row 2 (4 frames): victory - turning to the viewer, fist pump, "+("raising the axe high" if name=='PINUCCIA' else "raising "+W+" high")+", big grin with a thumbs up."))
    out.append((f"{n+5}. Mosse nuove: scivolata e scatto","LAYOUT: 2 rows. Row 1 (4 frames): forward slide on the ground - running start, dropping low, sliding on one hip with the leg extended and dust behind, getting up. Row 2 (4 frames): quick dodge roll forward - tuck, roll, roll, back on the feet ready."))
    out.append((f"{n+6}. Mosse nuove: alla guida dell'Ape","LAYOUT: one row of 4 frames: the character seen from the side SITTING (no vehicle drawn, just the seated pose, hands forward on invisible handlebars): steady; leaning forward; turning the head back to look behind; standing up to jump off."))
    return out
NOTES={
 'ALBI':["Il set senz'arma (fermo, camminata, pugni) è disegnato di tre quarti, mentre quello con l'arma è di profilo: quando prende o lascia l'arma il personaggio 'gira' di colpo.",
         "Corsa con l'arma: 4 fotogrammi presi da due serie diverse (grun0-1 e grun2b-3b), con le braccia in posizioni diverse: è la causa principale degli scatti.",
         "Sparo da fermo: solo 2 fotogrammi (gfire0, gfire2; manca il fotogramma di mezzo).",
         "Salto: 2 fotogrammi; il secondo è 13 px più basso del primo."],
 'SEBA':["Set a mani nude di tre quarti, set con l'UZI di profilo: stesso problema di Albi.",
         "Corsa con l'UZI: il personaggio è alto circa 119 px contro i 130 da fermo, quindi quando parte a correre 'si rimpicciolisce'.",
         "Sparo con l'UZI: 2 fotogrammi (gufire0, gufire2).",
         "Salto con l'UZI: 3 fotogrammi di altezze diverse (134, 121, 117 px).",
         "Tre serie diverse (gb, gs, gu) con piccole differenze di colore della maglia e del cappello."],
 'LOLLO':["Set a mani nude di tre quarti (fermo, camminata), set con le armi di profilo.",
         "Due armi diverse con serie complete (xg mitragliatrice, xs fucile a pompa): manca qualche fotogramma nella camminata col fucile (xsw2).",
         "Salto: 2 fotogrammi; il secondo è 20 px più basso del primo.",
         "Calcio rotante: bello, ma l'effetto bianco è disegnato dentro lo sprite: con un foglio pulito lo aggiungo io e non 'sporca' i bordi."],
 'ALECIO':["Tre serie diverse con il fucile (gf, gx, gy) e altezze diverse: la corsa gf è alta 122 px, la corsa gx 137 px. Passando da una all'altra il personaggio cambia taglia.",
         "Anche i dettagli cambiano: in gx si vede la maglia col logo, in gf la giacca è chiusa.",
         "Set senz'arma di tre quarti, come gli altri.",
         "Corsa: 5 fotogrammi verso destra e 4 verso sinistra, invece di usare lo stesso ciclo specchiato."],
 'PINUCCIA':["Manca un ciclo di corsa: per spostarsi usa la camminata.",
         "Morte: sotto il fotogramma die2 ci sono resti di scritte del foglio originale.",
         "Lancio dell'ascia (throw): le altezze vanno da 135 a 160 px, quindi il personaggio sembra 'saltellare' durante il lancio.",
         "Salto: 2 fotogrammi, con l'attacco in volo a 5 fotogrammi di altezze molto diverse (102-133 px)."],
}
md=["# SOTO Slug — Personaggi: analisi degli sprite e prompt per rifarli","",
"Versione 1.3.0.84. Ho controllato tutti i fotogrammi dei cinque personaggi (Albi 87, Seba 127, Lollo 139, Alecio 88, Pinuccia 52): misure, numero di fotogrammi per animazione e coerenza di vista, colori e vestiti.","",
"## Cosa ho trovato",
"**Problemi comuni a tutti**",
"1. **Due viste diverse.** Fermo, camminata e pugni sono disegnati di tre quarti (quasi di fronte); tutto quello con l'arma è di profilo. Quando il personaggio prende l'arma, o passa da fermo a sparare, sembra girarsi di colpo. È la causa principale della \"mancanza di continuità\".",
"2. **Taglie diverse tra serie.** I fotogrammi arrivano da fogli diversi, e alcune serie sono più piccole o più grandi del resto (fino a 15-20 px su 130).",
"3. **Pochi fotogrammi** proprio nelle animazioni che si vedono di più: corsa con l'arma (4-6), sparo (2), salto (2). Con 8 fotogrammi di corsa e 3 di sparo il movimento diventa fluido.",
"4. **Salto a due pose** di altezza molto diversa: il personaggio sembra rimpicciolirsi a metà salto.","",
"**Per personaggio**"]
for n,notes in NOTES.items():
    md.append(f"- **{n.title()}**"); md+= [f"  - {x}" for x in notes]
md+=["","## Come usare i prompt",
"1. **Comincia dalla scheda modello (prompt 0)** di ogni personaggio, allegando come riferimento il ritratto del personaggio e due-tre fotogrammi attuali che ti piacciono. Quando la scheda modello è giusta, **allegala a tutti i prompt successivi** di quel personaggio: è il modo più efficace per avere sempre lo stesso viso e gli stessi vestiti.",
"2. **Un prompt per immagine**, al massimo 2-3 righe per foglio: fogli più piccoli vengono più coerenti.",
"3. **Tutto di profilo verso destra**, anche fermo e camminata: il verso sinistro lo ottengo specchiando.",
"4. **Formato 16:9 o quadrato**, alla risoluzione più alta possibile. La scala la sistemo io: conta che sia uguale dentro il foglio.",
"5. **Se un foglio esce quasi giusto**, chiedi la correzione nella stessa conversazione (\"same sheet, but frame 3 at the same height as the others\").",
"6. **Ordine consigliato**: scheda modello → camminata/fermo → corsa con l'arma → sparo → salto. Sono le animazioni che si vedono di più; le altre possono arrivare dopo.","",
"## Mosse nuove proposte (in fondo a ogni personaggio)",
"- **Sparo in diagonale e verso l'alto**: utile contro nemici in volo e per il carro.",
"- **Camminata accovacciata**: per avanzare dietro i sacchi di sabbia.",
"- **Lancio della bomba** con un'animazione vera (oggi la bomba parte senza gesto).",
"- **Colpito, a terra e rialzarsi**: ora c'è un solo fotogramma di dolore.",
"- **Scivolata e capriola**: un piccolo scatto per schivare i colpi (nuovo comando).",
"- **Seduto alla guida**: serve per l'Ape blindata, quando la faremo.",""]
for name,c in CH.items():
    md.append(f"## {name.title()}")
    md.append("Descrizione usata in tutti i prompt (puoi correggerla se qualche dettaglio non è giusto):")
    md.append(f"> {c['look']}"); md.append("")
    for t,b in sheets(name,c): md.append(sheet(t,b).replace('{LOOK}',c['look']))
open('/home/claude/prompt_personaggi.md','w').write('\n'.join(md))
print(sum(1 for l in md if l.startswith('### ')),'prompts')
