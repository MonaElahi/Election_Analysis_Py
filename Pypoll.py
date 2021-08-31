#Pypoll.py
# 1. The data we need to retrieve
# 2.The total number of votes cast
# 3. A complete list of  candidates who received votes
# 4. The percetage of votes each candidate won
# 5.The total number of votes each candidate won
# 6. The winner of the election based on popular vote
# 
##file_to_load = "election_results.csv" 
#election_data = open(file_to_load, 'r')

#election_data.close()
    
#with open(file_to_load) as election_data:

    #print(election_data)

# Add our dependencies.

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# create a dictionary for candidate votes
candidate_votes = {}

# Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Assign a variable to load a file from a path
with open(file_to_load) as election_data:
    # Assign a variable to save the file to a path.
    file_reader = csv.reader(election_data)

#print the header row
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
    # Get the candidate name from each row.     
        candidate_name = row[2]
        if candidate_name not in candidate_options:


#print(headers)
# Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

# 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0  

            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# determine the % of votes for each candidate by looping the counts
# 1. iterate through the candidate list.
for candidate_name in candidate_votes:
    #2. retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. calculate the % of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. print the candidate name and % of votes
    #print(f'{candidate_name}: received {vote_percentage:.1f}% of the vote.')

# to do: print out each candidate's name, vote count and %of votes to the terminal
#determine winnning vote count and candidate
#determine if the votes is greater than the winning count
    print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
    if (votes > winning_count) and (vote_percentage > winning_percentage):
    #if true then set winning_count = votes and winning_percentage = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
    # And, set the winning_candidate equal to the candidate's name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f'--------------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winner Vote Count:{winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}%\n'
    f'--------------------------\n')
print(winning_candidate_summary)


# to do: print out the winning candidate, vote count and % to terminal


# Print the candidate list.
#print(candidate_votes)