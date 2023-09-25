# import the modules
import os
import csv
# establish the path
budget_csv = os.path.join("Resources", "budget_data.csv")
# lists to store the data
totalprofitsnlosses = []
month = []
profitsnlosses = []
changeinpnl = []
change_maxincrease = []
profitsmax_decrease = 0
profitsmax_decr_month = ""

# create a function
def read_csv(budget_csv):
    # create empty lists and variables to be used later
    month = []
    profitsnlosses = []
    changeinpnl = []
    profitsmax_incr_month = ""
    profitsmax_decrease = 0
    profitsmax_decr_month = ""
    profitsmax_increase = 0
# open the csv file:
    with open(budget_csv) as csvfile:
        # the values are separated by commas, csv.reader = using the imported module.
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)  # skip the header row
        for row in csvreader:  # loop through the rows beginning after the header
            # add month. month is 0 because that is its index position
            month.append(row[0])
            # add profits and losses column. its position is 1 because it's second
            profitsnlosses.append(row[1])
        # create a new variable to store the previous month's profit or loss
        past_pnl = (int(profitsnlosses[0]))
        # loop through the profits and losses list
        for i in range(1, len(profitsnlosses)):
            current_pnl = int(profitsnlosses[i])
            # calculate the change by subtracting past from current pnl
            changes = current_pnl - past_pnl
            changeinpnl.append(changes)
            # make the current element the past element so it can keep looping
            past_pnl = current_pnl
            # create a variable to store the month of the greatest increase in profits/losses
            if changes > profitsmax_increase:
                # then update profits max increase month and profitsmax increase amount
                profitsmax_increase = changes
                profitsmax_incr_month = month[i]
            if changes < profitsmax_decrease:
                profitsmax_decrease = changes
                profitsmax_decr_month = month[i]
    return month, profitsnlosses, changeinpnl, profitsmax_incr_month, profitsmax_increase, profitsmax_decrease, profitsmax_decr_month  #when using a function, you must always use the return function


month, profitsnlosses, changeinpnl, profitsmax_incr_month, profitsmax_increase, profitsmax_decrease, profitsmax_decr_month = read_csv(
    budget_csv)
# calculate the values that were returned
totalnumbermonths = len(month)
totalprofitsnlosses = round(sum(int(i) for i in profitsnlosses),2)
averagechangeinpnl = round(sum(changeinpnl) / (totalnumbermonths - 1), 2)
# print the results
print(f"Total Number of Months: {totalnumbermonths}")
print(f"Total Profits and Losses: ${totalprofitsnlosses:,}")
print(f"Average Change in Profits and Losses: ${averagechangeinpnl:,}")
print(f"Greatest Increase and Month: {profitsmax_incr_month}, ${profitsmax_increase:,}")
print(f"Greatest Decrease and Month: {profitsmax_decr_month}, ${profitsmax_decrease:,}")

# create the text file
with open('PyPollfinalresults.txt', 'a') as text:
    totalnumbermonths = len(month)
    totalprofitsnlosses = round(sum(int(i) for i in profitsnlosses),2)
    averagechangeinpnl = round(sum(changeinpnl) / (totalnumbermonths - 1),2)
    text.write(f"Total Number of Months: {totalnumbermonths}\n")
    text.write(f"Total Profits and Losses: ${totalprofitsnlosses:,}\n")
    text.write(f"Average Change in Profits and Losses: ${averagechangeinpnl:,}\n")
    text.write(f"Greatest Increase and Month: {profitsmax_incr_month} {profitsmax_increase:,}\n")
    text.write(f"Greatest Decrease and Month: {profitsmax_decr_month} {profitsmax_decrease:,}\n")


