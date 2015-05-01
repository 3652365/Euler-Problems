#!/usr/bin/python

'''
Problem 13
Large sum
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
one-hundred 50-digit numbers in p13 file.
'''
list = []
result = 0
sum = 0
fileObj = open("p13")
for line in fileObj:
    sum += int(line)

print str(sum)[:10]

