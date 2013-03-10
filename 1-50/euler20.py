#!/usr/bin/python

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)
  
def sumdigits(x):
	sum = 0
	for i in range(0, len(x)):
		sum += int(x[i])
	return sum  

x = factorial(100)
y = sumdigits(str(x))
print y
