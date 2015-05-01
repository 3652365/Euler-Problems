#!/usr/bin/python

'''
Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
result = 0
begin = 1 * 3 * 5 * 7  * 11 * 13 * 17 * 19
print begin
i = begin
while (True):
    flag = True
#    print i
    for k in range(1, 21):
#        print k
        tmp = i % k ==0
        if (tmp != True):
            flag = False
            break

    if (flag):
        result = i
        break

    i += 1

print 'result', result
