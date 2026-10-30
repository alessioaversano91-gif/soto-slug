# SOTO Slug — Checklist di sviluppo

Versione di riferimento: 1.3.0.63 BETA
Priorità: [A] alta · [M] media · [B] bassa

## 1. Bug e difetti noti
- [x] [A] Albi non muove le gambe quando spara camminando (1.3.0.6)
- [x] [A] Scritte al contrario su bottiglie e boss quando guardano a sinistra (1.3.0.6)
- [x] [M] Piccolo scatto laterale quando Albi si gira: verificato, le pose ruotano attorno alla testa (1.3.0.36)
- [x] [M] Stacco di stile nello sparo di Albi e Alecio: sostituito dalle pose dei fogli armati (1.3.0.28)
- [x] [M] Gamba sinistra di Seba sottile nella posa di tiro: posa rimossa col passaggio al mitra (1.3.0.36)
- [x] [M] Alecio rimpicciolito nella posa di tiro: vecchio sprite di sparo rimosso (1.3.0.36)
- [x] [M] Nemici entrati da sinistra che sparano da fuori schermo: ora sparano solo se visibili (1.3.0.30)
- [x] [M] Invio che agisce due volte nei menu: niente ripetizione tenendolo premuto, niente doppio comando col pulsante attivo (1.3.0.30)
- [ ] [B] Ritocchi visibili nello sfondo di Lione
- [x] [M] Fascia scura sopra il selciato di Lione: lo sfondo era alto 38 px meno del dovuto (1.3.0.12)
- [x] [B] Lampeggio ostacoli gestito nel disegno invece che nella logica (1.3.0.56)
- [x] [B] Font arcade incorporato nel gioco, funziona anche offline (1.3.0.36)
- [x] [B] Sprite centrati nelle schede di selezione, l'ascia di Pinuccia non tocca più il bordo (1.3.0.11)
- [x] [M] Luce dei lampioni che sbiancava i personaggi (1.3.0.7)

## 2. Grafica — asset da generare
### Personaggi
Ogni personaggio ha due fogli sprite: mani nude e armato. Dalla 1.3.0.28 tutti partono con lo stesso mitra generico; le armi bonus arriveranno lungo i livelli. Pinuccia per ora resta con l'ascia gigantesca.

**Albi**
- [x] [A] Albi a mani nude (1.3.0.2)
- [x] [A] Albi armato (mitra): fermo, sparo, cammina e spara, accucciato, salto, bomba in piedi/accucciato/in salto, atterraggio, sequenza di morte (1.3.0.28)
- [x] [M] Albi: corpo a corpo col mitra in piedi (3 fotogrammi), stordimento, vittoria, morte carbonizzata, posa di colpito nello stile nuovo (1.3.0.31)
- [x] [M] Albi: colpito col mitra in mano (2 fotogrammi) e corpo a corpo accucciato col mitra (3 fotogrammi) (1.3.0.32)
- [x] [B] Mitra disegnato dal foglio di Albi come arma provvisoria di Seba e Lollo (poi sostituito da UZI e fucile) e come icona dell'arma nell'HUD (1.3.0.32)
- [x] [M] Albi: salto a mezz'aria superato dalle pose di salto col mitra (1.3.0.28)

**Lollo**
- [x] [A] Lollo a mani nude (1.3.0.6)
- [x] [A] Lollo col fucile: fermo con respiro, sparo, cammina e spara, accucciato, salita e discesa del salto, sparo in salto, mira in alto e sparo in basso, lanci, corpo a corpo in piedi e accucciato, colpito, stordimento, vittoria, morte, corsa, attesa lunga, ingresso col paracadute, fucile a terra e nell'HUD (1.3.0.47)
- [x] [A] Lollo parte a mani nude in ogni livello e trova il fucile uccidendo il cane o al 12° nemico abbattuto (1.3.0.47)
- [x] [M] Lollo a mani nude: combo pugno-calcio-pugno-calcio rotante, calcio in salto, calcio da accucciato, lanci di bomba in 3 tempi, stordimento, vittoria, caduta e morte, raccolta dell'arma, ritratti HUD normale/colpito/vittoria (1.3.0.47)
- [x] [M] Lollo: fotogramma di salto a mezz'aria rigenerato, superato dalle pose di salto del nuovo foglio (1.3.0.47)
- [x] [B] Lollo: discesa col paracadute a mani nude in 2 tempi e atterraggio con la calotta che si affloscia (1.3.0.48)
- [x] [B] Lollo: morte carbonizzata col fucile (sagoma nera, poi mucchietto di cenere) (1.3.0.48)
- [x] [B] Lollo: arretra sparando col fucile (tieni premuto FUOCO e la direzione opposta: resta girato verso il nemico), camminata dedicata in 4 tempi (1.3.0.48)
- [x] [M] Lollo: calcio rotante speciale ad area a energia piena, al posto del colpo finale della combo; colpisce davanti e dietro e respinge i nemici (1.3.0.48)

**Fucile a pompa (shotgun)**
- [x] [B] Sprite salvati: Lollo fermo, sparo e camminata col fucile a pompa, fucile a terra, icona "S" (1.3.0.48, non ancora in gioco)
- [x] [A] Regole decise (10 ottobre):
  - solo Lollo
  - 20 colpi in totale
  - si ottiene con una serie: tot nemici abbattuti di fila senza subire danni
  - nemici standard: 1 colpo; gendarmi: 2 colpi; boss finale: almeno 10 colpi
