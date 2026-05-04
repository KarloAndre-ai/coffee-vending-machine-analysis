import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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


