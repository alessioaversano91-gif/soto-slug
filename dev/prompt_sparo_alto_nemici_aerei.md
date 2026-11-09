# SOTO Slug — Corsa sparando verso l'alto e nemici dall'alto (prompt, dalla 1.3.0.94)

## Come funzionerà nel gioco
- **Sparo verso l'alto in corsa.** Puoi già mirare in alto mentre ti muovi, ma oggi Albi e Alecio restano rigidi su un solo fotogramma e le gambe non si muovono. Con i fogli qui sotto, mirando in alto o in diagonale mentre corri, le gambe seguono la corsa e busto e arma restano puntati verso l'alto. Sono 8 fotogrammi in linea con la corsa normale, così il passaggio tra corsa dritta e corsa con la mira in alto non fa scatti.
- **Pinuccia** non ha armi da fuoco, quindi riceve un fendente d'ascia verso l'alto mentre corre: colpisce i nemici bassi in volo e quelli che scendono.
- **Nemici dall'alto.** Sei nemici in tema con il gioco: bottiglie, uccelli delle città e gendarmeria. Ognuno ha un modo diverso di attaccare dall'alto, così sparare in alto diventa utile e non solo decorativo. Li inserisco in tutte le città, con i colori della città (verde a Lione, giallo a Genova e così via). Il colore lo cambio io nel gioco, quindi basta un solo foglio per nemico.

## Regole che valgono per tutti i fogli (già scritte nei prompt)
- Fondo **magenta pieno #FF00FF**, niente griglia, niente pavimento, niente ombre.
- **Niente lampi, fumo, bossoli, esplosioni, scritte o didascalie.** Lampi ed esplosioni li disegna il gioco.
- **Spazio largo tra i fotogrammi.** Le armi lunghe toccavano spesso il fotogramma accanto.
- **Personaggi:** profilo verso destra, stessa scala del foglio "fermo" del personaggio, stessa testa e stessa corporatura (vedi la correzione fatta su Alecio nella 1.3.0.94).
- **Nemici:** profilo rivolto **verso sinistra**, perché arrivano da destra verso il giocatore.
- Per i personaggi, **allega sempre** la scheda modello e il foglio della corsa già fatto.

Ordine consigliato:
1. Albi e Alecio, che hanno già i fogli nuovi;
2. la bottiglia a elica e il gabbiano, che sono i nemici più frequenti;
3. tutto il resto.

---

# PARTE A — Corsa sparando verso l'alto (personaggi)

Struttura comune, uguale per tutti: **2 righe da 8 fotogrammi**.
- Riga 1: corsa con l'arma puntata **dritta verso l'alto**.
- Riga 2: corsa con l'arma puntata **in diagonale verso l'alto, a 45°**.

In entrambe le righe le gambe ripetono la corsa già fatta, fotogramma per fotogramma, mentre busto e arma restano fermi.

## A1. Albi
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline, SAME SIZE as the attached idle frames (same head size and same body proportions).

SUBJECT: ALBI: man in his thirties, very short dark brown hair, thick full brown beard, mustard-yellow hoodie with the hood down and white drawstrings, dark grey cargo trousers with side pockets, light grey sneakers, a big black hiking backpack on his back, a black compact submachine gun held with both hands.

LAYOUT: 2 rows of 8 frames.
Row 1: run cycle while aiming the gun STRAIGHT UP: the legs follow the attached run cycle exactly, frame by frame (both feet off the ground in frames 3 and 7); the upper body is upright, both hands hold the gun vertically above the shoulder with the muzzle pointing at the sky; the gun and arms stay in exactly the same position in all 8 frames, only a 1-2 pixel head bob.
Row 2: the same run cycle while aiming DIAGONALLY UP at 45 degrees, gun pointing up and to the right, arms and gun steady in all 8 frames.

