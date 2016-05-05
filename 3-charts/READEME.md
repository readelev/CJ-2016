# Hello! Welcome to Week 6.

![img](http://i.imgur.com/BXq5oUc.png?1)
*(without coffee this morning)*

# Homework (due May 4): In your cj-2016 repo, create a folder named 3-charts.

Here: [https://github.com/readelev/cj-2016/tree/master/3-charts](https://github.com/readelev/cj-2016/tree/master/3-charts)

## 1. Make a line chart comparing the stock performance of various tech companies

Uses this data (https://github.com/datademofun/matplotlibsampler/tree/master/data/stocks)

**NOTE:** I was completely wooed by Randal Olson's [beautiful line plot tuturial](http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/), so I created a [single CSV with the complied close values](https://github.com/readelev/cj-2016/tree/master/3-charts/data/STOCKS.csv) from all six stocks.

[This script](https://github.com/readelev/cj-2016/tree/master/3-charts/stocks-simple.py) makes this:

![img](http://i.imgur.com/CU1xzGV.png?1)

## 2. A scatterplot showing the relationship between two independent variables

[This script](https://github.com/readelev/cj-2016/tree/master/3-charts/scatter.py) makes this:

![img](http://i.imgur.com/18A9K5y.png?1)

It's not very pretty, but it does do its job, showing that there is **no correlation between the number of times a congress-person tweets and how many followers they have.**

The outlier is Obama, who has a dispproportionate number of followers (over 74 million) compared to tweets (14k).

Perhaps it's worth removing him and taking another look at the data -- perhaps there is a correlation and Obama (as an outlier) is skewing the data?

*Still working on (a) getting my colorbars to match, and (b) scaling the size of dots to correlate to number of followers.*

## 3. A stacked bar chart with categorical variables. An example: Number of twitter followers by congressional party and gender

[This script](https://github.com/readelev/cj-2016/tree/master/3-charts/tweets.py) makes this:

![img](http://i.imgur.com/B3TVGn9.png?1)

RAWR. Can't get this to work yet.

___

More practice:
* Inclass exercise [recreating the Economist's matplotlib visualization of climate data](https://github.com/datademofun/matplotlibsampler/blob/master/Basic-matplotlib-visualization-of-climate-data.ipynb), which looks something like this:

![img](http://i.imgur.com/FWWi4VA.png?1)

Code can be found here: [https://github.com/readelev/cj-2016/tree/master/3-charts/Economist.py](https://github.com/readelev/cj-2016/tree/master/3-charts/Economist.py)

