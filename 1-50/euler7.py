#!/usr/bin/python
import math

def isPrime(val):
	if val == 2:
		return True
	elif val % 2 == 0:
		return False
	max = int( math.sqrt(val) ) + 1
	for x in range(3, max):
		#a number is prime if it's only divisible by itself and 1
		if val % x == 0:
			#it has divisors other than 1 and itself, so not prime
			return False 
	return True

found = 1
x = 3
while found < 10001:
	if isPrime(x):
		found+=1
	x+=2
print x-2