CONSISTENCY: strict side view facing right in every frame, same height and scale in every frame and in both rows, feet on the same invisible baseline, evenly spaced frames with WIDE empty gaps so the gun never touches the next frame.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, captions, labels, muzzle flash, smoke, ejected casings, sparks, motion lines, dust, front view, three-quarter view, different scale between frames or rows, overlapping frames, painterly style, 3D render, blur.
```

## A2. Alecio
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline, SAME SIZE as the attached idle frames (same head size and same body proportions).

SUBJECT: ALECIO: man in his thirties, tanned skin, black hair styled in a tall slicked-back quiff with short faded sides, thick full black beard, black hooded puffer jacket worn open with a small orange "H" patch on the chest, grey t-shirt, dark brown cargo trousers with side pockets, black boots, no backpack, an assault rifle with a dark metal body, curved magazine, wooden stock and wooden handguard, held with both hands.

LAYOUT: 2 rows of 8 frames.
Row 1: run cycle while aiming the rifle STRAIGHT UP: the legs follow the attached run cycle exactly, frame by frame (both feet off the ground in frames 3 and 7); the upper body is upright, the rifle held vertically with the stock against the chest and the muzzle pointing at the sky; rifle and arms stay in exactly the same position in all 8 frames, only a 1-2 pixel head bob.
Row 2: the same run cycle while aiming DIAGONALLY UP at 45 degrees, the rifle pointing up and to the right, arms and rifle steady in all 8 frames.

CONSISTENCY: strict side view facing right in every frame, same height and scale in every frame and in both rows, feet on the same invisible baseline, evenly spaced frames with WIDE empty gaps so the rifle never touches the next frame.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, captions, labels, muzzle flash, smoke, ejected casings, sparks, motion lines, dust, front view, three-quarter view, different scale between frames or rows, overlapping frames, painterly style, 3D render, blur.
```

## A3. Seba (con il mitra raccolto)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline, SAME SIZE as the attached idle frames (same head size and same body proportions).

SUBJECT: SEBA: stocky man in his fifties, beige boonie bucket hat, tanned face, grey mustache, small round glasses, black t-shirt with a small white logo on the chest, olive camouflage cargo shorts with a tactical belt and pouches, fingerless olive gloves, grey sneakers, a black compact submachine gun.

LAYOUT: 2 rows of 8 frames.
Row 1: run cycle while aiming the submachine gun STRAIGHT UP with both hands: the legs follow the attached run cycle exactly, frame by frame (both feet off the ground in frames 3 and 7); upper body upright, the gun vertical above the shoulder, muzzle at the sky; gun and arms in exactly the same position in all 8 frames, only a 1-2 pixel head bob.
Row 2: the same run cycle while aiming DIAGONALLY UP at 45 degrees, gun and arms steady in all 8 frames.

CONSISTENCY: strict side view facing right in every frame, same height and scale in every frame and in both rows, feet on the same invisible baseline, evenly spaced frames with WIDE empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, captions, labels, muzzle flash, smoke, ejected casings, sparks, motion lines, dust, front view, three-quarter view, different scale between frames or rows, overlapping frames, painterly style, 3D render, blur.
```

## A4. Lollo (con il fucile a pompa raccolto)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline, SAME SIZE as the attached idle frames (same head size and same body proportions).

SUBJECT: LOLLO: lean man in his thirties, dark brown hair tied in a small top bun, full brown beard, faded blue denim vest over a black jacket, black t-shirt, ripped light-blue jeans, black boots, a black pump-action shotgun held with both hands.

LAYOUT: 2 rows of 8 frames.
Row 1: run cycle while aiming the shotgun STRAIGHT UP: the legs follow the attached run cycle exactly, frame by frame (both feet off the ground in frames 3 and 7); upper body upright, the shotgun vertical with the stock at the chest and the barrel at the sky; shotgun and arms in exactly the same position in all 8 frames, only a 1-2 pixel head bob.
Row 2: the same run cycle while aiming DIAGONALLY UP at 45 degrees, shotgun and arms steady in all 8 frames.

CONSISTENCY: strict side view facing right in every frame, same height and scale in every frame and in both rows, feet on the same invisible baseline, evenly spaced frames with WIDE empty gaps so the barrel never touches the next frame.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, captions, labels, muzzle flash, smoke, ejected shells, sparks, motion lines, dust, front view, three-quarter view, different scale between frames or rows, overlapping frames, painterly style, 3D render, blur.
```

