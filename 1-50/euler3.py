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

val = 600851475143

#trialdivision method
#you only have to check numbers up to the square root of the original number for factors. 
            
maxPrimeFactor = 0
top = math.sqrt(val)
for x in range(2, int(top)+1):
	if val % x == 0:
		#x is a factor, if x is prime, and it's larger than what we've found so far it's the largest prime factor
		if isPrime(x) and x > maxPrimeFactor:
			maxPrimeFactor = x                        
			
print maxPrimeFactor

