
from multiprocessing.sharedctypes import Value
import matplotlib.pyplot as plt
import csv
from datetime import datetime

readFileSitka = open("sitka_weather_2018_simple.csv","r")

csvFileSitka = csv.reader(readFileSitka, delimiter = ",")

readFileDeathValley = open("death_valley_2018_simple.csv","r")

csvFileDeathValley = csv.reader(readFileDeathValley, delimiter = ",")

headerRow = next(csvFileSitka)
headerRowDV = next(csvFileDeathValley)

for index, columnHeader in enumerate (headerRow):
    if columnHeader == "TMIN":
        tempMin = index
    if columnHeader == "TMAX":
        tempMax = index


highs = []
dates = []
lows = []


for record in csvFileSitka:
    lows.append(int(record[tempMin]))
    highs.append(int(record[tempMax]))
    currentDate = datetime.strptime(record[2], "%Y-%m-%d")
    dates.append(currentDate)
    nameSitka = record[1]


highsDV = []
datesDV = []
lowsDV = []

for index, columnHeader in enumerate (headerRowDV):
    if columnHeader == "TMIN":
        tempMin = index
    if columnHeader == "TMAX":
        tempMax = index

for record in csvFileDeathValley:
    try:
        high = int(record[tempMax])
        low = int(record[tempMin])
        currentDateDV = datetime.strptime(record[2], "%Y-%m-%d")
    
    except ValueError:
        print (f"Missing data for {currentDateDV}")
    
    else:
        highsDV.append(high)
        lowsDV.append(low)
        datesDV.append(currentDateDV)
        nameDV = record[1]


fig = plt.figure()

plt.subplot(2,1,1)
plt.plot(dates, highs, color = "red")
plt.plot(dates, lows, color = "green")

plt.fill_between(dates,highs,lows, facecolor = "green", alpha=0.1)

plt.title(nameSitka)

plt.subplot(2,1,2)
plt.plot(datesDV, highsDV, color = "red")
plt.plot(datesDV, lowsDV, color = "green")

plt.fill_between(datesDV,highsDV,lowsDV, facecolor = "green", alpha=0.1)

plt.title(nameDV)

fig.autofmt_xdate()

plt.suptitle("Temperature Comparison between "+nameSitka+" and "+nameDV)

plt.show()



