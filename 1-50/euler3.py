#!/usr/bin/python
import math
from riccio import isPrime

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

