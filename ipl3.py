'''Foreign umpire analysis
Obtain a source for country of origin of umpires. Plot a chart of number of umpires by in IPL by country. Indian umpires should be ignored as this would dominate the graph.'''


import csv
import matplotlib.pyplot as plt
total_umpires={}
with open('umpires.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        country = row[" country"]
        if country != ' India':
           total_umpires[country]=total_umpires.get(country,0)+1
umpires=list(total_umpires.items())
umpires.sort(key=lambda x:x[1],reverse=True)
plt.bar([x[0] for x in umpires],[x[1] for x in umpires])
plt.xticks(rotation=90)
plt.xlabel('umpire country')
plt.ylabel('total')
plt.show()
        



