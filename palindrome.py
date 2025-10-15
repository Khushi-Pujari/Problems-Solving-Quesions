num = int(input("Enter a no:"))
a = num
# st = input("Enter a string:")

def palin_num(a):
	rev_num = 0
	while(a > 0):
		last_digit = a % 10
		a = a // 10
		rev_num = rev_num * 10 + last_digit
	
	if num == rev_num:
		print("Num is a palindrome")
	else:
		print("Num is not a palindrome")




palin_num(a)