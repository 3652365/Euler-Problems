#!/usr/bin/python

'''
Problem 6
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first 
ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

sum_of_the_squares = 1
the_square_of_the_sum = 0

for i in range(1, 101):
    sum_of_the_squares += i ** 2
    the_square_of_the_sum += i

    
sum_of_the_squares = sum_of_the_squares - 1
the_square_of_the_sum = the_square_of_the_sum ** 2
print sum_of_the_squares
print the_square_of_the_sum

print 'result: ',the_square_of_the_sum - sum_of_the_squares
