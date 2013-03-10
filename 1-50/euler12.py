#!/usr/bin/python
from math import sqrt

def factors(n):
	fact=[1,n]
	check=2
	rootn=sqrt(n)
	while check<rootn:
		if n%check==0:
			fact.append(check)
			fact.append(n/check)
		check+=1
	if rootn==check:
		fact.append(check)
        fact.sort()
	return fact
	
def trianglenumber(x):
	sum = 0
	for i in range(1, x+1):
		sum += i
	return sum
  
x = 1
while True:
	trinum = trianglenumber(x)
	trifactors = factors(trinum)
	if len(trifactors) >= 500:
		print trinum
		break
	x += 1
	
