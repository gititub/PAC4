"""PAC4. PROGRAMACIÓ PER A LA CIÈNCIA DE DADES
    Author: Amèlia Martínez
"""

import pandas as pd
import sys
import os
import numpy as np
import statistics
import seaborn as sns
sns.set_palette("cool")
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import warnings
warnings.filterwarnings('ignore')

def read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame:
    """Function with 3 inputs: filepath(+/or\), gender ['M' for Male
    or 'F' for Female], and year [from 2016 to 2022] of the data.
    Reads the file in filepath and returns a pandas dataframe with
    two new columns:
    - gender: 'Male' or 'Female' 
    - year of the data"""
    year_n = [int(a) for a in str(year)]
    if gender == 'M':
        df = pd.read_csv(filepath + "players_" + str(year_n[2]) + str(year_n[3]) +
                         ".csv", low_memory = False)
        n = len(df.index)
        df['gender'] = ['Male']*n
        df['year'] = year
        return df
        
    elif gender == 'F':
        df = pd.read_csv(filepath + "female_players_" + str(year_n[2]) + str(year_n[3]) + ".csv", low_memory = False)
        n = len(df.index)
        df['gender'] = ['Female']*n
        df['year'] = year
        return df
      
def join_male_female(filepath: str, year: int) -> pd.DataFrame:
    """Function with 2 inputs: filepath  and year [from 2016 to 2022]
    of the data.
    Reads the file in filepath and returns a pandas dataframe with
    two new columns:
    - gender: 'Male' or 'Female' 
    - year of the data"""
    df1 = read_add_year_gender(filepath, 'M', year)
    df2 = read_add_year_gender(filepath, 'F', year)
    joined_result = df1.append(df2)
    return joined_result
  
  
def join_datasets_year(path: str, years: list) -> pd.DataFrame:
    """Function with 2 inputs: filepath(+/or\)and a list
    of years[from 2016 to 2022] of the data.
    Reads the file in filepath and returns a pandas dataframe 
    with joined gender of input years data with two new columns:
    - gender: 'Male' or 'Female' 
    - year of the data"""
    frames = []
    for year in years:
        temp_df = join_male_female(path, year)
        frames.append(temp_df)
        result = pd.concat(frames, ignore_index=True)
    return result

def find_max_col(df: pd.DataFrame, filter_col: str, cols_to_return: list) -> pd.DataFrame:
    """Una funció que rep un dataframe i, donat el nom d'una columna numèrica, ens retorni
    la/es fila/es en què el seu valor és màxim. A més, la funció rebrà com a argument una
    llista de noms de columnes. El dataframe que retorni ha de contenir nomes:
    - df: dataframe que conté les dades
    - filter_col: nom de la columna de la que volem saber el màxim
    - cols_to_return: llista de columnes que cal retornar"""
    try:
        df_max = df[cols_to_return][df[filter_col] == df[filter_col].max()]
        return df_max
    except:
        print("No és una columna numèrica")
    
years = list(range(2016,2023))
df3 = join_datasets_year('data/', years)

llista_columnes =['long_name' , 'player_positions', 'age']
find_max_col(df3, 'age', llista_columnes)

llista_columnes =['short_name' , 'year', 'overall']
find_max_col(df3, 'short name', llista_columnes)

def find_rows_query(df: pd.DataFrame, query: tuple, cols_to_return: list) -> pd.DataFrame:
    """La funció rep un dataframe i una query en forma de tupla. El primer element de la 
    tupla serà una llista de columnes sobre les que volem filtrar. El segon element serà 
    la llista de valors que volem fer servir al filtre. Si la columna és categòrica, el 
    valor serà un string. Si és numèrica, serà una tupla amb el valor mínim i màxim"""
    if type(query[1][0]) == tuple and type(query[1][1]) == tuple:
        df_query = df[cols_to_return][(df[query[0][0]] >= query[1][0][0])& (df[query[0][0]] <= query[1][0][1])&
                                      (df[query[0][1]] >= query[1][1][0])& (df[query[0][1]] <= query[1][1][1])]
    elif type(query[1][0]) == tuple and type(query[1][1]) == str:
        df_query = df[cols_to_return][(df[query[0][0]] >= query[1][0][0])& (df[query[0][0]] <= query[1][0][1])&
                                      (df[query[0][1]] == query[1][1])]      
    elif type(query[1][0]) == str and type(query[1][1]) == tuple:
        df_query = df[cols_to_return][(df[query[0][0]] == query[1][0])& (df[query[0][1]] >= query[1][1][0])&
                                     (df[query[0][1]] <= query[1][1][1])]
    else:
        df_query = df[cols_to_return][(df[query[0][0]] == query[1][0])& (df[query[0][1]] == query[1][1])]
    return df_query

