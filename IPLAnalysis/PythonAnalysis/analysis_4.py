
# coding: utf-8

# In[2]:

import numpy as np
from datetime import datetime
import os
import sys
import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#get_ipython().magic('matplotlib inline')
from scipy.misc import imread
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--Team", help="provide a search term, latitude, longitude and radius")
parser.add_argument("--Score", help="provide a search term, latitude, longitude and radius")
#parser.add_argument("--location", help="provide a search term, latitude, longitude and radius")
args = parser.parse_args()
batting_team = args.Team
j = int(args.Score)
# In[3]:

dict_1 = {}
dict_2 = {}
#batting_team = 'Royal Challengers Bangalore'
x = glob.glob(r'C:\Users\aniru\Desktop\Season\*.csv')
l = []

newpath = r'C:\Users\aniru\Desktop'
def creating_newpath(newpath, x) : #Creates a new path for every file or checks if it exsists.
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        newpath1 = os.path.join(newpath , x)
        return newpath1
    else :
        newpath1 = os.path.join(newpath, x)
        return newpath1


# In[4]:

def analysis_3 (df1,j) :
    match_id = df1.match_id.unique().tolist()
    df1 = df1.set_index(['match_id'] , drop = False)
#df2 = df1.set_index(['match_id'] ) #drop = False)
#df1['final_score'] = sum(df1['total_runs'])
    appended_data = []
    for i in match_id :
        df2 = df1[df1['match_id'] == i]
        df2 = df2[['batting_team','total_runs','winner','season','match_id']]
        df2['total_score'] = sum(df2['total_runs'])
        df2 = df2[['batting_team','total_score','winner','season','match_id']].drop_duplicates()
        appended_data.append(df2)
    df3 = pd.concat(appended_data, axis=0)
    df3 = df3[df3['total_score'] > j]
    length = len(df3.match_id.unique().tolist())
    df3 = df3[['batting_team','total_score','winner','season']]
    if length != 0 :
        df3 = df3[df3['winner'] == batting_team]
        df3 = df3.reset_index()
        df3['percentage_above_' + str(j) + '_and_won'] = round(len(df3['match_id'].unique().tolist())/length*100)
        df3 = df3[['batting_team','season','percentage_above_' + str(j) + '_and_won']].drop_duplicates().set_index(['season'])
        return df3


# In[5]:

dict_1 = {}
dict_2 = {}
#batting_team = 'Chennai Super Kings'
x = glob.glob(r'C:\Users\aniru\Desktop\Season\*.csv')
l = []
#j = 150
for i in x :
        df = pd.read_csv(i)
        if batting_team in df.batting_team.unique().tolist() :
            df1 = df[df['batting_team'] == batting_team]
            df1 = analysis_3(df1,j)
            l.append(df1)
df4 = pd.concat(l, axis=0)
df4 = df4.reset_index(drop = False)
df4

newpath1 = creating_newpath(newpath , 'Output')
newpath2  = creating_newpath(newpath1 , batting_team)
newpath3 = creating_newpath(newpath2 , batting_team)
# In[8]:

sns.set_style("whitegrid")
plt.subplots(figsize=(20,8))
sns.set_style("whitegrid")
ax = sns.barplot(x='season',y='percentage_above_'+str(j)+'_and_won',data=df4 , color = 'blue')
sns.set_style('whitegrid')
ax.set(title = 'Win rate of ' + batting_team + ' when they score above '+ str(j) + ' for all seasons in Percentage')
sns.set_style('whitegrid')
plt.savefig(os.path.join(newpath2 , 'analysis_4.jpg'))
df4.to_csv(os.path.join(newpath2,'analysis_4.csv'))
# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



