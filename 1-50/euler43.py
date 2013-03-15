#!/usr/bin/python
from riccio import get_permutations

divisors = [2,3,5,7,11,13,17]

def has_property(substrings):
	for index in range(7):
		if substrings[index] % divisors[index] != 0:
			return False
	return True

value = "0123456789"
candidates = get_permutations(value)
sum = 0

for candidate in candidates:
	substrings = [int(candidate[start:start+3]) for start in range(1,8)]
	if has_property(substrings):
		sum += int(candidate)
		
print sum