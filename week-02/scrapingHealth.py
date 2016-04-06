from csv import DictReader

fname = 'breach_report.csv'

with open(fname, 'r') as f:
	datarows = list(DictReader(f))
print("Opening", fname)

#total individuals affected

affected = sum(column["Individuals Affected"])
print(affected)

#paper vs. electronic

#this calculation is different in Python than in Excel because the Python
#scrip below calculates paper/film records only for breaches whose values
#in the "Location of Breached Information" column exactly matched the string
#"Paper/Films"

electronic = 0
paper = 0
numaffected_paper = 0
numaffected_elec = 0

for row in datarows :
	if "Paper/Films" == row["Location of Breached Information"] :
		paper += 1
print(paper)

total_breaches = len(datarows)
electronic = total_breaches - paper
print(electronic)


