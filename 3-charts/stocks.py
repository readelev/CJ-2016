import csv
import requests
from os.path import join
import matplotlib.pyplot as plt
import pandas as pd

%matplotlib

# Read the data into a pandas DataFrame.    
fname = 'STOCKS.csv'
stock_data = pd.read_csv(fname, parse_dates=['Date'])

# use much prettier colors :)
tableau6 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (44, 160, 44), (152, 223, 138), (214, 39, 40)]    
  
# Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.    
for i in range(len(tableau6)):    
    r, g, b = tableau6[i]    
    tableau6[i] = (r / 255., g / 255., b / 255.)    
  
# You typically want your plot to be ~1.33x wider than tall.  
# Common sizes: (10, 7.5) and (12, 9)    
plt.figure(figsize=(12, 9))    
  
# Remove the plot frame lines. They are unnecessary chartjunk.    
ax = plt.subplot(111)    
ax.spines["top"].set_visible(False)    
ax.spines["bottom"].set_visible(False)    
ax.spines["right"].set_visible(False)    
ax.spines["left"].set_visible(False)    
  
# Ensure that the axis ticks only show up on the bottom and left of the plot.    
# Ticks on the right and top of the plot are generally unnecessary chartjunk.    
ax.get_xaxis().tick_bottom()    
ax.get_yaxis().tick_left()    
  
# Limit the range of the plot to only where the data is.    
# Avoid unnecessary whitespace.    
plt.ylim(0, 1000)    
plt.xlim(2011, 2015) 

# Make sure your axis ticks are large enough to be easily read.    
# You don't want your viewers squinting to read your plot.    
plt.yticks(range(0, 1000, 100), [str(x) + "%" for x in range(2011, 2015, 1)], fontsize=14)    
plt.xticks(fontsize=14)    
  
# Provide tick lines across the plot to help your viewers trace along    
# the axis ticks. Make sure that the lines are light and small so they    
# don't obscure the primary data lines.    
for y in range(0, 1000, 100):    
	plt.plot(range(2011, 2015), [y] * len(range(2011, 2015)), "--", linewidth=0.5, color="black", alpha=0.3)    
  

# Remove the tick marks; they are unnecessary with the tick lines we just plotted.    
plt.tick_params(axis="both", which="both", bottom="off", top="off",    
                labelbottom="on", left="off", right="off", labelleft="on")    
  
# Now that the plot is prepared, it's time to actually plot the data!    
# Note that I plotted the majors in order of the highest % in the final year.    
STOCKS = ['AAPL', 'AMZN', 'FB', 'GOOG', 'MSFT', 'YHOO']

for rank, column in enumerate(STOCKS):    
    # Plot each line separately with its own color, using the Tableau 20    
    # color set in order.
    plt.plot(stock_data.Date.values, stock_data[column.replace("\n", " ")].values, linewidth=2.5, color=tableau20[rank]) 
    # Add a text label to the right end of every line. Most of the code below    
    # is adding specific offsets y position because some labels overlapped.    
	# y_pos = stock_data[column.replace("\n", " ")].values[-1] - 0.5
	# if column == "AAPL":
	# 	y_pos += 0.5
 #    elif column == "AMZN":
 #    	y_pos -= 0.5
 #    elif column == "FB":
 #    	y_pos += 0.75
 #    elif column == "GOOG":
 #    	y_pos -= 0.25
 #    elif column == "MSFT":
 #    	y_pos += 1.25
	# elif column == "YHOO":
	# 	y_pos += 0.25
    
    # Again, make sure that all labels are large enough to be easily read    
    # by the viewer.    
    plt.text(2011.5, y_pos, column, fontsize=14, color=tableau6[rank])    
  
# matplotlib's title() call centers the title on the plot, but not the graph,    
# so I used the text() call to customize where the title goes.    
  
# Make the title big enough so it spans the entire plot, but don't make it    
# so big that it requires two lines to show.    
  
# Note that if the title is descriptive enough, it is unnecessary to include    
# axis labels; they are self-evident, in this plot's case.    
plt.text(2.0, 2015, "Comparison of stock performance (2011-2015)", fontsize=17, ha="center")    
  
# Always include your data source(s) and copyright notice! And for your    
# data sources, tell your viewers exactly where the data came from,    
# preferably with a direct link to the data. Just telling your viewers    
# that you used data from the "U.S. Census Bureau" is completely useless:    
# the U.S. Census Bureau provides all kinds of data, so how are your    
# viewers supposed to know which data set you used?    
plt.text(1966, -8, "Data source: Yahoo Finance"    
       "\nCompiled: Dan Nguyen (danwin.com / @dancow)", fontsize=10)    
  
# Finally, save the figure as a PNG.    
# You can also save it as a PDF, JPEG, etc.    
# Just change the file extension in this call.    
# bbox_inches="tight" removes all the extra whitespace on the edges of your plot.    
plt.savefig("stock-comparison-2011-2015.png", bbox_inches="tight")  