## A5. Pinuccia (fendente d'ascia verso l'alto in corsa)
```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference sheets exactly: same character, same face, same outfit and colors, same proportions, same pixel density and outline, SAME SIZE as the attached idle frames (same head size and same body proportions).

SUBJECT: PINUCCIA: soldier with a very pale white face, black round glasses, a black steel helmet, a black padded tactical uniform with knee pads, belts and pouches, black boots, a big steel battle axe with a long wooden handle.

LAYOUT: 2 rows.
Row 1 (8 frames): run cycle holding the axe raised high above the head with both hands, blade up, as a guard against enemies from above: the legs follow the attached run cycle exactly, frame by frame (both feet off the ground in frames 3 and 7); axe and arms in the same position in all 8 frames.
Row 2 (5 frames): upward axe swing while running: axe low behind the hip; swinging up and forward; blade at its highest point above the head, arms fully extended upward; follow-through behind the head; back to the run pose.

CONSISTENCY: strict side view facing right in every frame, same height and scale in every frame and in both rows, feet on the same invisible baseline, evenly spaced frames with WIDE empty gaps so the axe never touches the next frame.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, captions, labels, swoosh trails, motion lines, sparks, dust, front view, three-quarter view, different scale between frames or rows, overlapping frames, painterly style, 3D render, blur.
```

---

# PARTE B — Nemici dall'alto

La scala è indicata rispetto al personaggio giocabile, che in gioco è alto circa 130 px. Per riferimento, le bottiglie nemiche attuali sono più o meno la metà del personaggio. **Allega lo sprite di una bottiglia nemica e un foglio di Albi** come riferimento di stile e di scala.

## B1. Bottiglia a elica (tutte le città, il più frequente)
**In gioco:** una bottiglia con un'elica al posto del tappo vola a mezz'aria e si ferma sopra di te. Lascia cadere tappi esplosivi e, quando è bassa di energia, si lancia in picchiata. Muore con 3 colpi, quindi si abbatte sparando in alto o in diagonale. Colpita, perde quota fumando e si rompe a terra.
```
Create a pixel art enemy sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series, matching the attached reference sprites (same pixel density, same outline, same comic tone).

SUBJECT: a comic flying liqueur bottle enemy: a green glass bottle with a paper label (no readable text on it), angry cartoon eyes and frowning eyebrows painted on the glass, two small white-gloved cartoon arms, and a small spinning helicopter propeller on top instead of the cork. About half the height of the attached player character.

LAYOUT: 3 rows.
Row 1 (4 frames): hovering in the air, propeller in 4 different spin positions, the bottle gently tilting.
Row 2 (3 frames): attack: tilting forward and dropping a small round cork bomb from under the bottle; the empty hands pointing down; diving down head first at an angle.
Row 3 (3 frames): hit (eyes squeezed shut, tilted); damaged and falling with a cracked glass and a bent propeller; smashed on the ground as glass shards with the bent propeller on top.

CONSISTENCY: strict side view facing LEFT (toward the player) in every frame, same scale in every frame, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, glossy glass highlight.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, readable labels, captions, explosions, smoke clouds, motion lines, front view, three-quarter view, different scale between frames, overlapping frames, painterly style, 3D render, blur.
```

