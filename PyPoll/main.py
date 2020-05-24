# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:54:02 2020

@author: betsy_k
"""
#dependencies
import os
import csv

#set up path
path = "/Users/betsy_k"

candidate = []

#read in data and populate candidate column
election_data = os.path.join(path, 'Python-Challenge/PyPoll/Resources', 'election_data.csv')

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:        
        candidate.append(row[2])

#calculate statistics
#total votes
total_votes = len(candidate)

#determine unique list of candidates
candidate_set = set(candidate)
unique_list = (list(candidate_set))

#determine total votes and percentage of votes for each candidate
c_votes = []
p_votes = []
for x in unique_list:
    total = candidate.count(x)
    pct = format((total/total_votes) * 100, '.3f')
    c_votes.append(total)
    p_votes.append(pct)

#combine candidate information into one list and sort from highest to lowest number of votes
total_candidates = tuple(zip(unique_list, c_votes, p_votes))
sort_candidates = sorted(total_candidates, key=lambda x: x[1], reverse=True)

#create variables to help summarize data
x = len(sort_candidates)
winner = sort_candidates[0][0]

#set output text file
output_path = os.path.join(path, 'Python-Challenge/PyPoll/Analysis', 'pypoll_results.txt')
OF = open(output_path, "w")

#create a function to both print to console and write to text file
def printing(text):
    print(text)
    OF.write(text + "\n")

printing("Election Results")
printing("-------------------------------------------")
printing(f"Total Votes: {str(total_votes)}")
printing("-------------------------------------------") 
for i in range(x):
    printing(f"{sort_candidates[i][0]}: {sort_candidates[i][2]}% ({sort_candidates[i][1]})")
printing("-------------------------------------------")   
printing(f"Winner: {winner}")
printing("-------------------------------------------")

OF.close()

    
    
