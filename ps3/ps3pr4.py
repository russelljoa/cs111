# 
# ps3pr4.py - Problem Set 3, Problem 4
#
# More algorithm design!
#

# funciton 1
def rem_first(c, s):
    """ removes the first occurrence of character c from a string s
    """
    if s == "":
        return ""
    elif s[0] == c:
        return s[1:]
    else:
        result_rest = rem_first(c, s[1:])
        return s[0] + result_rest


# function 2
def jscore(s1, s2):
    """returns the jotto score of s1 compared to s2"""
    if s1 == "" or s2 == "":
        return 0
    elif s1 == s2:
        return len(s1)
    
    else:
        if s1[0] in s2:
            jscore_rest = jscore(s1[1:], rem_first(s1[0], s2))
            return 1 + jscore_rest
        else:
            jscore_rest = jscore(s1[1:], s2)
            return jscore_rest

# function 3
def negate_last(n, values):
    """returns a version of values that does not have the last occurance (if any) of n"""
    if n not in values:
        return values
    elif values == []:
        return []
    elif len(values) == 1 and values[0] == n:
        return []
    
    else:
        values_rest = negate_last(n, values[:-1])
        if values[-1] == n:
            return values[:-1] + [values[-1] * -1]
        else:
            return values_rest + [values[-1]]

def first_occur(elem, seq):
    if len(seq) == 0:
        return 0
    else:
        index_rest = first_occur(elem, seq[1:])
        if elem != seq[0]:
            return 1 + index_rest
        else:
            return 0
        

print(first_occur('a', 'banana'))
        
