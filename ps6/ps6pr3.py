# 
# ps6pr3.py - Problem Set 6, Problem 3
#
# Functions that use loops
#

# funciton 1
def repeat(s, n):
    """returns a string s repeated n times using a loop"""
    newstring = ""
    if n <= 0:
        return ""
    else:
        for x in range(n):
            newstring += s
        return newstring

# function 2
def contains(s, c):
    """returns a boolean if a string s contains character c"""
    for x in s:
        if x == c:
            return True
    return False

# function 3
def add(vals1, vals2):
    """returns a list with the sums of the correspoinding indicies, padding with 0s to fill the difference between the two lists"""
    newlist = []
    if len(vals1) != len(vals2):
        if len(vals1) > len(vals2):
            vals2 = ([0] * (len(vals1) - len(vals2))) + vals2
        elif len(vals1) < len(vals2):
            vals1 = ([0] * (len(vals2) - len(vals1))) + vals1
    for x in range(len(vals1)):
        newlist += [vals1[x] + vals2[x]]
    return newlist

# function 4
def replace(vals, old, new):
    """modifies a list vals where values equal to old are switched to value(s) new. Does not return a value, it only changes the internal values of the list"""
    for x in range(len(vals)):
        if vals[x] == old:
            vals[x] = new
    

