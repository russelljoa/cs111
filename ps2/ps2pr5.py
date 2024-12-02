# 
# ps2pr5.py - Problem Set 2, Problem 5
#
# fun with recursion part 2
#
# fun functions (part 2):
#

# function 1
def double(s, c):
    """returns a string where all occurances of character c ar repeated"""
    if s == '':
        return ''
    else:
        print("starting call for", s)
        double_rest = double(s[1:], c)
        if s[0] == c:
            print(s[0] * 2)
            return s[0] * 2 + double_rest
        else:
            print(s[0])
            
            return s[0] + double_rest

# function 2
def process(vals, x):
    """returns a list where all numbers greater than x are replaced with 0"""
    if vals == []:
        return []
    else:
        vals_rest = process(vals[1:], x)
        if vals[0] > x:
            vals[0] = 0
            return vals[0:1] + vals_rest
        else:
            return vals[0:1] + vals_rest

# function 3
def mul_pairs(vals1, vals2):
    """returns a list of containing the multiples of each index in both lists in order"""
    if len(vals1) == 0 or len(vals2) == 0 or len(vals1) != len(vals2):
        return []
    else:
        multiples_rest = mul_pairs(vals1[1:], vals2[1:])
        return [vals1[0] * vals2[0]] + multiples_rest