llista_columnes =['short_name' , 'year', 'overall','league_name', 'gender']    
find_rows_query(df3, (['league_name', 'gender'], ['English Premier League', 'Male']), llista_columnes)

llista_columnes =['short_name' , 'year', 'overall','league_name', 'gender','age']
find_rows_query(df3, (['overall', 'age'], [(72,90), (18,25)]), llista_columnes)

llista_columnes =['short_name' , 'year', 'overall','league_name', 'gender','age']
find_rows_query(df3, (['league_name', 'age'], ['English Premier League', (18,25)]), llista_columnes)

llista_columnes =['short_name' , 'year', 'overall','league_name', 'gender','age']
find_rows_query(df3, (['age','league_name'], [(18,25),'English Premier League']), llista_columnes)

# des de l'any 2016 fins al 2022, ambdós inclosos, mostreu per pantalla el “short_name”, “year”,
# “age”, “overall” i “potential” dels jugadors de nacionalitat belga menors de 25 anys màxim
# “potential” al futbol masculí.

llista_col = ['short_name', 'year', 'age', 'overall', 'potential']

belg_fins24= df3[llista_col][(df3['age'] < 25)&(df3['nationality_name']=='Belgium')&
                             (df3['gender']=='Male')]
belg_fins24[belg_fins24['potential'] == belg_fins24['potential'].max()]

# des de l'any 2016 fins al 2022, ambdós inclosos, mostreu per pantalla el “short_name”, “year”,
# “age”, “overall” i “potential” de les porteres majors de 28 anys amb “overall” superior a 85 al futbol femení.

llista_col = ['short_name', 'year', 'age', 'overall', 'potential']

df3[llista_col][(df3['gender']=='Female')&(df3['age'] > 28)&(df3['overall'] > 85)]

height = df3['height_cm'].astype(float)/100
weight = df3['weight_kg'].astype(float)
df3['BMI'] = round(weight/(height*height), 3)
llista_col = ['short_name', 'year', 'age', 'overall', 'potential']
llista_col.append('BMI')

df3[(df3['year']== 2016)&(df3['gender']=='Male')]

def calculate_BMI(df: pd.DataFrame, gender: str, year: int, cols_to_return: list) -> pd.DataFrame:
    """Function with inputs: dataframe, gender, year: format XXXX, cols_to_return.
    Returns a dataframe with a new BMI column"""
    height = df['height_cm'].astype(float)/100
    weight = df['weight_kg'].astype(float)
    df['BMI'] = round(weight/(height*height), 3)
    cols_to_return.append('BMI')
    df_bmi = df[cols_to_return][(df['year']==year)&(df['gender']==gender)]
    return df_bmi

llista_col = ['short_name', 'year', 'age', 'overall', 'potential']
calculate_BMI(df3, 'Male', 2016, llista_col)

#  gràfica amb el BMI màxim per país. Filtreu per gènere masculí i any 2022. 

# df4['pais'] = df4['club_flag_url'].str.extract('flags/(\w+).png')

df4 = calculate_BMI(df3, 'Male', 2022, ['club_flag_url'])
df4['pais'] = df4['club_flag_url'].str.extract('flags/([a-zA-Z]+(?:-[a-zA-Z]+)*).png')
df4
# gràfica
df5 = df4.groupby('pais').BMI.agg(['max'])
ax = df5.plot(kind='bar', figsize=(16, 6), title='BMI max', rot=40)
plt.show()

llista_col = ['age']
data = calculate_BMI(df3, 'Female', 2020, llista_col) 
data.loc[(data['age']<25), "Age"]="From 18 to 24 years old" 
data.loc[(data['age']>24) & (data['age']<35), "Age"]="From 25 to 34 years old"
data.loc[(data['age']>34), "Age"]="From 35 to 44 years old"
data.loc[(data['BMI']< 18.5), 'Adult body mass index']="Underweight (BMI < 18.5 kg/m2)" 
data.loc[(data['BMI']>=18.5) & (data['BMI']<25), 'Adult body mass index']="Normal weight (18.5 kg/m2 <= BMI < 25 kg/m2)"
data.loc[(data['BMI']>=25) & (data['BMI']<30), 'Adult body mass index']="Overweight (25 kg/m2 <= BMI < 30 kg/m2)"
data

