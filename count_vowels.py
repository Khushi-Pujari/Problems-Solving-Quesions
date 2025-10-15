name = input("Enter a string:")
vowels = ['a','e','i','o','u']

def count_vowels(name):
	vowels_count = 0
	for x in name:
		x = x.lower()
		if x in vowels:
			vowels_count+=1

	
	print(vowels_count)




count_vowels(name)