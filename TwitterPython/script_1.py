import requests
import json
import os
import sys
import argparse
from datetime import datetime,date,timedelta
from requests_oauthlib import OAuth1
parser = argparse.ArgumentParser()
parser.add_argument("--search_term", help="provide a search term use quotes for a string with space") #Accepts any search term"
args = parser.parse_args()
cnt = 100
x = { "q" : args.search_term, "count" : cnt }
def creating_newpath(newpath,x) : #Creates a new path for every file or checks if it exsists.
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        newpath1 = newpath + "//" + x
        return newpath1
    else :
        newpath1 = newpath + "//" + x
        return newpath1


z = datetime.now().date() #accepts date and time
z = str(z)
e = datetime.now().time()
e = str(e)
m = x['q']
cwd = os.getcwd()
newpath = cwd + "//" + 'twitter' 
newpath1 = creating_newpath(newpath, m) #creates a twitter path in the current working directory
newpath2 = creating_newpath(newpath1,z) #creates a directory with search term inside twitter 
newpath3 = creating_newpath(newpath2,e) #creates a directory with date inside the search directory
newpath4 = creating_newpath(newpath3,e) # creates a directory with the time program was executed
r = requests.get('https://api.twitter.com/1.1/search/tweets.json?', auth=auth, params = x) #request for tweets
a = r.json()
y = a['statuses']
with open(os.path.join(newpath3 ,'tweetsof' + x['q'] + '.json'), "a") as f: #creates a json file with 100 tweets
	json.dump(y, f)
        f.close()
print(r.url)    
