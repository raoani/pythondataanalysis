
# coding: utf-8

# In[3]:

import matplotlib.pyplot as plt
import seaborn as sns
#%matplotlib inline
from scipy.misc import imread


# In[2]:

import numpy as np
from datetime import datetime
import os
import sys
import glob
import pandas as pd
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--Team", help="provide a search term, latitude, longitude and radius")
#parser.add_argument("--location", help="provide a search term, latitude, longitude and radius")
args = parser.parse_args()
batting_team = args.Team
dict_1 = {}
dict_2 = {}
newpath = r'C:\Users\aniru\Desktop'
def creating_newpath(newpath, x) : #Creates a new path for every file or checks if it exsists.
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        newpath1 = os.path.join(newpath , x)
        return newpath1
    else :
        newpath1 = os.path.join(newpath, x)
        return newpath1



def analysis_3( df, batting_team ) :
    df = df[df['batting_team'] == batting_team]
    l = []
    for j in df.over.unique().tolist() :
        df2 = df[df['over'] == j]
        df2 = df2.set_index(['over'] , drop = True)
        df2 = df2[['season','batting_team', 'player_dismissed' , 'dismissal_kind']]
        df2['player_dismissed'].fillna(0, inplace=True)
        #df2['dismissal_kind'].fillna(0, inplace=True)
         #df2['dismissal_kind'].fillna(0, inplace=True)
        df2 = df2[df2['player_dismissed'] != 0]
        #df2.loc[j,'run_outs'] = len(df2[df2['dismissal_kind'] == 'run out'])
        #df2.loc[j,'total_wickets'] = len(df2[df2['player_dismissed'] != 0])
        df2.loc[j,'total_wickets'] = j
        df2 = df2[['season' , 'batting_team' , 'total_wickets']]
        l.append(df2)
    l = pd.concat(l, axis=0)
    return l
	
	
	
x = glob.glob(r'C:\Users\aniru\Desktop\Season\*.csv')
appended_data = []
for g in  x :
    df1 = pd.read_csv(g)
    if batting_team in df1['batting_team'].unique().tolist() :
        df2 = analysis_3(df1, batting_team)
        appended_data.append(df2)
appended_data = pd.concat(appended_data, axis=0)
appended_data = appended_data.reset_index()
appended_data = appended_data.set_index(['over'])



newpath1 = creating_newpath(newpath , 'Output')




newpath2  = creating_newpath(newpath1 , batting_team)
newpath3 = creating_newpath(newpath2 , batting_team)
a = appended_data['total_wickets'].reset_index()


b = a['total_wickets'].tolist()
fig = plt.figure() 
ax = fig.add_subplot(1, 1, 1)
ax.hist(b, bins=20, color='blue')
ax.set_xlabel('over')
ax.set_ylabel('Total Wickets Fallen')
plt.xlim(1,20)
plt.ylim(1,100)
ax.set_title('Fall of wickets ranging all seasons :' + batting_team)
plt.savefig(os.path.join(newpath2 , 'analysis_1.jpg'))
appended_data.to_csv(os.path.join(newpath2,'analysis_1.csv'))

# In[1]:



# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



