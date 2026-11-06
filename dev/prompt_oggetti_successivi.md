# SOTO Slug — Prompt completi: gli oggetti successivi

Seconda serie di oggetti per i livelli. Ogni prompt è completo: si copia e si incolla così com'è. Valgono gli stessi consigli della prima serie (`prompt_oggetti_primi5.md`):
1. **Allega uno sprite del gioco come riferimento** (un fotogramma di Albi o il barile rosso appena fatto). Se lo strumento non accetta immagini, togli la frase "Match the attached reference".
2. **Formato orizzontale 16:9**, alla risoluzione più alta possibile.
3. **Un prompt per immagine.** Se un foglio è quasi giusto, chiedi la correzione nella stessa conversazione.
4. Se c'è un campo **"negative prompt"**, sposta lì il blocco "Avoid".
5. Le copie sfocate o "fantasma" che a volte compaiono nel foglio non sono un problema: le scarto io.

Ordine consigliato: prima **6 e 1** (premi e specialità, servono subito), poi **2, 3, 4, 7, 12** (cambiano il modo di giocare), poi il resto. Il veicolo da guidare (**11**) è il lavoro più grande, da fare per ultimo.

---

## 1. Premi: cassa di bombe, cassa di munizioni, kit medico, moneta, medaglia
Già nella prima serie, ma il foglio manca ancora: oggi dalle casse escono le icone vecchie.
```
Create a pixel art item sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: five small pickup items, each about one third of the height of a standing adult character, drawn slightly chunkier and brighter so they read clearly as bonuses:
A. Grenade box: olive green military wooden box with the lid open, three round hand grenades visible inside.
B. Ammo box: olive green metal ammo can with the lid open, a belt of brass bullets hanging out.
C. First-aid kit: white case with a red cross.
D. Gold coin: thick gold coin with a star embossed in the middle.
E. Star medal: golden star on a short red and white ribbon.

LAYOUT: 2 rows. Row 1: items A to E left to right. Row 2: the same five items in the same positions with a white shine sparkle on the upper left corner (2-frame blinking animation). Wide empty gaps, every item centered in its own cell, same scale in both rows.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline, light from the upper left, flat side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping items, items of different scale between rows.
```

## 2. Bombole del gas (esplosione a catena)
**In gioco:** gruppo di tre bombole davanti a un ristorante; colpite, fischiano e poi esplodono una dopo l'altra con fiammate verticali. Genova e Marsiglia.
```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: three orange LPG gas cylinders standing side by side, held together by a thin chain, brass valves on top, small dents and scratches. The group is as tall as a standing adult character's waist and twice as wide as one cylinder.

LAYOUT: one single row of 5 frames, evenly spaced with wide empty gaps, same scale and same baseline:
1. Intact group.
2. Hit: one cylinder hissing, a thin white jet of gas from its valve, a small dent.
3. First blast: the left cylinder bursting in a tall vertical column of orange flame, the other two still standing.
4. Chain blast: all three cylinders engulfed in a wide fireball with flying metal pieces.
5. Aftermath: three torn, blackened cylinder shells lying on the ground, thin smoke.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, strict side view, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, warning signs with words, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 3. Idrante (getto d'acqua)
**In gioco:** colpito, salta il tappo e parte un getto d'acqua per qualche secondo: allontana i nemici leggeri e spegne le vetture in fiamme. Tutte le città.
```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a red cast-iron street fire hydrant, old European style, with two side outlets and a domed cap, about knee height of a standing adult character.

