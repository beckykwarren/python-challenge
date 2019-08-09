import os
import csv

# define file path
csvpath_budget = os.path.join('..', 'Resources', 'budget_data.csv')

count = 0
total_profit = 0
change_list = []
prev_value = 0
greatest_increase = 0
greatest_decrease = 0


with open(csvpath_budget, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader_budget = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader_budget, None)

    # Read each row of data after the header
    for row in csvreader_budget:
        count = count + 1
        total_profit = total_profit + float(row[1])
        
        # Calculate change for rows > 1
        if count > 1:
            change = float(row[1])-prev_value

            # Create list of change values
            change_list.append(change)
            

            # Find greatest increase and greatest decrease
            if change>greatest_increase:
                greatest_increase = change
                increase_date = row[0]
            elif change<greatest_decrease:
                greatest_decrease = change
                decrease_date = row[0]

        # Set value from previous row
        prev_value = float(row[1])

# Calculate average change
average_change = float(sum(change_list)/len(change_list))

financial_file = open('financial_analysis.txt', 'w')
# financial_file.write("Financial Analysis\n------------------------------\n")
financial_file.write("%s\n%s\n%s %i\n%s%.0f\n%s %.2f\n%s %s %s%.0f%s\n%s %s %s%.0f%s\n"%("Financial Analysis","------------------------------","Total Months: ",count,"Total: $",total_profit,"Average Change: ",average_change,"Greatest Increase in Profits: ",increase_date,"($",greatest_increase,")","Greatest Decrease in Profits: ",decrease_date,"($",greatest_decrease,")"))

print(f"\nFinancial Analysis \n------------------------------")
print(f"Total Months: {count}")
print(f"Total: ${round(total_profit)}")
print(f"Average Change: {round(average_change)}")
print(f"Greatest Increase in Profits: {increase_date} (${round(greatest_increase)})")
print(f"Greatest Decrease in Profits: {decrease_date} (${round(greatest_decrease)})\n")

#print(f"{change_list[0]}, {change_list[1]}, {change_list[2]}")
#print(f"{sum(change_list)}, {len(change_list)}\n")
