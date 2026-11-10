# SOTO Slug — Alecio: fogli mancanti (dalla 1.3.0.93)

Per ogni prompt **allega la scheda modello di Alecio** (il foglio con le tre pose: profilo, fronte, con l'AK) e, se lo strumento lo permette, anche il foglio "fermo e camminata" già fatto. Insieme danno il riferimento per viso, vestiti, arma e scala.

Le regole che seguono valgono per tutti i fogli e sono già scritte dentro i prompt:
- **Vista:** tutto di profilo verso destra, con la stessa altezza e la stessa linea dei piedi in ogni fotogramma.
- **Effetti e testo:** niente lampi, fumo, bossoli, stelline, polvere, scritte, didascalie o griglie. Lampi e fumo li disegna il gioco.
- **Spazio tra i fotogrammi:** largo. Nei fogli consegnati la canna dell'AK toccava il personaggio accanto in quasi tutte le righe, e ho dovuto separare i fotogrammi a mano.
- **Scala:** la stessa in tutte le righe del foglio. Nel foglio della corsa la prima riga era disegnata più grande delle altre.
- **Proporzioni:** la stessa grandezza della testa e la stessa corporatura del foglio "fermo". I fogli consegnati lo disegnavano con la testa piccola nella camminata e grande nella corsa e nello sparo, e ho dovuto correggere a mano (1.3.0.94).
- **Fondo:** magenta pieno #FF00FF.

Ordine consigliato:
1. salto, che si vede più spesso;
2. paracadute;
3. corpo a corpo;
4. raccolta;
5. bruciato e attesa lunga;
6. accovacciato vero (aggiunto nella 1.3.0.98).

---

## Blocco comune (già incluso in ogni prompt qui sotto)
Questa è la descrizione di Alecio usata in tutti i prompt, presa dalla sua scheda modello:
> ALECIO: man in his thirties, tanned skin, black hair styled in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch on the chest, grey t-shirt, dark brown cargo trousers with side pockets, black boots, no backpack, an assault rifle with a dark metal body, curved magazine, wooden stock and wooden handguard.

---

## 1. Salto con l'AK (8 fotogrammi)
Oggi in salto Alecio usa i fotogrammi vecchi, e lo stacco di stile è il più visibile.
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline, SAME SIZE as the attached idle frames: same head size and same body proportions as the idle frames.

SUBJECT: ALECIO: man in his thirties, tanned skin, black hair styled in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch on the chest, grey t-shirt, dark brown cargo trousers with side pockets, black boots, no backpack, an assault rifle with a dark metal body, curved magazine, wooden stock and wooden handguard, held with both hands.

LAYOUT: 2 rows of 4 frames, ALL frames in mid-air (both feet off the ground, knees bent and tucked).
Row 1: jumping up with the rifle level pointing right; falling down with the rifle level and legs slightly extended; firing straight right in mid-air (small recoil, NO muzzle flash); throwing a round black hand grenade in mid-air with the free arm while the rifle stays in the other hand.
Row 2: in mid-air aiming straight up; in mid-air aiming straight up with a small recoil; in mid-air aiming straight down between the feet; the same with a small recoil.
The character is as tall as in the attached frames (the tucked legs make him only a little shorter).

CONSISTENCY: strict side view facing right in every frame, same scale in every frame and in both rows, evenly spaced frames with WIDE empty gaps so that the rifle barrel never touches the next frame.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, captions, labels, muzzle flash, smoke, ejected casings, sparks, motion lines, dust, front view, three-quarter view, different scale between frames or rows, overlapping frames, painterly style, 3D render, blur.
```

## 2. Paracadute (ingresso nel livello, 4 fotogrammi)
Durante la discesa non si spara e non ci si muove, per cui basta la posa appesa e l'atterraggio.
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size: same head size and same body proportions as the attached idle frames.

SUBJECT: ALECIO: man in his thirties, tanned skin, black hair in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch, grey t-shirt, dark brown cargo trousers, black boots, no backpack, an assault rifle with wooden stock and handguard.

LAYOUT: one row of 4 frames: (1) hanging from a beige military parachute by the harness straps, legs dangling, the rifle held across the chest, the canopy fully open above him (canopy about three times wider than the character, thin suspension lines down to his shoulders); (2) the same, legs swinging slightly; (3) touching the ground with bent knees, the canopy collapsing behind him; (4) standing in the ready pose with the rifle, the parachute lying deflated on the ground behind him.

CONSISTENCY: strict side view facing right, the character at the same scale in every frame, evenly spaced frames with wide empty gaps (the canopies must not touch each other).

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, muzzle flash, smoke, dust, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 3. Corpo a corpo con l'AK (in piedi e accovacciato, 6 fotogrammi)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size: same head size and same body proportions as the attached idle frames.

SUBJECT: ALECIO: man in his thirties, tanned skin, black hair in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch, grey t-shirt, dark brown cargo trousers, black boots, no backpack, an assault rifle with wooden stock and handguard.

LAYOUT: 2 rows of 3 frames.
Row 1, standing melee attack with the rifle: wind-up (rifle pulled back at the hip, stock forward); hitting forward with the wooden stock at head height; recovery back to the ready pose.
Row 2, the same attack while crouching low on bent knees: wind-up; jabbing forward with the stock at knee height; recovery.

CONSISTENCY: strict side view facing right, same scale in every frame, feet on the same baseline in each row, evenly spaced frames with WIDE empty gaps so the rifle never touches the next frame.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, impact stars, motion lines, muzzle flash, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 4. Raccoglie un oggetto e cambia arma (6 fotogrammi)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size: same head size and same body proportions as the attached idle frames.

SUBJECT: ALECIO: man in his thirties, tanned skin, black hair in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch, grey t-shirt, dark brown cargo trousers, black boots, no backpack, an assault rifle with wooden stock and handguard.

LAYOUT: 2 rows of 3 frames.
Row 1, picking up an item from the floor: bending down with the rifle in the right hand; grabbing a small box from the ground with the left hand; standing back up holding it.
Row 2, swapping weapons: slinging the rifle over the shoulder; pulling a new weapon (a generic black pump shotgun) forward; ready pose holding the shotgun with both hands.

CONSISTENCY: strict side view facing right, same height and scale in every frame, feet on the same baseline, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, sparkles, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 5. Bruciato e attesa lunga (6 fotogrammi)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size: same head size and same body proportions as the attached idle frames.

SUBJECT: ALECIO: man in his thirties, tanned skin, black hair in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch, grey t-shirt, dark brown cargo trousers, black boots, no backpack, an assault rifle with wooden stock and handguard.

LAYOUT: 2 rows.
Row 1 (2 frames), comic burnt death: standing completely blackened by an explosion with only white eyes visible and the quiff sticking up singed; then collapsing into a small black heap of ash.
Row 2 (4 frames), long idle when the player waits: fixing his quiff with one hand; stroking his beard; checking the rifle's magazine; resting the rifle on his shoulder and looking around.

CONSISTENCY: strict side view facing right, same height and scale in every frame, feet on the same baseline, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, smoke clouds, sparks, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```

## 6. Accovacciato con l'AK (4 fotogrammi)
Oggi da accovacciato Alecio usa la camminata a ginocchia piegate, che è alta quasi come in piedi (119 px contro 130). L'area colpibile è già bassa come per gli altri, ma a vista sembra che i colpi gli passino attraverso la testa. Serve una posa davvero bassa, come quella di Albi (circa l'80% dell'altezza in piedi).
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same outfit, same proportions, same size: same head size and same body proportions as the attached idle frames.

SUBJECT: ALECIO: man in his thirties, tanned skin, black hair in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch, grey t-shirt, dark brown cargo trousers, black boots, no backpack, an assault rifle with wooden stock and handguard.

LAYOUT: one row of 4 frames, all in a LOW crouch: one knee on the ground, back bent forward, the top of the head at about 75% of his standing height. (1) crouched, rifle level pointing right; (2) crouched firing, small recoil, NO muzzle flash; (3) crouched, pulling a round black hand grenade from the belt with the free hand; (4) crouched, arm extended forward after throwing the grenade (grenade not drawn).

CONSISTENCY: strict side view facing right, same scale in every frame, the knee and the front foot on the same baseline, evenly spaced frames with WIDE empty gaps so the rifle never touches the next frame.

STYLE: crisp hard-edged pixels, no anti-aliasing, limited palette, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF. No floor, no shadow, no gradient, no grid lines.

Avoid: text, letters, captions, labels, muzzle flash, smoke, ejected casings, front view, three-quarter view, different scale between frames, overlapping frames, blur.
```
