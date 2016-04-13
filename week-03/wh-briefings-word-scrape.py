import requests
from os import makedirs
from os.path import join
THE_URL = 'https://www.whitehouse.gov/briefing-room/press-briefings?page='
MAX_PAGE_NUM = 162
INDEX_PAGES_DIR = 'index-pages'
makedirs(INDEX_PAGES_DIR, exist_ok=True)

for page in range(0, MAX_PAGE_NUM):
	url = THE_URL.format(page)
	resp = requests.get(THE_URL, params={'page': page})
	print("Downloaded", resp.url)

	fname = join(INDEX_PAGES_DIR, '{}.html'.format(page))
	print("Saving to", fname)
	with open(fname, "w") as wf:
		wf.write(resp.text)

    


