# mayday-gaming.github.io

Pagina principale di Mayday Gaming: una card per ogni gioco dell'organizzazione, cliccabile per giocare.

- `index.html`: la pagina, senza dipendenze né build. Per aggiungere un gioco basta una riga nell'array `GAMES`.
- `covers/`: le copertine sono screenshot dei giochi, 960×600 (16:10), in JPG.
- Versione e ultima Release di ogni gioco vengono lette dall'API di GitHub nel browser, con una cache di un'ora.

Le copertine sono usate anche dal README del profilo dell'org (`mayday-gaming/.github`).
