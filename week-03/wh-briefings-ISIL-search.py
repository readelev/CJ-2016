from glob import glob
from os.path import join
BREIFS_DIR = "briefs"
filenames = glob(join(BREIFS_DIR, "*.html"))

import re
for fname in filenames:
	with open(fname, "r") as rf:
		txt = rf.read()
		txt = txt.upper()
		if re.search(r'\bISI[LS]\b', txt):
			print(fname, "mentions ISIS/ISIL")