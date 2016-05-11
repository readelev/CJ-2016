import matplotlib.pyplot as plt

# takes two sequences

xvals = [0, 1, 2, 3]
yvals = [23, 48, 65, 80]
plt.plot(xvals, yvals)

# other fun things
plt.savefit('whatever.png')
plt.close()
plt.bar(xvals, yvals)
plt.scatter(xvals, yvals, color="red")
ply.close()

# for examples...
fig, ax = plt.subplots()
ax.pie([12,32])

axs.bar(yrs, means)

~~~py
hots = []
colds = []

for d in datarows:
	year = int(d["year"])
	mean = float(d["annual_mean"])
	if mean <= 0:
		colds.append([year, mean])
	else:
		hots.appent([year, mean])

fig, ax = plt.subplots()


# ax.bar() ???


# PANDAS!

import pandas as pd

