import re
import requests
from bs4 import BeautifulSoup
from os.path import join


# 1. Download and save the listing page
LISTINGS_URL = "http://www.tdcj.state.tx.us/death_row/dr_executed_offenders.html"
print("Downloading from...\n", LISTINGS_URL)
resp = requests.get(LISTINGS_URL)

l_fname = "LISTINGS.html"
with open(l_fname, "w") as wf:
	wf.write(resp.text)

# 2. Extract and download the URLs the correspond to the Last Statement link
with open(l_fname, 'r') as rf:
	txt = rf.read()

soup = BeautifulSoup(txt, "lxml")

x = soup.find_all(href=re.compile("last.html$"))
for y in x:
	END_URL = y.attrs['href']
	url = LISTINGS_URL + END_URL
#DAN HELP!
	print("Downloading from...\n", url)
	resp = requests.get(url)

