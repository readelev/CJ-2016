import requests
import pdfplumber
import csv

url_a = "http://www.edd.ca.gov/jobs_and_training/warn/"
url_b = ".pdf"

NAMES = ["WARN-Report-for-7-1-2015-to-03-25-2016",
"WARNReportfor7-1-2014to06-30-2015",
"WARN_Interim_041614_to_063014",
"eddwarncn14",
"eddwarncn13",
"eddwarncn12"]

for name in NAMES:

	#downloading PDFs

	fname_pdf = (name + url_b)
	url = (url_a + name + url_b)
	print("Downloading", url, "into", fname_pdf)
	resp = requests.get(url)
	with open(fname_pdf, "wb") as f:
		f.write(resp.content)
		f.close()

#reading each (multipage) PDF to a CSV file

	outfile = open(name + ".csv", "w")
	outcsv = csv.writer(outfile)

	pdf = pdfplumber.open(fname_pdf)
	for page in pdf.pages:
		table = page.extract_table()
		for row in table[1:]:
			outcsv.writerow(row)
	outfile.close

