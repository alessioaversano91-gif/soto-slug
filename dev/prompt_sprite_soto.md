# SOTO Slug — Prompt per generare gli sprite con l'AI

Versione per la 1.3.0.81. I prompt sono in inglese perché i generatori di immagini li seguono meglio; le note sono in italiano.

## Regole che valgono per tutti i fogli
1. **Uno sprite sheet per volta, una sola cosa per foglio** (una vettura, un personaggio, un carro). Più cose nello stesso foglio fanno cambiare scala e stile.
2. **Fondo magenta pieno (#FF00FF)**, senza sfumature, ombre portate o pavimento. Il magenta lo tolgo io; l'ombra sotto le ruote la disegna il gioco.
3. **Niente scritte né numeri di riga.** Il foglio può avere le righe, ma senza titoli: i titoli a volte finiscono sopra lo sprite e vanno mascherati a mano. Se il generatore li mette lo stesso, va bene: li ignoro.
4. **Vista laterale pura, muso o viso verso destra.** Il verso sinistro lo ottengo specchiando.
5. **Stessa scala e stessa linea di terra in tutta la riga.** È l'errore più frequente: i fotogrammi in marcia disegnati più piccoli di quello da fermo. Lo correggo, ma il risultato è più pulito se è giusto all'origine.
6. **Spazio vuoto tra i fotogrammi**: almeno metà larghezza di uno sprite, così il ritaglio automatico non prende pezzi del vicino.
7. **Formato orizzontale grande** (16:9 o 2:1, almeno 2000 px di larghezza). Più grande è il foglio, più nitido è lo sprite in gioco.
8. **Prima immagine di riferimento**: se il generatore accetta immagini, allega uno sprite già nel gioco (es. la Panda bianca o Albi) e scrivi "match the style, palette and pixel density of the attached sprite". È il modo più sicuro per tenere lo stile coerente.

## Blocco di stile (da incollare in ogni prompt)
```
16-bit arcade pixel art in the style of classic side-scrolling run-and-gun games (Metal Slug era),
crisp hard-edged pixels, no anti-aliasing blur, limited palette with 3-4 shades per material,
dark 1-2 px outline, warm late-afternoon lighting from the upper left, slightly cartoonish proportions,
strict side view, facing right, sprite sheet on a solid flat magenta background (#FF00FF),
no ground, no cast shadow, no text, no labels, no frame numbers, no watermark,
generous empty space between frames, every frame at exactly the same scale and baseline.
```
**Da aggiungere come "negative prompt"** (se lo strumento lo prevede, altrimenti in fondo con "Avoid:"):
```
text, letters, captions, row titles, numbers, watermark, gradient background, floor, shadow on background,
perspective view, three-quarter view, isometric, blurry, painterly, 3D render, photorealistic, cropped frames,
overlapping frames, inconsistent scale between frames
```

## 1. Vettura parcheggiata da colpire (2 righe, 8 fotogrammi)
Dalla 1.3.0.81 le vetture non hanno più allarme né fuga: servono solo marcia e distruzione.
```
[STYLE BLOCK]
Sprite sheet of a [VEHICLE: e.g. "white 2010s Italian city car, Fiat Panda style, generic, no logos"],
2 rows, 4 frames per row, aligned on a grid.
Row 1 (driving): frame 1 parked and intact; frames 2-4 the same car driving, wheels rotating
(spokes in three different positions), tiny exhaust puff behind.
Row 2 (destruction): frame 1 damaged — cracked windows, bullet holes, dented doors;
frame 2 burning — flames from the hood and a window, black smoke, scorched paint;
frame 3 exploding — big orange fireball covering the car, flying debris and a door;
frame 4 burnt-out wreck — charred black and rust shell, no glass, no tires, low on the rims.
Same size, same side view and same baseline in all 8 frames.
```
**Note**: niente marchi o targhe leggibili (scrivi "generic, no logos"). Per le auto dei Carabinieri o della Police municipale: "livery inspired by Italian Carabinieri, no readable text".

## 2. Vettura solo traffico (1 riga, 4 fotogrammi)
Per autobus, tram, motorini e tutto ciò che passa soltanto in basso.
```
[STYLE BLOCK]
Sprite sheet of a [VEHICLE: e.g. "orange and white Genoa city bus, 12 m, generic, no logos"],
1 row, 4 frames: frame 1 standing still; frames 2-4 driving, wheels rotating
(three clearly different wheel positions), small exhaust puff. No driver visible
[or: driver visible through the window]. Same size and baseline in all frames.
```
**Note**: per il tram di Lione chiedi 3 fotogrammi di marcia con le ruote che girano (ora ne ha uno solo).

## 3. Cammeo che sfreccia (taxi, motorino)
```
[STYLE BLOCK]
Sprite sheet of a [VEHICLE], 1 row, 3 frames: frame 1 driving fast with speed lines behind;
frame 2 [special move: e.g. "wheelie, front wheel lifted, rider laughing and pointing"];
frame 3 skidding start with a cloud of tire smoke behind.
```

## 4. Personaggio giocabile (es. Pinuccia, pose a mani nude di Albi e Alecio)
```
[STYLE BLOCK]
Character sprite sheet of [CHARACTER: describe face, hair, beard, clothes, colors, body type in detail],
full body, about 2 heads wide and 6.5 heads tall, 6 rows aligned on a grid:
Row 1 idle breathing, 4 frames.
Row 2 walk cycle, 8 frames.
Row 3 jump: take-off, mid-air, landing, 3 frames.
Row 4 crouch, 2 frames.
Row 5 [ATTACK: e.g. "bare-handed punch and kick combo" / "axe swing and axe throw"], 6 frames.
Row 6 hurt (1 frame) and knocked down (3 frames).
Same character, same outfit, same scale and same baseline in every frame.
```
**Note**: allega sempre una foto o lo sprite già fatto del personaggio come riferimento; descrivi i vestiti con gli stessi colori ogni volta. Se il generatore sbaglia le proporzioni, chiedi una riga per volta.

## 5. Nemico o boss (carri di Mantova e boss diversi per città)
```
[STYLE BLOCK]
Boss sprite sheet of a [BOSS: e.g. "comic armored tank shaped like a giant bottle of Lambrusco,
riveted steel, cannon on top, tracks"], big, about 2.5x the height of a person, 4 rows:
Row 1 moving, 3 frames (tracks moving).
Row 2 attacks: cannon fire with muzzle flash, lob shot upwards, ram charge leaning forward — 3 frames.
Row 3 hit flash (white), heavily damaged with smoke, 2 frames.
Row 4 destruction: two explosion frames and the burnt wreck, 3 frames.
```

## 6. Oggetti di scena (chioschi, bancarelle, panchine, panni stesi)
```
[STYLE BLOCK]
Prop sheet for a [CITY / PLACE: e.g. "Genoa old town alley (caruggi)"]: 6 separate props in a row,
each standing alone: [list: "fruit market stall", "newspaper kiosk", "bench", "scooter parked",
"laundry line with hanging clothes", "trash bins"]. For each breakable prop add a second version
below it, smashed and broken.
```

## 7. Sfondi (es. Corso Italia in versione grande, Stazione Principe)
Gli sfondi non vanno su fondo magenta e non sono uno sprite sheet.
```
16-bit arcade pixel art background for a side-scrolling game, wide panorama 3168 x 1344 px,
[PLACE: e.g. "Corso Italia in Genoa: seafront promenade, palm trees, Liberty-style buildings,
the sea and the Boccadasse village in the distance"], late afternoon light, no people, no vehicles,
no text. The bottom 15% is a flat sidewalk edge where the street will be drawn by the game.
Layered depth: distant hills and sky at the top, buildings in the middle, details near the bottom.
Seamless left and right edges if possible.
```
**Note**: indica il punto di vista "eye level, horizon at 40% from the top" per restare coerente con gli altri sfondi.

## 8. Treno della Stazione Principe (finale di Genova)
```
[STYLE BLOCK]
Sprite sheet of an Italian regional train (generic, no logos), long side view, 3 rows:
Row 1 standing at the platform, doors open, 1 frame; doors closing, 1 frame.
Row 2 leaving: 4 frames with wheels turning and slight sparks.
Row 3 a single carriage close-up with the open door, 1 frame (for the jump-on scene).
```

## Come provare e correggere
- **Se la scala cambia tra i fotogrammi**: ripeti la frase "every frame at exactly the same scale and baseline" e chiedi meno fotogrammi per riga.
- **Se compaiono scritte**: aggiungi "absolutely no text anywhere" all'inizio del prompt.
- **Se lo stile è troppo "pittorico"**: aggiungi "chunky visible pixels, 1 pixel = 4x4 screen pixels".
- **Se il fondo non è magenta pieno**: "background must be one flat color #FF00FF, nothing else".
- Mandami il foglio così com'è: ritaglio, scala, pulizia del magenta e specchiatura li faccio io.
