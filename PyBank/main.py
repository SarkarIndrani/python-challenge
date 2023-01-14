# Project Instructions:
# Create a Python script to analyze the finalcial records
# from the given dataset called 'budget_data.csv'
# Task to calculate each of the following values:
# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period 
# Calculate the changes in "Profit/Losses" over the entire period,
# and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period
# ********************************************************************************

import os
import csv

# define the path to the csv file and txt output file
csvpath = os.path.join('PyBank','Resources','budget_data.csv')   


# Variables
no_of_month= 0                      # Total number of months
prof_loss = 0                       # Profit n Loss Summatory
prof_loss_changes = 0               
diff = 0                            # Difference between lines
change_per_month = []
total_changes = 0                   # Adds up changes
prev_row = 0
gr_inc_amt = 0                      # Greatest increase
gr_in_mon = ""                      # Greatest increase month
gr_dec_mon = ""                     # Greatest decrease month
gr_dec_amt = 0                      # Greatest decrease

with open(csvpath) as csvfile: 
      
      # CSV reader specifies delimiter and variable that holds contents
      csvreader = csv.reader(csvfile, delimiter=',')
      next (csvreader)  # skip the header
      
      for row in csvreader:    
            no_of_month +=1                           # total number of month      
            prof_loss = prof_loss + int(row[1])       # net total amount of "Profit/losses" over the entire period      
            diff = int(row[1]) - prev_row             # Difference between rows
            prev_row = int(row[1])                    # Acquires the current value for the next loop
            total_changes = total_changes + diff      # Adding up the changes
            change_per_month.append(diff)             # Create a changes list
            
      
            # The greatest increase in profits (date and amount) 
            # over the entire period
            if diff > gr_inc_amt:
                  gr_inc_amt = diff
                  gr_inc_mon = row[0]
                  
                  
            # The greatest decrease in losses (date and amount) 
            # over the entire period
            elif diff < gr_dec_amt:
                  gr_dec_amt = diff
                  gr_dec_mon = row[0]

      # Adjust acummulated changes by substracting the first value
      total_changes = total_changes - change_per_month[0]
      
      print("FINANCIAL ANALYSIS")
      print()           
      print("-----------------------------")  
      print()          
      print(f"Total Months: {str(no_of_month)}")
      print(f"Total: ${str(prof_loss)}")
      print(f"Average Change: $ {str(round(total_changes/(no_of_month-1),2))}")
      print(f"Greatest Increase in Profits: {gr_inc_mon} ($ {str(gr_inc_amt)} )")
      print(f"Greatest Decrease in Profits: {gr_dec_mon} ($ {str(gr_dec_amt)} )")
      
 
      
#print to text file
 
txtpath = os.path.join('PyBank','analysis','result.txt')

with open(txtpath, 'w') as txtfile:
      txtfile.write("FINANCIAL ANALYSIS\n")           
      txtfile.write("-----------------------------\n")            
      txtfile.write(f"Total Months: {str(no_of_month)}\n")
      txtfile.write(f"Total: ${str(prof_loss)}\n")
      txtfile.write(f"Average Change: $ {str(round(total_changes/(no_of_month-1),2))}\n")
      txtfile.write(f"Greatest Increase in Profits: {gr_inc_mon} ($ {str(gr_inc_amt)} )\n")
      txtfile.write(f"Greatest Decrease in Profits: {gr_dec_mon} ($ {str(gr_dec_amt)} )\n")
      
txtfile.close()
      




      
      