#!/usr/bin/python
from riccio import factorial

x_max = 20
y_max = 20
	
print factorial(x_max+y_max) / (factorial(x_max) * factorial(y_max))
