# Tämä on python-skripti, joka hakee sähköpörssin hinnan ja tallentaa sen JSON-muodossa
# tiedostoon data/data.json. Skriptiä voi ajaa komennolla python fetch.py
# Skriptiä voi ajaa myös ajastetusti esim. crontabilla. 

import datetime
import json
import time
import urllib.request
import os



hour = datetime.datetime.now().hour
date = datetime.datetime.today().strftime('%Y-%m-%d')

url_current = (f"https://api.porssisahko.net/v1/price.json?date={date}&hour={hour}")
url_next = (f"https://api.porssisahko.net/v1/price.json?date={date}&hour={hour+1}")
url_next2 = (f"https://api.porssisahko.net/v1/price.json?date={date}&hour={hour+2}")

print (url_current)
print(url_next)
print(url_next2)

dirname = "data"
filename_current = "current.json"
filename_next = "next.json"
filename_next2 = "next2.json"
filepath_current = os.path.join(dirname,filename_current)
filepath_next = os.path.join(dirname,filename_next)
filepath_next2 = os.path.join(dirname,filename_next2)

if not os.path.exists(dirname):
    os.mkdir(dirname)

if not os.path.isfile(filepath_current):
    with open(filepath_current,'w') as file:
        file.close()

if not os.path.isfile(filepath_next):
    with open(filepath_next,'w') as file:
        file.close()

if not os.path.isfile(filepath_next2):
    with open(filepath_next2,'w') as file:
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

# Next hour 

req_next = urllib.request.Request(url_next, headers=headers)

with open(filepath_next, "w") as file:
    
    response = urllib.request.urlopen(req_next).read()
    print(response)
    data_in = json.loads(response)
    
    time.sleep(0.01)
    file.seek(0)
    file.write(json.dumps(data_in))
    file.close()

# Third hour

req_next2 = urllib.request.Request(url_next2, headers=headers)

with open(filepath_next2, "w") as file:
    
    response = urllib.request.urlopen(req_next2).read()
    print(response)
    data_in = json.loads(response)
    
    time.sleep(0.01)
    file.seek(0)
    file.write(json.dumps(data_in))
    file.close()    