#!/usr/bin/env python
# coding: utf-8

# ## Exercici 6: La millor defensa.
# 
# En aquest exercici final de l'assignatura us demanem que utilitzeu les vostres habilitats
# com a científics de dades per:
# 
# 
# a) Formalitzar un problema a partir d’objectius generals.
# 
# 
# b) Implementar una solució seguint els principis vistos a l’assignatura.
# 
# 
# c) Trobar una solució al problema inicial i comunicar-ne els resultats de manera efectiva.
# 
# 
# A continuació teniu un enunciat amb una mica de literatura que descriu el problema “general”. Al final de l'exercici trobareu un resum dels punts més importants:
# 
# 
# Un dels vostres clients representa un misteriós grup d'inversió que ha comprat un conegut
# club de futbol “en hores baixes”. El client us indica que ha decidit començar la reconstrucció de l'equip per la defensa i que, per tant, necessita saber quins futbolistes formen la millor línia defensiva del món, els diners no són un obstacle.
# 
# 
# El client us deixa molt clars els punts següents:
# 
# 
# - Origen de Dades: La millor manera de jutjar la qualitat dels futbolistes és consultar
# la base de dades d’aquesta PAC. Concretament, el client està interessat únicament
# en les dades del 2022 (female_players_22.csv i players_22.csv).
# 
# 
# - Definició de “defensa”. Una línia defensiva es compon de 4 jugadors/es: 2
# defenses centrals (CB segons la notació de la columna “player_positions”); 1
# defensa lateral dret (RB); i 1 defensa lateral esquerre (LB).
# 
# 
# - No s'han de repetir jugadors/es: Si un jugador/a pot jugar en més d'una
# d'aquestes posicions es pot considerar en més d'un rol, però sempre com a màxim
# en una posició a cada línia defensiva. Per exemple, a l'arxiu female_players_22.csv
# s'indica que “Magdalena Lilly Eriksson” pot ocupar les posicions “LB” i “CB”.
# Aquesta jugadora podrà, per tant, optar a ser part de la nostra “defensa ideal” tant
# com a lateral dret com a central, però una alineació que la inclogui alhora en les
# dues posicions serà considerada errònia.
# 
# 
# - Masculí/Femení/Veterans/es: El club disposa d'un equip masculí en hores
# particularment baixes, i un equip femení entre els millors del continent. Per tant, el
# client vol conèixer les millors línies defensives masculina i femenina. A més, el
# client sap del cert que un projecte anomenat “European VetLeague”, on competiran
# equips mixtos de jugadores/es a partir de 30 anys, està a punt de veure la llum. Per
# això, vol conèixer també la millor línia defensiva de jugadors/es de qualsevol sexe
# que tinguin 30 anys o més.
# 
# Pregunteu al client quins criteris defineixen la qualitat d'una línia defensiva, però aquest gesticula vagament en direcció de les columnes F a B7 del nostre dataset obert en excel i us indica que cal triar les (entre 3 i 5) característiques més importants per a cada posició (LB, RB,CB). 
# 
# El client vol tenir una estimació de quina aportació produeix cada possible línia defensiva en els tres criteris següents:
# 
# 1) defensa; 
# 
# 2) control de pilota (possessió); 
# 
# i 3) atac. Si fos possible, la defensa i l'atac haurien d'estar dividits en tres zones: esquerra, central i dreta.
# 
# 
# Els vostres intents d'aconseguir més concreció del vostre cap resulten infructuosos doncs està molt ocupat comptant feixos de bitllets que treu de la bossa d'esport que el client ha deixat.
# Només us indica que aquest és el projecte més important de l'empresa i que la vostra feina
# depèn del seu resultat, per no parlar de la felicitat dels centenars de milers de seguidors del club.
# 
# 
# Punts importants:
# 
# 
# a) Formalització del problema: El primer que heu de fer és determinar quins jugadors
# poden jugar a cadascuna de les posicions d'interès. De la mateixa manera, heu de decidir,
# per a cada posició, quines variables (de les representades per les columnes del dataset)
# són més importants. Us recomanem triar un reduït nombre de candidats (no més de 50) a
# ocupar cadascuna de les 4 posicions seguint algun criteri de la vostra elecció. Obtinguda
# la llista de candidats per a cada posició, el següent pas seria determinar totes les
# possibles línies defensives que s'hi puguin constituir. Després, caldrà fer una estimació de
# la contribució a l'atac, la possessió i la defensa de cada línia en base al vostre criteri propi.
# Així, podreu ordenar les línies de millor a pitjor i quedar-vos amb la millor.
# 
# 
# b) Implementació: El vostre lliurament ha d'incloure el codi necessari per trobar la solució al problema implementant els criteris subjectius que heu definit. Recordeu que es valoraran
# els mateixos aspectes de modularitat, documentació i eficiència que a la resta de la PAC.
# 
# 
# c) Presentació dels resultats: El vostre lliurament ha d'incloure també un petit informe (de
# no més de 2 pàgines, en format pdf) que expliqui quins criteris heu utilitzat per modelar
# cadascun dels aspectes del problema i que presenti els resultats obtinguts per a les
# millors línies defensives masculina, femenina i de jugadors veterans. Es valorarà
# positivament la inclusió d'alguns gràfics que acompanyin l'explicació.
# 
# 
# d) Cal tenir carnet d’entrenador? No cal tenir coneixements avançats de futbol per fer
# aquest exercici. La feina del Data Scientist consisteix a treure el màxim d'informació de les
# dades recopilades per els experts en el tema. Tampoc no hi ha una solució única ni es
# compararà el resultat amb el d’altres estudiants. El que es valorarà és que la idea
# plantejada tingui sentit, que l’informe comuniqui el que s’ha fet de manera efectiva i que la
# implementació sigui correcta.

