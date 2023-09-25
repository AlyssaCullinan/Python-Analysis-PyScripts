# In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
# You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:
# 	• The total number of votes cast - done
# 	• A complete list of candidates who received votes - done
# 	• The percentage of votes each candidate won
# 	• The total number of votes each candidate won
# 	• The winner of the election based on popular vote
# Your analysis should align with the following results:
# Election Results-------------------------Total Votes: 369711-------------------------Charles Casper Stockham: 23.049% (85213)Diana DeGette: 73.812% (272892)Raymon Anthony Doane: 3.139% (11606)-------------------------Winner: Diana DeGette-------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# import the module
import os
import csv

# specify the file to write to
file = os.path.join("Resources", "election_data.csv")

# create the variables
ballot_id = []
county = []
candidate_name = []
candidates_w_votes = []
votes = {}

# open the file using "read" mode. Specify the variable to hold the contents
with open(file, 'r') as electioncsv:
    # intiailize the csv.reader, specify the delimiter
    csvreader = csv.reader(electioncsv, delimiter=",")
    # skip the first row since there is a header
    csv_header = next(csvreader)

    for row in csvreader: 
        #add ballot id
        ballot_id.append(row[0])
        # add county name, the brackets are for the index
        county.append(row[1])
        # add name
        candidate_name.append(row[2])
    
    for name in candidate_name:
        if name not in candidates_w_votes:
            candidates_w_votes.append(name)
        if name in votes:
            votes[name] +=1
        else:
            votes[name] = 1
    
# calculate the total votes by getting the length of the list
total_votes = len(ballot_id)
# print the total votes - use:, to create a comma in the result
print(f"Total Votes: {total_votes:,} ")   
# loop through the dictionary using for, 'name,count' and using .item 
for name, count in votes.items():
        percentage = (count/total_votes)*100
        # make sure the print statement is within the for loop
        print(f"{name}:{count:,} ({percentage:.2f}%)")
# calculate the max and then print the winner   
max_votesname = (max(votes, key=votes.get))
print(f'The winner is {max_votesname}')

with open('finalresultsPypolls.txt', 'a') as text:
     text.write(f'Total Votes: {total_votes:,}\n')
     for name, count in votes.items():
        percentage = (count/total_votes)*100
        # make sure the print statement is within the for loop
        text.write(f"{name}:{count:,} ({percentage:.2f}%)\n")
     text.write(f'The winner is {max_votesname}\n')
