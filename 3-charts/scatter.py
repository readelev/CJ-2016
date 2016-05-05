import csv
import requests
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib

fname = 'legislators-twitter.csv'
df = pd.read_csv(fname)

X = df['Tweets']
Y = df['Followers']
Z = range(len(Y))
color = 'seismic'
fig, ax = plt.subplots()

ax.scatter(X, Y, c=Z, cmap=color, alpha=0.5);

# add colorbar!
cbar = plt.colorbar(color)
cbar.ax.get_yaxis().set_ticks([])
cbar.ax.set_ylabel('# of contacts', rotation=270)

# Write titles and axis labels
ax.set_title("US Legislators:\nIs there a correlation between the number of times they tweet and followers?", fontsize=16)
ax.set_ylabel("num. followers",fontsize=14)
ax.legend(numpoints=1, loc='upper right')


plt.show()

# Save file
plt.savefig("tweets-v-followers.png", bbox_inches="tight") 