- [x] [A] Serie di 8 nemici abbattuti di fila senza subire danni (vale ogni nemico tranne il carro); il primo danno la azzera; vale anche a mani nude (1.3.0.49)
- [x] [A] Shotgun a terra a fine serie; raccolto dà 20 colpi; una nuova serie con lo shotgun carico lascia a terra una ricarica che riporta i colpi a 20 (1.3.0.49)
- [x] [A] Danni: nemici standard e cane 1 colpo, gendarmi 2 colpi (lo shotgun non viene parato dal manganello), carro boss di ogni livello 10 colpi; auto e ostacoli danno forte (1.3.0.49)
- [x] [A] A colpi finiti torna all'arma di prima: fucile se già trovato, altrimenti mani nude; perdendo una vita lo shotgun si perde (1.3.0.49)
- [x] [A] Pose dello shotgun: fermo con respiro, sparo con fiammata disegnata e pompata, cammina e spara, camminata in 4 tempi, accucciato e sparo, salto in salita e discesa, sparo in salto, mira in alto, sparo in basso, lanci (in piedi, accucciato, in salto), corpo a corpo, colpito; icona "S" nell'HUD (1.3.0.49)
- [x] [B] HUD: contatore "SERIE n/8" e colpi rimasti "POMPA n" sopra l'icona dell'arma (1.3.0.49)
- [x] [B] Colpo a rosa: 3 pallettoni, ogni sparo colpisce fino a 3 nemici in fila, gittata corta; suono dedicato, pompata e bossolo rosso (1.3.0.49)
- [x] [B] Ultimi 5 colpi: scritta "ULTIMI COLPI!", contatore rosso e segnale acustico a ogni colpo (1.3.0.49)
- [x] [B] Riepilogo di fine livello: riga "SERIE MIGLIORE" con 250 punti per nemico (la medaglia "NESSUN DANNO!" da 5000 punti c'era già) (1.3.0.49)
- [ ] [M] Confermare: "boss finale" oggi è il carro di ogni livello; se intendi solo il boss dell'ultimo livello, cambia solo quello
- [x] [B] Correzioni shotgun col fucile in mano: lancio in piedi, pugno del corpo a corpo, colpito (1.3.0.51)
- [x] [B] Shotgun: vittoria in 2 tempi, stordimento con le stelline, caduta e morte col fucile a pompa, corsa in 4 tempi (1.3.0.51)
- [x] [B] Morendo con lo shotgun la sequenza di morte lo mostra in mano; si perde alla ripartenza (1.3.0.51)
- [x] [A] Foglio completo del fucile a pompa ricevuto e integrato (1.3.0.49)

**Seba**
- [x] [A] Seba a mani nude (1.3.0.7)
- [ ] [M] Seba: fotogramma di salto a mezz'aria e parata rigenerati con margine sopra il cappello
- [x] [A] Seba: parte a pugni e bombe, trova l'UZI eliminando il cane (Genova) o 12 nemici; set UZI integrato (1.3.0.40)

**Alecio**
- [x] [A] Alecio a mani nude (1.3.0.8)
- [x] [M] Alecio: salto a mezz'aria superato dalle pose col mitra (1.3.0.35)
- [x] [A] Alecio armato (mitra): mira, sparo con rinculo, corsa e sparo nei due versi, accucciato, granata, vittoria, stordimento, morte bruciato (1.3.0.28)
- [x] [A] Alecio: set completo dal foglio "Full Combat Expansion" — corsa e sparo a piena risoluzione, sparo con rinculo, corpo a corpo col mitra in piedi e accucciato, salto e sparo in aria, bomba in piedi e in salto, colpito, stordimento, vittoria, caduta e morte, morte carbonizzata, atterraggio (1.3.0.33)
- [x] [M] Alecio: mitra sempre visibile nel salto, con la posa dello sparo in aria (1.3.0.35)
- [x] [B] Alecio: salita e discesa dedicate col mitra, lancio della bomba accucciato, seconda posa di colpito col mitra, suo mitra isolato per l'HUD (1.3.0.45-46)
- [x] [M] Alecio: corsa e sparo con tutti i fotogrammi completi, zaino compreso anche se incoerente (1.3.0.29)
- [x] [B] Alecio: corsa e sparo in risoluzione piena (1.3.0.33)

**Pinuccia**
- [x] [A] Pinuccia con ascia gigantesca: foglio unico, lancio in 5 tempi, fendente, affondo, attacco basso, lancio in aria (1.3.0.10)
- [x] [M] Pinuccia: proporzioni uniformate agli altri personaggi (1.3.0.10)
- [x] [B] Pinuccia: pose di presa dell'ascia per il boomerang (1.3.0.56) e attacco in salto completo in 5 tempi, la schiacciata (1.3.0.58)

**Tutti**
- [x] [M] Salto per Albi (1.3.0.5), Lollo (1.3.0.6), Seba (1.3.0.7)
- [x] [M] Salto per Alecio (1.3.0.8)
- [x] [M] Salto per Pinuccia (1.3.0.10)
- [ ] [B] Ritratti HUD con espressioni

### Nemici
- [x] [A] Bottiglia di birra ridisegnata: vetro marrone, tappo a corona dorato, etichetta "BIRRA" con spiga, fascetta sul collo (1.3.0.25)
- [ ] [A] Bottiglia Chartreuse: camminata, attacco, morte
- [ ] [M] Bottiglia volante con ali disegnate
- [x] [M] Boss di Lione: Carro Chartreuse con movimento, tre attacchi, colpo subito ed esplosione (1.3.0.9)
- [x] [A] Vecchio boss con difetti grafici (bottiglia tagliata, cingoli finti) ritirato (1.3.0.16)
- [x] [M] Boss di Genova e Marsiglia: Carro Chartreuse Gialla ed Élixir, da sinistra, più resistenti e rapidi (1.3.0.16)
- [ ] [M] Fogli dedicati per i boss di Genova e Marsiglia (oggi varianti di colore del carro)
- [ ] [B] Proiettili nemici disegnati
- [x] [A] Gendarmerie de Lyon: nuovo nemico solo a Lione, più raro (circa 1 su 7), 10 HP, da destra e da sinistra (1.3.0.19)
- [x] [M] Gendarmerie: minaccia "HALTE!", fendente, colpo dall'alto, balzo, granata, parata, danno, morte e corpo a terra (1.3.0.19)
- [ ] [B] Gendarmerie: rigenerare i due fotogrammi finali di "Attacco verso il basso" separati (nel foglio le asce si sovrappongono)
- [x] [A] Auto della Gendarmerie a Lione e Marsiglia: 2 apparizioni (destra e sinistra), testacoda, sosta con lampeggianti, fuga dopo i colpi (1.3.0.20)
- [x] [A] Pastore tedesco solo a Genova: 3 apparizioni (destra, sinistra, destra), morso in corsa, ringhio e balzo, 1 punto di danno (1.3.0.20)
- [ ] [M] Nemico dedicato per Marsiglia a piedi, sul modello della Gendarmerie
- [ ] [B] Auto: usare le pose di frenata senza lampeggianti (righe 2 e 4 del foglio) se servono scene diverse
### Sfondi e scenografia
- [x] [A] Concept di Marsiglia: Vieux Port e Notre-Dame de la Garde (1.3.0.12)
- [x] [A] Concept di Genova: Porto Antico, Lanterna, San Lorenzo, galeone (1.3.0.13)
- [x] [A] Genova panoramica: il livello attraversa tutto il porto, dal Porto Antico al cantiere navale (1.3.0.14)
- [x] [M] Marsiglia panoramica: dalla Cattedrale de la Major al porto turistico (1.3.0.15)
- [x] [A] Marsiglia parte 2: porto dei pescatori con il faro, stesse impostazioni della parte 1, boss solo alla fine della parte 2 (1.3.0.21)
- [x] [M] Marsiglia parte 2: nemici o eventi propri, se vuoi differenziarla dalla parte 1 — pioggia di bottiglie dai pescherecci (1.3.0.56)
- [x] [A] Stage 4 Mantova: castello di San Giorgio, Sant'Andrea, ponte sul Mincio; solo nemici base (Chartreuse, birra, volante) e Carro Chartreuse come boss (1.3.0.22)
- [ ] [A] Mantova: nemici personalizzati (in arrivo)
- [x] [B] Selezione stage su due righe per ospitare 4 città (1.3.0.22)
- [x] [A] Nuovo ordine del viaggio: Genova > Lione > Mantova > Marsiglia; numerazione, selezione stage e boss seguono il viaggio (1.3.0.23)
- [x] [M] Boss sempre più resistenti lungo il viaggio: 260 > 300 > 340 > 400 punti energia (1.3.0.23)
- [x] [B] Selezione diretta della parte 2 di Marsiglia dal menu degli stage (1.3.0.55)
- [x] [M] Lione panoramica: da Saint-Jean a Fourvière e ai ponti sulla Saona (1.3.0.16)
- [x] [B] Marsiglia: cartelli con le scritte di Lione, risolto dal nuovo panorama (1.3.0.15)
- [x] [A] Palais Longchamp piatto sostituito dal concept di Marsiglia (1.3.0.12)
- [x] [A] Palazzo Ducale piatto sostituito dal concept di Genova (1.3.0.13)
- [ ] [M] Strato intermedio in parallasse per Lione
- [ ] [M] Ostacoli disegnati
- [x] [B] Banchina di Genova accordata ai colori del panorama (1.3.0.14)
- [x] [B] Strada di Marsiglia accordata ai colori del panorama (1.3.0.15)
- [ ] [B] Logo grafico del titolo

## 3. Meccaniche di gioco
- [x] [A] Energia (20), 3 vite, morte con le pose dei fogli, respawn e GAME OVER con "Riprova lo stage" (1.3.0.25)
- [x] [A] Modalità GOD (predefinita, invincibili) e LIFE (vite e game over): selezione stage, pausa, tasto G (1.3.0.26)
- [x] [M] Tabella dei danni nemici pronta: bottiglie 1-2, carri 2-3, Gendarmerie 3-5; con la GOD MODE vengono solo conteggiati (1.3.0.19)
- [x] [A] Confermare Seba: mitra come tutti; ha più bombe (14) come richiamo al granatiere (1.3.0.30)
- [x] [A] Pausa: P / Esc / pulsante II, automatica se si cambia scheda; menu con Continua, Audio, Modalità, Titolo (1.3.0.25)
- [ ] [M] Piattaforme su cui atterrare
- [x] [M] Mira verso l'alto automatica (Albi e Seba con UZI) e sparo verso il basso in salto (Albi) (1.3.0.43)
- [x] [M] Corpo a corpo per Albi (1.3.0.2), Lollo con calcio alternato (1.3.0.6) e Seba con montante basso (1.3.0.7)
- [x] [M] Corpo a corpo per Alecio: pugni, calcio basso, pugno basso in affondo (1.3.0.8)
- [x] [M] Corpo a corpo per Pinuccia: fendente, affondo, attacco basso (1.3.0.10)
- [x] [A] Passaggio tra mani nude e arma: mitra sempre in mano, mani nude solo nel corpo a corpo (1.3.0.28)
- [ ] [A] Armi bonus lungo il livello (idee in arrivo)
- [x] [A] Pinuccia resta con l'ascia gigante (deciso il 3 ottobre)
- [x] [B] Pose di morte dei fogli in uso, con il fantasmino di Pinuccia (1.3.0.25); parata ancora da usare
- [ ] [B] Usare le pose di parata presenti nei fogli (le pose di morte sono in uso), compresa la sequenza di morte di Pinuccia con il fantasmino (servono energia e game over)
- [x] [M] Bombe limitate con rifornimenti: scorta per personaggio, cassa +3, infinite in GOD (1.3.0.30)
- [ ] [M] Armi raccoglibili
- [x] [M] Ondate costruite a mano: 2-3 per città in punti fissi, schermo bloccato, nemici da entrambi i lati, poi un momento di calma (1.3.0.55)
- [x] [M] Difficoltà crescente lungo il viaggio: più nemici insieme, arrivi più ravvicinati, bottiglie più resistenti nelle ultime città (1.3.0.55)
- [x] [M] Riepilogo di fine stage con bonus (1.3.0.30)
- [x] [M] Finale e titoli di coda dopo Marsiglia (1.3.0.36)
- [ ] [B] Ostaggi da liberare
- [ ] [B] Veicolo guidabile
- [x] [B] Moltiplicatore combo fino a x3 (1.3.0.36)
- [x] [B] Barra di avanzamento e freccia GO (1.3.0.30)
- [ ] [B] Modalità a 2 giocatori

## 4. Audio
- [x] [A] Effetti sonori chiptune sintetizzati: 32 suoni per armi, esplosioni, vetri, nemici, auto, boss, mappa e jingle (1.3.0.25)
- [x] [M] Musica chiptune: titolo, mappa, un tema per città, boss; interruttore MUSICA in pausa e tasto N (1.3.0.27)
- [x] [M] Voce annunciatore — voce sintetica del browser, disattivabile (1.3.0.56)
- [x] [B] Tasto muto (M e pulsante sulla pulsantiera), ricordato tra una partita e l'altra (1.3.0.25)
- [x] [B] Audio sbloccato al primo tocco o tasto, come richiesto da iPhone e dai browser (1.3.0.25)

## 5. Interfaccia e comandi
- [x] [A] Pulsantiera touch sotto lo schermo (1.3.0.4)
- [x] [A] Legenda dei tasti (1.3.0.4)
- [x] [A] Salto per Albi (1.3.0.5)
- [x] [M] Menu impostazioni: volume musica ed effetti, scossoni ridotti, vibrazione, schermo intero (1.3.0.36)
- [x] [M] Supporto gamepad (1.3.0.36)
- [x] [M] Pulsante schermo intero (impostazioni, pulsantiera, tasto F) (1.3.0.36)
- [x] [M] Vibrazione del telefono quando si viene colpiti (1.3.0.36)
- [x] [A] Pulsantiera a due pollici: frecce grandi con scorrimento del dito a sinistra, fuoco/salto/bomba a destra (1.3.0.16)
- [x] [M] Selezione personaggi: solo posa ferma che respira (1.3.0.16)
- [x] [B] Schermata iniziale: personaggi fermi che respirano, non più camminata e spari (1.3.0.17)
- [x] [A] Pulsantiera rivista: salto nella croce di sinistra (▲ sopra ▼) con salto in corsa scivolando da ▶ a ▲; BOMB grande come FIRE (1.3.0.18)
- [ ] [M] Collaudo della nuova pulsantiera su telefono vero (tempi di scivolamento del pollice, dimensioni reali)
- [x] [B] Layout orizzontale per telefono (1.3.0.56)
- [x] [B] Nome del boss nella barra energia (Carro Chartreuse a Lione) (1.3.0.9)
- [x] [B] Nomi dei boss di Genova e Marsiglia (1.3.0.16)
- [x] [B] Avviso d'arrivo del boss non più sovrapposto alla barra energia (1.3.0.16)
- [x] [B] Tasti indietro nei menu, anche con Esc (1.3.0.36)
- [x] [B] Classifica coi nomi (10 punteggi) e migliori tempi del Boss Rush (1.3.0.55)

## 6. Tecnica e prestazioni
- [x] [A] Ridurre il peso del file: WebP senza perdita, da 4 MB a 2,5 MB (1.3.0.11)
- [x] [B] Peso del gioco: da 11,9 MB a 5,6 MB (compressione degli sprite e pose inutilizzate escluse dall'assemblaggio) (1.3.0.55)
- [x] [M] Tetto massimo di particelle (1.3.0.30)
- [x] [M] Luci più leggere per i telefoni (1.3.0.30)
- [x] [B] Pulizia del codice ereditato: vecchie armi, vecchi sprite di sparo, boss ritagliato, codice morto (1.3.0.30)
- [x] [B] Rimuovere anche i disegnatori procedurali di cielo, mare e città di Genova e Marsiglia (ancora collegati alle etichette degli stage) (1.3.0.56)
- [ ] [B] Motore separato dagli asset (parzialmente fatto: gli sprite restano in PNG nei sorgenti e vengono convertiti solo nell'assemblaggio)

## 7. Specifiche per i fogli sprite
- Sfondo magenta o verde pieno
- Margine attorno a ogni fotogramma, soprattutto sopra la testa
- Stessa scala per tutte le righe
- Fotogrammi rivolti a destra
- Niente ombre, fiammate o scritte nelle celle
- Sprite attuale allegato come riferimento

## 8. Da osservare durante le prove
- [ ] Piedi che galleggiano o affondano
- [ ] Scatti nei cambi di posa
- [ ] Ritmo: momenti vuoti o caotici
- [x] Durata dei livelli — misurata col bot: 75-130 s a città, Marsiglia 160-260 s (1.3.0.56)
- [x] Bilanciamento del boss tra i personaggi — tarato col bot: pugni e calci contro i carri dimezzati (1.3.0.56)
- [ ] Fluidità e batteria sul telefono
- [ ] Comodità dei comandi touch

## 9. Extra — cose che si potrebbero aggiungere
Idee emerse durante lo sviluppo, da valutare. Nessuna è indispensabile.

### Gioco
- [x] L'auto della Gendarmerie fa scendere due gendarmi a Lione (1.3.0.36)
- [x] Casse con la stella che lasciano bombe, caffè, specialità o punti (1.3.0.36) —: bombe, punti, e cibo tipico che ricarica energia (quenelle a Lione, focaccia a Genova, bouillabaisse a Marsiglia, tortelli di zucca a Mantova)
- [ ] Idee per i nemici di Mantova: bottiglie di Lambrusco e zanzare del Mincio come nemico volante
- [x] Boss "ferito": sotto il 50% fuma, perde pezzi e attacca più spesso (1.3.0.36)
- [x] Bottiglie che cadono dall'alto con avviso a terra (1.3.0.36)
- [x] Ascia di Pinuccia che torna indietro come un boomerang (il foglio ha già le pose di presa) (1.3.0.56)
- [x] Checkpoint a metà livello in modalità LIFE (1.3.0.36)

### Ambientazione
- [x] Uccelli in volo sui panorami: gabbiani, piccioni, rondini (1.3.0.36)
- [x] Barche che dondolano e acqua che luccica (servono le posizioni dell'acqua nei panorami) — acqua che luccica (1.3.0.56); barche ferme perché fanno parte del dipinto
- [ ] Primo piano in parallasse (scogli, canneti, parapetti) staccato dal panorama, per dare profondità
- [x] Pioggia e lampi a Lione (1.3.0.36)
- [x] Lampioni che si accendono al tramonto di Mantova — aloni dei lampioni in tutte le città, più forti a Mantova, e lucciole (1.3.0.56)

### Presentazione
- [x] Mappa del viaggio tra uno stage e l'altro, stile mappa missioni di Metal Slug, con rotta animata e ritratto del personaggio (1.3.0.23)
- [x] Riepilogo di fine stage con precisione, nemici abbattuti e "danni che avresti subito" (il gioco li conta già in GOD MODE) (1.3.0.56)
- [x] Battute prima del boss: una frase per personaggio e per città, col ritratto (1.3.0.55)
- [ ] Ritratti dell'HUD che sbattono le palpebre o cambiano espressione quando si viene colpiti

### Comodità
- [x] Salvataggio di stage completati, record per città e impostazioni (1.3.0.36)
- [x] Scelta diretta di una parte (3-2) dal menu (1.3.0.55)
- [x] Opzione per ridurre scossoni e lampi (1.3.0.36)
- [x] Mappa più viva: mercantile nel Mar Ligure, barca a vela nel Golfo del Leone, fumo sulle città liberate, timbro "MISSIONE COMPIUTA" che cala sulla città appena liberata (1.3.0.24)
- [x] Sulla mappa: punti fatti in ogni città (1.3.0.36)
- [x] Pinuccia: morte con il sangue attivata, con interruttore SANGUE in pausa e tasto B (1.3.0.27)
- [x] Musica chiptune per titolo, stage e boss, sintetizzata come gli effetti (1.3.0.27)
- [x] Oggetti che ricaricano l'energia: caffè +4 e specialità della città +10, paracadute durante il boss (1.3.0.27)
- [ ] Taratura della frequenza degli oggetti dopo qualche partita in modalità LIFE
- [x] Secondo tema musicale per la parte 2 di Marsiglia (1.3.0.36)
- [x] Regolazione separata del volume di musica ed effetti (già presente nelle impostazioni)

## Aggiunte 1.3.0.30
- [x] [M] Tratti dei personaggi: Albi equilibrato, Seba picchiatore con più bombe, Lollo scattante, Alecio a raffica, Pinuccia con l'ascia; schede FUOCO / FORZA / VELOCITÀ
- [x] [B] Versione mostrata a schermo e nella scheda del browser ricavata da un'unica costante (era rimasta ferma alla 1.3.0.26)
- [x] [M] Taratura dei tratti dopo qualche partita (cadenza di Alecio, forza di Seba) — Seba ridimensionato contro i carri (1.3.0.56)
- [x] [M] Alecio sempre senza zaino: zaino rimosso e schiena ricostruita in 10 pose (corsa, sparo, lancio, salto, colpito) (1.3.0.34)
- [x] [M] Lione: l'auto della polizia da sinistra sorpassa il personaggio e parcheggia davanti a lui, poi scendono i gendarmi (1.3.0.37)
- [x] [M] Lione: entrambe le auto della polizia arrivano da sinistra e sorpassano il personaggio (1.3.0.38)

## Marsiglia: Vespa e Trevor (dalla 1.3.0.39)
- [x] [A] Auto della polizia rimosse da Marsiglia, parte 1 e 2 (1.3.0.39)
- [x] [A] Sprite della Vespa con Trevor: arrivo, derapata, sosta, ripartenza con fumo (1.3.0.54)
- [x] [A] Sprite di Trevor: in sella, accanto alla Vespa, dito puntato (1.3.0.54); camminata, colpito e morte non servono perché Trevor non si può colpire
- [x] [A] Ruolo di Trevor: gendarme in borghese, intoccabile, scatena due gendarmi più forti (10 ottobre)
- [x] [M] Scena di Trevor a Marsiglia (1.3.0.54): al 30% della parte 1 arriva da destra sgommando, scende, punta il dito, scritta "TREVOR CI HA SBIRRATO!", due gendarmi scelti (16 di energia invece di 10, attaccano più spesso), schermo bloccato finché non cadono, poi "VIA LIBERA!"; riparte con la Vespa nel fumo. Passaggi in Vespa: 2 nella parte 1, 2 nella parte 2, mai durante il boss

## Sprite mancanti — riepilogo al 9 ottobre (1.3.0.39)
Priorità alta
- [x] Seba con UZI (1.3.0.40)
- [x] Seba con UZI: lancio bomba, corpo a corpo, stordimento, vittoria, caduta e morte, atterraggio, UZI a terra e nell'HUD (1.3.0.41)
- [x] Seba: morte carbonizzata, raccolta dell'UZI, set completo a mani nude (lanci, stordimento, vittoria, atterraggio, caduta), combo di pugni con uppercut e colpo finale, pugno in salto (1.3.0.42)
- [x] Seba: sparo in alto (1.3.0.43)
- [x] Lollo armato: foglio completo col fucile (1.3.0.47)
- [x] Vespa e Trevor (Marsiglia) (1.3.0.54)
- [ ] Nemici personalizzati di Mantova
Priorità media
- [ ] Bottiglia Chartreuse animata: camminata, attacco, morte (oggi gambe e braccia disegnate dal codice)
- [ ] Bottiglia di birra animata, stesso schema
- [ ] Bottiglia volante con ali disegnate
- [ ] Boss dedicati per Genova e Marsiglia (sprite; dalla 1.3.0.55 ogni carro ha già un comportamento proprio)
- [x] Alecio: lancio accucciato, seconda posa di colpito, icona del fucile (1.3.0.45)
Priorità bassa
- [x] Ritratti HUD con espressioni per Albi, Alecio, Lollo (1.3.0.43-47) e Seba (1.3.0.52); manca Pinuccia
- [ ] Proiettili nemici disegnati (gocce, schiuma, colpo del carro)
- [ ] Ostacoli disegnati (sacchi, casse, barili, auto distrutta)
- [ ] Logo grafico del titolo
- [ ] Gendarmerie: due fotogrammi finali di "attacco verso il basso" separati
- [x] Alecio: salita e discesa dedicate del salto col mitra (1.3.0.46)
- [x] [B] Titolo e selezione: tutti i personaggi in posa ferma a mani nude (1.3.0.41)
- [x] [M] Albi: corsa col mitra abbassato, attesa lunga, raccolta oggetti, ingresso col paracadute, ritratti HUD normale/colpito/vittoria (1.3.0.43)
- [x] [B] Albi: corsa col mitra sempre visibile, paracadute disegnato con discesa e atterraggio (1.3.0.44)
- [ ] [B] Albi: cammina e spara verso sinistra (anche il nuovo foglio è rivolto a destra; resta la versione specchiata)
- [x] [M] Alecio: mira in alto, sparo in basso, salita del salto, lancio accucciato e carica, seconda posa di colpito, morte carbonizzata a terra, corsa a mitra abbassato, attesa lunga, raccolta, paracadute, ritratti, icona del fucile (1.3.0.45)
- [x] [M] Mira verso l'alto e sparo verso il basso per Lollo, ritratti di Lollo (1.3.0.47)
- [x] [M] Ritratti HUD di Seba: normale, colpito, vittoria (1.3.0.52)
- [ ] [M] Ritratti con espressioni per Pinuccia
- [x] [M] Alecio: fermo col mitra, discesa del salto col mitra, lancio in piedi in 4 tempi, lancio accucciato completo, paracadute mimetico disegnato (1.3.0.46)
- [ ] [B] Extra: arretrare sparando anche per Albi, Seba e Alecio (servono camminate all'indietro dedicate)
- [x] [B] Extra: casse del fucile a pompa come ricompensa del bonus delle casse — casse con raffica doppia o ricarica dello shotgun (1.3.0.56)
- [x] [B] Extra: a 5/8 della serie arpeggio, anello di scintille attorno a Lollo, scritta "SERIE 5/8!" e contatore dell'HUD che pulsa (1.3.0.50)
- [x] [B] Extra: lo shotgun sbalza indietro le bottiglie abbattute (il corpo scivola via e i cocci volano nella direzione del colpo) e spinge indietro i nemici che restano in piedi; scossa dello schermo (1.3.0.50)
- [x] [B] Extra: fumetto "SHOTGUN!" quando Lollo raccoglie il fucile a pompa; fumetti di Trevor (1.3.0.55)

## Sprite mancanti — riepilogo al 10 ottobre (1.3.0.50)
- [x] [A] Vespa e Trevor (Marsiglia) (1.3.0.54)
- [ ] [A] Nemici personalizzati di Mantova
- [ ] [A] Pinuccia: set completo sullo schema degli altri (vittoria, stordimento, lanci della bomba, morte, paracadute, attesa lunga, raccolta, corsa, ritratti)
- [x] [M] Seba: ritratti HUD, ingresso col paracadute (a mani nude: discesa seduto; con l'UZI: discesa in 2 tempi e atterraggio sparando con la calotta a terra), attesa lunga con l'UZI (1.3.0.52)
- [ ] [M] Bottiglie animate (Chartreuse, birra, volante con ali)
- [ ] [M] Boss dedicati per Genova e Marsiglia
- [x] [B] Shotgun di Lollo: set completo (1.3.0.51)
- [ ] [B] Proiettili nemici, ostacoli, logo del titolo, Gendarmerie (2 fotogrammi separati), Albi cammina e spara verso sinistra
- [ ] [B] Extra: attesa lunga e respiro più marcato con lo shotgun (oggi respiro sintetico sul fotogramma fermo)
- [x] [B] Seba a mani nude: paracadute disegnato in 2 tempi, atterraggio con la calotta a terra, poi in piedi con l'imbracatura e in posa pronta (1.3.0.53)
- [x] [M] Seba a mani nude: guardia coi pugni alzati da fermo (2 tempi), attesa lunga (si toglie il cappello e si gratta la testa), colpito in 2 tempi, discesa del salto a braccia aperte, atterraggio accucciato (1.3.0.53)
- [ ] [B] Seba: pose non ancora usate dal foglio a mani nude — il colpito in ginocchio ora è la reazione ai colpi forti (1.3.0.56); restano (passo dopo l'atterraggio, inginocchiato con la mano a terra, posa pronta in avanti, colpito in ginocchio); il colpito in ginocchio può diventare la reazione ai colpi forti
- [ ] [B] Trevor, sprite facoltativi: discesa e risalita sulla Vespa distinte (oggi 4 fotogrammi quasi uguali), gesto mentre fischia o chiama i gendarmi alla radio, saluto o clacson nei passaggi, ritratto per un fumetto di dialogo
- [ ] [B] Trevor, da confermare: gendarmi uno accanto a Trevor e uno da sinistra (oggi) oppure entrambi dai lati; passaggi anche nella parte 2 (oggi sì); i passaggi sono innocui (oggi sì)

## Migliorie senza sprite (1.3.0.55)
- [x] [A] Gioco alleggerito da 11,9 a 5,6 MB
- [x] [A] Carri con carattere proprio e seconda fase sotto metà energia (barra del boss che pulsa): Lione raffiche, Genova bottiglie a ventaglio, Mantova speronata, Marsiglia pioggia di bottiglie sui bersagli segnati
- [x] [A] Difficoltà crescente e ondate a schermo bloccato
- [x] [M] Battute prima del boss e fumetti
- [x] [M] 13 medaglie salvate, classifica coi nomi, Boss Rush a tempo
- [x] [B] Scelta della parte di Marsiglia, tutorial alla prima partita (ripetibile dalle impostazioni)
- [x] [M] Collaudo automatico: 5 personaggi × 4 città completati in automatico, senza blocchi
- [x] [M] Correzione: i nemici addosso al giocatore ora vengono colpiti (prima i colpi partivano oltre il nemico)
- [x] [B] Rete di sicurezza: ondate e scontro di Trevor non bloccano lo schermo per più di 45-60 secondi
- [x] [B] Extra: medaglie visibili anche nel riepilogo di fine tappa (1.3.0.56)
- [x] [B] Extra: battuta di risposta del carro (il nemico che replica al personaggio) (1.3.0.56)
- [ ] [M] Taratura della difficoltà dopo qualche partita vera (le ondate e la seconda fase dei carri sono calibrate a tavolino)

## Seconda serie di migliorie senza sprite (1.3.0.56)
- [x] [A] Misure col bot senza invincibilità (morti, durata, tempo del boss per personaggio e città) e taratura
- [x] [A] Difficoltà a scelta (facile, normale, difficile), salvata
- [x] [A] Continua il viaggio dal titolo
- [x] [M] Boomerang di Pinuccia; colpo forte di Seba in ginocchio
- [x] [M] Marsiglia 2: pioggia di bottiglie dai pescherecci; casse con raffica doppia o ricarica dello shotgun
- [x] [M] Riepilogo con precisione, medaglie della tappa e danni che avresti subito; risposta del carro; annunciatore
- [x] [B] Riflessi sull'acqua, aloni dei lampioni, lucciole a Mantova
- [x] [B] Layout orizzontale per telefono; codice degli sfondi procedurali rimosso
- [x] [B] Correzione: con un campo nome lasciato aperto i tasti dei menu non rispondevano più
- [ ] [B] Pinuccia: posa senza ascia mentre il boomerang è in volo (oggi da ferma la tiene ancora in mano: serve uno sprite)
- [ ] [B] Primo piano in parallasse: serve un disegno (parapetti, canneti, scogli) separato dal panorama
- [ ] [M] Prova dell'annunciatore e del layout orizzontale su telefono vero

## Terza serie di migliorie senza sprite (1.3.0.57)
- [x] [A] Impatto dei colpi: fermo immagine sui colpi forti, rallentatore sull'esplosione del carro
- [x] [M] Suoni per arma (mitra, UZI, fucile, mitragliatore), passi per superficie, atterraggio bagnato a Lione
- [x] [M] Musica che reagisce: tema del boss più incalzante nella seconda fase, ritmo più teso durante ondate e scontro di Trevor
- [x] [M] Statistiche totali (nella schermata Classifica)
- [x] [M] Foto della partita (fine tappa e pausa): condivisione sul telefono, download altrove
- [x] [M] Accessibilità: colori per daltonici, testo grande, sottotitoli dell'annunciatore, mira assistita
- [x] [M] Tasti personalizzabili (tastiera e gamepad) e promemoria dei comandi nella pausa
- [x] [M] Collaudo automatico a ogni build (menu + 3 livelli giocati dal bot)
- [x] [B] Correzione: le maiuscole accentate (À, È, Ù) non esistono nel carattere del gioco; ora "MODALITA'", "E'", "PIU'"
- [ ] [B] Sfida del giorno: scartata (l'ordine delle città è cronologico e resta fisso)
- [ ] [B] Trucchi sbloccabili con le medaglie: scartati per ora (non toccherebbero l'ordine delle città, se un giorno servissero)
- [ ] [M] Prova su telefono vero: foto e condivisione, vibrazione, layout orizzontale, voce

## Ultime migliorie senza sprite (1.3.0.58)
- [x] [M] Pinuccia: schiacciata in salto con l'ascia (5 fotogrammi del suo foglio), onda d'urto su entrambi i lati
- [x] [M] Finale del viaggio: la squadra al completo festeggia a Marsiglia coi fuochi d'artificio, poi i titoli di coda
- [x] [M] Partita salvata al checkpoint anche chiudendo la pagina ("RIPRENDI" nel titolo)
- [x] [B] Risparmio batteria: disegno a 30 immagini al secondo, meno particelle e luci, gioco alla stessa velocità
- [x] [B] Seba: due varianti di atterraggio col paracadute (inginocchiato o in piedi) e due di atterraggio dal salto
- [x] [B] Un po' più di cibo dopo aver perso più vite nella stessa città
- [ ] [B] Versione in inglese (solo se il gioco verrà fatto girare fuori dall'Italia)
- [ ] [M] Due giocatori in locale (dopo gli sprite del weekend)
- [x] [B] Pose ancora inutilizzate: Seba "passo dopo l'atterraggio"; auto dei gendarmi senza lampeggianti (1.3.0.59)

## Prestazioni, copia dei salvataggi, ultime pose (1.3.0.59)
- [x] [B] Prestazioni: aloni dei lampioni, foschia, luci delle esplosioni, riflettore del finale e pannello della mappa disegnati una volta e riusati (nessuna sfumatura ricreata a ogni fotogramma)
- [x] [M] Impostazioni: ESPORTA SALVATAGGI / IMPORTA SALVATAGGI (file .json con progressi, medaglie, classifica, record e impostazioni; file non validi rifiutati)
- [x] [B] Seba: primo passo dopo l'atterraggio con la posa dedicata
- [x] [B] Auto dei gendarmi in avvicinamento silenzioso (dalla seconda in poi, circa 1 su 2): arriva a luci spente, inchioda con i fotogrammi senza lampeggianti, poi accende sirena e lampeggianti

## Check funzionale del 23/10 (1.3.0.59) — da correggere, senza sprite nuovi
- [x] [A] Telefoni alti (390×844, 412×915): il gioco sborda di 2-5 px per lato e la pagina scorre di lato (1.3.0.60)
- [x] [M] Frecce ← → assenti nel carattere: ora disegnate ruotando la freccia ↑, anche su INDIETRO e nel tutorial (1.3.0.60)
- [x] [M] Su telefono: "TOCCA PER GIOCARE", niente suggerimenti da tastiera né legenda dei tasti (1.3.0.60)
- [x] [B] Medaglie: tutte e 13 visibili senza scorrere (1.3.0.60)
- [x] [M] Sfondi di Genova e Marsiglia (parte 1): tolta la scritta dalla fascia sopra il porto, che ora si legge come una galleria a vetri (1.3.0.60)
- [x] [B] Cartello di Lione con "MUCEM" (museo di Marsiglia): scritta tolta, resta la freccia (1.3.0.61)
- [x] [M] Curva di difficoltà riequilibrata: Lione più leggera, seconda parte di Marsiglia più dura (danni subiti dal bot: Lione da 93 a 69, Marsiglia da 57 a 85) (1.3.0.61)
- [x] [B] Su PC niente pulsantiera touch né legenda: il gioco è circa 1,6 volte più grande; toccando lo schermo la pulsantiera ricompare (1.3.0.61)
- [x] [B] Pose mai mostrate: rinculo dei carri colpiti (3 varianti) e gendarme che si abbassa sotto i colpi sparati in piedi (1.3.0.60)
- [x] [B] Vecchie pose di Albi e Alecio: tolte nella 1.3.0.61, rimesse nella 1.3.0.62 per usarle (vedi sezione sotto)
- [x] [M] Collaudo funzionale completo: percorso da tastiera su PC e touch su telefono (34 controlli), 49 test automatici, bot con tutti i personaggi in tutte le città (1.3.0.61)

## Pose a mani nude di Albi e Alecio — checklist di implementazione
Nel gioco dalla 1.3.0.62, oggi mai mostrate. Set completo per entrambi (46 fotogrammi):
camminata verso destra (6) e di tre quarti (6), pugno (3), pugno basso (2), salto (2), accucciato, colpito, a terra.
Solo Alecio: calcio (2). Seba e Lollo hanno già il loro set a mani nude; Pinuccia aspetta la posa senza ascia.

### Da decidere prima di iniziare
- [ ] [A] Albi e Alecio restano armati dall'inizio (regola attuale: solo Seba e Lollo partono a mani nude). Le pose servono quindi per i momenti senza arma, non per l'avvio del livello
- [ ] [A] Scegliere quali proposte fare tra quelle sotto (1 e 2 sono il consiglio)

### 1. Arma persa (meccanica nuova) [A]
Un colpo pesante (cannonata del carro, granata, ascia dall'alto del gendarme) fa volare l'arma: si resta a mani nude finché non la si raccoglie.
- [ ] Regola: probabilità di perdere l'arma per colpo pesante (proposta: 1 su 4), mai durante la cutscene di Trevor né nella Boss Rush
- [ ] L'arma cade a terra a qualche passo e lampeggia; se non la raccogli entro 8 s torna in mano da sola
- [ ] Albi: camminata, pugni (in piedi e bassi), salto, accucciato, colpito con le pose a mani nude
- [ ] Alecio: come Albi, più il calcio alternato al pugno (come Lollo)
- [ ] Seba e Lollo: usano il loro set a mani nude già pronto; lo shotgun di Lollo non si perde
- [ ] Pinuccia esclusa finché non arriva la posa senza ascia
- [ ] Danni a mani nude uguali a quelli di Seba e Lollo (contro i carri ×0,55)
- [ ] Morte a mani nude: posa "a terra" (albi_dead0 / alecio_dead0)
- [ ] Scritta "ARMA PERSA!" e annunciatore; medaglia nuova "A MANI NUDE" (abbatti 5 nemici senz'arma)
- [ ] Test automatico: arma persa, raccolta, ritorno automatico, nessuna posa mancante

### 2. Scene e menu [M]
- [ ] Scelta personaggio: la scheda selezionata cammina sul posto (camminata a destra)
- [ ] Mappa del viaggio: piccolo omino che cammina lungo la rotta al posto dell'icona (camminata di tre quarti)
- [ ] Finale e titoli di coda: la squadra entra in scena camminando prima della festa
- [ ] Vittoria di stage: uscita di scena a piedi verso destra

### 3. Idee minori [B]
- [ ] Riposo lungo: dopo 20 s fermo, il personaggio si sgranchisce con un pugno a vuoto (pugno 0-2)
- [ ] Modalità due giocatori (quando si farà): set a mani nude per il secondo giocatore nei momenti senz'arma

## Beta 1.3.0.63 — primo rilascio interno
- [x] [A] Verifica del link dell'artifact da non iscritti: chiede di accedere a Claude, quindi non basta per chi non ha un account
- [x] [A] File unico funzionante da solo, senza Claude e senza internet: foto, esporta/importa e salvataggi provati
- [x] [M] Nome della pagina, icona, etichetta "BETA" nel titolo, voci per "Aggiungi a schermata Home" su telefono
- [x] [B] Schermo intero: niente errori dove non è disponibile (iPhone, pagine incorporate), pulsanti nascosti se non serve
- [x] [M] Pacchetto per i tester: file del gioco + LEGGIMI (come si gioca, comandi, problemi noti, come segnalare)
- [ ] [A] Pubblicare la beta su un indirizzo aperto a tutti, per i telefoni (es. GitHub Pages o Netlify)
- [ ] [M] Prova su iPhone vero (Safari) e su un Android
- [ ] [B] Raccolta segnalazioni dei tester

