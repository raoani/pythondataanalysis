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
cwd = os.getcwd() #opens current working directory


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


newpath1 = creating_newpath(newpath,m)   #creates a directory with the name stackoverflow in present working directory.
newpathoutput1 = creating_newpath(newpathoutput,m)   #creates a directory output were the outputs of each analysis are available
newpathuid2 = creating_newpath(newpathuid,m) #creates a directory with the user_id
newpath2 = creating_newpath(newpath1,z)  #creates a directory with search term
newpath3 = creating_newpath(newpath2,z)  #creates a directory with todays's date.



r = requests.get('https://api.stackexchange.com/2.2/questions?key=q5*VT6u7xCuP)L7A*80abA((&order=desc&sort=activity&site=stackoverflow',params=dict_1)  #requests for questions of particular search_term
y  = r.json() #stroes it in Json



with open(os.path.join(newpath2 ,'questionsof' + dict_1['tagged'] + e + '.json'), "a") as f: #opens a json file with questionsof"search_term""time".
	json.dump(y, f)   #dumps the json data
        f.close()   #closes file
print(r.url)  #prints the searched URL


