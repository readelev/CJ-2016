import requests

url_a = 'http://www.nyc.gov/html/nypd/downloads/zip/analysis_and_planning/'
url_b = '_sqf_csv.zip'

for n in range(2010, 2016):
	url = url_a + str(n) + url_b
	fname = str(n) + '.zip'
	print("Downloading", url, "to:", fname)

	resp = requests.get(url)
	f = open(fname, "wb")
	f.write(resp.content)
	f.close()

