import pandas as pd
import numpy as np

#open text file by file name
file = open('input1.txt')

#read and split file into list formate
text = file.read().split()

#Create dataframe from list
df = pd.DataFrame(text)

#rename column name from 0 to 'text'
df = df.rename(columns={0:'text'})

#remove rows from datafram that have string staring from these regular expression that mansion below
df = df[~df['text'].str.contains('([A-Z]|[a-z]|[0-9]:?)')]

#remove 44 rows that have bed string data
df = df.iloc[44:]

#chech if any row is null
np.where(pd.isnull(df))

#create a column'text_length' with word length from text column
df["text_Length"]= df["text"].str.len()

#calculating text_length mean
df["text_Length"].mean()
