# 
# ps2pr4.py - Problem Set 2, Problem 4
#
# fun with recursion Part 1
#
# fun functions (part 1):
#

# function 1
def sum_squares(vals):
    """returns the sum of the squares of the numbers in a list [vals]"""
    if len(vals) == 0:
        return 0
    elif len(vals) == 1:
        return vals[0]**2
    else:
        return vals[0]**2 + sum_squares(vals[1:])

# function 2
def count_bu(s):
    """returns the total number of times b and u appear in the string s"""
    if s == '':
        return 0
    else:
        num_in_rest = count_bu(s[1:])
        if s[0] == 'b' or s[0] == 'u':
            return num_in_rest + 1
        else:
            return num_in_rest