#!/usr/bin/python
from riccio import fib 

n = 5
fib_n_minus_one = 3
fib_n_minus_two = 2
while True:
	#get fib for the current n
	fib = fib_n_minus_one + fib_n_minus_two
	if len(str(fib)) >= 1000:
		print n
		break
	#increase n for next loop
	n += 1
	#update n-1 and n-2 answers
	fib_n_minus_two = fib_n_minus_one
	fib_n_minus_one = fib
  
