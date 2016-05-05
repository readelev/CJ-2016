import csv
import requests

import matplotlib.pyplot as plt
import pandas as pd

fname = 'STOCKS.csv'
df = pd.read_csv(fname, parse_dates=['Date'])
fig, ax = plt.subplots()

# Remove the plot frame lines. They are unnecessary chartjunk.   
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False) 

# Remove the tick marks; they are unnecessary with the tick lines we just plotted.    
plt.tick_params(axis="both", which="both", bottom="off", top="off",    
                labelbottom="on", left="off", right="off", labelleft="on") 

# pretty colors
tableau6 = [(255, 127, 14), (227, 119, 194), (44, 160, 44), (214, 39, 40), (109, 204, 218), (31, 119, 180)]

# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau6)):    
    r, g, b = tableau6[i]    
    tableau6[i] = (r / 255., g / 255., b / 255.)  

# Ensure that the axis ticks only show up on the bottom and left of the plot.    
# Ticks on the right and top of the plot are generally unnecessary chartjunk.    
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()  

# Make sure ticks are large enough to read
plt.xticks(fontsize=14) 
plt.yticks(fontsize=14)

# TIME TO PLOT DATA!
COLUMNS = ['AAPL', 'AMZN', 'FB', 'GOOG', 'MSFT', 'YHOO']

for rank, column in enumerate(COLUMNS) :
	plt.plot(df['Date'], df[column.replace("\n", " ")].values, color=tableau6[rank], alpha=1.00, linewidth=2)

ax.legend()
ax.set_title("Stock prices at close (2011-2015)", fontsize=20)
ax.set_ylabel('Price ($)', fontsize=16)
ax.set_xlabel('Date', fontsize=16)
   
plt.text(2011, -8, "Data source: Yahoo Finance"    
       "\nCompiled: Dan Nguyen (danwin.com / @dancow)", fontsize=10)    

plt.savefig("stock-comparison-2011-2015.png", bbox_inches="tight")  