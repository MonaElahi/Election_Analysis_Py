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



import csv
import os

file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join("analysis","election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

#print the header row
    #for row in file_reader:
        #print(row)
    headers = next(file_reader)
    print(headers)