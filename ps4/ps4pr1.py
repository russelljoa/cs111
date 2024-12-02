# 
# ps4pr1.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
#

# funciton 1

def dec_to_bin(n):
    """returns the binary value of a decimal int n given to the function"""
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    else:
        if n % 2 == 1:
            n_rest = dec_to_bin((n-1)/2)
            return n_rest + "1"
        else:
            n_rest = dec_to_bin(n/2)
            return n_rest + "0" 



# function 2
def bin_to_dec(b):
    """returns the decimal int value of a binary string b"""
    if b == "0":
        return 0
    if b == "1":
        return 1
    else:
        b_rest = bin_to_dec(b[1:])
        if b[0] == "1":

            return (2) ** (len(b) - 1) + b_rest
        else:
            return b_rest
        




