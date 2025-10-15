num1 = 10
num2 = 5
num3 = 11

def largest_num(num1):
    if num1 > num2 and num1 > num3:
        print("num1 is greater")
    elif num2 > num1 and num2 > num3:
        print("num2 is greater")
    else:
        print("num 3 is greater")


largest_num(num1)
