import csv

total = 0

with open ('bank.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=';')
	uttak = []
	beskrivelse = []
	for row in readCSV:
		ut = row[4]
		temp = ut.replace("-", "")
		temp = temp.replace(",", ".")
		uttak.append(temp)
		besk = row[1]
	#	temp = ut.replace("-", "")
	#	temp = temp.replace(",", ".")
		beskrivelse.append(besk)

uttak.pop(0)

print(uttak)
print(beskrivelse)
print(total)