LAYOUT: 2 rows on an even grid, wide empty gaps, same scale and same baseline in every frame:
Row 1 (3 frames): intact hydrant; hydrant with the cap blown off flying upward and the first splash; broken hydrant without cap, dripping.
Row 2 (4 frames): a tall vertical jet of white and light blue water shooting from the open top, about three times the hydrant's height, splashing droplets at the top, 4 frames of a looping animation with the spray changing shape.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline on the hydrant, water drawn with pixel highlights, light from the upper left, strict side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no puddle, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 4. Insegna appesa che cade
**In gioco:** insegna di bottega appesa a due catene sopra la strada; spari alle catene e cade sui nemici sotto. Una per città, con il disegno della città sulla tavola.
```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: an old shop sign: a wrought iron bracket fixed to a wall, a painted wooden board hanging from it on two chains. The board is about as wide as a standing adult character is tall. The board shows only a painted picture, no words.

LAYOUT: 2 rows on an even grid, wide empty gaps.
Row 1 (4 frames, same board, same scale, the bracket always in the same place at the top): hanging still; one chain snapped and the board tilted at 45 degrees; the board falling (bracket stays, board in mid-air, rotated); the board crashed and split in two on the ground with a puff of dust.
Row 2 (4 separate boards, intact, no bracket): the same board painted with four different pictures: a golden anchor on dark blue; a red lion head on cream; a white sailing ship on teal; a green pumpkin on yellow.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, strict side view, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No wall behind the bracket, no floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, words on the sign, captions, labels, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 5. Container appeso alla gru
**In gioco:** al Porto Antico di Genova e a Marsiglia, un container sospeso sopra la strada; un'ombra a terra avvisa prima che cada. Puoi farlo cadere tu sparando al gancio.
```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a 20-foot steel shipping container, rusty dark red with vertical corrugated sides, hanging from a big yellow harbor crane hook by four steel cables that meet at the hook. Seen strictly from the long side. The container is about twice as long as a standing adult character is tall.

LAYOUT: one single row of 4 frames, evenly spaced with wide empty gaps, same scale:
1. Hanging: hook at the top, cables taut, container level.
2. Snapping: one cable broken with bright sparks at the hook, the container tilting.
3. Falling: the container alone in mid-air, slightly rotated, cables trailing, no hook.
4. Crashed: the container on the ground, crumpled corners, doors burst open, a cloud of dust at the base.
Also draw, under frame 1, a flat dark oval shadow on its own (used as the warning on the ground).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, strict side view, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No crane tower, no floor, no gradient.

Avoid: text, letters, numbers, shipping company names, captions, labels, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 6. Specialità della città (una città per immagine)
**In gioco:** le specialità nascoste esistono già; questi sprite le rendono riconoscibili. Quattro prompt pronti.

### Genova
```
Create a pixel art food item sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: three Genoese food specialties as small pickup items, each about one third of the height of a standing adult character, appetizing and slightly exaggerated: a square slice of golden focaccia with dimples and oil shine; a wedge of farinata (thin golden chickpea pancake) with a dark crispy edge; a small glass jar of bright green pesto with a basil leaf on the lid.

LAYOUT: 2 rows. Row 1: the three items left to right. Row 2: the same three items in the same positions with a white shine sparkle on the upper left (2-frame blinking animation). Wide empty gaps, same scale in both rows.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline, light from the upper left, flat side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No plate, no table, no shadow, no gradient.

Avoid: text, letters, numbers, labels on the jar, captions, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping items.
```
### Lione
```
Create a pixel art food item sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: three Lyon food specialties as small pickup items, each about one third of the height of a standing adult character, appetizing and slightly exaggerated: a slice of bright pink praline tart; a dry saucisson with a white skin and a cut slice showing the inside; a golden quenelle (oval dumpling) in a little pool of creamy sauce in a small dish.

LAYOUT: 2 rows. Row 1: the three items left to right. Row 2: the same three items in the same positions with a white shine sparkle on the upper left (2-frame blinking animation). Wide empty gaps, same scale in both rows.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline, light from the upper left, flat side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No table, no shadow, no gradient.

Avoid: text, letters, numbers, labels, captions, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping items.
```
### Marsiglia
```
Create a pixel art food item sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: three Marseille food specialties as small pickup items, each about one third of the height of a standing adult character, appetizing and slightly exaggerated: a bowl of orange bouillabaisse fish soup with a fish tail and a mussel sticking out; three navette biscuits (small boat-shaped orange-blossom cookies) stacked; a slice of toasted bread with rouille and a little garlic clove beside it.

LAYOUT: 2 rows. Row 1: the three items left to right. Row 2: the same three items in the same positions with a white shine sparkle on the upper left (2-frame blinking animation). Wide empty gaps, same scale in both rows.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline, light from the upper left, flat side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No table, no shadow, no gradient.

Avoid: text, letters, numbers, labels, captions, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping items.
```
### Mantova
```
Create a pixel art food item sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: three Mantua food specialties as small pickup items, each about one third of the height of a standing adult character, appetizing and slightly exaggerated: a small plate of tortelli di zucca (pumpkin ravioli) with melted butter and sage leaves; a round crumbly sbrisolona almond cake with a piece broken off; a whole orange pumpkin with a green stem.

LAYOUT: 2 rows. Row 1: the three items left to right. Row 2: the same three items in the same positions with a white shine sparkle on the upper left (2-frame blinking animation). Wide empty gaps, same scale in both rows.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline, light from the upper left, flat side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No table, no shadow, no gradient.

Avoid: text, letters, numbers, labels, captions, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping items.
```

