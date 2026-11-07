# SOTO Slug — Personaggi: analisi degli sprite e prompt per rifarli

Versione 1.3.0.84. Ho controllato tutti i fotogrammi dei cinque personaggi (Albi 87, Seba 127, Lollo 139, Alecio 88, Pinuccia 52): misure, numero di fotogrammi per animazione e coerenza di vista, colori e vestiti.

## Cosa ho trovato
**Problemi comuni a tutti**
1. **Due viste diverse.** Fermo, camminata e pugni sono disegnati di tre quarti (quasi di fronte); tutto quello con l'arma è di profilo. Quando il personaggio prende l'arma, o passa da fermo a sparare, sembra girarsi di colpo. È la causa principale della "mancanza di continuità".
2. **Taglie diverse tra serie.** I fotogrammi arrivano da fogli diversi, e alcune serie sono più piccole o più grandi del resto (fino a 15-20 px su 130).
3. **Pochi fotogrammi** proprio nelle animazioni che si vedono di più: corsa con l'arma (4-6), sparo (2), salto (2). Con 8 fotogrammi di corsa e 3 di sparo il movimento diventa fluido.
4. **Salto a due pose** di altezza molto diversa: il personaggio sembra rimpicciolirsi a metà salto.

**Per personaggio**
- **Albi**
  - Il set senz'arma (fermo, camminata, pugni) è disegnato di tre quarti, mentre quello con l'arma è di profilo: quando prende o lascia l'arma il personaggio 'gira' di colpo.
  - Corsa con l'arma: 4 fotogrammi presi da due serie diverse (grun0-1 e grun2b-3b), con le braccia in posizioni diverse: è la causa principale degli scatti.
  - Sparo da fermo: solo 2 fotogrammi (gfire0, gfire2; manca il fotogramma di mezzo).
  - Salto: 2 fotogrammi; il secondo è 13 px più basso del primo.
- **Seba**
  - Set a mani nude di tre quarti, set con l'UZI di profilo: stesso problema di Albi.
  - Corsa con l'UZI: il personaggio è alto circa 119 px contro i 130 da fermo, quindi quando parte a correre 'si rimpicciolisce'.
  - Sparo con l'UZI: 2 fotogrammi (gufire0, gufire2).
  - Salto con l'UZI: 3 fotogrammi di altezze diverse (134, 121, 117 px).
  - Tre serie diverse (gb, gs, gu) con piccole differenze di colore della maglia e del cappello.
- **Lollo**
  - Set a mani nude di tre quarti (fermo, camminata), set con le armi di profilo.
  - Due armi diverse con serie complete (xg mitragliatrice, xs fucile a pompa): manca qualche fotogramma nella camminata col fucile (xsw2).
  - Salto: 2 fotogrammi; il secondo è 20 px più basso del primo.
  - Calcio rotante: bello, ma l'effetto bianco è disegnato dentro lo sprite: con un foglio pulito lo aggiungo io e non 'sporca' i bordi.
- **Alecio**
  - Tre serie diverse con il fucile (gf, gx, gy) e altezze diverse: la corsa gf è alta 122 px, la corsa gx 137 px. Passando da una all'altra il personaggio cambia taglia.
  - Anche i dettagli cambiano: in gx si vede la maglia col logo, in gf la giacca è chiusa.
  - Set senz'arma di tre quarti, come gli altri.
  - Corsa: 5 fotogrammi verso destra e 4 verso sinistra, invece di usare lo stesso ciclo specchiato.
- **Pinuccia**
  - Manca un ciclo di corsa: per spostarsi usa la camminata.
  - Morte: sotto il fotogramma die2 ci sono resti di scritte del foglio originale.
  - Lancio dell'ascia (throw): le altezze vanno da 135 a 160 px, quindi il personaggio sembra 'saltellare' durante il lancio.
  - Salto: 2 fotogrammi, con l'attacco in volo a 5 fotogrammi di altezze molto diverse (102-133 px).

