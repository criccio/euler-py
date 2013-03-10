#!/usr/bin/python
import math
            
max = 2000000

PRIME = 1
NOTPRIME = 0

nums = [PRIME for i in range(0,max+1)] 
nums[0] = NOTPRIME
nums[1] = NOTPRIME

top = math.sqrt(max)
for p in range(2,int(top)):
	if nums[p] == NOTPRIME:
		continue
	for y in range(2,max):
		index = p * y
		if index > max:
			break
		nums[index] = NOTPRIME

sum = 0
for x in range(1, max):
	if nums[x] == PRIME:
		sum += x

print sum

