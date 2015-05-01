#!/usr/bin/python
import math

'''
Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
num = 600851475143
i = 2

while (1):
    tmp = 0
    while (i <= math.sqrt(num)):
        if (num % i == 0):
            tmp = num / i
            print '%s * %s' % (i, tmp)
            break
        i += 1

    if (tmp == 0):
        break
    num = tmp
    

print 'largest prime factor', num
    
