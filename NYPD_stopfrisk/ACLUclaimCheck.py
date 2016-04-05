from csv import DictReader

#2011 data fucked up?
for n in range(2012, 2016):
	fname = str(n) + '.csv'
	print("Opening", fname)

	with open(fname, 'r') as f:
		datarows = list(DictReader(f))

	total_stops = 0
	total_innocent = 0

	asians = 0
	blacks = 0
	natives = 0
	blackhisp = 0
	whitehisp = 0
	whites = 0
	unknowns = 0
	others = 0

	for row in datarows:
		total_stops += 1

		if 'N' == row['arstmade'] and 'N' == row['sumissue'] :
			total_innocent += 1

		if 'A' == row['race'] :
			asians += 1
		if 'B' == row['race'] :
			blacks += 1
		if 'I' == row['race'] :
			natives += 1
		if 'P' == row['race'] :
			blackhisp += 1
		if 'Q' == row['race'] :
			whitehisp += 1
		if 'W' == row['race'] :
			whites += 1
		if 'X' == row['race'] :
			unknowns += 1
		if 'Z' == row['race'] :
			others += 1

	n = str(n)

	print('In ' + n + ', New Yorkers were stopped by the police ' + str(total_stops) + ' times.')
	print(str(total_innocent) + ' were totally innocent. ' + str(round(100*(total_innocent/total_stops))) + ' percent.')
	print(str(asians) + ' were asian. ' + str(round(100*(asians/total_stops))) + ' percent.')
	print(str(blacks) + ' were black. ' + str(round(100*(blacks/total_stops))) + ' percent.')
	print(str(natives) + ' were native. ' + str(round(100*(natives/total_stops))) + ' percent.')
	print(str(blackhisp) + ' were black hispanic. ' + str(round(100*(blackhisp/total_stops))) + ' percent.')
	print(str(whitehisp) + ' were white hispanic. ' + str(round(100*(whitehisp/total_stops))) + ' percent.')
	print(str(whites) + ' were white. ' + str(round(100*(whites/total_stops))) + ' percent.')
	print(str(unknowns) + ' were of unknown race. ' + str(round(100*(unknowns/total_stops))) + ' percent.')
	print(str(others) + ' were of race "other". ' + str(round(100*(others/total_stops))) + ' percent.')




