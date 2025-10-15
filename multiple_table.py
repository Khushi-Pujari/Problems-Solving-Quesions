num = int(input("Enter a no:"))

def multiple_table(num):
	multi_num = 1
	while(multi_num < 11):
		table = multi_num * num
		multi_num += 1
		print(table)

multiple_table(num)