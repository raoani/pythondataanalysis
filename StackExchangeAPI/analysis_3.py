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
x = find_path(newpath)
dict_2 ={}
dict_3 ={}
print(x)
for i in range(len(x)) :
	newpath1 = newpath + '//' + x[i]
	x1 = find_path(newpath1)
	print(x1)
	for j in range(len(x1)) :
		with open(os.path.join(newpath1 , x1[j])) as f:
			data = json.load(f)
		for j1 in range(len(data['items'])) :
			user_id = data['items'][j1]['owner']['user_id']
			r = requests.get('https://api.stackexchange.com/2.2/users/{0}/tags?key=q5*VT6u7xCuP)L7A*80abA((&order=desc&site=stackoverflow'.format(user_id))
			y  = r.json()
			lst1 = []
			for j2 in range(len(y['items'])) :
				jai = str(y['items'][j2]['name'])
				lst1.append(jai)
				dict_3[str(user_id)] = lst1
			r1 = requests.get('https://api.stackexchange.com/2.2/users/{0}?key=q5*VT6u7xCuP)L7A*80abA((&order=desc&site=stackoverflow'.format(user_id))
			y1 = r1.json()
			dict_2[str(user_id)] = {str(y1['items'][0]['display_name']) : str(y1['items'][0]['link'])}
			a.append(user_id)
print(dict_3)
print(dict_2)
