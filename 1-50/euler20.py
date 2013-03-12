#!/usr/bin/python
from riccio import factorial

def sumdigits(x):
	sum = 0
	for i in range(0, len(x)):
		sum += int(x[i])
	return sum  

x = factorial(100)
y = sumdigits(str(x))
print y
