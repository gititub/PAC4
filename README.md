
El focus de dades d'aquest projecte es descarrega "FIFA 22 Complete Player Dataset" disponible a Kaggle. El conjunt de dades que farem servir correspòn a les de FIFA 2022 masculí i femení des del 2016 fins al 2022.

**PAC4.py inclou el codi de les funcions aquí descrites**

**Podeu trobar tot el material a https://github.com/gititub/PAC4**

## Exercici 1: lectura i pre-procés
El primer que cal fer es crear funcions que llegeixin i processin les nostre dades.

a) Una funció que llegeixi un fitxer de jugadors que afegeix dues columnes a la informació
obtinguda. Aquesta informació afegida s’expressara en dues noves columnes “gender” i
“year” (que fan referencia al genere dels esportistes en el fitxer i a l’any en que es van
publicar les dades). La funció ha de tornar el dataframe de pandas resultant d’afegir les
dues columnes mencionades a la informacion inicial .
read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame
- filepath: string amb la ruta de l’arxiu que volem llegir
- gender: 'M' o 'F' (segons les sigles de “Male” or “Female”)
- year: Any al que corresponen les dades en format XXXX (per exemple, 2020)


b) Una funció que creï un sol dataframe amb les dades de tots els jugadors/es d'un mateix
any. Aquest dataframe també ha de contenir informació sobre el gènere i any a què es
corresponen les dades de cada futbolista.
join_male_female(path: str, year: int) -> pd.DataFrame
- path: ruta a la carpeta que conté les dades
- year: any del que es volen llegir les dades, format XXXX (per exemple, 2020)


c) Una funció que llegeixi la informació corresponent a futbolistes d’ambdós gèneres durant
diversos anys i que torni un únic dataframe. Aquest dataframe ha de contenir, a més,
informació sobre el gènere i any a què es corresponen les dades de cada futbolista.
join_datasets_year(path: str, years: list) -> pd.DataFrame
- path: ruta a la carpeta que conté les dades
- years: llista d’anys que es volen incloure en el dataframe, en format [XXXX,...]


## Exercici 2: estadistica basica


Volem crear una sèrie de funcions que ens permetin obtenir certes estadístiques bàsiques
del conjunt de futbolistes. En concret:

a) Una funció que, rebi un dataframe i, donat el nom d'una columna numèrica, ens retorni
la/es fila/es en què el seu valor és màxim. A més, la funció rebrà com a argument una
llista de noms de columnes. El dataframe que retorni la funcion només ha de contenir
aquestes columnes.
find_max_col(df: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame
- df: dataframe que conté les dades
- filter_col: nom de la columna de la que volem saber el màxim
- cols_to_return: llista de columnes que cal retornar


b) Una funció per a filtrar les dades amb filtres avançats. La funció rebrà una query (o
consulta) en forma de tupla. El primer element de la tupla serà una llista de columnes
sobre les que volem filtrar. El segon element serà la llista de valors que volem fer servir al
filtre. Si la columna és categòrica, el valor serà un string. Si és numèrica, serà una tupla
amb el valor mínim i màxim (tots dos han de ser inclosos al filtre).
Igual que a l'exercici 2a, s'inclou un argument que ens indica quines columnes volem que
ens torni la funció.
find_rows_query(df: pd.DataFrame, query: tuple, cols_to_return: list) ->
pd.DataFrame
- df: dataframe que conté les dades
- query: tupla que conté la query
- cols_to_return: llista de columnes que cal retornar


c) Considerant tot el conjunt de dades proporcionat (des de l'any 2016 fins al 2022, ambdós
inclosos), mostreu per pantalla el “short_name”, “year”, “age”, “overall” i “potential” de:
- Els jugadors de nacionalitat belga menors de 25 anys màxim “potential” al futbol
masculí.
- Les porteres majors de 28 anys amb “overall” superior a 85 al futbol femení.


## Exercici 3: BMI


Els/Les esportistes professionals segueixen un rigorós control dietètic i realitzen més
activitat física que la població general. Volem estudiar si això resulta en un índex de massa
corporal (BMI per les sigles en anglès) diferent del de la població general.
En primer lloc, cal crear una funció que, donats: un dataframe amb les dades, un gènere i
un any,retorni un dataframe que inclogui una columna amb l'índex de massa corporal (BMI) de
cada futbolista d'aquest gènere i any. La funció també rebrà com a argument una llista de
columnes. El dataframe que retorni la funció han de contenir aquestes columnes, a més de la
nova columna BMI.

calculate_BMI(df: pd.DataFrame, gender: str, year: int, cols_to_return: list) ->
pd.DataFrame
- df: dataframe que conté les dades
- gender: gènere que volem estudiar
- year: any que volem estudiar en format XXXX (per exemple 2020)
- cols_to_return: llista de columnes que cal retornar (sense columna BMI)

a) Mostreu una gràfica amb el BMI màxim per país. Filtreu per gènere masculí i any 2022. La
informació sobre el país on juga cada futbolista (no confondre amb la nacionalitat del
jugador) es pot extreure de la columna club_flag_url. 

Considerant la següent classificació:
Category BMI
underweight < 18.5

normal weight [18.5, 25)

overweight [25, 30)

obese ≥ 30

Trobeu sorprenents els valors obtinguts? Per què?

