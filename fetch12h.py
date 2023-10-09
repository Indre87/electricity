# Tämä on python-skripti, joka hakee sähköpörssin hinnan ja tallentaa sen JSON-muodossa
# tiedostoon data/data.json. Skriptiä voi ajaa komennolla python fetch.py
# Skriptiä voi ajaa myös ajastetusti esim. crontabilla. 

import datetime
import json
import time
import urllib.request
import os

hour = datetime.datetime.now()
date = datetime.datetime.today().strftime('%Y-%m-%d')

url_current = (f"https://api.porssisahko.net/v1/latest-prices.json")


print (url_current)

dirname = "data"
filename_current = "latest-prices.json"
filepath_current = os.path.join(dirname,filename_current)


if not os.path.exists(dirname):
    os.mkdir(dirname)

if not os.path.isfile(filepath_current):
    with open(filepath_current,'w') as file:
        file.close()


headers={'Content-Type': 'application/json', 'Accept': 'application/json', 'User-Agent': 'Mozilla/5.0'}

# Current hour

req_current = urllib.request.Request(url_current, headers=headers)

with open(filepath_current, "w") as file:
    
    response = urllib.request.urlopen(req_current).read()
    print(response)
    data_in = json.loads(response)
    
    time.sleep(0.01)
    file.seek(0)
    file.write(json.dumps(data_in))
    file.close()
