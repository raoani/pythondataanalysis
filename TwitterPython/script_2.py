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
cwd = os.getcwd()
newpath = cwd + "//" + 'twitter'
def find_path(newpath) : #searches for a particular path and lists the directories in that path
	if not os.path.exists(newpath):
       		print('no file found')
	else :
		a = os.listdir(newpath)
		return a
z = []
dict_1 = {}
x = find_path(newpath)
print(x)
for i in range(len(x)) : 
	newpath1 = newpath + "//" + x[i] 
	x1 = find_path(newpath1)
	#print(x1)
	for j in range(len(x1)) :
		newpath2 = newpath1 + "//" + x1[j]
		x2 = find_path(newpath2)
		#print(x2)
		for k in range(len(x2)) :
			newpath3 = newpath2 + "//" + x2[k]
			x3 = find_path(newpath3)
			if any(".json" in s for s in x3):
				with open(os.path.join(newpath3 , x3[0])) as f:
					data = json.load(f)
				for e in range (len(data)) :
					d = data[e][u"source"]
					z.append(d)
			else :
				for s2 in range(len(x3)) :
					newpath4 = newpath3 + '//' + x3[s2] 	
					x4 = find_path(newpath4)
				#print(x4)
					if any(".json" in s1 for s1 in x4):
						with open(os.path.join(newpath4 , x4[0])) as p:
							data = json.load(p)
						for e1 in range (len(data)) :
							d = data[e1][u"source"] #searcher for source
							z.append(d)# stores it in a list
names = np.array(z)
o = np.unique(names)#stores unique sources
lst1 = []
lst2 = []
sum1 = 0.0
sum2 = 0.0
percentage = 0.0
a2 = ""
a3 = ''
for w in range(len(o)) : #counts the number of each sources
	count = 0
	for p in range(len(z)) :
		if z[p] == o[w] :
			count = count + 1
	dict_1[o[w]] = count
lst2 = dict_1.values() 
sum1 = float(sum(lst2))
sum2 = float(max(lst2)) #maximum source
percentage = sum2/sum1*100 #finds the percentage of maximum source 
for key, value in dict_1.iteritems() :
	if value == max(dict_1.values()) :
		a1 = key #searches for the source name
a1 = str(a1)
a2 = re.match( r'(<[ \w \W]*">)([\w\s]*)', a1)
a3 = a2.group(2) #source name will be in unicode, group(2) has just the source name
with open('Source.csv', 'w') as csv_file: #Stores the analysed value in csv file.
    writer = csv.writer(csv_file,delimiter=',')
    writer.writerow(["Number of Unique sources",len(o)])
    writer.writerow(["Max no of times the is source used to tweet" , max(dict_1.values()), "Source", a3])
    writer.writerow(["Percentage of tweets from the source", percentage])
					
	
