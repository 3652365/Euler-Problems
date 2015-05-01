#!/usr/bin/python

'''
Problem 16
Power digit sum
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

a = str(2 ** 1000)
result = 0

for i in a:
    result += int(i)


print result

print sum([int(i) for i in str(2 ** 1000)])
