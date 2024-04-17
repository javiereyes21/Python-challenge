import csv
import os


#Variables
total_months= 0
total= 0
previous_profit_loss= 0
profit_changes= []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]


with open(r"C:\Users\javie\Documents\DataAnalytics\Python-challenge\PyBank\Resources\budget_data.csv",'r') as analysis:

    Financial_Analysis= csv.reader(analysis, delimiter=",")
    
    next(Financial_Analysis)

    

    for row in Financial_Analysis: 
        # row = [Jan-10,1088983]
        total_months += 1
        total+= int(row[1])

        #change in profit/loss
        profit_change= int(row[1]) - previous_profit_loss
        if previous_profit_loss != 0:
            profit_changes.append(profit_change)

        previous_profit_loss = int(row[1])

        # Greatest increase and decrease
        if profit_change > greatest_increase[1]:
            greatest_increase = [row[0], profit_change]
        if profit_change < greatest_decrease[1]:
            greatest_decrease = [row[0], profit_change]

        previous_profit_loss = int(row[1])

        # Average

        average_change = sum(profit_changes) / len(profit_changes) if len(profit_changes) > 0 else 0

        
print("Financial Analysis")
print("-----------------------")
print("Total Months: " + str(total_months))
print("total: ", total)
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")