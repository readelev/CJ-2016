import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd

fname = 'legislators-twitter.csv'
df = pd.read_csv(fname)

X = df['Tweets']
Y = df['Followers']
color = 'seismic'
fig, ax = plt.subplots()

ax.scatter(X, Y, cmap=color, alpha=0.5)
ax.set_ylim(0, 1000000) # Remove some outliers (in this case, Obama) for legibility (thanks Alec for the tip!)

ax.legend()
ax.set_title("US Legislators:\nIs there a correlation between the number of times they tweet and followers?", fontsize=16)
ax.set_ylabel("Number of followers", fontsize=14)
ax.set_xlabel("Number of tweets", fontsize=14)

plt.savefig("tweets-v-followers.png", bbox_inches="tight") 
