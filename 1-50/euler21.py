#!/usr/bin/python
import math

def sum_of_proper_divisors(val):
	divisors = [i for i in range(1,int(val /2)+1) if val % i == 0]
	return sum(x for x in divisors)

amicable = {}

for a in range(1,10001):
	a_sum = sum_of_proper_divisors(a)
	b = a_sum
	b_sum = sum_of_proper_divisors(b)
	if a == b_sum and a-b != 0:
		if not a in amicable.keys():
			amicable[a] = a
		if not b in amicable.keys():
			amicable[b] = b	
	
print sum(x for x in amicable.keys())