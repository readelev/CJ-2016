import csv
import requests
from os.path import join
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib

# Are num tweets related to 

fname = 'legislators-twitter.csv'
df = pd.read_csv(fname)

X = df['Tweets']
Y = df['Followers']

plt.scatter(X,Y)
plt.show()