## Come usare i prompt
1. **Comincia dalla scheda modello (prompt 0)** di ogni personaggio, allegando come riferimento il ritratto del personaggio e due-tre fotogrammi attuali che ti piacciono. Quando la scheda modello è giusta, **allegala a tutti i prompt successivi** di quel personaggio: è il modo più efficace per avere sempre lo stesso viso e gli stessi vestiti.
2. **Un prompt per immagine**, al massimo 2-3 righe per foglio: fogli più piccoli vengono più coerenti.
3. **Tutto di profilo verso destra**, anche fermo e camminata: il verso sinistro lo ottengo specchiando.
4. **Formato 16:9 o quadrato**, alla risoluzione più alta possibile. La scala la sistemo io: conta che sia uguale dentro il foglio.
5. **Se un foglio esce quasi giusto**, chiedi la correzione nella stessa conversazione ("same sheet, but frame 3 at the same height as the others").
6. **Ordine consigliato**: scheda modello → camminata/fermo → corsa con l'arma → sparo → salto. Sono le animazioni che si vedono di più; le altre possono arrivare dopo.

## Mosse nuove proposte (in fondo a ogni personaggio)
- **Sparo in diagonale e verso l'alto**: utile contro nemici in volo e per il carro.
- **Camminata accovacciata**: per avanzare dietro i sacchi di sabbia.
- **Lancio della bomba** con un'animazione vera (oggi la bomba parte senza gesto).
- **Colpito, a terra e rialzarsi**: ora c'è un solo fotogramma di dolore.
- **Scivolata e capriola**: un piccolo scatto per schivare i colpi (nuovo comando).
- **Seduto alla guida**: serve per l'Ape blindata, quando la faremo.

## Albi
Descrizione usata in tutti i prompt (puoi correggerla se qualche dettaglio non è giusto):
> ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

### 0. Scheda modello (da fare per prima)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: one row of 3 frames, standing still, arms relaxed: (1) strict side view facing right; (2) front view; (3) strict side view facing right holding a compact black assault rifle / submachine gun held with both hands. This is the reference model sheet for all the other sheets: the cleanest, most detailed version of the character.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 1. Fermo e camminata con l'arma
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 2 rows. Row 1 (4 frames): idle breathing loop holding a compact black assault rifle / submachine gun held with both hands low and ready. Row 2 (8 frames): walk cycle holding a compact black assault rifle / submachine gun held with both hands pointed right, contact - down - passing - up for each leg, the weapon steady at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 2. Corsa con l'arma (8 fotogrammi)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: one row of 8 frames: run cycle holding a compact black assault rifle / submachine gun held with both hands pointed forward, body leaning forward, long strides, both feet off the ground in frames 3 and 7, the weapon and the arms stay in the same position in every frame (only the legs and a light body bob move).

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 3. Sparo in tutte le direzioni
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 3 rows of 3 frames. Row 1: standing, firing a compact black assault rifle / submachine gun held with both hands straight right - aim, muzzle flash with recoil, recover. Row 2: standing, firing diagonally up at 45 degrees - aim, flash, recover. Row 3: firing straight up - aim, flash, recover. Bright yellow-white muzzle flashes, ejected brass casings.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 4. Salto (5 fotogrammi) e sparo in volo
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 2 rows. Row 1 (5 frames): jump - crouched take-off, rising with knees up, apex tucked, falling with legs stretched down, landing crouch. Row 2 (3 frames): in mid-air firing a compact black assault rifle / submachine gun held with both hands straight down - aim, attack, recover.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 5. Accovacciato: fermo, camminata, attacco
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 2 rows. Row 1 (4 frames): crouched idle (2 frames) and crouched attack with a compact black assault rifle / submachine gun held with both hands (2 frames). Row 2 (6 frames): crouch-walk cycle, low and steady, the head at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 6. Lancio della bomba
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 2 rows. Row 1 (4 frames): standing grenade throw - reaching to the belt, arm back with a round black grenade, throwing forward, follow-through. Row 2 (3 frames): the same throw while crouched.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 7. Colpito, a terra e di nuovo in piedi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 2 rows. Row 1 (4 frames): hurt reaction - hit flinch, stagger back, knocked off the feet in the air, lying on the back. Row 2 (4 frames): getting up - rolling to the side, on one knee, standing up, shaking the head.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 8. Sconfitta e vittoria
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 2 rows. Row 1 (4 frames): defeat - knees giving way, falling forward, on the ground, lying still. Row 2 (4 frames): victory - turning to the viewer, fist pump, raising a compact black assault rifle / submachine gun held with both hands high, big grin with a thumbs up.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 9. Mosse nuove: scivolata e scatto
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: 2 rows. Row 1 (4 frames): forward slide on the ground - running start, dropping low, sliding on one hip with the leg extended and dust behind, getting up. Row 2 (4 frames): quick dodge roll forward - tuck, roll, roll, back on the feet ready.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 10. Mosse nuove: alla guida dell'Ape
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALBI: man in his thirties, short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, white sneakers with grey soles, a big black hiking backpack on his back.

