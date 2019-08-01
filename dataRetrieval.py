# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 16:20:54 2019

@author: Praveen
"""
import pytz,datetime

import csv
import json
import time
import requests 

token= 'Rj9LEtwnmFfparBkSq3coy7l'
sensor_1= '5139'
sensor_2= '3246'
local = pytz.timezone ("America/Los_Angeles")
strt=input("Enter Start Date and Time(yyyy-m-d hh:mm:ss)")
endt=input("Enter End Date and Time(yyyy-m-d hh:mm:ss)")
#strt="2019-5-17 09:10:10"
#endt="2019-5-20 19:10:10"
naiveS = datetime.datetime.strptime (strt, "%Y-%m-%d %H:%M:%S")
naiveE = datetime.datetime.strptime (endt, "%Y-%m-%d %H:%M:%S")
local_S = local.localize(naiveS, is_dst=None)
utc_SS = local_S.astimezone(pytz.utc)
utc_S1=str(utc_SS.timestamp())
utc_S=str(int(float(utc_S1)))

local_E = local.localize(naiveE, is_dst=None)
utc_EE = local_E.astimezone(pytz.utc)
utc_E1=str(utc_EE.timestamp())
utc_E=str(int(float(utc_E1)))
print('utc_S='+utc_S)
print('utc_E='+utc_E)

site1='https://api.plumelabs.com/2.0/organizations/6/sensors/measures?sensor_id='+sensor_1+'&token='+token+'&start_date='+utc_S+'&end_date='+utc_E
site2='https://api.plumelabs.com/2.0/organizations/6/sensors/measures?sensor_id='+sensor_2+'&token='+token+'&start_date='+utc_S+'&end_date='+utc_E

site3='https://api.plumelabs.com/2.0/organizations/6/sensors/positions?sensor_id='+sensor_1+'&token='+token+'&start_date='+utc_S+'&end_date='+utc_E
site4='https://api.plumelabs.com/2.0/organizations/6/sensors/positions?sensor_id='+sensor_2+'&token='+token+'&start_date='+utc_S+'&end_date='+utc_E

#print('Site='+site)
print('Downloading..')
# URL of the image to be downloaded is defined as image_url 
r1 = requests.get(site1) # create HTTP response object 
r2 = requests.get(site2) # create HTTP response object 

r3 = requests.get(site3) # create HTTP response object 
r4 = requests.get(site4) # create HTTP response object 
  
# send a HTTP request to the server and save 
# the HTTP response in a response object called r 
with open("Flow1_Raw_Data.txt",'wb') as f: 
  
    # Saving received content as a png file in 
    # binary format 
  
    # write the contents of the response (r.content) 
    # to a new file in binary mode. 
    f.write(r1.content)
with open("Flow2_Raw_Data.txt",'wb') as f: 
    f.write(r2.content)

with open("Flow1_GPS_Raw_Data.txt",'wb') as f: 
    f.write(r3.content)

with open("Flow2_GPS_Raw_Data.txt",'wb') as f: 
    f.write(r4.content)
#x=[{"pollutants":{"no2":{"value":135.13,"pi":113.51},"voc":{"value":147,"pi":11.76},"pm25":{"value":23.58,"pi":47.16},"pm10":{"value":73.89,"pi":89.81}},"date":1558067210},{"pollutants":{"no2":{"value":150.9,"pi":120.92},"voc":{"value":122,"pi":9.76},"pm25":{"value":22.21,"pi":44.43},"pm10":{"value":97.76,"pi":111.1}},"date":1558067270}]
f1=open("Flow1_Raw_Data.txt",'r')
f2=open("Flow2_Raw_Data.txt",'r')

f3=open("Flow1_GPS_Raw_Data.txt",'r')
f4=open("Flow2_GPS_Raw_Data.txt",'r')


x1=f1.read()
x2=f2.read()
x3=f3.read()
x4=f4.read()

x1=str(x1[12:])
x1=x1[:-40]  #Change the value if Extra Data Error encountered.. 40 for more data 27 for less data
x1 = x1.replace("'", '"')

x2=str(x2[12:])
x2=x2[:-41]  #Change the value if Extra Data Error encountered.. 40 for more data 27 for less data
x2 = x2.replace("'", '"')

x3=str(x3[13:])
x3=x3[:-27]  #Change the value if Extra Data Error encountered.. 40 for more data 27 for less data
x3 = x3.replace("'", '"')

x4=str(x4[13:])
x4=x4[:-40]  #Change the value if Extra Data Error encountered.. 40 for more data 27 for less data
x4 = x4.replace("'", '"')

x1 = json.loads(x1)
x2 = json.loads(x2)
x3 = json.loads(x3)
x4 = json.loads(x4)

f1 = csv.writer(open("Flow1_Data.csv","w+", newline=""), delimiter=",")
f2 = csv.writer(open("Flow2_Data.csv","w+", newline=""), delimiter=",")
f3 = csv.writer(open("Flow1_GPS_Data.csv","w+", newline=""), delimiter=",")
f4 = csv.writer(open("Flow2_GPS_Data.csv","w+", newline=""), delimiter=",")

#f = csv.writer(open("Flow_Data.csv", "w+"))
print('Saving..')
# Write CSV Header, If you dont need that, remove this line
f1.writerow(["Datetime", "PM2.5(ug/m3)", "PM10(ug/m3)", "NO2(ppb)", "VOC(ppb)"])
f2.writerow(["Datetime", "PM2.5(ug/m3)", "PM10(ug/m3)", "NO2(ppb)", "VOC(ppb)"])
for x1 in x1:
    f1.writerow([time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(int(x1["date"])-19800)),
                x1["pollutants"]["pm25"]["value"],
                x1["pollutants"]["pm10"]["value"],
                x1["pollutants"]["no2"]["value"],
                x1["pollutants"]["voc"]["value"]])
    
for x2 in x2:
    f2.writerow([time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(int(x2["date"])-19800)),
                x2["pollutants"]["pm25"]["value"],
                x2["pollutants"]["pm10"]["value"],
                x2["pollutants"]["no2"]["value"],
                x2["pollutants"]["voc"]["value"]])
    
f3.writerow(["Datetime", "Horizontal_accuracy", "Longitude", "Latitude"])
f4.writerow(["Datetime", "Horizontal_accuracy", "Longitude", "Latitude"])
for x3 in x3:
    f3.writerow([time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(int(x3["date"])-19800)),
                x3["horizontal_accuracy"],
                x3["longitude"],
                x3["latitude"]])

for x4 in x4:
    f4.writerow([time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(int(x4["date"])-19800)),
                x4["horizontal_accuracy"],
                x4["longitude"],
                x4["latitude"]])

print('Done!!')