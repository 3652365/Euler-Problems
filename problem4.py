#!/usr/bin/python

'''
Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def ispalindrome(num):
    '''slow'''
    reverse_num = list(str(num))
    reverse_num.reverse()
    a = str(reverse_num)
    b = str(list(str(num)))
 #   print a,b
    
    if (a == b):
#        print num
        return True
   
def is_palindrome(num):
    '''fast'''
    num = str(num)
    for i in range(len(num)):
        if (num[i] != num[len(num) - i - 1]):
            return False

    return True


product = 0
largest = 0
palindromelist = []
for i in range(100, 999):
    for k in range(100, 999):
        product = i * k
        if ((is_palindrome(product)) and (largest < product)):
               largest = product
               
print 'largest palindrome: ',largest

