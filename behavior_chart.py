from random import *
import csv
from statistics import mean
import matplotlib.pyplot as plt
x = []
y = []
with open('behavior.csv') as infile:
    reader = csv.reader(infile)
    for row in reader:
        x.append(row[0])
        y.append(int(row[1]))
print(x)
print(y)
print(mean(y))
plt.figure(1)
plt.bar(x,y,color='g', width=0.72,  label='Checkmarks')
plt.xlabel('Time (24H Format)')
plt.ylabel('Checkmarks')
plt.title('Performance Throughout the Day over 10 Days')
plt.legend()
plt.figure(2)
x = []
y = []
gym = []
with open('progress.csv') as infile:
    reader = csv.reader(infile)
    for row in reader:
        x.append(row[0])
        y.append(int(row[1]))
        gym.append(int(row[2]))
print(x,y)
barlist = plt.bar(x,y,color='r', width=0.72, label='Checkmarks')
plt.xlabel('Date')
plt.ylabel('Checkmarks')
plt.title('Performance over the 10 days')
for i in range(len(barlist)):
    if gym[i] ==1: barlist[i].set_color('g')

plt.show()


