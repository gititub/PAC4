"""PAC4. PROGRAMACIÓ PER A LA CIÈNCIA DE DADES
    Author: Amèlia Martínez
"""

import pandas as pd
import sys
import os
import psutil
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
