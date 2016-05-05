import csv
import requests
from os.path import join
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib

# Are num tweets related to gender, party?

legislators = pd.read_csv('legislators.csv')
tweets = pd.read_csv('legislators-twitter.csv')

fig, ax = plt.subplots()

X = tweets['Followers']
Y1 = legislators['gender']
Y2 = legislators['party']

ax.plot(X, Y1)
ax.plot(X, Y2, color='orange')

# Remove the plot frame lines. They are unnecessary chartjunk.   
ax.set_visible(False)    

plt.show()


