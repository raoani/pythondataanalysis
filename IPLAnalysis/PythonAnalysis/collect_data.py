
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from datetime import datetime
import os
import sys

matches = pd.read_csv(r'C:\Users\aniru\Desktop\matches.csv')
matches.rename(columns={'id': 'match_id'}, inplace=True)


# In[2]:

deliveries = pd.read_csv(r'C:\Users\aniru\Desktop\deliveries.csv')


# In[16]:

def creating_newpath(newpath) : #Creates a new path for every file or checks if it exsists.
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        newpath1 = os.path.join(newpath)
        return newpath1
    else :
        newpath1 = os.path.join(newpath)
        return newpath1


# In[17]:

newpath = os.path.join(r'C:\Users\aniru\Desktop' , "Seasons")
newpath1 = creating_newpath(newpath)
nwpath = os.path.join(newpath1,'combined')
nwpath2= creating_newpath(nwpath)


# In[ ]:




# In[ ]:




# In[18]:

combined = pd.merge(matches, deliveries, on = 'match_id', how = 'outer')
combined.season.value_counts()
combined.to_csv((os.path.join(nwpath,'combined.csv')))
season_list = combined.season.unique().tolist()
season_list
combined.set_index(keys=['season'], drop=False,inplace=True)
j = 1
for i in season_list :
    year = combined.loc[combined['season']== i]
    year.to_csv(os.path.join(newpath,'season_' + str(j) + '.csv'))
    j = j + 1


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



