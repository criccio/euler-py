#!/usr/bin/python

target=100

sumOfSquares = 0
sum = 0
squareOfSum = 0
for x in range(1, target+1):
	sumOfSquares += (x * x)
	sum += x
squareOfSum = (sum * sum)

answer = squareOfSum - sumOfSquares
print answer
