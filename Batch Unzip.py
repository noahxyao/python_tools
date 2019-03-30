#! python 3
# extract all zipfiles to current directory

import zipfile, os
from pathlib import Path
n = 1
path = Path("/home/noah/Documents/Code Testing Environment")
os.chdir(path)

for root, dirs, files in os.walk(path):
	for f in files:
		exampleZip = zipfile.ZipFile('{0:03d}_newfile' .format(n))
		exampleZip.extractall()
		exampleZip.close()
		n += 1