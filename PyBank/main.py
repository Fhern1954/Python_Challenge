#Dependencies
import os
import csv

#Path to collect data from Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

date = []
profit_loss = []
rolling_diff = []

#Read in the csv file
with open(budget_csv, 'r') as csvfile:
    #Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    #remove the header row
    csv_header = next(csvreader)

#pulling out date & profit/loss numbers into lists.
    for row in csvreader:
        date.append(row[0])
        profit_loss.append(row[1])
    # print(date)
    # print(profit_loss) 
     

#number of months calculation
    num_months = len(profit_loss)
    print(f'Total Months: {num_months}')

 
#calculate rolling_diff and store values in list. with help from study group & Paul Anderson
#calculate "Total" (net profit/loss)
    prev = 0
    total = 0
    for num2 in profit_loss:
        if prev == 0: #skip first row
            prev = int(num2)
            total = int(num2)
        else:
            rolling_diff.append(int(num2) - (prev))
            total += int(num2)
            prev = int(num2)
    # print(total)
    # print(rolling_diff)

#calculate average change in profit/loss.
avg_change = round(sum(rolling_diff) / len(rolling_diff), 2)
print(f'Total: ${total}')
print(f'Average Change: $ {avg_change}')


#calculate Max & Min change 
min_change = min(rolling_diff)
max_change = max(rolling_diff)


#calculate Min & Max month
min_month = (date[rolling_diff.index(min_change) + 1])
max_month = (date[rolling_diff.index(max_change) + 1])
# print(f'Max month: {max_month}')  
# print(f'Min month: {min_month}')

print(f'Greatest Increase in Profits: {max_month} (${max_change})')
print(f'Greatest Decrease in Profits: {min_month} (${min_change})')

#SUCCESS!!!!!!!
