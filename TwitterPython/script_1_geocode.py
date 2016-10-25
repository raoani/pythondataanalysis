import requests
import json
import os
import sys
import argparse
from datetime import datetime,date,timedelta
from requests_oauthlib import OAuth1
from geopy.geocoders import Nominatim
import geocoder
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('PozqKlpn6dpxJ2qR1Mgc2VDov', 'NAuyMFdsKTGDb3WQ8NoYo4S1ExeeGgh9KR5n27VCMHv6FUH3V0',
                  '84084965-Of9l5EGjcPar9mcHBNhPzlK3Mx4GktMo85WfjZPbL', 'LS8S3jaT9RhiCprzZfxWUDvjGwnSTdfEiXbVDmczCND3Y')
requests.get(url, auth=auth)
parser = argparse.ArgumentParser()
parser.add_argument("--search_term", help="provide a search term, latitude, longitude and radius")
parser.add_argument("--location", help="provide a search term, latitude, longitude and radius")
args = parser.parse_args()
cnt = 100
g = geocoder.google(args.location)
a = g.latlng
x = { "q" : args.search_term, "geocode" : str(a[0])+','+str(a[1])+ ",100mi" , "count" : cnt }
def creating_newpath(newpath,x) :
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        newpath1 = newpath + "//" + x
        return newpath1
    else :
        newpath1 = newpath + "//" + x
        return newpath1

#Same as script_1.py but also accepts a location term
z = datetime.now().date()
z = str(z)
e = datetime.now().time()
e = str(e)
m = x['q']
n =  args.location
cwd = os.getcwd()
newpath = cwd + "//" + 'twitter'
newpath1 = creating_newpath(newpath, m)
newpath2 = creating_newpath(newpath1,z)#creates a directory with location name
newpath3 = creating_newpath(newpath2,n)
newpath4 = creating_newpath(newpath3,e)
newpath5 = creating_newpath(newpath4,e)

r = requests.get('https://api.twitter.com/1.1/search/tweets.json?', auth=auth, params = x)
a = r.json()
y = a['statuses']
with open(os.path.join(newpath4 ,'tweetsof' + x['q'] + '.json'), "a") as f:
	json.dump(y, f)
        f.close()
print(r.url)    
