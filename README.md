# AstroTO

Il repository contiene i codici utilizzati per estrapolare e analizzare le immagini pervenute dalla ISS.

## Il progetto

A differenza di quanto pianificato, in cui si voleva analizzare l'espansione urbana nel corso degli anni.

A seguito di aver ricevuto le immagini dalla stazione spaziale, la maggior parte delle quali mostra il ghiacciaio presente sulla catena montuosa dell'Himalaya,
si è ritenuto più stimolante valutare la dimensione del ghiacchiaio nel corso degli anni per capire se vi è stata una diminuzione dello stesso o meno, a partire 
dall'anno 1984 ad oggi.

Di seguito il dettaglio del contenuto del repository.

## Programmi python

* main.py: programma principale, caricato su raspberryPi, utilizzato per scattare immagini a bordo della ISS
* stich_img.py: programma utilizzato per la post elaborazione, per unire le foto significative di ogni anno preso in considerazione
* white.py: programma che riconosce i pixel bianchi, in modo da valutare l'estensione del ghiacciaio preoso in esame.
