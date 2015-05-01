#!/usr/bin/python

'''
Problem10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

def is_primes(num):
    for i in range(2, num / 2 + 1):
        if (num % i == 0):
            return False
    return True

result = 0
for k in range(2 * 1000000):
    if (is_primes(k)):
        result += k

    if (k % 100000 == 0):
        print 'process to ', k

print result
