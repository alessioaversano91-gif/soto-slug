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

---

# Oggetti da inserire nei livelli: proposte
Idee prese dai classici arcade a scorrimento (Metal Slug, Final Fight, Contra, Streets of Rage), adattate alle quattro città. Per ognuna: cosa fa in gioco, dove, cosa serve disegnare e il prompt. Priorità: **[A]** alta (rende i livelli più vari subito), **[M]** media, **[B]** bassa.

## Riepilogo
| # | Oggetto | Tipo | Città | Priorità |
|---|---|---|---|---|
| 1 | Ostaggio da liberare | interattivo, premio | tutte | A |
| 2 | Barile rosso esplosivo | distruggibile, esplode | tutte | A |
| 3 | Cassa con premio a sorpresa | distruggibile, premio | tutte | A |
| 4 | Distributore automatico | distruggibile, energia | Lione, Marsiglia, Mantova | M |
| 5 | Bancarella / banco del mercato | distruggibile, premio | tutte (merce diversa per città) | A |
| 6 | Bombole del gas | distruggibile, esplosione a catena | Genova, Marsiglia | M |
| 7 | Idrante | distruggibile, getto d'acqua | tutte | M |
| 8 | Insegna appesa che cade | trappola per i nemici | tutte | M |
| 9 | Container sospeso alla gru | pericolo / trappola | Genova 1-1 Porto, Marsiglia | M |
| 10 | Ape car / muletto da guidare | veicolo del giocatore | Genova 1-1, Mantova | B (grande) |
| 11 | Mitragliatrice fissa sui sacchi | postazione da usare | tutte | M |
| 12 | Tombino con vapore | pericolo a tempo | Lione, Marsiglia | B |
| 13 | Animali di scena (gabbiani, piccioni) | scenario animato | tutte | B |
| 14 | Panni stesi e bandiere | scenario animato | Genova 1-3 caruggi, Marsiglia | B |
| 15 | Cassa di bombe e cassa di munizioni | premio | tutte | A |
| 16 | Specialità della città nascoste | premio | tutte (già nel gioco, nuovi sprite) | M |

## 1. Ostaggio da liberare [A]
**In gioco:** come i prigionieri di Metal Slug. Un turista o un passante legato e imbavagliato; lo liberi sparando alle corde o toccandolo. Si alza, ti ringrazia con un saluto, ti lascia un premio (arma, bombe, energia) e scappa fuori schermo. A fine livello il riepilogo conta gli ostaggi liberati (nuovo obiettivo e medaglia).
**Fotogrammi:** legato seduto (2, si agita), liberato (1), saluto (3), consegna del premio (2), corsa via (4).
```
[STYLE BLOCK]
Character sprite sheet of a tourist hostage: middle-aged man with Hawaiian shirt, shorts, camera around the neck,
sunburnt, tied up with ropes and a gag. 4 rows on a grid:
Row 1 sitting tied up on the ground, struggling, 2 frames.
Row 2 ropes falling off, standing up, then a grateful military salute, 4 frames.
Row 3 pulling an item out of his pocket and handing it forward, 2 frames.
Row 4 running away to the left, comic panic, 4 frames.
```
*Varianti per città: pescatore a Genova, cuoco con toque a Lione, signora col cagnolino a Marsiglia, contadino a Mantova.*

## 2. Barile rosso esplosivo [A]
**In gioco:** si distingue dai barili attuali per il colore e il simbolo di pericolo. 3 colpi e salta in aria: danno ad area ai nemici (e a te, se sei vicino). Lo si usa di proposito contro i gruppi.
```
[STYLE BLOCK]
Prop sprite sheet: a red steel oil drum with a yellow hazard symbol (no text), 1 row, 4 frames:
intact; dented with small leak and sparks; bulging and glowing orange about to blow; scorched bottom ring after the blast.
```

## 3. Cassa con premio a sorpresa [A]
**In gioco:** cassa di legno con un punto di domanda dipinto; rompendola esce un premio a caso (arma, bombe, energia, punti, a volte una bottiglia nemica a sorpresa).
```
[STYLE BLOCK]
Prop sprite sheet: wooden supply crate with a painted question mark, metal corners, 1 row, 4 frames:
intact; cracked; breaking apart with flying planks; broken planks on the ground.
```

