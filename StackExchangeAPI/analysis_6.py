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
	#print(x1)
	for j in range(len(x1)) :
		with open(os.path.join(newpath1 , x1[j])) as f:
			data = json.load(f)
		for j1 in range(len(data['items'])) :
			if data['items'][j1]['owner']['user_type'] == 'registered' :
				user_id = data['items'][j1]['owner']['user_id']
				r1 = requests.get('https://api.stackexchange.com/2.2/users/{0}/answers?((&order=desc&sort=activity&site=stackoverflow'.format(user_id))
				y1 = r1.json()
			#print (y1)
				dict_2[str(user_id)] = {str(data['items'][j1]['owner']['display_name']) : len(y1['items'])}
			#print(y1['items'])
			#print(len(y1['items']))
				if (len(y1['items']) == 0) :
					answer_count = 0
					dict_3[str(user_id)] = answer_count
				else : 
					answer_count = 0
					for j2 in range (len(y1['items'])) :
						#print(y1['items'][j2]['is_accepted'])	
						if ((y1['items'][j2]['is_accepted']) == True) :
							answer_count = answer_count + 1
							dict_3[str(user_id)] = answer_count
						else :
							answer_count = 0
							dict_3[str(user_id)] = answer_count
				#print (y1['items'][j2])
					#print(dict_3)
#print(len(dict_3))
#print(dict_2)
#print(len(dict_2))
with open(os.path.join(newpathoutput, args.search_term + 'user_id_answers.csv'), 'w') as csv_file: #Stores the analysed value in csv file.
	writer = csv.writer(csv_file,delimiter=',')
	writer.writerow(["Name","No of Answers","Number of Correct Answers"])
for key, value in dict_2.iteritems() :
	with open(os.path.join(newpathoutput, args.search_term + 'user_id_answers.csv'), 'a') as csv_file: #Stores the analysed value in csv file.
				writer = csv.writer(csv_file,delimiter=',')
				writer.writerow([dict_2[key].keys()[0],dict_2[key].values()[0],dict_3[key]])
