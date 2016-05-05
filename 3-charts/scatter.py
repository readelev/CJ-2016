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

ax.scatter(X, Y, cmap=color, alpha=0.5);

ax.legend()
ax.set_title("US Legislators:\nIs there a correlation between the number of times they tweet and followers?", fontsize=16)
ax.set_ylabel("Number of followers", fontsize=14)
ax.set_xlabel("Number of tweets", fontsize=14)

plt.colorbar(color)
plt.show()

plt.savefig("tweets-v-followers.png", bbox_inches="tight") 
