"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""


def longest_alphabetical_substr(s):
	max_length = 0
	temp_length = 0
	longest_substr = s[0]
	temp_substr = s[0]
	for i, x in enumerate(s):
		if i == 0:
			continue	
		if x >= s[i-1]:
			temp_substr += x
			temp_length += 1
		else:
			temp_substr = x
			temp_length = 0

		if temp_length > max_length:
			longest_substr = temp_substr
			max_length = temp_length
	return longest_substr

s = 'azcbobobegghakl'

print('Longest substring in alphabetical order is: ' + longest_alphabetical_substr(s))