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

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)
  
def fib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fib(n-1) + fib(n-2)


