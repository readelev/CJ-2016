import requests
from bs4 import BeautifulSoup
url = "http://stash.compjour.org/samples/webpages/whitehouse-press-briefings-page-50.html"
resp = requests.get(url)
txt = resp.text


soup = BeautifulSoup(txt, "lxml")

# The number of <h3> tags
len(soup.find_all('h3'))

# Extract each press briefing URL from webpage
urls = []
for h in soup.find_all('h3'):
	a = h.find('a')
	urls.append(a.attrs['href'])

print(urls)





