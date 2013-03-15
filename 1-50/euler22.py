#!/usr/bin/python

def load_names():
	file = open('../data/names.txt',"rU")  
	ts = file.read()
	file.close()
	return sorted([name.replace('"','').upper() for name in ts.split(',')])

total_value = 0
index = 1

for name in load_names():
	total_value += sum(ord(letter)-64 for letter in name) * index
	index += 1
	
print total_value