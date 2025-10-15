num = int(input("Enter a no:"))

def factorial_num(num):
    fact_num = num
    secnum = num - 1
    while(secnum >= 1):
        fact_num = fact_num * secnum
        secnum -= 1

    print(fact_num)

factorial_num(num)