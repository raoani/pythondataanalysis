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
parser.add_argument("--location", help="provide a location,state")
parser.add_argument("--search_term", help="provide a search term")
args = parser.parse_args()
f = args.location
f1 = args.search_term
def find_path(newpath) :
	if not os.path.exists(newpath):
       		print('no file found')
	else :
		a = os.listdir(newpath)
		return a
#similar to script_2.py 
dict_1 = {}
x = find_path(newpath) 
newpath1 = newpath + "//" + str(f1)
x1 = find_path(newpath1)
for j in range(len(x1)) :
	newpath2 = newpath1 + "//" + x1[j]
	x2 = find_path(newpath2)
	for s in range(len(x2)) :
		if x2[s] == f :
			newpath3 = newpath2 + "//" + f
			x3 = find_path(newpath3)
			for k in range(len(x3)) :
				newpath4 = newpath3 + "//" + x3[k]
				x4 = find_path(newpath4)
				#print(x4)
				if any(".json" in s for s in x4):
					with open(os.path.join(newpath4 , x4[0])) as p:
						data = json.load(p)
					for i in range(len(data)) : #checks if the tweet is a retweeted tweet or not
						if 'retweeted_status' in data[i].keys() : 
							m = (data[i]['retweeted_status']['user']['screen_name'])#stores the user's name
							dict_1[str(m)] = { "followers_count" : data[i]['retweeted_status']['user']['followers_count'], "No of Retweets" : data[i]['retweeted_status']['retweet_count'] }#Creates a dictionary with no of retweets and the number of followers they have
with open(f + f1 + '.csv', 'w') as csv_file:
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(["Data Analysed for : ", "Location : ", f, "Search term: ", f1])
    writer.writerow(["Names" , "Followers count" , "Retweeted Count"])
    dict1_values = dict_1.values()
    dict1_keys = dict_1.keys()
    for a1 in range(len(dict1_values)) :
       		writer.writerow([dict1_keys[a1] , str(dict1_values[a1]['followers_count']) , str(dict1_values[a1]['No of Retweets'])]) 
dvalues = dict_1.values()
lst_1 = []
tmp = 0
max_list = 0
name = {}
for cnt in range(len(dict_1.values())) :
	tmp = dvalues[cnt]['No of Retweets']
	lst_1.append(int(tmp))
max_list = max(lst_1)
for cnt1 in range(len(dvalues)) :
	tmp1 = dvalues[cnt1]['No of Retweets']
	if int(tmp1) == max_list :
		name = dvalues[cnt1]
for key, value in dict_1.iteritems() :
	if value == name :
		o = key
with open(f + f1  + '.csv', 'a') as csv_file:
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(["Names" , o , "Max number of retweets", max_list])

	



