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
#newpathuid = cwd + '//' + 'stackoverflow' + '//' + 'user_id_' + args.search_term
x = find_path(newpath)
dict_2 ={}
dict_3={}
for i in range(len(x)) :
	newpath1 = newpath + '//' + x[i]
	x1 = find_path(newpath1)
	for j in range(len(x1)) :
		with open(os.path.join(newpath1 , x1[j])) as f:
			data = json.load(f)
		for j1 in range(len(data['items'])) :
			user_id = data['items'][j1]['owner']['user_id']
			s  = data['items'][j1]['tags']
			dict_3[str(data['items'][j1]['title'])] = str(s)
			s1 = data['items'][j1]['answer_count']
			dict_2[str(data['items'][j1]['title'])] = str(s1) 	
			for j2 in range(len(s)) :
				a.append(s[j2])
print(a)
print(len(a))

