# SOTO Slug — Albi: fogli mancanti (dalla 1.3.0.89)

Per ogni prompt **allega la scheda modello di Albi** (il foglio con le tre pose: profilo, fronte, con il mitra) e, se lo strumento lo permette, anche il foglio "fermo e camminata" già fatto: sono il riferimento di viso, vestiti, arma e scala.

Regole che valgono per tutti (sono già dentro i prompt):
- tutto **di profilo verso destra**, stessa altezza e stessa linea dei piedi in ogni fotogramma;
- **niente lampi, fumo, nuvole di respiro, scritte, didascalie o griglie**: i lampi e il fumo li disegna il gioco, e le scritte vanno cancellate a mano;
- fondo **magenta pieno #FF00FF**.

Ordine consigliato: 1 (corsa), 2 (sparo pulito), 3 (corpo a corpo), 4 (raccolta arma), poi il resto.

---

## Blocco comune (già incluso in ogni prompt qui sotto)
Descrizione di Albi usata ovunque:
> ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down and white drawstrings, dark grey cargo trousers with side pockets, light grey sneakers, a big black hiking backpack on his back, a black compact submachine gun.

---

## 1. Corsa con il mitra (8 fotogrammi) — sostituisce il foglio scartato
Il foglio precedente non convinceva: qui chiedo una corsa più compatta, con l'arma ferma e la stessa altezza della camminata.
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline, SAME SIZE as the attached walk cycle.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down and white drawstrings, dark grey cargo trousers with side pockets, light grey sneakers, a big black hiking backpack on his back, a black compact submachine gun held with both hands at chest height pointing right.

LAYOUT: one single row of 8 frames: a compact arcade run cycle (not a sprint): body leaning slightly forward, knees lifting, short quick strides, both feet off the ground in frames 3 and 7, the head bobbing up and down by only 2-3 pixels. The upper body, arms and gun stay in exactly the same position in all 8 frames; only the legs and a light bob change. The character is as tall as in the attached walk cycle.

CONSISTENCY: strict side view facing right in every frame, same height and scale in every frame, feet on the same invisible baseline, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, captions, labels, muzzle flash, smoke, breath puffs, dust, motion lines, front view, three-quarter view, different scale between frames, long sprinting strides, overlapping frames, painterly style, 3D render, blur.
```

## 2. Sparo senza lampo (fermo, in diagonale, verso l'alto, in volo)
Nei fogli attuali il lampo copre l'arma nel fotogramma dello sparo, per cui ho potuto usare poco. Qui chiedo solo il rinculo, senza effetti.
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit, same proportions, same pixel density and outline, same size.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down, dark grey cargo trousers, light grey sneakers, a big black hiking backpack, a black compact submachine gun.

LAYOUT: 4 rows of 3 frames, firing animation WITHOUT any muzzle flash (the game draws the flash): aim, recoil (gun and shoulders pushed back 3-4 pixels, ejected brass casing near the gun), back to aim.
Row 1: standing, gun pointing straight right.
Row 2: standing, gun pointing diagonally up at 45 degrees.
Row 3: standing, gun pointing straight up.
Row 4: in mid-air (knees tucked, both feet off the ground), gun pointing straight right.

CONSISTENCY: strict side view facing right, same height and scale in every frame, feet on the same baseline in rows 1-3, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: muzzle flash, fire, smoke, sparks, text, letters, numbers, captions, labels, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 3. Corpo a corpo con il mitra (in piedi e accovacciato)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie, dark grey cargo trousers, light grey sneakers, a big black hiking backpack, a black compact submachine gun.

LAYOUT: 2 rows.
Row 1 (4 frames), standing melee: wind-up pulling the gun back; swinging the gun stock forward; impact with the stock fully extended forward at head height (small white impact star); recovery back to ready.
Row 2 (3 frames), the same melee while crouched low: wind-up, stock strike forward at knee height, recovery.

CONSISTENCY: strict side view facing right, same height and scale in every frame, feet on the same baseline, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, motion trails, smoke, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 4. Raccoglie un oggetto e cambia arma
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie, dark grey cargo trousers, light grey sneakers, a big black hiking backpack, a black compact submachine gun.

LAYOUT: 2 rows.
Row 1 (4 frames), picking up an item while standing still: holding the gun in the right hand, bending down, picking a small box from the ground with the left hand, standing back up looking at it.
Row 2 (4 frames), the same pick-up while walking forward: mid-step bending, grabbing, straightening, back to the walking pose with the gun pointing right.

CONSISTENCY: strict side view facing right, same height and scale in every frame, feet on the same baseline, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 5. In volo: sparo in basso e lancio della bomba
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie, dark grey cargo trousers, light grey sneakers, a big black hiking backpack, a black compact submachine gun.

LAYOUT: 2 rows, all frames in mid-air with knees tucked and both feet off the ground.
Row 1 (2 frames): pointing the gun straight down between the feet; the same with a small recoil (no muzzle flash).
Row 2 (3 frames): throwing a round black hand grenade in mid-air: arm back with the grenade, arm forward releasing it, follow-through with the gun in the other hand.

CONSISTENCY: strict side view facing right, same scale in every frame, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: muzzle flash, smoke, text, letters, captions, labels, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 6. Paracadute (ingresso nel livello)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie, dark grey cargo trousers, light grey sneakers, a big black hiking backpack, a black compact submachine gun.

LAYOUT: one row of 4 frames: (1) hanging from a beige military parachute, legs dangling, the canopy fully open above him (canopy about three times wider than the character); (2) the same, legs swinging slightly; (3) touching the ground with bent knees, the canopy collapsing behind him; (4) standing in the ready pose with the gun, the parachute lying deflated on the ground behind.

CONSISTENCY: strict side view facing right, the character at the same scale in every frame, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 7. Bruciato e attesa lunga
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie, dark grey cargo trousers, light grey sneakers, a big black hiking backpack, a black compact submachine gun.

LAYOUT: 2 rows.
Row 1 (2 frames), comic burnt death: standing completely blackened by an explosion with only white eyes visible and smoke wisps above the head; then collapsing into a small black heap of ash.
Row 2 (4 frames), long idle when the player waits: looking at the wrist, scratching the beard, yawning, adjusting the backpack strap; the gun held low in the right hand.

CONSISTENCY: strict side view facing right, same height and scale in every frame, feet on the same baseline, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 8. Rifare senza scritte: scivolata e capriola
Il foglio che hai mandato è bello ma ha le didascalie sotto ogni fotogramma (RUNNING START, Tuck…): conviene rigenerarlo pulito, e con il mitra in mano.
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size.

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie, dark grey cargo trousers, light grey sneakers, a big black hiking backpack, a black compact submachine gun held in the right hand in every frame.

LAYOUT: 2 rows of 4 frames.
Row 1, forward slide: running start; dropping low; sliding on one hip with the front leg extended and a small dust cloud behind; getting back up to the ready pose.
Row 2, forward dodge roll: tucking down; rolling (upside down); rolling (on the back); back on the feet in the ready pose.

CONSISTENCY: strict side view facing right, same scale in every frame, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: ANY text, captions or labels under the frames, letters, numbers, motion lines, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```
