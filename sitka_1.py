import matplotlib.pyplot as plt
import csv

readFile = open("sitka_weather_07-2018_simple.csv","r")

csvFile = csv.reader(readFile, delimiter = ",")

headerRow = next(csvFile)

for index, columnHeader in enumerate (headerRow): #enumerate can be ran on any list object
    print (index, columnHeader)

highs = []

for record in csvFile:
    highs.append(int(record[5]))

print (highs)


plt.plot(highs, color = "red")

plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel("")
plt.ylabel("temperatures (F)", fontsize = 16)
plt.tick_params(axis="both", which = "major", labelsize = 16)

plt.show()