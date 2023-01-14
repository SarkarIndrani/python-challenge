#project instructions:
#In this challenge, your task helping a small, rural town modernize its vote counting process.
#You will get a set of poll data called 'election_data.csv'. It has three coloumns: Voter Id, County, Candidate.
#Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.
#**********************************************************************************************************

import os
import csv

#Assign a variable to set a file from a relative path
csvpath = os.path.join("PyPoll","Resources", "election_data.csv")

#Assign a variable to save file to a path
txtpath = os.path.join("PyPoll","analysis", "election_analysis.txt")


total_votes = 0             #total vote counter
candidate_list = []         # creating blank candidate list
candidate_votes = {}        # creating blank candidate dictionary
winner = ""                 # initilize winner canditate
winning_count = 0           # initilize counter
winning_percentage = 0


with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     header = next(csvreader) # dismiss header
     
     #loop through each row in csv file
     for row in csvreader:
        total_votes += 1                #incrementing vote count
        candidate_name = row[2]         #get name from each row
        
        #If the candidate does not match any existing canditate,
        #add them to the candidate list.        
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            #Add start tracking that candidate's voter count
            candidate_votes[candidate_name] = 0
        #increment candidate's voter count
        candidate_votes[candidate_name] +=1
        
     
            
#save the results to 'election_analysis.txt' file.
with open(txtpath, "w") as txt_file:
    
    #print the final vote count to the terminal
     election_output = (
         f"\nElection Results\n"
         f"------------------------------\n"
         f"Total Votes: {total_votes: }\n"
         f"------------------------------\n"        
         
     )   
     
     print(election_output, end="")  
     #After printing the final vote count to the terminal
     #save the final vote count to the text file.
     txt_file.write(election_output)
     
     for candidate_name in candidate_votes:
        #get vote count and percentage
        votes = candidate_votes[candidate_name]        
        vote_percentage = float(votes)/float(total_votes) * 100
        
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes:})\n")
         
        #print each candidate's voter count and percentage to the terminal
        print(candidate_results)
        # save candidate_results to text file
        txt_file.write(candidate_results)
         
        #Determine winning vote count, winning percentage, and winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winner = candidate_name
            winning_percentage = vote_percentage
            
     #print winner
     winner_candidate = (
        f"------------------------------\n"
        f"Winner: {winner}\n"
        f"------------------------------\n"

     )
     #print winner candidate to the terminal
     print(winner_candidate)
     # save it to the text file
     txt_file.write(winner_candidate)
    
             
         
         
             
        
        
    
    


              