LAYOUT: one row of 4 frames: the character seen from the side SITTING (no vehicle drawn, just the seated pose, hands forward on invisible handlebars): steady; leaning forward; turning the head back to look behind; standing up to jump off.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

## Seba
Descrizione usata in tutti i prompt (puoi correggerla se qualche dettaglio non è giusto):
> SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

### 0. Scheda modello (da fare per prima)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: one row of 3 frames, standing still, arms relaxed: (1) strict side view facing right; (2) front view; (3) strict side view facing right holding a black UZI submachine gun held with one hand. This is the reference model sheet for all the other sheets: the cleanest, most detailed version of the character.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 1. A mani nude: fermo e camminata
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (4 frames): idle breathing loop, fists up in a light boxing guard, the chest rising and falling slightly. Row 2 (8 frames): walk cycle with fists up, contact - down - passing - up for each leg, smooth and even steps.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 2. A mani nude: colpi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (6 frames): punch combo - jab (wind-up, hit, recover) then cross (wind-up, hit, recover). Row 2 (6 frames): a hook punch and an uppercut, 3 frames each (wind-up, hit, recover).

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 3. Raccoglie l'arma
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: one row of 5 frames: bending down to the ground, grabbing a black UZI submachine gun held with one hand, standing up, checking the weapon, ready pose with the weapon pointing right.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 4. Corsa con l'arma (8 fotogrammi)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: one row of 8 frames: run cycle holding a black UZI submachine gun held with one hand pointed forward, body leaning forward, long strides, both feet off the ground in frames 3 and 7, the weapon and the arms stay in the same position in every frame (only the legs and a light body bob move).

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 5. Sparo in tutte le direzioni
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 3 rows of 3 frames. Row 1: standing, firing a black UZI submachine gun held with one hand straight right - aim, muzzle flash with recoil, recover. Row 2: standing, firing diagonally up at 45 degrees - aim, flash, recover. Row 3: firing straight up - aim, flash, recover. Bright yellow-white muzzle flashes, ejected brass casings.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 6. Salto (5 fotogrammi) e sparo in volo
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (5 frames): jump - crouched take-off, rising with knees up, apex tucked, falling with legs stretched down, landing crouch. Row 2 (3 frames): in mid-air firing a black UZI submachine gun held with one hand straight down - aim, attack, recover.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 7. Accovacciato: fermo, camminata, attacco
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (4 frames): crouched idle (2 frames) and crouched attack with a black UZI submachine gun held with one hand (2 frames). Row 2 (6 frames): crouch-walk cycle, low and steady, the head at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 8. Lancio della bomba
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (4 frames): standing grenade throw - reaching to the belt, arm back with a round black grenade, throwing forward, follow-through. Row 2 (3 frames): the same throw while crouched.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 9. Colpito, a terra e di nuovo in piedi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (4 frames): hurt reaction - hit flinch, stagger back, knocked off the feet in the air, lying on the back. Row 2 (4 frames): getting up - rolling to the side, on one knee, standing up, shaking the head.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 10. Sconfitta e vittoria
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (4 frames): defeat - knees giving way, falling forward, on the ground, lying still. Row 2 (4 frames): victory - turning to the viewer, fist pump, raising a black UZI submachine gun held with one hand high, big grin with a thumbs up.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 11. Mosse nuove: scivolata e scatto
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: 2 rows. Row 1 (4 frames): forward slide on the ground - running start, dropping low, sliding on one hip with the leg extended and dust behind, getting up. Row 2 (4 frames): quick dodge roll forward - tuck, roll, roll, back on the feet ready.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 12. Mosse nuove: alla guida dell'Ape
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers.

