
import matplotlib.pyplot as plt
import csv
from datetime import datetime



readFile = open("sitka_weather_2018_simple.csv","r")

csvFile = csv.reader(readFile, delimiter = ",")

headerRow = next(csvFile)

for index, columnHeader in enumerate (headerRow): #enumerate can be ran on any list object
    print (index, columnHeader)

highs = []
dates = []
lows = []

"""  
testDate = datetime.strptime("1997/10/16", "%Y-%m-%d")
test2 = date("1997/10/16")
"""

for record in csvFile:
    lows.append(int(record[6]))
    highs.append(int(record[5]))
    current_date = datetime.strptime(record[2], "%Y-%m-%d")
    dates.append(current_date)



fig = plt.figure()

plt.plot(dates, highs, color = "red")
plt.plot(dates, lows, color = "green")

plt.fill_between(dates,highs,lows, facecolor = "green", alpha=0.1)

plt.title("Daily low and high temperatures, July 2018", fontsize = 16)
plt.xlabel("Month of July")
plt.ylabel("temperatures (F)", fontsize = 16)
plt.tick_params(axis="both", which = "major", labelsize = 16)

fig.autofmt_xdate()

plt.show()



plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2) #The first one is the top one, and the 3rd is the one that we are working with
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaskas 2018")

plt.show()