## B2. Gabbiano (Genova, Marsiglia) e piccione (Lione, Mantova) che bombardano
**In gioco:** attraversa lo schermo in alto da destra a sinistra stringendo una bottiglia tra le zampe e la lascia cadere sopra di te: un cerchio a terra avvisa dove cadrà. Muore con 1 colpo e lascia cadere la bottiglia dove si trova. Nei livelli sul porto arrivano a stormi di 3.
```
Create a pixel art enemy sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series, matching the attached reference sprites (same pixel density, same outline, same comic tone).

SUBJECT: two comic birds on the same sheet. Bird 1: a big white-and-grey seagull with a yellow beak and an angry cartoon eyebrow. Bird 2: a plump grey city pigeon with an iridescent green-purple neck and an angry cartoon eyebrow. Each bird carries a small green glass bottle clutched in its feet. Each bird is about one third of the height of the attached player character, wings included.

LAYOUT: 4 rows.
Row 1 (6 frames): seagull flying, full wing-flap cycle, carrying the bottle.
Row 2 (3 frames): seagull dropping the bottle (feet opening, bottle falling just below); flying away without the bottle; hit and falling with feathers flying and dizzy eyes.
Row 3 (6 frames): pigeon flying, full wing-flap cycle, carrying the bottle.
Row 4 (3 frames): pigeon dropping the bottle; flying away without it; hit and falling with feathers flying.

CONSISTENCY: strict side view facing LEFT in every frame, same scale for each bird in every frame, evenly spaced frames with wide empty gaps (the wing tips must not touch the next frame).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, labels, captions, motion lines, speed lines, front view, three-quarter view, different scale between frames, overlapping frames, painterly style, 3D render, blur.
```

## B3. Bottiglia paracadutista (tutte le città)
**In gioco:** è il rovescio del vostro ingresso nel livello. Le bottiglie nemiche scendono dal cielo appese a un piccolo paracadute: se le colpisci in aria, valgono più punti e non arrivano a terra. Se atterrano, diventano bottiglie normali che camminano. Colpendo il paracadute, la bottiglia cade di colpo e si rompe.
```
Create a pixel art enemy sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series, matching the attached reference sprites (same pixel density, same outline, same comic tone).

SUBJECT: a comic liqueur bottle enemy with angry cartoon eyes painted on the glass and two small white-gloved cartoon arms, hanging from a small round olive-green military parachute by thin lines. The bottle is about half the height of the attached player character; the canopy is about twice as wide as the bottle.

LAYOUT: 2 rows.
Row 1 (4 frames): descending under the open parachute, swinging slightly left and right, arms holding the lines; the same with a surprised face looking down.
Row 2 (4 frames): the canopy torn and collapsing, the bottle falling fast with a scared face; landing on the ground with bent glass "knees" and the parachute draped behind; standing up ready, the deflated parachute on the ground behind; smashed into glass shards on the ground.

CONSISTENCY: strict side view facing LEFT in every frame, the bottle at the same scale in every frame, evenly spaced frames with wide empty gaps (the canopies must not touch each other).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, readable labels, captions, explosions, motion lines, front view, three-quarter view, different scale between frames, overlapping frames, painterly style, 3D render, blur.
```

## B4. Drone della gendarmeria (Lione e Marsiglia)
**In gioco:** un quadricottero nero che si piazza in alto, davanti a te, e spara raffiche in diagonale verso il basso. Ha 6 colpi di energia. È il nemico per cui serve davvero la diagonale: se resti fermo sotto, ti colpisce. Colpito, fuma e poi precipita.
```
Create a pixel art enemy sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series, matching the attached reference sprites (same pixel density, same outline).

SUBJECT: a black police quadcopter drone: compact armored body with a dark blue stripe and a small blue-and-red siren light on top, four rotors on short arms, a small machine gun turret hanging under the body. About the same width as the attached player character and one third of his height.

LAYOUT: 3 rows.
Row 1 (4 frames): hovering, the four rotors in 4 different spin positions (blurred discs in alternating shapes), the siren light alternating blue and red.
Row 2 (3 frames): turret aiming diagonally down-left; firing recoil (no muzzle flash); turret aiming straight down.
Row 3 (3 frames): hit (body tilted, sparks NOT drawn); damaged with one broken rotor and a bent arm, tilted 30 degrees; crashed wreck lying on the ground.

CONSISTENCY: strict side view (slightly from below, as seen from the street) facing LEFT, same scale in every frame, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, metallic highlights.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, logos, captions, muzzle flash, explosions, smoke clouds, motion lines, front view, top view, different scale between frames, overlapping frames, painterly style, 3D render, blur.
```

