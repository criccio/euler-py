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
	if n <= 1:
		return 1
	else:
		return n * factorial(n-1)
  
def fib(n):
	if n == 1:
		return 1
	if n == 2:
		return 1
	return fib(n-1) + fib(n-2)

def isLeapYear(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False
	elif year % 4 == 0:
		return True
	return False	
	
def get_permutations(val):
    result = []
    if len(val) == 1:
        result = [val]
    else:
        for i, c in enumerate(val):
            for perm in get_permutations(val[:i] + val[i+1:]):
                result += [c + perm]
    return result		
    
def isPalindrome(n):
	x = str(n)
	y = ""
	for i in range(len(x), 0, -1):
		y += x[i-1]
	if x == y:
		return True
	return False	
