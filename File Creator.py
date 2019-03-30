#! python 3
#Create 10 binary files with 4 characters

import os

x = int(input('Number of files to be created: '))
for n in range(x):
	output = 'output_file_{0:03d}.txt' .format(n+1) 
	print (output)
	with open(output, 'wb') as fout:
		fout.write(os.urandom(4)) # replace 1024 with size_kb if not unreasonably large

print ('Files Created!')