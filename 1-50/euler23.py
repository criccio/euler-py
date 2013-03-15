#!/usr/bin/python

abundant_numbers = []

for val in range(28124):
	divisors = [i for i in range(1,int(val/2)+1) if val % i == 0]
	sum_of_divisors = sum(x for x in divisors)
	if sum_of_divisors > val:
		abundant_numbers.append(val)
		
sum = 0
for i in range (28123,0,-1):
	found = False
	for a in abundant_numbers:
		if a > i:
			break
		b = i - a
		if b in abundant_numbers:
			found = True
			break #for a...
	#if we scanned all abundant_numbers and we didn't find anything, add to sum
	if not found:
		sum += i
print sum