LAYOUT: one row of 4 frames: the character seen from the side SITTING (no vehicle drawn, just the seated pose, hands forward on invisible handlebars): steady; leaning forward; turning the head back to look behind; standing up to jump off.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

## Lollo
Descrizione usata in tutti i prompt (puoi correggerla se qualche dettaglio non è giusto):
> LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

### 0. Scheda modello (da fare per prima)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: one row of 3 frames, standing still, arms relaxed: (1) strict side view facing right; (2) front view; (3) strict side view facing right holding a black pump-action shotgun held with both hands. This is the reference model sheet for all the other sheets: the cleanest, most detailed version of the character.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 1. A mani nude: fermo e camminata
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): idle breathing loop, fists up in a light boxing guard, the chest rising and falling slightly. Row 2 (8 frames): walk cycle with fists up, contact - down - passing - up for each leg, smooth and even steps.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 2. A mani nude: colpi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (6 frames): punch combo - jab (wind-up, hit, recover) then cross (wind-up, hit, recover). Row 2 (6 frames): a strong straight kick and a spinning roundhouse kick, 3 frames each (wind-up, hit, recover).

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 3. Raccoglie l'arma
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: one row of 5 frames: bending down to the ground, grabbing a black pump-action shotgun held with both hands, standing up, checking the weapon, ready pose with the weapon pointing right.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 4. Corsa con l'arma (8 fotogrammi)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: one row of 8 frames: run cycle holding a black pump-action shotgun held with both hands pointed forward, body leaning forward, long strides, both feet off the ground in frames 3 and 7, the weapon and the arms stay in the same position in every frame (only the legs and a light body bob move).

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 5. Sparo in tutte le direzioni
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 3 rows of 3 frames. Row 1: standing, firing a black pump-action shotgun held with both hands straight right - aim, muzzle flash with recoil, recover. Row 2: standing, firing diagonally up at 45 degrees - aim, flash, recover. Row 3: firing straight up - aim, flash, recover. Bright yellow-white muzzle flashes, ejected brass casings.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 6. Salto (5 fotogrammi) e sparo in volo
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (5 frames): jump - crouched take-off, rising with knees up, apex tucked, falling with legs stretched down, landing crouch. Row 2 (3 frames): in mid-air firing a black pump-action shotgun held with both hands straight down - aim, attack, recover.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 7. Accovacciato: fermo, camminata, attacco
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): crouched idle (2 frames) and crouched attack with a black pump-action shotgun held with both hands (2 frames). Row 2 (6 frames): crouch-walk cycle, low and steady, the head at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 8. Lancio della bomba
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): standing grenade throw - reaching to the belt, arm back with a round black grenade, throwing forward, follow-through. Row 2 (3 frames): the same throw while crouched.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 9. Colpito, a terra e di nuovo in piedi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): hurt reaction - hit flinch, stagger back, knocked off the feet in the air, lying on the back. Row 2 (4 frames): getting up - rolling to the side, on one knee, standing up, shaking the head.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 10. Sconfitta e vittoria
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): defeat - knees giving way, falling forward, on the ground, lying still. Row 2 (4 frames): victory - turning to the viewer, fist pump, raising a black pump-action shotgun held with both hands high, big grin with a thumbs up.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 11. Mosse nuove: scivolata e scatto
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): forward slide on the ground - running start, dropping low, sliding on one hip with the leg extended and dust behind, getting up. Row 2 (4 frames): quick dodge roll forward - tuck, roll, roll, back on the feet ready.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 12. Mosse nuove: alla guida dell'Ape
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots.

