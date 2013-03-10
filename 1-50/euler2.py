#!/usr/bin/python
max = 4000000
sum = 0

fibOne = 1
fibTwo = 2
#loop as long as the items in our sequence are below the max
while fibOne < max and fibTwo < max:
	#if either of them is even, add it to the sum
	if fibOne % 2 == 0:
		sum += fibOne
	if fibTwo % 2 == 0:
		sum += fibTwo;
	#determine the next two items in the sequence
	next = fibOne + fibTwo
	nextnext = fibTwo + next
	fibOne = next
	fibTwo = nextnext
print sum