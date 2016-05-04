import csv
import requests
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/datademofun/matplotlibsampler/master/data/climate/nasa-gistemp-annual-mean.csv'
resp = requests.get(url)
datarows = csv.DictReader(resp.text.splitlines())

%matplotlib

colds = []
hots = []
for d in datarows:
    yr = int(d['year'])
    mean = float(d['annual_mean'])
    if mean < 0:
        colds.append((yr, mean))
    else:
        hots.append((yr, mean))

fig, ax = plt.subplots()
ax.bar([x[0] for x in colds], [x[1] for x in colds], color='blue')                
ax.bar([x[0] for x in hots], [x[1] for x in hots], color='orange')