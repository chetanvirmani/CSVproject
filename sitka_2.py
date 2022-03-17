#using the datetime module
#adding dates to the x axis for the month of July 2018



import matplotlib.pyplot as plt
import csv
from datetime import datetime
from datetime import date


readFile = open("sitka_weather_07-2018_simple.csv","r")

csvFile = csv.reader(readFile, delimiter = ",")

headerRow = next(csvFile)

for index, columnHeader in enumerate (headerRow): #enumerate can be ran on any list object
    print (index, columnHeader)

highs = []
dates = []


for record in csvFile:
    highs.append(int(record[5]))
    current_date = datetime.strptime(record[2], "%Y-%m-%d")
    dates.append(current_date)


fig = plt.figure()

plt.plot(dates, highs, color = "red")

plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel("Month of July")
plt.ylabel("temperatures (F)", fontsize = 16)
plt.tick_params(axis="both", which = "major", labelsize = 16)

fig.autofmt_xdate()

plt.show()

