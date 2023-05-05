'''Number of matches won per team per year in IPL.
Plot a stacked bar chart.'''
import csv
import matplotlib.pyplot as plt

# Load the data into a list of dictionaries
with open('matches.csv', 'r') as file:
    reader = csv.DictReader(file)
    matches = [row for row in reader]

# Group the data by season and team, and count the number of matches won by each team in each season
matches_won = {}
for match in matches:
    season = match['season']
    winner = match['winner']
    if season not in matches_won:
        matches_won[season] = {}
    if winner not in matches_won[season]:
        matches_won[season][winner] = 0
    matches_won[season][winner] += 1

# Create a pivot table with the number of matches won by each team in each season
teams = set([team for season in matches_won for team in matches_won[season]])
matches_won_pivot = []
for season in matches_won:
    row = {'season': season}
    for team in teams:
        if team in matches_won[season]:
            row[team] = matches_won[season][team]
        else:
            row[team] = 0
    matches_won_pivot.append(row)

# Create a stacked bar chart using the pivot table
fig, ax = plt.subplots(figsize=(12,6))
bottom = [0] * len(matches_won_pivot)
for team in teams:
    values = [row[team] for row in matches_won_pivot]
    ax.bar([row['season'] for row in matches_won_pivot], values, bottom=bottom, label=team)
    bottom = [b+v for b,v in zip(bottom, values)]

# Add labels and title
ax.set_xlabel('Season')
ax.set_ylabel('Number of Matches Won')
ax.set_title('Number of Matches Won by Team by Season')
ax.legend()

# Show the plot
plt.show()
