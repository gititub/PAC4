# PAC4
## Exercici 6: La millor defensa.

En aquest exercici final de l'assignatura utilitzarem les nostres habilitats
com a científics de dades per:

a) Formalitzar un problema a partir d’objectius generals.

b) Implementar una solució seguint els principis vistos a l’assignatura.

c) Trobar una solució al problema inicial i comunicar-ne els resultats de manera efectiva.

Un dels vostres clients representa un misteriós grup d'inversió que ha comprat un conegut
club de futbol “en hores baixes”. El client ens indica que ha decidit començar la reconstrucció de l'equip per la defensa i que, per tant, necessita saber quins futbolistes formen la millor línia defensiva del món, els diners no són un obstacle.


El client deixa molt clars els punts següents:


- Origen de Dades: El focus de dades d'aquest projecte es descarrega "FIFA 22 Complete Player Dataset" disponible a Kaggle. El conjunt de dades que farem servir correspòn a les de FIFA 2022 masculí i femení (female_players_22.csv i players_22.csv).


- Definició de “defensa”. Una línia defensiva es compon de 4 jugadors/es: 2
defenses centrals (CB segons la notació de la columna “player_positions”); 1
defensa lateral dret (RB); i 1 defensa lateral esquerre (LB).


- No s'han de repetir jugadors/es: Si un jugador/a pot jugar en més d'una
d'aquestes posicions es pot considerar en més d'un rol, però sempre com a màxim
en una posició a cada línia defensiva. 


- Masculí/Femení/Veterans/es: El club disposa d'un equip masculí en hores
particularment baixes, i un equip femení entre els millors del continent. Per tant, el
client vol conèixer les millors línies defensives masculina i femenina. A més, el
client sap del cert que un projecte anomenat “European VetLeague”, on competiran
equips mixtos de jugadores/es a partir de 30 anys, està a punt de veure la llum. Per
això, vol conèixer també la millor línia defensiva de jugadors/es de qualsevol sexe
que tinguin 30 anys o més.

El client vol tenir una estimació de quina aportació produeix cada possible línia defensiva en els tres criteris següents:

1) defensa; 

2) control de pilota (possessió); 

3) atac. 

Si fos possible, la defensa i l'atac haurien d'estar dividits en tres zones: esquerra, central i dreta.

Punts importants:

a) Formalització del problema: El primer que farem és determinar quins jugadors
poden jugar a cadascuna de les posicions d'interès. De la mateixa manera, decidirem,
per a cada posició, quines variables (de les representades per les columnes del dataset)
són més importants. Obtinguda la llista de candidats per a cada posició, el següent pas serà determinar totes les
possibles línies defensives que s'hi puguin constituir. Després, caldrà fer una estimació de
la contribució a l'atac, la possessió i la defensa de cada línia en base al nostre criteri propi.
Així, ordenarem les línies de millor a pitjor i ens quedarem amb la millor.


b) Implementació: inclou el codi necessari per trobar la solució al problema implementant els criteris subjectius que hem definit. 

c) Presentació dels resultats: inclou un petit informe que explica quins criteris hem utilitzat per modelar
cadascun dels aspectes del problema i que presenta els resultats obtinguts per a les
millors línies defensives masculina, femenina i de jugadors veterans. Inclou alguns gràfics que acompanyen l'explicació.

Pasos per executar el codi:
1. git clone 
2. unzip PAC4-main.zip
3. cd ./PAC4-main
4. pip install -r requirements.txt
5. python3 ./PAC4.py
