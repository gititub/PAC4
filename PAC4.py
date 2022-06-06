"""PAC4. PROGRAMACIÓ PER A LA CIÈNCIA DE DADES
    Author: Amèlia Martínez
"""

import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
import numpy as np


def read_add_year_gender(filepath: str, gender: str, year: int) -> pd.DataFrame:
    """Function with 3 inputs: filepath(+/or\), gender ['M' for Male
    or 'F' for Female], and year [from 2016 to 2022] of the data.
    Reads the file in filepath and returns a pandas dataframe with
    two new columns:
    - gender: 'Male' or 'Female' 
    - year of the data"""
    year_n = [int(a) for a in str(year)]
    if gender == 'M':
        df = pd.read_csv(filepath + "players_" + str(year_n[2]) +
                         str(year_n[3]) + ".csv", low_memory = False)
        n = len(df.index)
        df['gender'] = ['Male']*n
        df['year'] = year
        return df
        
    elif gender == 'F':
        df = pd.read_csv(filepath + "female_players_" + str(year_n[2]) +
                         str(year_n[3]) + ".csv", low_memory = False)
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
df3 = join_datasets_year('/home/datasci/prog_datasci_2/activities/activity_4/data/', years)

llista_columnes =['long_name' , 'player_positions', 'age']
find_max_col(df3, 'age', llista_columnes)

llista_columnes =['short_name' , 'year', 'overall']
find_max_col(df3, 'short name', llista_columnes)
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
df4 = calculate_BMI(df3, 'Male', 2022, ['club_flag_url'])
df4['pais'] = df4['club_flag_url'].str.extract('flags/(\w+).png')
df4

#  gràfica amb el BMI màxim per país. Filtreu per gènere masculí i any 2022. 
df4 = calculate_BMI(df3, 'Male', 2022, ['club_flag_url'])
df4['pais'] = df4['club_flag_url'].str.extract('flags/([a-zA-Z]+(?:-[a-zA-Z]+)*).png')
df4


import matplotlib.pyplot as plt

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

data3 = data[['BMI','Age','Adult body mass index']].groupby(['Age','Adult body mass index']).mean().unstack()

data2 = pd.read_csv('data/ine.csv', sep=';')
#data2['Total'] = pd.to_numeric(data2['Total']).astype(float)
#data22 = data2[['Age','Adult body mass index','Total']].groupby(['Age','Adult body mass index']).mean().unstack()
data2

ax = data3.plot(kind='bar', figsize=(16, 6), title='BMI', rot=40)
plt.show()

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

col_query = [("player_positions","del_rep"), ("short_name","one")]

d= {41: {'short_name': ['Iniesta', 'Iniesta', 'Iniesta'], 'overall': [88, 88, 87], 'potential': [88, 88, 87],
'player_positions': ['CM', 'CM', 'CM, LM'], 'year': [2016, 2017, 2018]}}

clean_up_players_dict(d, col_query)

ids = [261799,158023,20801,41]
cols = ['short_name',"player_positions", 'year', 'age', 'overall', 'potential']
d = players_dict(df3, ids, cols)
col_query = [("short_name","del_rep"), ('potential','one')]

clean_up_players_dict(d, col_query)

years = [16,17,18]
ids = [226328, 192476, 230566]
df9 = join_datasets_year('/home/datasci/prog_datasci_2/activities/activity_4/data/', years)
cols = ["short_name", "overall", "potential", "player_positions", "year"]
d9 = players_dict(df9, ids, cols)

col_query = [("short_name","del_rep"), ('potential','one')]

clean_up_players_dict(d9, col_query)
