num = int(input("Enter a no:"))

def sum_of_digit(num):
	total = 0
	while(num > 0):
		last_digit = num % 10
		total += last_digit
		num = num // 10
	
	print(total)


sum_of_digit(num)