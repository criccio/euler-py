#!/usr/bin/python

number = 2 ** 1000
s = str(number)
sum = 0
for i in range(0, len(s)):
	sum += int(s[i])
print sum
