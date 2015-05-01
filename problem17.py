#!/usr/bin/python

'''
Problem 17
Number letter counts
If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''

first = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 
             11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen',
             19:'nineteen'}

ty = {20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety'}

h = {100:'hundred', 1000:'thousand'}

word = ''
def conv(num):
    global word

    if num < 20:
        word += first[num]
    elif num >= 20 and num <= 99:
        mod = num % 10
        if mod == 0:
            word += ty[num]
        else:
            a = ty[num / 10 * 10]
            b = first[mod]
            word += '%s-%s' % (a, b)
    elif num >= 100 and num <= 999:
        mod = num % 100
        word += '%s hundred' % (first[num / 100])
        if mod == 0:
            pass
            #word += '%s hundred' % (first[num / 100])
        elif mod < 20:
            word +=  ' and %s' % first[mod]
        elif mod >= 20 and mod <= 99:
            num = mod
            mod = num % 10
            if mod == 0:
                word += ' and %s' % ty[num]
            else:
                a = ty[num / 10 * 10]
                b = first[mod]
                word += ' and %s-%s' % (a, b)
    else:
        word += 'one thousand'
        
    return word
'''
for i in xrange(1, 1001):
    n = len(str(i))
    tmp = 10 ** (n - 1)
    if (n >= 3):
        print '%s %s' % (words_map[i / tmp], words_map[tmp])
    elif (i <= 20):
        print words_map[i]
    else:
        print words_map[i / tmp * tmp]
    
#    print tmp, i 
'''

for i in xrange(1, 1001):
    conv(i)

print len(word.replace(' ','').replace('-',''))
