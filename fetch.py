# Tämä on python-skripti, joka hakee sähköpörssin hinnan ja tallentaa sen JSON-muodossa
# tiedostoon data/data.json. Skriptiä voi ajaa komennolla python fetch.py
# Skriptiä voi ajaa myös ajastetusti esim. crontabilla. 

import datetime
import json
import time
import urllib.request
import os


hour = datetime.datetime.now().hour
date = datetime.date.today()
 
url_current = "https://api.porssisahko.net/v1/price.json?date=2023-10-03&hour=20"
url_next = "https://api.porssisahko.net/v1/price.json?date=2023-10-03&hour=21"

dirname = "data"
filename_current = "current.json"
filename_next = "next.json"
filepath_current = os.path.join(dirname,filename_current)
filepath_next = os.path.join(dirname,filename_next)

if not os.path.exists(dirname):
    os.mkdir(dirname)

if not os.path.isfile(filepath_current):
    with open(filepath_current,'w') as file:
        file.close()

if not os.path.isfile(filepath_next):
    with open(filepath_next,'w') as file:
        file.close()


headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}

req_current = urllib.request.Request(url_current, headers=headers)
data_out = {}
with open(filepath_current, "r+") as file:
    try:
        data_out = json.load(file)
    except:
        print("No JSON data found")
    
    response = urllib.request.urlopen(req_current).read()
    print(response)
    data_in = json.loads(response)
    
    time.sleep(0.01)
    file.seek(0)
    file.write(json.dumps(data_in, sort_keys=True, 
               indent=4, separators=(',', ': ')))
    file.close()

req_next = urllib.request.Request(url_next, headers=headers)
data_out = {}
with open(filepath_next, "r+") as file:
    try:
        data_out = json.load(file)
    except:
        print("No JSON data found")
    
    response = urllib.request.urlopen(req_next).read()
    print(response)
    data_in = json.loads(response)
    
    time.sleep(0.01)
    file.seek(0)
    file.write(json.dumps(data_in, sort_keys=True, 
               indent=4, separators=(',', ': ')))
    file.close()