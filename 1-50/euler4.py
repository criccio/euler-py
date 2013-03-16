#!/usr/bin/python
from riccio import isPalindrome
	
largestAnswer = 0
for x in range(999, 99, -1):
	for y in range(999, 99, -1):
		product = x * y  
		#if the product is a palindrome, then we have a potential answer
		if isPalindrome(product):
			if product > largestAnswer:
				largestAnswer = product
print largestAnswer

