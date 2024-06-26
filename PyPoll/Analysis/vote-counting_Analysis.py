import csv

#Variables

total_votes = 0
candidates = {}
winner = ""

with open(r"C:\Users\javie\Documents\DataAnalytics\Python-challenge\PyPoll\Resources\election_data.csv", 'r') as file:
    csvreader = csv.reader(file, delimiter=',')

    next(csvreader)

    for row in csvreader:
        #total votes
        total_votes += 1

        #Candidate name
        candidate_name = row[2]

        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

print("Election Results")
print("-------------------------")

    # % of votes

max_votes = 0
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}% ({votes})")
    if votes > max_votes:
        max_votes = votes
        winner = candidate

print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Winner: {winner}")

with open("election_results.txt", "w") as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        text_file.write(f"{candidate}: {percentage:.2f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")

print("Results exported to 'election_results.txt'")
