from shutil import unpack_archive

for n in range(2010, 2016):
	fname = str(n) + '.zip'
	print('Unzipping: ', fname)
	unpack_archive(fname)


