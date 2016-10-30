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
x = find_path(newpath)
dict_2 ={}
dict_3={}
countg = 0.0
countb = 0.0
counts = 0.0
for i in range(len(x)) :
	newpath1 = newpath + '//' + x[i]
	x1 = find_path(newpath1)
	for j in range(len(x1)) :
		with open(os.path.join(newpath1 , x1[j])) as f:
			data = json.load(f)
		for j1 in range(len(data['items'])) :
			user_id = data['items'][j1]['owner']['user_id']
			r = requests.get('https://api.stackexchange.com/2.2/users/{0}?key=q5*VT6u7xCuP)L7A*80abA((&order=desc&sort=modified&site=stackoverflow'.format(user_id))
			y  = r.json()
			a.append(user_id)
			for i in range(len(y['items'])) :
				d = y['items'][i]['badge_counts']
				countg = countg + d['gold']
				counts = counts + d['silver']
				countb = countb + d['bronze']
				dict_2[str(user_id)]=  (d)
				dict_3[str(user_id)] = str(y['items'][0]['display_name'])
dict_4 = {}
newpathoutput = cwd + '//' + 'output'
sum1 = countg + counts + countb
gold = countg/sum1*100
silver = counts/sum1*100
bronze = countb/sum1*100
for key, value in dict_2.iteritems() :
	gd = dict_2[str(key)]['gold']
	gs = dict_2[key]['silver']
	gb = dict_2[key]['bronze']
	dict_4[dict_3[key]] = [gd/countg*100, gs/counts*100, gb/countb*100]
print(dict_4)
with open(os.path.join(newpathoutput, args.search_term + 'badges_percentage.csv'), 'w') as csv_file: #Stores the analysed value in csv file.
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(["Total percentage of each badge : ","gold = "+ str(gold),"silver = " + str(silver), "bronze = " + str(bronze)])
    writer.writerow(["Name", "% of gold","% of silver", "% of bronze"])
for key1, value1 in dict_4.iteritems() :
	with open(os.path.join(newpathoutput, args.search_term + 'badges_percentage.csv'), 'a') as csv_file: #Stores the analysed value in csv file.
    		writer = csv.writer(csv_file,delimiter=',')
		writer.writerow([key1, dict_4[key1][0], dict_4[key1][1], dict_4[key1][2]])
  