# In[1]:


import pandas as pd
import seaborn as sns
sns.set_palette("cool")
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('data/players_22.csv', low_memory = False)


# In[5]:


for col_name in df.columns: 
    print(col_name)


# In[6]:


df['player_positions'].str.split().apply(lambda x: x[0]).unique()


# In[7]:


#weights
a = 0.5
b = 1
c= 2
d = 3

df['best_center_backs'] = (d*df.defending + c*df.mentality_interceptions +
                           d*df.defending_sliding_tackle + d*df.defending_standing_tackle +
                           b*df.mentality_vision + b*df.mentality_composure +
                           b*df.skill_curve + a*df.skill_ball_control+
                           b*df.skill_long_passing + c*df.movement_acceleration +
                           b*df.movement_sprint_speed + d*df.power_stamina +
                           d*df.power_jumping + b*df.power_long_shots +
                           d*df.defending_marking_awareness +
                           c*df.mentality_aggression)/(a + 6*b + 3*c + 6*d)

df['best_wb'] = (d*df.defending + b*df.skill_ball_control + a*df.dribbling +
                 a*df.defending_marking_awareness + d*df.defending_standing_tackle +
                 d*df.defending_sliding_tackle + a*df.mentality_positioning +
                 c*df.attacking_crossing + b*df.attacking_short_passing +
                 c*df.skill_long_passing + d*df.movement_reactions + d*df.movement_agility +
                 c*df.power_stamina + a*df.attacking_finishing)/(4*a + 2*b + 3*c + 5*d)


# In[8]:


# Best Right Wing Back Talents (RB, RWB)

wing_back_right = df[df.player_positions.str.contains('\\b(?:RB)|(?:RWB)\\b', regex=True)]

# Best Left Wing Back Talents (LB, LWB)

wing_back_left = df[df.player_positions.str.contains('\\b(?:LB)|(?:LWB)\\b', regex=True)]

# Best Centre Back Talents (CB)

center_back = df[df.player_positions.str.contains('CB')]


# In[9]:


#DEFENSOR LATERAL DRET:
plt.figure(figsize= (15,6))
sd = wing_back_right.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("RB Score")


# In[10]:


#DEFENSOR LATERAL ESQUERRA:
plt.figure(figsize= (15,6))
sd = center_back.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


# In[11]:


#DEFENSOR CENTRAL:
plt.figure(figsize= (15,6))
sd = wing_back_left.sort_values('best_center_backs',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_center_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


# In[13]:


import pandas as pd
import matplotlib as plt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


#FEMENÍ
df = pd.read_csv('data/female_players_22.csv', low_memory = False)

#weights
a = 0.5
b = 1
c= 2
d = 3

df['best_center_backs'] = (d*df.defending + c*df.mentality_interceptions +
                           d*df.defending_sliding_tackle + d*df.defending_standing_tackle +
                           b*df.mentality_vision + b*df.mentality_composure +
                           b*df.skill_curve + a*df.skill_ball_control+
                           b*df.skill_long_passing + c*df.movement_acceleration +
                           b*df.movement_sprint_speed + d*df.power_stamina +
                           d*df.power_jumping + b*df.power_long_shots +
                           d*df.defending_marking_awareness +
                           c*df.mentality_aggression)/(a + 6*b + 3*c + 6*d)

df['best_wb'] = (d*df.defending + b*df.skill_ball_control + a*df.dribbling +
                 a*df.defending_marking_awareness + d*df.defending_standing_tackle +
                 d*df.defending_sliding_tackle + a*df.mentality_positioning +
                 c*df.attacking_crossing + b*df.attacking_short_passing +
                 c*df.skill_long_passing + d*df.movement_reactions + d*df.movement_agility +
                 c*df.power_stamina + a*df.attacking_finishing)/(4*a + 2*b + 3*c + 5*d)

# Best Right Wing Back Talents (RB, RWB)

wing_back_right = df[df.player_positions.str.contains('\\b(?:RB)|(?:RWB)\\b', regex=True)]

# Best Left Wing Back Talents (LB, LWB)

wing_back_left = df[df.player_positions.str.contains('\\b(?:LB)|(?:LWB)\\b', regex=True)]

# Best Centre Back Talents (CB)

center_back = df[df.player_positions.str.contains('CB')]


# In[14]:


#DEFENSORA LATERAL DRETA:
plt.figure(figsize= (15,6))
sd = wing_back_right.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("RB Score")


# In[15]:


sd = sd.sort_values(['overall','potential'],ascending=(False,False)).head(10)
sd


# In[16]:


#DEFENSORA LATERAL ESQUERRA:
plt.figure(figsize= (15,6))
sd = center_back.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


# In[17]:


#DEFENSORA CENTRAL:
plt.figure(figsize= (15,6))
sd = wing_back_left.sort_values('best_center_backs',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_center_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


# https://www.edureka.co/blog/football-world-cup-best-xi-analysis-using-python/
# 
# 