# Plot dades dataset
data3 = data[['BMI','Age','Adult body mass index']].groupby(['Age','Adult body mass index']).mean().unstack()
ax = data3.plot(kind='bar', figsize=(16, 6), title='BMI', rot=40)
plt.show()

#Plot dades ine
data2 = pd.read_csv('ine.csv', sep=';')
data2['Total'] = data2['Total'].str.replace(",", "").astype(float)
data22 = data2[['Age','Adult body mass index','Total']].groupby(['Age','Adult body mass index']).mean().unstack()
ax = data22.plot(kind='bar', figsize=(16, 6), title='BMI', rot=40)
plt.show()

# Diccionaris


def players_dict(df: pd.DataFrame, ids: list, cols:list) -> dict:
    """Inputs:
    - df: dataframe que conté les dades
    - ids: llista d’identificador “sofifa_id”
    - cols: llista de columnes de les que volem informació
    retorna un diccionari:
    - que tingui com a claus els identificadors “sofifa_id” continguts a la llista “ids”
    - que tingui com a valors diccionaris amb la informació corresponent a cada
    jugador/a. Concretament, les claus de cadascun d'aquests diccionaris seran els
    noms de les columnes incloses a “col” i els seus valors seran la informació de tots
    els anys disponibles al dataframe per a cada futbolista"""
    cols.append('sofifa_id')
    df = df[cols]
    df.set_index('sofifa_id', inplace=True)
    df = df.groupby('sofifa_id').agg(lambda x: x.values.tolist()).T
    df_dict = df.to_dict()
    result= dict((k, df_dict[k]) for k in ids if k in df_dict)
    return result
    
ids = [261799,158023,20801]
cols = ['short_name', 'year', 'age', 'overall', 'potential']
players_dict(df3, ids, cols)

def clean_up_players_dict(player_dict: dict, col_query: list) -> dict:
    """ player_dict: diccionari amb el format de l’apartat(a), col_query:
    llista de tuples amb detalls sobre la información que cal simplificar
    Cada tupla de la llista estarà composta per dos valors:1)el nom duna columna
    i 2) una cadena de caràcters. Aquesta cadena pot contenir dos valors possibles,
    els quals ens indiquen l'operació a realitzar sobre la columna/clau del diccionari:
    - “one”: ens hem de quedar només amb el primer valor que aparegui
    - “del_rep”: primer hem de descompondre la informació i després eliminar les
    repeticions
    - La informació referent a les columnes que no apareixen a col_query es retornarà
    sense canvis."""
    res = dict()
    for ident, params in player_dict.items():
        params[col_query[0][0]] = set(params[col_query[0][0]])
        params[col_query[1][0]] = params[col_query[1][0]][:1]
        res[ident] = params
    return res

# Prova 1
col_query = [("player_positions","del_rep"), ("short_name","one")]
d= {41: {'short_name': ['Iniesta', 'Iniesta', 'Iniesta'], 'overall': [88, 88, 87], 'potential': [88, 88, 87],
'player_positions': ['CM', 'CM', 'CM, LM'], 'year': [2016, 2017, 2018]}}
clean_up_players_dict(d, col_query)

# Prova2
ids = [261799,158023,20801,41]
cols = ['short_name',"player_positions", 'year', 'age', 'overall', 'potential']
d = players_dict(df3, ids, cols)
col_query = [("short_name","del_rep"), ('potential','one')]
clean_up_players_dict(d, col_query)

# Considerant el dataframe amb ambdós gèneres i els anys 2016, 2017 i 2018,
# mostreu per pantalla:
# El diccionari construït amb la funció de l'apartat 4a amb la informació de
# les columnes ["short_name", "overall", “potential”, "player_positions", "year"]
# i els ids = [226328, 192476, 230566]
years = [16,17,18]
ids = [226328, 192476, 230566]
df9 = join_datasets_year('data/', years)
cols = ["short_name", "overall", "potential", "player_positions", "year"]
d9 = players_dict(df9, ids, cols)
# La query que passaríeu a la funció de l'apartat 4b per netejar aquest diccionari:
col_query = [("short_name","del_rep"), ('potential','one')]
# El diccionari “net”;
clean_up_players_dict(d9, col_query)

# La millor defensa. 
# Millor linia defensiva dels jugadors de 30 anys o més (masculí i femení)

