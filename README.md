# SOTO Slug - TEX Edition

Run and gun in stile arcade tra Genova, Lione, Mantova e Marsiglia.

**Versione attuale:** 1.3.0.70 BETA

- **Gioca qui:** https://alessioaversano91-gif.github.io/soto-slug/ (PC e telefono, nessun account richiesto)
- Su PC si puo' anche scaricare `index.html` e aprirlo con un doppio clic: funziona senza internet.
- Istruzioni, comandi e problemi noti: [LEGGIMI](LEGGIMI.md).

## Struttura

| Percorso | Contenuto |
|---|---|
| `index.html` | Il gioco completo in un unico file (quello che serve GitHub Pages) |
| `LEGGIMI.md` | Guida per i tester |
| `dev/game_template.html` | Motore del gioco con i segnaposto dei dati |
| `dev/build_bundle.json` | Dati generati: sprite, metadati, carattere, icone |
| `dev/assemble_bundle.py` | Unisce motore e dati e produce il gioco |
| `dev/extract_bundle.py` | Ricava `build_bundle.json` da una build pubblicata |
| `dev/tests/` | Test automatici (Playwright) e bot che gioca i livelli |
| `dev/soto_checklist.md` | Checklist di sviluppo |

Versioni: MAJOR.MINOR.PATCH.BUILD, a ogni rilascio cresce solo BUILD.
