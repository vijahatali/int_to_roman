roman = {}
roman[1000] = "M"
roman[900] = "CM"
roman[500] = "D"
roman[400] = "CD"
roman[100] = "C"
roman[90] = "XC"
roman[50] = "L"
roman[40] = "XL"
roman[10] = "X"
roman[9] = "IX"
roman[5] = "V"
roman[4] = "IV"
roman[1] = "I"

def int_to_romen(num):
	output = ''
	for key,value in roman.items():
		if num < key:
			output += value
			num -= key
			b = num
			int_to_romen(b)
		elif num >= key:
			output += value
			num -= key
	return output

a = int(input("Enter the integer:"))
print(int_to_romen(a))