data6 = join_male_female('data/', 2022)
players = data6[data6['age']>29]
players['player_positions'].str.split().apply(lambda x: x[0]).unique()

#weights
a = 0.5
b = 1
c= 2
d = 3

players['best_center_backs'] = (d*players.defending + c*players.mentality_interceptions +
                           d*players.defending_sliding_tackle + d*players.defending_standing_tackle +
                           b*players.mentality_vision + b*players.mentality_composure +
                           b*players.skill_curve + a*players.skill_ball_control+
                           b*players.skill_long_passing + c*players.movement_acceleration +
                           b*players.movement_sprint_speed + d*players.power_stamina +
                           d*players.power_jumping + b*players.power_long_shots +
                           d*players.defending_marking_awareness +
                           c*players.mentality_aggression)/(a + 6*b + 3*c + 6*d)

players['best_wb'] = (d*players.defending + b*players.skill_ball_control + a*players.dribbling +
                 a*players.defending_marking_awareness + d*players.defending_standing_tackle +
                 d*players.defending_sliding_tackle + a*players.mentality_positioning +
                 c*players.attacking_crossing + b*players.attacking_short_passing +
                 c*players.skill_long_passing + d*players.movement_reactions + d*players.movement_agility +
                 c*players.power_stamina + a*players.attacking_finishing)/(4*a + 2*b + 3*c + 5*d)

# Best Right Wing Back Talents (RB, RWB)

wing_back_right = players[players.player_positions.str.contains('\\b(?:RB)|(?:RWB)\\b', regex=True)]

# Best Left Wing Back Talents (LB, LWB)

wing_back_left = players[players.player_positions.str.contains('\\b(?:LB)|(?:LWB)\\b', regex=True)]

# Best Centre Back Talents (CB)

center_back = players[players.player_positions.str.contains('CB')]

#DEFENSOR LATERAL DRET:
plt.figure(figsize= (15,6))
sd = wing_back_right.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("RB Score")

#DEFENSOR LATERAL ESQUERRA:
plt.figure(figsize= (15,6))
sd = wing_back_left.sort_values('best_center_backs',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_center_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")

#DEFENSOR CENTRAL:
plt.figure(figsize= (15,6))
sd = center_back.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("CB Score")

# MILLOR DEFENSA EQUIP MASCULÍ

df = pd.read_csv('data/players_22.csv', low_memory = False)

for col_name in df.columns: 
    print(col_name)

df['player_positions'].str.split().apply(lambda x: x[0]).unique()

#Establim els pesos de cada característica
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

#DEFENSOR LATERAL DRET:
plt.figure(figsize= (15,6))
sd = wing_back_right.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("RB Score")


#DEFENSOR LATERAL ESQUERRA:
plt.figure(figsize= (15,6))
sd = wing_back_left.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")

#DEFENSOR CENTRAL:
plt.figure(figsize= (15,6))
sd = center_back.sort_values('best_center_backs',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_center_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


# MILLOR DEFENSA EQUIP FEMENÍ
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


#DEFENSORA LATERAL DRETA:
plt.figure(figsize= (15,6))
sd = wing_back_right.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("RB Score")


sd = sd.sort_values(['overall','potential'],ascending=(False,False)).head(10)
sd


#DEFENSORA LATERAL ESQUERRA:
plt.figure(figsize= (15,6))
sd = wing_back_left.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


#DEFENSORA CENTRAL:
plt.figure(figsize= (15,6))
sd = center_back.sort_values('best_center_backs',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_center_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


#Referències:

#https://www.geeksforgeeks.org/how-to-combine-two-dataframe-in-python-pandas/
#https://www.geeksforgeeks.org/read-multiple-csv-files-into-separate-dataframes-in-python/
#https://stackoverflow.com/questions/70177540/how-to-groupby-aggregate-min-max-and-plot-grouped-bars
#https://stackoverflow.com/questions/66978572/extract-part-of-url-from-column-of-urls-in-python
#https://es.stackoverflow.com/questions/155042/expresi%C3%B3n-regular-con-gui%C3%B3n-medio-en-una-clase-de-caracteres
#https://stackoverflow.com/questions/47837594/melting-a-pandas-dataframe-into-dictionary-with-unique-keys-based-on-a-column
#https://www.geeksforgeeks.org/python-converting-all-strings-in-list-to-integers/
#https://www.edureka.co/blog/football-world-cup-best-xi-analysis-using-python/
