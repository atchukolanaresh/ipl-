'''Top 10 economical bowlers in the year 2015
Plot a bar chart.'''
import csv
import matplotlib.pyplot as plt

# Step 1: Read the matches dataset
with open('matches.csv') as f:
    matches = list(csv.DictReader(f))

# Step 2: Read the deliveries dataset
with open('deliveries.csv') as f:
    deliveries = list(csv.DictReader(f))

# Step 3: Join the datasets based on match_id
joined_data = []
for match in matches:
    match_id = match['id']
    match_deliveries = [delivery for delivery in deliveries if delivery['match_id'] == match_id]
    for delivery in match_deliveries:
        joined_data.append({**match, **delivery})

# Step 4: Filter the joined dataset to include only matches played in 2015 and only consider the bowling team that had completed at least 5 innings
filtered_data = [row for row in joined_data if row['season'] == '2015' and row['is_super_over'] == '0' and row['inning'] == '2']
inning_counts = {}
for row in filtered_data:
    team = row['bowling_team']
    if team not in inning_counts:
        inning_counts[team] = set()
    inning_counts[team].add(row['match_id'])
bowling_teams = [team for team, innings in inning_counts.items() if len(innings) >= 5]
filtered_data = [row for row in filtered_data if row['bowling_team'] in bowling_teams]

# Step 5: Calculate the economy rate for each bowler by dividing the total runs conceded by the total number of overs bowled
bowler_stats = {}
for row in filtered_data:
    bowler = row['bowler']
    runs = int(row['total_runs'])
    balls = int(row['ball'])
    if balls <= 6:
        bowler_stats.setdefault(bowler, {'runs': 0, 'balls': 0})
        bowler_stats[bowler]['runs'] += runs
        bowler_stats[bowler]['balls'] += balls
economy_rates = {}
for bowler, stats in bowler_stats.items():
    overs = stats['balls'] // 6 + (stats['balls'] % 6) / 10
    economy_rate = stats['runs'] / overs
    economy_rates[bowler] = economy_rate

# Step 6: Sort the bowlers by their economy rate and take the top 10
top_10_economy_rates = sorted(economy_rates.items(), key=lambda x: x[1])[:10]
top_10_bowlers = [x[0] for x in top_10_economy_rates]
top_10_economy_rates = [x[1] for x in top_10_economy_rates]

# Step 7: Plot a bar chart
plt.bar(top_10_bowlers, top_10_economy_rates)
plt.xticks(rotation=90)
plt.xlabel('Bowler')
plt.ylabel('Economy Rate')
plt.title('Top 10 Economical Bowlers in IPL 2015')
plt.show()