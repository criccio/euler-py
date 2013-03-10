#!/usr/bin/python

def isPalindrome(n):
	x = str(n)
	y = ""
	for i in range(len(x), 0, -1):
		y += x[i-1]
	if x == y:
		return True
	return False 
	
largestAnswer = 0
for x in range(999, 99, -1):
	for y in range(999, 99, -1):
		product = x * y  
		#if the product is a palindrome, then we have a potential answer
		if isPalindrome(product):
			if product > largestAnswer:
				largestAnswer = product
print largestAnswer

