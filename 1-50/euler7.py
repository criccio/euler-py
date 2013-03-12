#!/usr/bin/python
import math
from riccio import isPrime

found = 1
x = 3
while found < 10001:
	if isPrime(x):
		found+=1
	x+=2
print x-2



