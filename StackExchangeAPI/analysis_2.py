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
newpathoutput = cwd + '//' + 'output'
def find_path(newpath) : #searches for a particular path and lists the directories in that path
	if not os.path.exists(newpath):
       		print('no file found')
	else :
		a = os.listdir(newpath)
		return a
newpath = cwd + '//' + 'stackoverflow' + '//' + args.search_term
lst1 = []
x = find_path(newpath)
dict_2 ={}
dict_3 ={}
#print(x)
for i in range(len(x)) :
	newpath1 = newpath + '//' + x[i]
	x1 = find_path(newpath1)
	print(x1)
	for j in range(len(x1)) :
		with open(os.path.join(newpath1 , x1[j])) as f:
			data = json.load(f)
		for j1 in range(len(data['items'])) :
			if data['items'][j1]['owner']['user_type'] == 'registered' :
				user_id = data['items'][j1]['owner']['user_id']
				r = requests.get('https://api.stackexchange.com/2.2/users/{0}?key=q5*VT6u7xCuP)L7A*80abA((&order=desc&sort=modified&site=stackoverflow'.format(user_id))
				y  = r.json()
				dict_3[str(user_id)] = {str(y['items'][0]['display_name']) : str(y['items'][0]['link'])}
				dict_2[str(user_id)] = y['items'][0]['reputation']
				a.append(user_id)
#print(len(a))
#print(a)
with open(os.path.join(newpathoutput, args.search_term + 'reputation.csv'), 'w') as csv_file: #Stores the analysed value in csv file.
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow([" Questions according to Reputation "])
lst1 = sorted(dict_2.values(),reverse=True)
#print(lst1)
for i1 in range(len(lst1)) :
	for key , value in dict_2.iteritems() :
		if value == lst1[i1] :
			jai = key
			with open(os.path.join(newpathoutput, args.search_term + 'reputation.csv'), 'a') as csv_file: #Stores the analysed value in csv file.
				writer = csv.writer(csv_file,delimiter=',')
    				writer.writerow([dict_3[key].keys()[0],dict_3[key].values()[0],dict_2[key]])
    
