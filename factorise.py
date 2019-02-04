def checkio(number):
	mylist = list()
	for i in range(1, number + 1):
		# print(number)
		if number % i == 0 and i != 1:
			print(i)
			print(number/i, "I", i)
			if number/i < 10 and i < 10:
				print(i)
				mylist.append(i)
	print(mylist)
	return 0

print(checkio(21))