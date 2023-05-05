'''Number of matches played per year for all the years in IPL.
Plot a bar chart.'''
import csv
import matplotlib.pyplot as plt
matches={}
with open('matches.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        season = row["season"]
        if season == season :
           matches[season]=matches.get(season,0)+1
matches=list(matches.items())
matches.sort(key=lambda x:x[1],reverse=True)
plt.bar([x[0] for x in matches],[x[1] for x in matches])
plt.xticks(rotation=90)
plt.xlabel('season')
plt.ylabel('total_matches')
plt.show()
        