## 4. Distributore automatico [M]
**In gioco:** distrugge 5 colpi; cadono 2-3 lattine che ridanno energia (come l'espresso). Da colpo, scintille e vetro rotto.
```
[STYLE BLOCK]
Prop sprite sheet: street vending machine for drinks, generic, no brand, glowing front panel, 1 row, 3 frames:
intact and lit; glass cracked, sparks, light flickering; smashed and dark. Plus 3 small separate cans of soda.
```

## 5. Bancarella / banco del mercato [A]
**In gioco:** copertura che si rompe; rompendola cade la merce: frutta e verdura (punti), a volte la specialità della città. Un tocco di colore per ogni città.
```
[STYLE BLOCK]
Prop sprite sheet: open-air market stall with a striped awning, crates of [GOODS: "fish and anchovies" (Genoa) /
"saucissons and cheeses" (Lyon) / "olives, soaps and lavender bags" (Marseille) / "pumpkins and melons" (Mantua)],
1 row, 3 frames: intact; awning torn and goods spilling; collapsed stall. Plus 6 small separate goods items.
```

## 6. Bombole del gas [M]
**In gioco:** gruppo di 3 bombole davanti a un ristorante. Esplodono una dopo l'altra (catena), con fiammate che salgono: ottime contro i nemici, pericolose per te.
```
[STYLE BLOCK]
Prop sprite sheet: three orange LPG gas cylinders standing together, chained, 1 row, 4 frames:
intact; one hissing with a jet of gas; one exploding in a tall flame; burnt and torn cylinders.
```

## 7. Idrante [M]
**In gioco:** colpito, spara un getto d'acqua verticale per qualche secondo che spinge via i nemici leggeri e spegne le vetture in fiamme.
```
[STYLE BLOCK]
Prop sprite sheet: red street fire hydrant, 1 row, 4 frames: intact; cap blown off; tall water jet (2 frames, splashing).
```

## 8. Insegna appesa che cade [M]
**In gioco:** insegna di un negozio appesa a due catene. Spari alle catene e cade sui nemici sotto (danno forte). Una per livello, come piccolo "trucco" da scoprire.
```
[STYLE BLOCK]
Prop sprite sheet: old shop sign hanging from two chains (wrought iron frame, painted wooden board, no readable text),
1 row, 4 frames: hanging still; one chain snapped, tilted; falling; crashed and broken on the ground.
```

## 9. Container sospeso alla gru [M]
**In gioco:** al Porto Antico e a Marsiglia, un container appeso alla gru sopra la strada; un'ombra a terra avvisa prima che cada (come i cerchi rossi dei pescherecci). Puoi farlo cadere tu sparando al gancio, schiacciando i nemici sotto.
```
[STYLE BLOCK]
Prop sprite sheet: shipping container hanging from a harbor crane hook with steel cables, 1 row, 3 frames:
hanging; cable snapping with sparks; container crashed on the ground, dented, doors open.
```

## 10. Ape car o muletto da guidare [B]
**In gioco:** il "veicolo" del giocatore, come lo Slug di Metal Slug: ci sali sopra, spara e investe, ha una sua barra di energia; quando si rompe salti giù prima che esploda. Lavoro grande (nuovi comandi e collisioni), da fare dopo i punti A.
```
[STYLE BLOCK]
Vehicle sprite sheet: a three-wheeled Italian mini truck (Ape style, generic, no logos) armored with metal plates
and a machine gun mounted on the cargo bed, 4 rows: Row 1 idle and driving, 4 frames; Row 2 firing the gun, 3 frames;
Row 3 damaged with smoke, 2 frames; Row 4 exploding and wreck, 3 frames. Empty driver seat.
```

## 11. Mitragliatrice fissa sui sacchi [M]
**In gioco:** postazione dietro i sacchi di sabbia: se ti avvicini e premi sparo, la usi per qualche secondo con colpi potenti e cadenza alta, ma non puoi muoverti. Anche i nemici possono usarla.
```
[STYLE BLOCK]
Prop sprite sheet: heavy machine gun on a tripod behind a low wall of sandbags, 1 row, 4 frames:
idle; firing with big muzzle flash (2 frames); destroyed and bent.
```

## 12. Tombino con vapore [B]
**In gioco:** ogni tanto sbuffa vapore caldo per un secondo: chi ci passa sopra (tu o i nemici) prende danno. Ritmo da imparare, come le trappole di Contra.
```
[STYLE BLOCK]
Prop sprite sheet: round cast-iron manhole cover in the street (side view, flat), 1 row, 4 frames:
closed; cover lifting with first wisps; tall white steam column (2 frames).
```

## 13. Animali di scena [B]
**In gioco:** gabbiani al porto e piccioni nelle piazze, a terra; quando spari o passi vicino si alzano in volo. Solo scenario, ma rende vive le città.
```
[STYLE BLOCK]
Animal sprite sheet: [ANIMAL: "seagull" / "city pigeon"], 2 rows: Row 1 standing and pecking, 3 frames;
Row 2 taking off and flying away, 4 frames. Small, about one quarter of a person's height.
```

## 14. Panni stesi e bandiere [B]
**In gioco:** tra i palazzi dei caruggi (Genova 1-3) e del Panier (Marsiglia), si muovono al vento; con l'evento "vento" sventolano di più. Solo scenario, da mettere in alto.
```
[STYLE BLOCK]
Prop sprite sheet: a laundry line stretched between two windows with hanging clothes (shirts, sheets, socks),
1 row, 4 frames of gentle waving in the wind. Separate row: a small flag on a pole, 4 frames waving.
```

## 15. Cassa di bombe e cassa di munizioni [A]
**In gioco:** i premi classici, da far uscire dalle casse a sorpresa e dagli ostaggi: +5 bombe, ricarica arma speciale.
```
[STYLE BLOCK]
Item sprite sheet, small icons about 40 px in game: a military box of hand grenades (lid open, 3 grenades visible);
an ammo box with bullets; a first-aid kit; a gold coin; a star medal. 1 row, each item with a 2-frame shine animation.
```

## 16. Specialità della città [M]
**In gioco:** le specialità nascoste esistono già; servono sprite più riconoscibili.
```
[STYLE BLOCK]
Food item sprite sheet, small icons about 40 px in game, 1 row, each with a 2-frame shine:
[Genoa: focaccia slice, farinata, jar of pesto] [Lyon: praline tart, saucisson, quenelle]
[Marseille: bouillabaisse bowl, navette biscuits, pastis glass] [Mantua: tortelli di zucca, sbrisolona cake, pumpkin].
```

## Ordine consigliato
1. **Barile rosso, cassa a sorpresa, cassa di bombe/munizioni** (2, 3, 15): pochi fotogrammi, cambiano subito il modo di giocare.
2. **Ostaggio** (1): è l'elemento più "arcade" e dà un nuovo obiettivo per ogni livello.
3. **Bancarella per città** (5): colore locale con un solo prompt a variante.
4. Poi trappole e scenario (6-9, 11-14), e per ultimo il veicolo da guidare (10).
