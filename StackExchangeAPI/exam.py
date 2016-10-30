import requests 
import json
from datetime import datetime,date,timedelta
import argparse
import os
import sys
parser = argparse.ArgumentParser()
parser.add_argument("--search_term", help="provide a search term use quotes for a string with space")
args = parser.parse_args()
dict_1 = {'tagged': args.search_term}
#r = requests.get('https://api.stackexchange.com/2.2/questions?questions?order=desc&sort=activity&site=stackoverflow',params=dict_1)
#r.json()
cwd = os.getcwd()
def creating_newpath(newpath,x) : #Creates a new path for every file or checks if it exsists.
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        newpath1 = newpath + "//" + x
        return newpath1
    else :
        newpath1 = newpath + "//" + x
        return newpath1
newpath =  cwd + '//' + 'stackoverflow'
newpathoutput = cwd + '//' + 'output'
newpathuid = cwd + '//' + 'stackoverflow' + '//' + 'user_id_' + args.search_term
z = datetime.now().date() #accepts date and time
z = str(z)
e = datetime.now().time()
e = str(e)
m = dict_1['tagged']
newpathoutput1 = creating_newpath(newpathoutput,m)
newpathuid2 = creating_newpath(newpathuid,m)
newpath1 = creating_newpath(newpath,m)
newpath2 = creating_newpath(newpath1,z)
newpath3 = creating_newpath(newpath2,z)
r = requests.get('https://api.stackexchange.com/2.2/questions?key=q5*VT6u7xCuP)L7A*80abA((&order=desc&sort=activity&site=stackoverflow',params=dict_1)
y  = r.json()
with open(os.path.join(newpath2 ,'questionsof' + dict_1['tagged'] + e + '.json'), "a") as f: 
	json.dump(y, f)
        f.close()
print(r.url)


