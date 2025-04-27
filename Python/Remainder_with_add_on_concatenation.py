"""
If you're given a number x and you know the remainder mod k. 
If you concatenate it with another number y, (i.e xy), then you can quickly calculate the remainder of the new value

Proof:
X mod k = rem 
new_value = x*10**(len(y)) + y 
new_remainder = new_value % k = (x*10**(len(y)) + y)  % k = (rem * 10 ** (len(y)) + y) % k
"""


def new_rem(y, rem, k):
    return (rem * 10**(len(str(y))) + y) % k
