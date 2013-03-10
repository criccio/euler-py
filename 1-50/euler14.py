#!/usr/bin/python

def isOdd(x):
	if x % 2 == 0:
		return False
	return True
  
#n => n/2 (n is even)
#n => 3n + 1 (n is odd)
def createchain(x):
	chain = [x]
	next = x
	while True:
		if isOdd(next):
			next = 3 * next + 1
		else:
			next = next/2
		chain.append(next)
		if next == 1:
			return chain
  
answer = 0
x = 999999
largest = 0
while x > 0:
	chain = createchain(x)
	if len(chain) > largest:
		answer = x
		largest = len(chain)
	x -= 1
print answer
