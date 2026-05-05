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
