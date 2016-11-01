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
newpathoutput = cwd + '//' + 'output'
for i in range(len(x)) :
	newpath1 = newpath + '//' + x[i]
	x1 = find_path(newpath1)
	for j in range(len(x1)) :
		with open(os.path.join(newpath1 , x1[j])) as f:
			data = json.load(f)
		for j1 in range(len(data['items'])) :
			if data['items'][j1]['owner']['user_type'] == 'registered' :
				user_id = data['items'][j1]['owner']['user_id']
				dict_3[str(user_id)] = str(data['items'][j1]['title']) 	
				if data['items'][j1]['is_answered'] == True :
					question_id = data['items'][j1]['question_id']
					r = requests.get('https://api.stackexchange.com/2.2/questions/{0}/answers?key=q5*VT6u7xCuP)L7A*80abA((&order=desc&sort=activity&site=stackoverflow'.format(question_id))
					y  = r.json()
					for j2 in range(len(y['items'])) :
					 	if y['items'][j2]["is_accepted"] == True :
							dict_2[str(user_id)] = {y['items'][j2]['owner']['display_name'] : y['items'][j2]['score'] }
with open(os.path.join(newpathoutput, args.search_term + 'answers_id.csv'), 'w') as csv_file: #Stores the analysed value in csv file.
			writer = csv.writer(csv_file,delimiter=',')
    			writer.writerow(["Question","Answered By","Score"])
for key, value in dict_2.iteritems() :
	with open(os.path.join(newpathoutput, args.search_term + 'answers_id.csv'), 'a') as csv_file: #Stores the analysed value in csv file.
				writer = csv.writer(csv_file,delimiter=',')
    				writer.writerow([dict_3[key],dict_2[key].keys()[0],dict_2[key].values()[0]])

