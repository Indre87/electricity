# Tämä on python-skripti, joka hakee sähköpörssin hinnan ja tallentaa sen JSON-muodossa
# tiedostoon data/data.json. Skriptiä voi ajaa komennolla python fetch.py
# Skriptiä voi ajaa myös ajastetusti esim. crontabilla. 

import datetime
import json
import time
import urllib.request
import os

url = "https://api.porssisahko.net/v1/price.json?date=2023-10-03&hour=19"
dirname = "data"
filename = "data.json"
filepath = os.path.join(dirname,filename)

if not os.path.exists(dirname):
    os.mkdir(dirname)

if not os.path.isfile(filepath):
    with open(filepath,'w') as file:
        file.close()

dt = datetime.datetime(2020, 1, 22)
end = datetime.date.today()
end = datetime.datetime(end.year, end.month, end.day)
step = datetime.timedelta(hours=24)
headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}
req = urllib.request.Request(url, headers=headers)

data_out = {}
with open(filepath, "r+") as file:
    try:
        data_out = json.load(file)
    except:
        print("No JSON data found")
    
    response = urllib.request.urlopen(req).read()
    print(response)
    data_in = json.loads(response)
    
    time.sleep(0.01)
    file.seek(0)
    file.write(json.dumps(data_in, sort_keys=True, 
               indent=4, separators=(',', ': ')))
    file.close()