#!/usr/bin/python

answer = 0
            
for a in range(0,1000):
	for b in range(a+1, 1000):                
		for c in range(b+1,1000):
			if a + b + c != 1000:
				continue
			if ((a * a) + (b * b)) == c * c:
				answer = a * b * c
				break
		if answer > 0:
			break
	if answer > 0:
		break
print answer
