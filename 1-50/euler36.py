#!/usr/bin/python
from riccio import isPalindrome

sum = 0
for i in range(1000000):
	if isPalindrome(i):
		binary_representation = bin(i)[2:]
		if binary_representation[0] != 0:
			if isPalindrome(binary_representation):
				sum += i
print sum
		