LAYOUT: one row of 4 frames: the character seen from the side SITTING (no vehicle drawn, just the seated pose, hands forward on invisible handlebars): steady; leaning forward; turning the head back to look behind; standing up to jump off.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

## Alecio
Descrizione usata in tutti i prompt (puoi correggerla se qualche dettaglio non è giusto):
> ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

### 0. Scheda modello (da fare per prima)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: one row of 3 frames, standing still, arms relaxed: (1) strict side view facing right; (2) front view; (3) strict side view facing right holding a black and wood AK-style assault rifle held with both hands. This is the reference model sheet for all the other sheets: the cleanest, most detailed version of the character.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 1. Fermo e camminata con l'arma
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 2 rows. Row 1 (4 frames): idle breathing loop holding a black and wood AK-style assault rifle held with both hands low and ready. Row 2 (8 frames): walk cycle holding a black and wood AK-style assault rifle held with both hands pointed right, contact - down - passing - up for each leg, the weapon steady at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 2. Corsa con l'arma (8 fotogrammi)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: one row of 8 frames: run cycle holding a black and wood AK-style assault rifle held with both hands pointed forward, body leaning forward, long strides, both feet off the ground in frames 3 and 7, the weapon and the arms stay in the same position in every frame (only the legs and a light body bob move).

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 3. Sparo in tutte le direzioni
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 3 rows of 3 frames. Row 1: standing, firing a black and wood AK-style assault rifle held with both hands straight right - aim, muzzle flash with recoil, recover. Row 2: standing, firing diagonally up at 45 degrees - aim, flash, recover. Row 3: firing straight up - aim, flash, recover. Bright yellow-white muzzle flashes, ejected brass casings.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 4. Salto (5 fotogrammi) e sparo in volo
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 2 rows. Row 1 (5 frames): jump - crouched take-off, rising with knees up, apex tucked, falling with legs stretched down, landing crouch. Row 2 (3 frames): in mid-air firing a black and wood AK-style assault rifle held with both hands straight down - aim, attack, recover.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 5. Accovacciato: fermo, camminata, attacco
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 2 rows. Row 1 (4 frames): crouched idle (2 frames) and crouched attack with a black and wood AK-style assault rifle held with both hands (2 frames). Row 2 (6 frames): crouch-walk cycle, low and steady, the head at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 6. Lancio della bomba
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 2 rows. Row 1 (4 frames): standing grenade throw - reaching to the belt, arm back with a round black grenade, throwing forward, follow-through. Row 2 (3 frames): the same throw while crouched.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 7. Colpito, a terra e di nuovo in piedi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 2 rows. Row 1 (4 frames): hurt reaction - hit flinch, stagger back, knocked off the feet in the air, lying on the back. Row 2 (4 frames): getting up - rolling to the side, on one knee, standing up, shaking the head.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 8. Sconfitta e vittoria
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 2 rows. Row 1 (4 frames): defeat - knees giving way, falling forward, on the ground, lying still. Row 2 (4 frames): victory - turning to the viewer, fist pump, raising a black and wood AK-style assault rifle held with both hands high, big grin with a thumbs up.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 9. Mosse nuove: scivolata e scatto
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: 2 rows. Row 1 (4 frames): forward slide on the ground - running start, dropping low, sliding on one hip with the leg extended and dust behind, getting up. Row 2 (4 frames): quick dodge roll forward - tuck, roll, roll, back on the feet ready.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 10. Mosse nuove: alla guida dell'Ape
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: ALECIO: broad man in his thirties, black hair combed up, thick black beard, black padded bomber jacket open over a grey t-shirt with a small dark logo, dark brown trousers, black shoes.

