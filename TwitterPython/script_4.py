import requests
import json
import os
import sys
import argparse
import unicodedata
from datetime import datetime,date,timedelta
import glob
import numpy as np
import csv
cwd = os.getcwd()
newpath = cwd + "//" + 'twitter'
parser = argparse.ArgumentParser()
#parser.add_argument("--location", help="provide a location,state")
parser.add_argument("--search_term", help="provide a search term")
args = parser.parse_args()
#f = args.location
f1 = args.search_term
def find_path(newpath) :
	if not os.path.exists(newpath):
       		print('no file found')
	else :
		a = os.listdir(newpath)
		return a
x = find_path(newpath) 
newpath1 = newpath + "//" + str(f1)
x1 = find_path(newpath1)
dict_1 = {}
dict_2 = {}
#print(x1)
for j in range(len(x1)) :
	newpath2 = newpath1 + "//" + x1[j]
	x2 = find_path(newpath2)
	#print(x2)
	for s in range(len(x2)) :
		newpath3 = newpath2 + "//" + x2[s]
		x3 = find_path(newpath3)
		#print(x3)
		if any(".json" in s for s in x3):
			with open(os.path.join(newpath3 , x3[0])) as p:
				data = json.load(p)
			for i1 in range(len(data)) :
				a2 = data[i1]['user']['followers_count']*data[i1]['user']['friends_count']
				a3 = data[i1]['user']['statuses_count']
				dict_1[str(data[i1]['user']['screen_name'])] = a2
				dict_2[str(data[i1]['user']['screen_name'])] = a3
		else :
			for s2 in range(len(x3)) :
				newpath4 = newpath3 + '//' + x3[s2] 	
				x4 = find_path(newpath4)
				#print(x4)
			if any(".json" in s for s in x4):
				with open(os.path.join(newpath4 , x4[0])) as p:
					data = json.load(p)
				for i1 in range(len(data)) :
					a2 = data[i1]['user']['followers_count']*data[i1]['user']['friends_count']
					a3 = data[i1]['user']['statuses_count']
					dict_1[str(data[i1]['user']['screen_name'])] = a2
					dict_2[str(data[i1]['user']['screen_name'])] = a3
#print(dict_1,dict_2)
max_value1 = max(dict_1.values())
max_value2 = max(dict_2.values())
#print(max_value1, max_value2)
for key, value in dict_1.iteritems() :
	if value == max(dict_1.values()) :
		a4 = key
for key, value in dict_2.iteritems() :
	if value == max(dict_2.values()) :
		a5 = key
with open(f1 + '.csv', 'w') as csv_file:
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(["Data analysed for :" , f1])
    writer.writerow(["Most Popular user", a4, "count" , max_value1])
    writer.writerow(["Most active user" , a5, "No of statuses", max_value2])


