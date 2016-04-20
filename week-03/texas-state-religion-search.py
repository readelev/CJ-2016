import re
import requests
from glob import glob
from os import makedirs
from os.path import join
from bs4 import BeautifulSoup

# 1. Download and save the listing page
LAST_DIR = "last_statements"
BASE_URL = "http://www.tdcj.state.tx.us/death_row"
makedirs(LAST_DIR, exist_ok=True)

print("Downloading from...\n", BASE_URL)
resp = requests.get(BASE_URL + "/dr_executed_offenders.html")
l_fname = "LISTINGS.html"
with open(l_fname, "w") as wf:
	wf.write(resp.text)

# 2. Extract and download the URLs the correspond to the Last Statement link
with open(l_fname, 'r') as rf:
	txt = rf.read()

indexsoup = BeautifulSoup(txt, "lxml")
links = indexsoup.find_all(href=re.compile("last.html$"))
for l in links:
	END_URL = l.attrs['href']
	url = BASE_URL + "/" + END_URL
	print("Downloading from...\n", url)
	resp = requests.get(url)

	# create filename from relative href path
	full_fname = join(LAST_DIR, END_URL.replace("dr_info/", ""))
	print("Saving to...\n", full_fname)
	with open(full_fname, "w") as wf:
		wf.write(resp.text)

# 3. Glob through the downloaded URLs, come up with your own filter for "religious"/"non-religious" statements, e.g. does it contain "God"?
filenames = glob(join(LAST_DIR, "*.html"))
for fname in filenames:
	with open(fname, "r") as rf:
		txt = rf.read()
		txt = txt.upper()

HOLYPATTERN = "God|Lord|Christ\w*|Islam|heaven|angel|creator|Allah|M[uo]hammed"

def texasgodtester(txt)
	pattern = re.compile('Offender:')

	otag = txt.find('p', text=pattern)
	offender_name = otag.find_next_sibling('p').text

	is_religious = False
	lastwords = txt.find('div', {'id':'body'}).text

filenames = glob(join(LAST_DIR, "*.html"))
for fname in filenames:
	with open(fname, "r") as rf:
		txt = rf.read()
		txt = txt.upper()
		for word in HOLYWORDS:
			if 

		#if re.search(r'\b' + word + '\b', txt):
		#	print(fname, "mentions religion")

