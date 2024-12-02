# 
# ps5pr9.py - Problem Set 5, Problem 9
#
# Processing sequences with loops
#

# funciton 1
def sum_squares(vals):
    """Returns the sum of all values in a list squared using a for loop"""
    total = 0
    for x in vals:
        total += x**2
    return total

# function 2
def double(s, target):
    """Returns a replica of a string s but every character target is repeated"""
    newstring = ''
    for x in s:
        if x == target:
            newstring += x*2
        else:
            newstring += x
    return newstring

# function 3
def process(vals, x):
    """returns a new list of vals where every element larger than x is replaced with 0"""
    newlist = []
    for i in vals:
        if i > x:
            newlist += [0]
        else:
            newlist += [i]
    return newlist

# function 4
def diff(vals1, vals2):
    """returns a new list with the absolute difference of the values of vals1 and vals2, adding excess values to the end"""
    compare = [[len(vals1), vals1], [len(vals2), vals2]]
    rest_list = max(compare)[1][min(compare)[0]:]
    newlist = []
    for x in range(min(compare)[0]):
        if vals1[x] - vals2[x] < 0:
            newlist += [(vals1[x] - vals2[x]) * -1]
        else:
            newlist += [vals1[x] - vals2[x]]
    return newlist + rest_list