**En les persones que practiquen esport o exercici físic de forma regular amb un IMC en grau d'obesitat, sobretot si no és una modalitat purament tècnica, no els haurem de catalogar com a tals sense estimar abans per mesures complementàries el greix corporal. L'antropometria és una tècnica fàcil i poc costosa que ens permet el mesurament de plecs cutanis i estimar-ne els components gras i magre. En les persones amb sobrepès s'ha de complementar l'estudi mitjançant la valoració del perímetre abdominal en relació amb la talla, i és aconsellable considerar-los des dels punts de tall més específics segons la població de procedència. En esportistes fins a un IMC de 32,8 kg/m2 no es pot considerar sobrepès degut al seu component predominantment magre o lliure de greix.**

b) Compareu en una gràfica el BMI del conjunt de futbolistes que desitgeu amb el de la
població espanyola. Podeu descarregar les dades de la pàgina de l'INE:
https://www.ine.es/jaxiPx/Tabla.htm?path=/t15/p420/a2019/p03/l0/&file=01001.px&L=1


## Exercici 4: diccionaris


Volem poder seguir l'evolució dels/de les jugadors/es que apareixen en diferents anys al
nostre conjunt de dades. En un primer pas crearem una funció per seleccionar amb quins
jugadors (identificats amb la columna “sofifa_id”) volem treballar i quines columnes volem
mostrar:

a) Creeu una funció que, donat un dataframe amb les dades, una llista d'identificadors i una
llista de columnes:

players_dict(df: pd.DataFrame, ids: list, cols:list) -> dict

- df: dataframe que conté les dades
- ids: llista d’iidentificador “sofifa_id”
- cols: llista de columnes de les que volem informació
retorni un diccionari:

- que tingui com a claus els identificadors “sofifa_id” continguts a la llista “ids”
- que tingui com a valors diccionaris amb la informació corresponent a cada
jugador/a. Concretament, les claus de cadascun d'aquests diccionaris seran els
noms de les columnes incloses a “col” i els seus valors seran la informació de tots
els anys disponibles al dataframe per a cada futbolista.

Nota 1: Cal fer servir la columna “sofifa_id exclusivament com a clau. No s'inclourà a la
llista “cols” en cap cas.


El diccionari anterior conté informació redundant. Per exemple, la columna “short_name”
contindrà tantes repeticions com anys aparegui cada futbolista a les dades. En altres casos, com
ara la columna “player_positions”, el diccionari contindrà informació parcialment repetida però
amb la possibilitat d'incloure nous valors. Finalment, en columnes com a “potential”, cadascun
dels valors obtinguts representa informació rellevant.


b) Per tal d’eliminar només la informació redundant, creeu la funció:
clean_up_players_dict(player_dict: dict, col_query: list) -> dict
- player_dict: diccionari amb el formato de l’apartat (a) players_dict
- col_query: llista de tuples amb detalls sobre la información que cal simplificar

La funció ha de recórrer un a un els elements del diccionari i fer els canvis indicats per la
llista de tuples col_query.
Cada tupla de la llista estarà composta per dos valors: 1) el nom duna columna i 2) una
cadena de caràcters. Aquesta cadena pot contenir dos valors possibles, els quals ens
indiquen l'operació a realitzar sobre la columna/clau del diccionari:

- “one”: ens hem de quedar només amb el primer valor que aparegui
- “del_rep”: primer hem de descompondre la informació i després eliminar les
repeticions
- La informació referent a les columnes que no apareixen a col_query es retornarà
sense canvis.

c) Considerant el dataframe amb ambdós gèneres i els anys 2016, 2017 i 2018, mostreu per
pantalla:

● El diccionari construït amb la funció de l'apartat 4a amb la informació de les
columnes ["short_name", "overall", “potential”, "player_positions", "year"] i els ids =
[226328, 192476, 230566].

● La query que passaríeu a la funció de l'apartat 4b per netejar aquest diccionari.

● El diccionari “net”.


## Exercici 5: evolució


Volem estudiar l’evolució d’algunes característiques dels/les esportistes:
a) Implementeu la funció:
top_average_column(data: dict, identifier: str, col: str, threshold: int) -> list
- data: diccionari “net” que conté la informació de diversos sofifa_id
- identifier: columna/clau que es fara servir com identificador
- col: nom d’una columna/clau numérica
- threshold: mínim número de dades necessàries

Aquesta funció cal que:

● Per a cada sofifa_id, calculi el valor mitjà de la característica col si teniu informació
de threshold o més anys. Si no, s'ignora aquest sofifa_id. Si algun element de la
llista té el valor NaN, també s'ignora aquest sofifa_id.

● Retorni una llista de tuples formades per tres elements: valor de la columna
identifier; mitjana de la característica; i un diccionari compost per la clau year que
contingui la llista d'anys corresponents als valors i la clau value amb aquests
valors.

● Ordeni la llista de tuples a retornar en ordre descendent segons la mitjana
calculada.

b) Feu servir la funció anterior per obtenir l'evolució dels 4 futbolistes amb millor mitjana de
movement_sprint_speed entre el 2016 i el 2022 (inclosos). Utilitzeu “short_name” com a
identificador i mostreu el resultat per pantalla. Representeu gràficament l'evolució
obtinguda.




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


c) Presentació dels resultats: inclou un **Informe.md** que explica quins criteris hem utilitzat per modelar
cadascun dels aspectes del problema i que presenta els resultats obtinguts per a les
millors línies defensives masculina, femenina i de jugadors veterans. Inclou alguns gràfics que acompanyen l'explicació.

## Pasos per executar el codi:
1. git clone 
2. unzip PAC4-main.zip
3. cd ./PAC4-main
4. pip install -r requeriments.txt
5. python3 ./PAC4.py
6. python3 ./Exercici6_homes_dones.py
