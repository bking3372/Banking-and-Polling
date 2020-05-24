# -*- coding: utf-8 -*-
"""
Created on Wed May 20 12:23:59 2020

@author: betsy_k
"""
#dependencies
import os
import csv

date = []
pft_lss = []

#set up path
path = "/Users/betsy_k"

#read in data and populate data
budget_data = os.path.join(path, 'Python-Challenge/PyBank/Resources', 'budget_data.csv')


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        date.append(row[0])
        pft_lss.append(int(row[1]))

#calculate statistics
#total number of months and total profit/loss
nbr_mths = len(date)
total_pl = sum(pft_lss)

#calculate change in profit/loss by each date
r = nbr_mths - 1
change = []
for i in range(r):
    x = pft_lss[i+1] - pft_lss[i]
    change.append(x)

#average change aross entire period
avg_chg = round((sum(change) / len(change)),2)

#determine greatest increase and decrease for entire period
min_pl = min(change)
max_pl = max(change)

#create list of dates to match the changes; first date needs to be removed
new_date = date[1:]

#zip the pl changes and corresponding date together
new_file = zip(new_date, change)

#find the dates corresponding to the greatest increase and decrease
for row in new_file:
    if row[1] == min_pl:
        grt_dec_date = row[0]
    if row[1] == max_pl:
        grt_inc_date = row[0]

#output variables
date_inc = grt_inc_date + ' $' + '(' + str(max_pl) + ')'
date_dec = grt_dec_date + ' $' + '(' + str(min_pl) + ')'

#output file
output_path = os.path.join(path, 'Python-Challenge/PyBank/Analysis', 'pybank_results.txt')
OF = open(output_path, "w")

#create a function to both print to console and write to text file
def printing(text):
    print(text)
    OF.write(text + "\n")

printing("Financial Analysis")
printing("---------------------------------------------------")
printing(f"Total Months: {str(nbr_mths)}")
printing(f"Total: ${str(total_pl)}")
printing(f"Average Change: ${str(avg_chg)}")
printing(f"Greatest Increase in Profits: {date_inc}") 
printing(f"Greatest Decrease in Profits: {date_dec}")
   
OF.close()







        
        
