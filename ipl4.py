''' Stacked chart of matches played by team by season
Plot a stacked bar chart of ...

number of games played
by team
by season'''



import csv
import matplotlib.pyplot as plt

# Load the data into a list of dictionaries
with open('matches.csv', 'r') as file:
    reader = csv.DictReader(file)
    matches = [row for row in reader]

# Group the data by season and team, and count the number of matches played by each team in each season
matches_played = {}
for match in matches:
    season = match['season']
    team1 = match['team1']
    team2 = match['team2']
    if season not in matches_played:
        matches_played[season] = {}
    if team1 not in matches_played[season]:
        matches_played[season][team1] = 0
    if team2 not in matches_played[season]:
        matches_played[season][team2] = 0
    matches_played[season][team1] += 1
    matches_played[season][team2] += 1
#print(matches_played)

# Create a pivot table with the number of matches played by each team in each season
teams = set([team for season in matches_played for team in matches_played[season]])
matches_played_pivot = []
for season in matches_played:
    row = {'season': season}
    for team in teams:
        if team in matches_played[season]:
            row[team] = matches_played[season][team]
        else:
            row[team] = 0
    matches_played_pivot.append(row)
# Create a stacked bar chart using the pivot table
fig, ax = plt.subplots(figsize=(12,6))
bottom = [0] * len(matches_played_pivot)
for team in teams:
    values = [row[team] for row in matches_played_pivot]
    ax.bar([row['season'] for row in matches_played_pivot], values, bottom=bottom, label=team)
    bottom = [b+v for b,v in zip(bottom, values)]

# Add labels and title
ax.set_xlabel('Season')
ax.set_ylabel('Number of Matches Played')
ax.set_title('Number of Matches Played by Team by Season')
ax.legend()

# Show the plot
plt.show()

