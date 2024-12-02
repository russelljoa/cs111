# 
# ps2pr3.py - Problem Set 2, Problem 3
#
# writing functions
#
# functions:
#

# function 1
def compare(s1, s2):
    """returns the string that comes later in the dictionary"""
    if s1 >= s2:
        return s1
    else:
        return s2

#function 2
def combine(s1, s2, n):
    """returns a new string with the last n characters are followed by the first n characters of s2"""
    return s1[-1 * n:] + s2[:n]

# function 3
def reverse_n(vals, n):
    """returns the list but with the first n values in reverse order"""
    return vals[n-1::-1] + vals[n:]