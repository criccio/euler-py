#!/usr/bin/python
from riccio import factorial

def sum_of_factorials(number):
	digits = [int(digit) for digit in str(number)]
	sum = 0
	for digit in digits:
		sum += factorial(digit)
		if sum > number:
			break # no need to keep going	
	return sum	
		
sum = 0
for i in range(3,50000):
	s = sum_of_factorials(i)
	if s == i:
		sum += i
		
print sum