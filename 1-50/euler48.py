#!/usr/bin/python

def mypow(x,y):
	product = 1
	for i in range(1, y+1):
		product *= x
	return product
  
def mymain():
	sum = 0
	for n in range(1, 1001):
		sum += mypow(n,n)
	print sum
  
print str(sum([i**i for i in range(1,1001)]))[-10:]
