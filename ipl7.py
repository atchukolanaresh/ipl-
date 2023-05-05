''''Extra runs conceded per team in the year 2016
Plot a bar chart.'''
import csv
import matplotlib.pyplot as plt
team_runs = {}
with open('matches.csv') as  matches:
    reader=csv.DictReader(matches)
    for row in reader:
        if row['season']== '2016':
            team_runs[row['winner']]=team_runs.get(row['winner'],0)+int(row['win_by_runs'])
    plt.bar(team_runs.keys(),team_runs.values())
    plt.xticks(rotation=90)
    plt.title('total exceded runs in 2016')
    plt.xlabel('team names')
    plt.ylabel('exceeded runs')
    plt.show()

