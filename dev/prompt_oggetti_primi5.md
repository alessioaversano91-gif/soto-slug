# SOTO Slug — Prompt completi: i primi 5 oggetti

Ogni prompt è completo: copialo così com'è, senza aggiungere il blocco di stile (è già dentro). Sono in inglese perché i generatori lo seguono meglio.

## Come usarli per avere fogli puliti
1. **Allega uno sprite del gioco come riferimento** (per esempio un fotogramma di Albi o la Panda bianca) e lascia nel prompt la frase "Match the attached reference". Se lo strumento non accetta immagini, cancella quella frase: il resto funziona lo stesso.
2. **Formato orizzontale 16:9**, la risoluzione più alta che lo strumento consente.
3. **Un prompt per immagine.** Per ostaggio e bancarella genera una città alla volta.
4. Se lo strumento ha un campo **"negative prompt"**, incolla lì il blocco "Avoid" in fondo a ogni prompt e toglilo dal testo principale.
5. **Se un risultato è quasi giusto**, chiedi la correzione nella stessa conversazione ("same sheet, but every frame at the same size") invece di ripartire da zero.
6. Mandami il foglio così com'è: ritaglio, scala, pulizia del magenta e specchiatura li faccio io.

---

## 1. Barile rosso esplosivo
```
Create a pixel art sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a red steel oil drum, 55-gallon size, two raised ribs around the body, a slightly rusty top rim, a bright yellow hazard diamond with a black flame pictogram painted on the front (pictogram only, no letters). Height of the drum = about half the height of a standing adult character.

LAYOUT: one single row of 4 frames, left to right, evenly spaced with wide empty gaps between them, all frames at exactly the same scale and sitting on the same invisible baseline:
1. Intact: clean red paint, small highlight on the left edge.
2. Damaged: two bullet dents, a thin leak of dark liquid, two small yellow sparks.
3. About to explode: the drum bulges outward, seams glowing orange-white, small flames licking out of the cracks.
4. After the blast: only the scorched, torn bottom ring of the drum, blackened, with a thin wisp of smoke.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, strict side view, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no vignette.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective or three-quarter view, 3D render, painterly style, blurry pixels, frames touching or overlapping, frames of different sizes.
```

## 2. Cassa con premio a sorpresa
```
Create a pixel art sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: a sturdy wooden supply crate made of horizontal planks, dark metal reinforcements on the four corners, a big yellow question mark painted on the front with stencil style. Size: a cube about half the height of a standing adult character.

LAYOUT: one single row of 4 frames, left to right, evenly spaced with wide empty gaps, all frames at exactly the same scale and on the same invisible baseline:
1. Intact crate.
2. Cracked: two planks split, splinters, the question mark scratched.
3. Breaking apart: planks flying outward in all directions, small dust cloud, a soft golden glow coming from inside.
4. Debris: a small pile of broken planks and bent corner plates lying flat on the ground.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, strict side view, flat orthographic.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters other than the question mark, numbers, captions, labels, watermark, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```

## 3. Casse di bombe e di munizioni (premi)
```
Create a pixel art item sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: five small pickup items, each one about one third of the height of a standing adult character, drawn in a slightly bigger, chunkier and brighter style so they read clearly as bonuses:
A. Grenade box: olive green military wooden box with the lid open, three round hand grenades visible inside.
B. Ammo box: olive green metal ammo can with the lid open, a belt of brass bullets hanging out.
C. First-aid kit: white case with a red cross.
D. Gold coin: thick gold coin with a star embossed in the middle.
E. Star medal: golden star on a short red-white ribbon.

LAYOUT: 2 rows. Row 1: the five items A to E, left to right, normal state. Row 2: the same five items in the same positions with a white shine sparkle on the upper left corner (for a 2-frame blinking animation). Wide empty gaps between items, every item centered in its own cell, same scale in both rows.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette, dark 1-2 px outline, light from the upper left, flat side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping items, items of different scale between rows.
```

## 4. Ostaggio da liberare (una città per immagine)
Sostituisci il blocco **SUBJECT** con la variante della città. Il resto del prompt resta uguale.

