#Version 3: Der Path ist immer der mit der .py Datei, Ankündigungs path ist für alle Betriebssysteme angepasst.
import os
#If I want my own path: 'D:\\My Files\\Code Testing Environment\\Python\\Bombardier Test\\Python only'
#path = os.path.join('D:\\', 'My Files', 'Code Testing Environment','Python','Bombardier Test','Python only')
print ('The created folders are in: ' + os.getcwd())

#Path Beispiele der fertigen Ordner
#0812-0001\\A010_Schienen
#0812-0001\\D030_Montage
#5812-0001\\A010_Schienen

with open("Input.txt") as f:
	components_list = f.read().splitlines()

for line in components_list:
	print (line)


def makedirectories(train, component):
		for i in component:
			os.makedirs(train + '\\' + str(i))

#if I want to change my path:
#os.chdir(path)

for n in range(10):

	ew1 = 'EW1\\0812-' + str(n+1).zfill(4)
	mw1 = 'MW1\\1812-' + str(n+1).zfill(4)
	ew2 = 'EW2\\5812-' + str(n+1).zfill(4)
	mw2 = 'MW2\\9812-' + str(n+1).zfill(4)

	#erste stupide Schritte
	#os.makedirs(a + '\\' + str(components_list[0]))
	#os.makedirs(a + '\\' + str(components_list[1]))
	#os.makedirs('0812-0001\\D030_Montage')
	#os.makedirs('5812-0001\\A010_Schienen')


	makedirectories(ew1,components_list)
	makedirectories(mw1,components_list)
	makedirectories(ew2,components_list)
	makedirectories(mw2,components_list)