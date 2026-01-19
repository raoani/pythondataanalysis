import requests
import json
import os
import sys
import argparse
import unicodedata
from datetime import datetime,date,timedelta
import glob
import numpy as np
import ast
import csv
import re
a = []
parser = argparse.ArgumentParser()
parser.add_argument("--search_term", help="provide a search term. Use ; instead of comma to search multiple tags")
args = parser.parse_args()
dict_1 = {}
cwd = os.getcwd()


def find_path(newpath) : #searches for a particular path and lists the directories in that path
	if not os.path.exists(newpath):
       		print('no file found')
	else :
		a = os.listdir(newpath)
		return a


newpath = cwd + '//' + 'stackoverflow' + '//' + args.search_term
newpathuid = cwd + '//' + 'stackoverflow' + '//' + 'user_id_' + args.search_term

x = find_path(newpath)   #searches the path provided by newpath

dict_2 ={}
dict_3={}


for i in range(len(x)) :
	newpath1 = newpath + '//' + x[i]
	x1 = find_path(newpath1)  
	for j in range(len(x1)) : #itterates through each file inside the path
		with open(os.path.join(newpath1 , x1[j])) as f:   #opens the json files inside the directories
			data = json.load(f)
		for j1 in range(len(data['items'])) :   #analysis of data inside json
			if data['items'][j1]['owner']['user_type'] == 'registered' :  #checks if the user has deleted his account or not 
				user_id = data['items'][j1]['owner']['user_id'] #extracts the user_ID
				dict_3[str(user_id)] = {str(data['items'][j1]['owner']['display_name']) : str(data['items'][j1]['title'])}  #stores user_id as the key with name and title of question as the values
				r = requests.get('https://api.stackexchange.com/2.2/users/{0}?&order=desc&sort=modified&site=stackoverflow'.format(user_id))
				y  = r.json()
				with open(os.path.join(newpathuid , 'user_id') , 'a') as outfile:
    					json.dump(y, outfile)
				a.append(user_id)
				for i in range(len(y['items'])) :
					d = y['items'][i]['badge_counts']
					count = d['bronze'] + d['silver']*10 + d['gold']*20
					dict_2[str(user_id)]=  count
l= []
newpathoutput = cwd + '//' + 'output'
#print(dict_3)
#print(dict_2)
#print(sorted(dict_2.values(),reverse=True))
for key, value in dict_2.iteritems() :
	if value == max(dict_2.values()) :
		jai = key
	elif value == sorted(dict_2.values(),reverse=True)[1] :
		jai1 = key
	elif value == sorted(dict_2.values(),reverse=True)[2] :
		jai2 = key
	
#print(dict_3[jai])
#print(dict_3[jai1])
#print(dict_3[jai2])
with open(os.path.join(newpathoutput, args.search_term + 'top_3_questions.csv'), 'w') as csv_file: #Stores the analysed value in csv file.
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(["Top questions according to badge count"])
    writer.writerow(["User Name", "Question Asked"])
    writer.writerow([dict_3[jai].keys()[0],dict_3[jai].values()[0]])
    writer.writerow([dict_3[jai1].keys()[0],dict_3[jai1].values()[0]])
    writer.writerow([dict_3[jai2].keys()[0],dict_3[jai2].values()[0]])
