import requests

#get data
url = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/2011_sqf_csv.zip'
fname = '2011.zip'
print("Downloading", url, "to:", fname)

resp = requests.get(url)
f = open(fname, "wb")
f.write(resp.content)
f.close()


#unzip data
from shutil import unpack_archive

print('Unzipping: ', fname)
unpack_archive(fname)

#read data
from csv import DictReader
with open(fname, 'r') as f:
    datarows = list(DictReader(f))

xcount = 0
for row in datarows:
    if '28' == row['age'] and '06-03-2011' == row['datestop'] and 'N' == row['arstmade']:
        xcount += 1

print(xcount)