## 7. Mitragliatrice fissa sui sacchi
**In gioco:** postazione dietro i sacchi di sabbia: se ti avvicini e premi sparo la usi per qualche secondo, con colpi potenti ma senza poterti muovere. Anche i nemici possono usarla.
```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a heavy machine gun on a low tripod, mounted behind a curved wall of stacked sandbags (two layers), the gun barrel pointing right over the sandbags, an ammo belt hanging from the left side. The sandbags reach the waist of a standing adult character; nobody is operating the gun.

LAYOUT: one single row of 5 frames, evenly spaced with wide empty gaps, same scale and same baseline:
1. Idle.
2. Firing: big bright muzzle flash at the barrel tip, the gun recoiling slightly.
3. Firing: smaller muzzle flash, brass casings flying out to the left.
4. Overheated: barrel glowing orange with a thin wisp of smoke.
5. Destroyed: the gun bent and broken, sandbags torn with sand spilling.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, strict side view, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, logos, soldiers, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 8. Tombino con vapore
**In gioco:** ogni tanto sbuffa vapore caldo per un secondo; chi ci passa sopra (tu o i nemici) prende danno. Lione e Marsiglia.
```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a round cast-iron manhole cover set in the street, seen from the side so it looks like a thin flat dark plate lying on the ground, about as wide as a standing adult character's shoulders, with a small raised grid pattern on its edge.

LAYOUT: one single row of 5 frames, evenly spaced with wide empty gaps, same scale and same baseline (the ground line at the bottom of every frame):
1. Closed, still.
2. The cover lifting a little on one side, first thin wisps of white steam escaping.
3. Tall column of white steam, as tall as a standing adult character, the cover jumping a little.
4. Same steam column at full height, different puffy shape (for a looping animation).
5. Steam fading into small puffs, the cover settling back.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline on the cover, soft-looking but pixel-drawn steam with 3 shades of white and light grey, light from the upper left, strict side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No street, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective view, top-down view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 9. Animali di scena (due immagini)
**In gioco:** a terra in alcuni punti; quando spari o passi vicino si alzano in volo. Solo scenario.
### Gabbiano (Genova, Marsiglia)
```
Create a pixel art animal sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a seagull, white body, grey wings with black tips, yellow beak and orange legs, slightly comic and cheeky expression. Standing, it is about one quarter of the height of a standing adult character.

LAYOUT: 2 rows on an even grid, wide empty gaps, every frame at the same scale, strict side view facing right:
Row 1 (4 frames): standing; pecking the ground; looking around; squawking with the beak wide open.
Row 2 (4 frames): crouching to take off; first wing flap leaving the ground; wings fully up while flying; wings fully down while flying (frames 3 and 4 loop).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```
### Piccione (Lione, Mantova)
```
Create a pixel art animal sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a plump city pigeon, blue-grey body, iridescent green and purple neck, two dark wing bars, orange eye, pink feet. Standing, it is about one fifth of the height of a standing adult character.

LAYOUT: 2 rows on an even grid, wide empty gaps, every frame at the same scale, strict side view facing right:
Row 1 (4 frames): standing; walking with the head forward; walking with the head back; pecking the ground.
Row 2 (4 frames): crouching to take off; first wing flap leaving the ground; wings fully up while flying; wings fully down while flying (frames 3 and 4 loop).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 10. Panni stesi e bandierine
**In gioco:** tesi tra i palazzi dei caruggi (Genova 1-3) e del Panier (Marsiglia), in alto; si muovono al vento e di più con l'evento "vento". Solo scenario.
```
Create a pixel art decoration sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: A. a laundry line stretched horizontally with a gentle sag, hanging clothes pegged to it: a white shirt, a striped blue sheet, a red dress, two socks and a towel; the line is about three times as wide as a standing adult character is tall. B. a short string of small colored triangular bunting flags (red, yellow, blue, green, white).

