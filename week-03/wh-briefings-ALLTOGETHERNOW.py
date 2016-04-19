from glob import glob
from os import makedirs
from os.path import join
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

BASE_URL = "https://www.whitehouse.gov/briefing-room/press-briefings"
INDEX_PAGES_DIR = "/Users/Reade/Desktop/cj-2016/index-pages/"
BRIEFS_DIR = "briefs"
makedirs(BRIEFS_DIR, exist_ok=True)

# Gather all index pages
ip_fnames = glob(join(INDEX_PAGES_DIR, "*.html"))

for fname in ip_fnames:
	# get the text
	with open(fname, 'r') as rf:
		txt = rf.read()

	# parse the HTML
	soup = BeautifulSoup(txt, "lxml")

	# select for <a> tags nested within <h3> tags
	for rawr in soup.find_all("h3"):
		href = rawr.find('a').attrs["href"]
		url = urljoin(BASE_URL, href)
		print("Downloading from...\n", url)
		resp = requests.get(url)

	# create filename from relative href path
		fname = href.replace('/', '-').strip('-') + '.html'
		full_fname = join(BRIEFS_DIR, fname)
		print("Saving to...\n", full_fname)
		with open(full_fname, "w") as wf:
			wf.write(resp.text)
