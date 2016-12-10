
# coding: utf-8

# In[7]:

import numpy as np
from datetime import datetime
import os
import sys
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#get_ipython().magic('matplotlib inline')
import argparse
import matplotlib.patches as mpatches

parser = argparse.ArgumentParser()
parser.add_argument("--number", help="provide a search term, latitude, longitude and radius")
#parser.add_argument("--location", help="provide a search term, latitude, longitude and radius")
args = parser.parse_args()
k = int(args.number)

def creating_newpath(newpath, x) : #Creates a new path for every file or checks if it exsists.
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        newpath1 = os.path.join(newpath , x)
        return newpath1
    else :
        newpath1 = os.path.join(newpath, x)
        return newpath1

# In[39]:


dict_1 = {}
dict_2 = {}
#batting_team = 'Royal Challengers Bangalore'
x = glob.glob(r'C:\Users\aniru\Desktop\Season\*.csv')
l = []
matches = pd.read_csv(r'C:\Users\aniru\Desktop\matches.csv')
matches.rename(columns={'id': 'match_id'}, inplace=True)
deliveries = pd.read_csv(r'C:\Users\aniru\Desktop\deliveries.csv')
df1 = pd.merge(matches, deliveries, on = 'match_id', how = 'outer')
a = df1.batsman.unique().tolist()
df1['total_batsman'] = 0
df1 = df1.set_index(['batsman'], drop = False)
for i in a :
    df2 = df1[df1['batsman'] == i ]
    df1.loc[i,'total_batsman'] = sum(df2['batsman_runs'])
df3 = df1[['batsman' , 'total_batsman']]
df3 = df3.drop_duplicates(['batsman'])
df4 = df3.sort_values(by = ['total_batsman'], ascending= False)
df4 = df4.reset_index(drop=True)
a = df4.batsman.unique().tolist()[k-1]



# In[25]:

def analysis (df5, a) :
    y = df5[df5['batsman']==a]['batting_team'].unique()[0]
#y = df6.iloc[0]['batting_team']
    df5 = df5[df5['batting_team']==y]
    df5 = df5.set_index('batting_team' , drop=False)
#y
    batsman_runs = sum(df5[df5['batsman']==a]['batsman_runs'])
    team_runs = sum(df5['batsman_runs'])
    percentage_runs = round(batsman_runs/team_runs*100)
    df5.loc[y,'total_runs_by_'+a] = sum(df5[df5['batsman']==a]['batsman_runs'])
    df5.loc[y, 'total_runs_by_team'] = sum(df5['batsman_runs'])
    df5.loc[y,'percentage_runs_by_'+a] = percentage_runs
    df5 = df5[['season','total_runs_by_team','total_runs_by_'+a,'percentage_runs_by_'+a]].drop_duplicates()
    return df5 


# In[40]:

x = glob.glob(r'C:\Users\aniru\Desktop\Season\*.csv')
appended_data = []
for i in x :
    df5 = pd.read_csv(i)
    df5= analysis(df5, a)
    appended_data.append(df5)
appended_data = pd.concat(appended_data, axis=0)
appended_data.set_index(['season'])


# In[41]:

newpath = r'C:\Users\aniru\Desktop'
newpath1 = creating_newpath(newpath , 'Output')
newpath2  = creating_newpath(newpath1 , a)
newpath3 = creating_newpath(newpath2 , a)
df4.to_csv(os.path.join(newpath2,'analysis_top_batsman.csv'))
fig = plt.figure() 
sns.barplot(x =appended_data.season , y = appended_data['total_runs_by_team'] , color = "#79c36a")
bottom_plot = sns.barplot(x = appended_data.season, y = appended_data['total_runs_by_' + a], color = "blue")
sns.set_style('whitegrid')
bottom_plot.set(xlabel='Seasons', ylabel='Total runs by team and ' + a, title = 'Runs Scored by ' + a + ' through all seasons')
red_patch = mpatches.Patch(color='#79c36a', label='Total Runs By a Team')
blue_patch  = mpatches.Patch(color = 'blue' , label = 'Runs by ' + a)
sns.set_style('whitegrid')
plt.legend(handles=[red_patch,blue_patch])
plt.ylim([0,3500])
plt.savefig(os.path.join(newpath2 , 'analysis_3.jpg'))
appended_data.to_csv(os.path.join(newpath2,'analysis_3.csv'))

# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



