'''Top batsman for Royal Challengers Bangalore
Consider only games played by Royal Challengers Bangalore. Now plot the total runs scored by top 10 batsman playing for Royal Challengers Bangalore over the history of IPL.

Plot only top 10 batsmen by runs scored in RCB.

'''


import csv
import matplotlib.pyplot as plt

total_runs = {}
with open('deliveries.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        team = row['batting_team']
        if team == 'Royal Challengers Bangalore':
           batsman=row['batsman']
           runs=int(row['total_runs'])
           total_runs[batsman]=total_runs.get(batsman,0)+runs
players=list(total_runs.items())
players.sort(key=lambda x:x[1],reverse=True)
players=players[:10]
plt.bar([x[0] for x in players],[x[1] for x in players])
plt.xticks(rotation=90)
plt.xlabel('player names')
plt.ylabel('score')
plt.show()
        


