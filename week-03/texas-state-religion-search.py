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
# for l in links:
# 	END_URL = l.attrs['href']
# 	url = BASE_URL + "/" + END_URL
# 	print("Downloading from...\n", url)
# 	resp = requests.get(url)

# 	# create filename from relative href path
# 	full_fname = join(LAST_DIR, END_URL.replace("dr_info/", ""))
# 	print("Saving to...\n", full_fname)
# 	with open(full_fname, "w") as wf:
# 		wf.write(resp.text)

# 3. Glob through the downloaded URLs, come up with your own filter for 
# "religious"/"non-religious" statements, e.g. does it contain "God"?
HOLYPATTERN = "(GOD)|(LORD)|(ISLAM)|(CHRIST)|(CHRISTIAN)|(FAITH)|(HEAVEN)|(ANGEL)|(ALLAH)|(M[OU]HAMMED)"
NOT_HOLY = []
HOLY_MEN = []

filenames = glob(join(LAST_DIR, "*.html"))
for fname in filenames:
	with open(fname, "r") as rf:
		lastwords = rf.read()
		lastwords = lastwords.upper()
		
		offender_name = fname.replace("last_statements/", "")
		offender_name = offender_name.replace("last.html", "")

		match = re.search(HOLYPATTERN, lastwords)
		if match != None:
			HOLY_MEN.append(offender_name)
			print(match.span(0))
			print(offender_name + " talked about " + str(match.group(0)))
		else:
			NOT_HOLY.append(offender_name)

print(NOT_HOLY)
print(str(len(NOT_HOLY)) + " death row inmates didn't mention religion.")
print(str(len(HOLY_MEN)) + " inmates mentioned religion.")