# 
# ps4pr2.py - Problem Set 4, Problem 2
#
# Using conversion functions
#

from ps4pr1 import bin_to_dec
from ps4pr1 import dec_to_bin

# funciton 1
def mul_bin(b1, b2):
    """returns the binary representation of the product of b1 and b2"""
    return dec_to_bin(bin_to_dec(b1) * bin_to_dec(b2))

#print(mul_bin('1001', '101'))

def largest_bin(binvals):
    """returns the largest binary value in a list of binary numbers"""
    return dec_to_bin(max([bin_to_dec(x) for x in binvals]))

print(largest_bin(['1100', '10011', '101', '10000']))