'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.

'''

def digital_root(n):
    # for loop inside of a while loop
    # Variable i needs to be a integer or int
    # Variable i could each digit in the string or str
    # while checks if over 9
    
    while n > 9:
        n = sum(int(i) for i in str(n))
    return n
    