```
Create a pixel art character sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series, inspired by its tied-up prisoners. Match the attached reference: same pixel density, outline thickness, proportions and warm palette.

SUBJECT: [paste one of the city variants below]. Comic, friendly, slightly exaggerated proportions, full body, the same height as the attached playable character when standing.

LAYOUT: 4 rows on an even grid, wide empty gaps between frames, every frame at exactly the same scale and on the same baseline, the character always seen in strict side view facing right:
Row 1 (tied up, 2 frames): sitting on the ground with knees up, hands tied behind the back, ropes around the chest, a white cloth gag; frame 2 struggling and leaning to the other side.
Row 2 (freed, 4 frames): ropes falling off; getting up; standing straight; a big military salute with a happy face.
Row 3 (gives a reward, 2 frames): reaching into a pocket or bag; holding a small item forward with an outstretched arm.
Row 4 (runs away, 4 frames): a comic panicked run cycle, arms flailing.

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective or three-quarter view, 3D render, painterly style, blur, overlapping frames, frames of different sizes, different outfit between frames.
```
**Varianti SUBJECT:**
- **Genova** — `an old Genoese fisherman: white stubble beard, navy blue knit sailor cap, thick dark blue wool sweater, yellow rubber overalls, rubber boots, weathered tanned face`
- **Lione** — `a plump French chef: tall white chef's toque, white double-breasted chef jacket, checked trousers, red neckerchief, curled black mustache, rosy cheeks`
- **Marsiglia** — `an elegant elderly lady: lilac curly hair, big round sunglasses, flowered summer dress, pearl necklace, small handbag; a tiny white poodle tied up next to her (in row 2 and row 4 the poodle runs with her)`
- **Mantova** — `a country farmer from the Po valley: straw hat, checked shirt with rolled sleeves, blue work overalls, rubber boots, big gray mustache, a red handkerchief in the back pocket`

## 5. Bancarella del mercato (una città per immagine)
Sostituisci **GOODS** e **AWNING** con la variante della città.

```
Create a pixel art prop sprite sheet for a 16-bit side-scrolling run-and-gun arcade game in the style of the classic Metal Slug series. Match the attached reference: same pixel density, outline thickness and warm palette.

SUBJECT: an open-air street market stall seen strictly from the side: a wooden counter on trestles, wooden crates displayed on top and below, a striped fabric awning [AWNING] on two thin poles, a small hand-written price board with only drawn symbols (no letters). The stall is as tall as a standing adult character with the awning, and about twice as wide as tall. Goods: [GOODS].

LAYOUT: 2 rows on an even grid, wide empty gaps:
Row 1, 3 frames at exactly the same scale and baseline: (1) intact stall; (2) damaged: awning torn and hanging, a crate cracked, goods spilling on the counter; (3) collapsed: counter broken in the middle, awning on the ground, crates scattered.
Row 2: 6 small separate loose goods from this stall, each about one fifth of a person's height, spread out in a line (they are the items that fall on the ground).

STYLE: crisp hard-edged pixels, no anti-aliasing, no blur, limited palette with 3-4 shades per material, dark 1-2 px outline, light from the upper left, flat orthographic side view.

BACKGROUND: one solid flat magenta color #FF00FF filling the whole image. No floor, no cast shadow, no gradient, no people.

Avoid: text, letters, numbers, captions, labels, watermark, logos, perspective view, 3D render, painterly style, blur, overlapping frames, frames of different sizes.
```
**Varianti:**
- **Genova** — AWNING `(white and blue stripes)`; GOODS `crates of fresh anchovies and fish on ice, lemons, bunches of basil, a basket of focaccia`
- **Lione** — AWNING `(red and white stripes)`; GOODS `hanging dry saucissons, wheels and wedges of cheese, baguettes in a basket, small jars`
- **Marsiglia** — AWNING `(yellow and orange stripes)`; GOODS `bowls of green and black olives, stacked blocks of soap, small lavender sachets, bunches of dried lavender`
- **Mantova** — AWNING `(green and white stripes)`; GOODS `orange pumpkins of different sizes, yellow melons, baskets of pears, braids of onions`
