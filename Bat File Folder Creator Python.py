#Create a txt file, rename it to .bat and run it to create folders with no python language needed.
import os

with open("Input.txt") as f:
	components_list = f.read().splitlines()

index = 0
while index < len(components_list):
	components_list[index] = "\t\tmd " + components_list[index]
	print (components_list[index])
	index += 1

def writetofile(number):
	output.write("\tmd " +  number + "\n")
	output.write("\tcd " +  number + "\n")
	output.write("\n".join(components_list))
	output.write("\n\tcd..\n")
	

train = ["EW1", "EW2", "MW1", "MW2"]
num = ["0812-", "5812-", "1812-", "9812-"]

output = open("Output.txt", "w")


for i in range(4):
	output.write("md " +  train[i] + "\n")
	output.write("cd " +  train[i] + "\n")
#für beliebig viele Zug Nummern hier in range einsetzen:
	for n in range(10):
		WK = num[i] + str(n+1).zfill(4)
		writetofile(WK)
	
	output.write("cd..\n")



"""
stupides einzeln anlegen:
output = open("Output.txt", "w")
output.write("md EW1\n")
output.write("cd EW1\n")
output.write("md 0812-0001\n")
output.write("cd 0812-0001\n")
output.write("\n".join(components_list))
output.write("\ncd..\n")
output.write("md 0812-0002\n")
output.write("cd 0812-0002\n")
...
output.write("cd..")"""