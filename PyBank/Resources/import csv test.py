import csv

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read CSV file
with open("budget_data.csv", 'r') as analysis:
    csvreader = csv.reader(analysis, delimiter=',')
    
    # Skip header
    next(csvreader)

    # Loop through rows
    for row in csvreader:
        # Count total months
        total_months += 1
        
        # Calculate net total
        net_total += int(row[1])
        
        # Calculate change in profit/loss
        profit_change = int(row[1]) - previous_profit_loss
        if previous_profit_loss != 0:
            profit_changes.append(profit_change)
        
        # Update previous profit/loss for next iteration
        previous_profit_loss = int(row[1])
        
        # Find greatest increase
        if profit_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change
        
        # Find greatest decrease
        if profit_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change

# Calculate average change
average_change = sum(profit_changes) / len(profit_changes)

# Output results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")