LAYOUT: 2 rows on an even grid, wide empty gaps, same scale in every frame, flat side view:
Row 1 (4 frames): the laundry line A, the clothes swinging gently in the wind, 4 frames of a looping animation.
Row 2 (4 frames): the bunting B fluttering in the wind, 4 frames of a looping animation.
The ends of the line and of the bunting stop at the frame edges (they will be attached to walls in the game).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3 shades per fabric, dark 1 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No walls, no windows, no sky, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 11. Veicolo da guidare: Ape blindata
**In gioco:** come lo Slug di Metal Slug. Ci sali, spara e investe, ha la sua energia; quando sta per esplodere salti giù. Genova 1-1 e Mantova. È il lavoro più grande (comandi e collisioni nuovi): conviene farlo per ultimo.
```
Create a pixel art vehicle sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a small Italian three-wheeled mini truck (Ape style, generic, no logos), light blue paint, armored with riveted grey metal plates on the doors and the cargo bed, a heavy machine gun on a swivel mount in the cargo bed pointing right, spare tire and sandbags on the bed. The cab is empty (the player character is added on top in the game). The vehicle is slightly taller than a standing adult character with the gun, and about twice as long as it is tall.

LAYOUT: 4 rows on an even grid, wide empty gaps, every frame at exactly the same scale and baseline, strict side view facing right:
Row 1 (4 frames): parked; driving with wheels rotating (three different wheel positions), small exhaust puff.
Row 2 (3 frames): the gun firing with a big muzzle flash; the gun firing with a smaller flash and brass casings; the vehicle jumping with the front wheel in the air.
Row 3 (2 frames): damaged with dents, cracked windshield and grey smoke from the engine; heavily damaged with flames from the hood and sparks.
Row 4 (3 frames): exploding in a big orange fireball with flying metal plates; second explosion frame with smoke; burnt-out wreck on the ground.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, license plates, brand names, captions, labels, watermark, logos, driver, perspective or three-quarter view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 12. Distributore automatico
**In gioco:** colpito, si rompe e fa cadere 2-3 lattine che ridanno un po' di energia (come il caffè). Lione, Marsiglia e Mantova.
```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a street vending machine for cold drinks, generic, no brand: a tall red and white metal cabinet with a glowing glass front showing rows of colorful cans, a coin slot and a dispensing flap at the bottom. As tall as a standing adult character.

LAYOUT: 2 rows on an even grid, wide empty gaps.
Row 1 (3 frames, same scale and baseline): intact with the front panel lit; hit: glass cracked, sparks, the light flickering half off; destroyed: glass smashed, panel dark, a door hanging open, a little smoke.
Row 2: four separate small soda cans (red, green, orange, blue), each about one eighth of a person's height, plain colors with a simple stripe, lying on their side.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, strict side view, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No wall, no floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, brand names, logos on the cans or on the machine, captions, labels, watermark, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```
