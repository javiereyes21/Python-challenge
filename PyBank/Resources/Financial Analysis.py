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
    print (Financial_Analysis)

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

        #Greatest Increase

        
        print=("Financial Analysis")
        print("-----------------------")
        print("Total Months: ", int(total_months))
        print("total: ", total)