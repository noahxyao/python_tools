# rename files in batches with increments of one in path
# if file entry exists, it is skipped. If the ascending number is interrupted, all futher files are renamed
# Thus assigning the first weirdly named file the current position in i and adding + 1 to all following filenames 
# The highest named number can thus not exceed the amount of files 

from pathlib import Path
import os

path = Path("/home/noah/Documents/Code Testing Environment")
os.chdir(path)

i = 1
for root, dirs, files in os.walk(path):
	for f in files:
		
		old_file_name = f
		new_file_name = '{0:03d}_newfile' .format(i)

		if old_file_name == new_file_name:
			i += 1
		else:
			os.rename(old_file_name, new_file_name)
			i += 1