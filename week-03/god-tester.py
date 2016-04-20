import re
import requests
from glob import glob
from os.path import join

HOLYWORDS = ["CHRIST", "GOD", "LORD", "HEAVEN", "HELL", "ALLAH", "CREATOR", "DIVINE"]
filenames = glob(join(LAST_DIR, "*.html"))
for fname in filenames:
	with open(fname, "r") as rf:
		txt = rf.read()
		txt = txt.upper()
		for word in HOLYWORDS:
		if re.search(r'\b' + word + '\b', txt):
			print(fname, "mentions religion")