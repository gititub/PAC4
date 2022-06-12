#!/usr/bin/env python
# coding: utf-8

# ## Exercici 6: La millor defensa.

import pandas as pd
import seaborn as sns
sns.set_palette("cool")
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


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
sd = center_back.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")

#DEFENSOR CENTRAL:
plt.figure(figsize= (15,6))
sd = wing_back_left.sort_values('best_center_backs',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_center_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


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
sd = center_back.sort_values('best_wb',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_wb']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")


#DEFENSORA CENTRAL:
plt.figure(figsize= (15,6))
sd = wing_back_left.sort_values('best_center_backs',ascending=False)[:10]
x2 = np.array(list(sd['short_name']))
y2 = np.array(list(sd['best_center_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("LB Score")

#Referències:
# https://www.edureka.co/blog/football-world-cup-best-xi-analysis-using-python/
# 
# 
