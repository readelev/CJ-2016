from glob import glob
from bs4 import BeautifulSoup

filenames = glob('index-pages/*.html')
for fn in filenames:
	txt = open(fn).read()
	soup = BeautifulSoup(txt)


for h in 



	#for h in soup.find_all('h3'):
		#atag = h.find('a')
		#rel_url = atag['href']

		#url = urljoin( + rel_url)
		#requets.get()
		#print(url)