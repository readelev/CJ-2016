import requests
import pdfplumber
import csv

url_a = "https://jfs.ohio.gov/warn/"
url_b = ".stm"

NAMES = ["WARN_2015",
"WARN2014",
"WARN_2013",
"WARN_2012"]

for name in NAMES:
	fname_pdf = (name + ".pdf")
	url = (url_a + name + url_b)
	print("Downloading", url, "into", fname_pdf)
	resp = requests.get(url)
	with open(fname_pdf, "wb") as f:
		f.write(resp.content)
		f.close()


	outfile = open(name + ".csv", "w")
	outcsv = csv.writer(outfile)

	pdf = pdfplumber.open(fname_pdf)
	for page in pdf.pages:
		table = page.extract_table()
		for row in table[1:]:
			outcsv.writerow(row)
	outfile.close

