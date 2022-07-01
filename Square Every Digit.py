'''
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer


'''

"""
Things to improve on:
check to see if input is a Number

Next evo: multi runs, with 2nd paramiter 



I learned with this exercise operators and strings and intiger usage.
"""

def square_digits(num):
    r = '' # setup variable before using.
    for n in str(num):
        r += str((int(n))**2) # Operators ** for Exponentiation. 
        # or r = r + 
    return int(r)
    
print("Square Every Digit: ",square_digits(9119))
