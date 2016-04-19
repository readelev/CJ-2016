from glob import glob
from os.path import join
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://www.whitehouse.gov/"
INDEX_PAGES_DIR = "/Users/Reade/Desktop/cj-2016/index-pages/"
ip_fnames = glob(join(INDEX_PAGES_DIR, "*.html"))

for fname in ip_fnames:
	# get the text
	with open(fname, 'r') as rf:
		txt = rf.read()

	# parse the HTML
	soup = BeautifulSoup(txt, "lxml")

	# extract the URLs
	for h in soup.find_all('h3'):
		a = h.find('a')
		url = urljoin(BASE_URL, a.attrs['href'])
		print(url)