## B5. Nemico al balcone (tutte le città, fisso in alto)
**In gioco:** dalle finestre e dai balconi dei palazzi una bottiglia si affaccia e ti lancia vasi di fiori e bottigliette. Tocca a te colpirla in alto prima di passarci sotto. Muore con 2 colpi e cade giù dal balcone. Rende utile lo sparo verso l'alto anche mentre corri.
```
Create a pixel art enemy sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series, matching the attached reference sprites (same pixel density, same outline, same comic tone).

SUBJECT: a small Italian-style building balcony with a wrought-iron railing and green wooden window shutters, and a comic liqueur bottle enemy with angry cartoon eyes and two small white-gloved cartoon arms that lives behind it. The balcony is about as wide as the attached player character; the bottle is about half his height.

LAYOUT: 2 rows.
Row 1 (4 frames): shutters closed; shutters opening with the bottle peeking out; the bottle leaning over the railing holding a terracotta flower pot above its head; throwing the pot down (pot just leaving the hands).
Row 2 (4 frames): the bottle hit, eyes squeezed shut; the bottle falling over the railing head first; the empty balcony with the shutters open; the same balcony with one shutter hanging broken.

CONSISTENCY: front-facing building facade (the balcony seen straight on from the street) with the bottle turned toward the LEFT, the balcony at exactly the same size and position in every frame so the frames can be stacked, evenly spaced frames with wide empty gaps.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image around the balcony (no wall behind it). No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, readable labels, captions, motion lines, explosions, different scale between frames, overlapping frames, painterly style, 3D render, blur.
```

## B6. Mongolfiera-bottiglia (mini-boss in volo, una per città)
**In gioco:** a metà livello una mongolfiera a forma di bottiglia si ferma in alto. Dal cesto due bottiglie lanciano bottiglie e calano bombe a grappolo. Ha una barra di energia come i boss: la colpisci solo sparando in alto o in diagonale. Quando la buchi si sgonfia sputando fuori i passeggeri.
```
Create a pixel art enemy sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series, matching the attached reference sprites (same pixel density, same outline, same comic tone).

SUBJECT: a comic hot-air balloon shaped like a giant green liqueur bottle lying upside down (the envelope is the bottle body, the bottle neck points down into a small burner), patched fabric, ropes down to a wicker basket; inside the basket two small comic bottle enemies with angry cartoon eyes and white-gloved cartoon arms. The whole balloon is about three times the height of the attached player character.

LAYOUT: 3 rows.
Row 1 (3 frames): floating, the burner flame small/big/small, the basket swinging slightly.
Row 2 (3 frames): the bottles in the basket throwing a small bottle down; leaning over and dropping a cluster of three small cork bombs; the basket tilted after the throw.
Row 3 (3 frames): heavily damaged, envelope full of holes and torn patches; deflating and wrinkling, tilting sideways; collapsed envelope draped over the basket on the ground.

CONSISTENCY: strict side view facing LEFT, same scale in every frame, evenly spaced frames with wide empty gaps (the balloons must not touch each other).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no grid lines.

Avoid: text, letters, numbers, readable labels, captions, explosions, smoke clouds, motion lines, front view, three-quarter view, different scale between frames, overlapping frames, painterly style, 3D render, blur.
```
