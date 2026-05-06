import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.options.display.max_rows = 9999

# reading the csv and taking a look at the overview and info of the dataset
df1 = pd.read_csv('index_1.csv')
df2 = pd.read_csv('index_2.csv')


#concatenating both frames
frames = [df1, df2]
df = pd.concat(frames)
#evaluating the differences in info
print(df1.info())
print(df2.info())
print(df.info())

#calculating total revenue
total_revenue = df['money'].sum()
print(total_revenue)

#finding the average of the cost
total_avg = df['money'].mean()
print()
print(total_avg)

#the highest price 
highest_charge = df['money'].max() 

#highest price is $40 but how many are at the price of $40
print()
print(highest_charge)

#retrieving info on all those with the max() cost. 
top_coffee = df.loc[df['money'] == highest_charge, ['coffee_name', 'money']]
print(top_coffee)

#finding which is the most common one to be purchased. 
print()
print(top_coffee['coffee_name'].value_counts())

#looking to get the lowest cost. 
lowest_charge = df['money'].min()
print()
print(lowest_charge)

#retrieving all those that are at $15
lowest_coffee = df.loc[df['money'] == lowest_charge, ['coffee_name', 'money']]
print()
print(lowest_coffee)

#finding the most purchased coffee. 
most_purchased = df['coffee_name'].value_counts()
print()
print(most_purchased)

#the amounts of cash_type taken. 
cashTypeDF = df['cash_type'].value_counts()
print()
print(cashTypeDF)

#finding the coffee that generated the most revenue.
sumsOfCoffee = df.groupby('coffee_name')['money'].sum().sort_values(ascending = False)
print()
print(sumsOfCoffee)

#shows popular and most profitable 
popAndProfit = df.groupby('coffee_name').agg(
    no_of_purchased = ('coffee_name', 'count'),
    revenue = ('money', 'sum')
)

print()
print(popAndProfit.sort_values(by = 'revenue', ascending = False))

#finding the average price per type
avg_price = df.groupby('coffee_name').agg(
    count =('coffee_name', 'count'),
    avgCost = ('money', 'mean')
)
print()
print(avg_price.sort_values(by = 'avgCost', ascending = False))


#percentage of cards vs. cash
summary = df ['cash_type'].value_counts().to_frame('count')
summary['percent'] = summary['count'] / summary['count'].sum() * 100
print(summary['percent'])

#finding the average transaction value per payment type.
avg_transaction = df.groupby('cash_type').agg(
    avg_transaction_value = ('money', 'mean')
)
print()
print(avg_transaction)