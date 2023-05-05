'''Total runs scored by team
Plot a chart of the total runs scored by each teams over the history of IPL. Hint: use the total_runs field.

'''



import csv
import matplotlib.pyplot as plt

# Create empty dictionaries to store the total runs scored by each team
total_runs = {}

# Open the CSV file containing the IPL data
with open('deliveries.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Extract the relevant data from each row
        team = row['batting_team']
        runs = int(row['total_runs'])

        # Add the runs scored by the team to the corresponding dictionary entry
        total_runs[team] = total_runs.get(team, 0) + runs
        

        

# Create a list of tuples containing the team name, total runs
team_data = [(team, total_runs[team]) for team in total_runs]

# Sort the list in descending order of total runs
team_data.sort(key=lambda x: x[1], reverse=True)

# Create a bar chart of the total runs scored by each team
plt.bar([x[0] for x in team_data],[x[1] for x in team_data])
plt.xticks(rotation=90)
plt.title('Total runs scored by team')
plt.xlabel('Team')
plt.ylabel('Total Runs')

# Display the chart
plt.show()



