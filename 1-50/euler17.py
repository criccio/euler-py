#!/usr/bin/python

#
# for number to english name
#
SUFFIXES = [ "", "thousand", "million", "billion" ]
NAMES = [ "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen" ]
TENS = [ "", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]

#recursive worker function for Number To English
def NumToName(number, depth):
	minorTriplet = int(number % 1000)
	majorRemaining = int(number / 1000)
	triplet = tripletToString(minorTriplet)
	major = ""
	if majorRemaining > 0:
		major = NumToName(majorRemaining, depth + 1)
		return major + " " + triplet + " " + SUFFIXES[depth]
	else:
		return triplet + " " + SUFFIXES[depth]

#helper function, converts a number from 0 - 999 into an english string
def tripletToString(number):
	minorTenths = int(number % 100)
	hundreds = int(number / 100)

	tenthsValue = ""
	if minorTenths >= 20:
		tensPlace = int(minorTenths / 10)
		ones = int(minorTenths % 10)
		tenthsValue = TENS[tensPlace] + " " + NAMES[ones]
	if minorTenths < 20:
		tenthsValue = NAMES[minorTenths]
	if hundreds == 0:
		return tenthsValue
	else:
		if minorTenths == 0:
			return NAMES[hundreds] + " hundred " + tenthsValue		
		else:
			return NAMES[hundreds] + " hundred and " + tenthsValue
		

total_length = 0
for i in range(1,1001):
	words = NumToName(i,0).strip().split(' ')
	size = sum(len(word) for word in words)
	total_length += size
	
print total_length