LAYOUT: one row of 4 frames: the character seen from the side SITTING (no vehicle drawn, just the seated pose, hands forward on invisible handlebars): steady; leaning forward; turning the head back to look behind; standing up to jump off.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

## Pinuccia
Descrizione usata in tutti i prompt (puoi correggerla se qualche dettaglio non è giusto):
> PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

### 0. Scheda modello (da fare per prima)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: one row of 3 frames, standing still, arms relaxed: (1) strict side view facing right; (2) front view; (3) strict side view facing right holding a big steel battle axe with a long wooden handle. This is the reference model sheet for all the other sheets: the cleanest, most detailed version of the character.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 1. Fermo e camminata con l'arma
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): idle breathing loop holding a big steel battle axe with a long wooden handle low and ready. Row 2 (8 frames): walk cycle holding a big steel battle axe with a long wooden handle pointed right, contact - down - passing - up for each leg, the weapon steady at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 2. Corsa con l'ascia
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: one row of 8 frames: run cycle carrying the axe on the right shoulder, body leaning forward, long strides, both feet off the ground in frames 3 and 7.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 3. Colpi d'ascia
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (5 frames): overhead axe strike - axe raised behind the head, swinging over, impact in front at ground level, follow-through, recovery. Row 2 (5 frames): horizontal sweep - wind-up behind, swing, impact at waist height, follow-through, recovery.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 4. Lancio e ripresa dell'ascia
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (5 frames): throwing the axe forward - wind-up behind, step forward, release with the arm extended, empty-handed follow-through, empty-handed ready pose. Row 2 (3 frames): catching the spinning axe back - hand open, catch, back to ready. Separate small row: the axe alone spinning in the air, 4 frames (0, 90, 180, 270 degrees).

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 5. Salto (5 fotogrammi) e sparo in volo
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (5 frames): jump - crouched take-off, rising with knees up, apex tucked, falling with legs stretched down, landing crouch. Row 2 (3 frames): in mid-air swinging the axe down - aim, attack, recover.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 6. Accovacciato: fermo, camminata, attacco
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): crouched idle (2 frames) and crouched attack with a big steel battle axe with a long wooden handle (2 frames). Row 2 (6 frames): crouch-walk cycle, low and steady, the head at the same height in every frame.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 7. Lancio della bomba
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): standing grenade throw - reaching to the belt, arm back with a round black grenade, throwing forward, follow-through. Row 2 (3 frames): the same throw while crouched.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 8. Colpito, a terra e di nuovo in piedi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): hurt reaction - hit flinch, stagger back, knocked off the feet in the air, lying on the back. Row 2 (4 frames): getting up - rolling to the side, on one knee, standing up, shaking the head.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 9. Sconfitta e vittoria
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): defeat - knees giving way, falling forward, on the ground, lying still. Row 2 (4 frames): victory - turning to the viewer, fist pump, raising the axe high, big grin with a thumbs up.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 10. Mosse nuove: scivolata e scatto
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: 2 rows. Row 1 (4 frames): forward slide on the ground - running start, dropping low, sliding on one hip with the leg extended and dust behind, getting up. Row 2 (4 frames): quick dodge roll forward - tuck, roll, roll, back on the feet ready.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```

### 11. Mosse nuove: alla guida dell'Ape
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheet exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline.

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots.

LAYOUT: one row of 4 frames: the character seen from the side SITTING (no vehicle drawn, just the seated pose, hands forward on invisible handlebars): steady; leaning forward; turning the head back to look behind; standing up to jump off.

CONSISTENCY: STRICT SIDE VIEW FACING RIGHT in every frame (profile, not three-quarter, not front), the same height and the same scale in every frame, feet on the same invisible baseline, the same outfit details in every frame. Evenly spaced frames on a grid with wide empty gaps, no frame touching another.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, slightly cartoonish proportions (about 2 heads wide and 6.5 heads tall when standing).

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, frame numbers, watermark, front view, three-quarter view, back view, different scale between frames, cropped limbs, extra fingers, overlapping frames, painterly style, 3D render, blur.
```
