#!/usr/bin/python

def evenlyDivisibleUpTo(val, max):
	#go in reverse order (i think the higher numbers will have fewer true cases so the loop will exit faster)
	for x in range(max, 0, -1):
		if val % x != 0:
			return False
	return True

target = 20

answer = target
while True:
	if evenlyDivisibleUpTo(answer, target):
		break; #//we found it, break out of the loop. we just need the first one found
	answer+=target; # can increment by target since the others won't be evenly divisible by it
print answer
