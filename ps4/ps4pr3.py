
# 
# ps4pr3.py - Problem Set 4, Problem 3
#
# Functions that process binary numbers
#

# function 1
def count_evens_rec(binvals):
    """returns the count of the number of evens in a list of biniary values using recursion"""
    if binvals == []:
        return 0
    else:
        binvals_rest = count_evens_rec(binvals[1:])
        if binvals[0][-1] == "0":
            return 1 + binvals_rest
        else:
            return binvals_rest
        
# function 2
def count_evens_lc(binvals):
    """returns the count of the number of evens in a list of biniary values using list comprehension"""
    return len([[x] for x in binvals if x[-1] == "0"])


# function 3
def add_bitwise(b1, b2):
    """returns the sum of two binary numbers"""
    if b1 == '':
        return b2
    if b2 == '':
        return b1
    else:
        add_rest = add_bitwise(b1[:-1], b2[:-1])
        if b1[-1] != b2[-1]:
            return add_rest + "1" 
        elif b1[-1] == "0" and b2[-1] == "0":
            return add_rest + "0"
        elif b1[-1] == "1" and b2[-1] == "1":
            return add_bitwise(add_bitwise(b1[:-1], b2[:-1]), "1") + "0"