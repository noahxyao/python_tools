#! Python 3

# This one scans the current directory for anything named after its 
# structure and renames files upward from the highest number of said file
# No correctly named files are touched!

from pathlib import Path
import os, re



path = Path("D:/My Files/Code Testing Environment/Python/Batch Renamer/Files to Rename")
os.chdir(path)


# scan for highest file number to place all new renamed entries after it
maxfilenumber = 0
nextfilenumber = 0
for root, dirs, files in os.walk(path):
	for f in files:
		if "_newfile.txt" in f:
			if int(f[:3]) > maxfilenumber:
				maxfilenumber = int(f[:3])
				nextfilenumber = maxfilenumber + 1
				print ('maxfilenumber: {maxfilenumber}, nextfilenumber: {nextfilenumber}' .format(maxfilenumber = maxfilenumber, nextfilenumber = nextfilenumber) )
			

for root, dirs, files in os.walk(path):
	for f in files:
		if "_newfile.txt" not in f:
			old_file_name = f
			new_file_name = '{0:03d}_newfile.txt' .format(nextfilenumber)
			os.rename(old_file_name, new_file_name)
			nextfilenumber += 1