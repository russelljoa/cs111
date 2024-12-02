# 
# ps2pr6.py - Problem Set 2, Problem 6
#
# fun with recursion part 3
#
# fun recursion functions:
#

# function 1
def letter_score(letter):
    """returns the corresponding scrabble score of a letter. Returns 0 if not a-z"""
    one_score = ["a", "e", "i", "l", "n", "o", "r", "s", "t", "u"]
    two_score = ["d", "g"]
    three_score = ["b", "c", "m", "p"]
    four_score = ["f", "h", "v", "w", "y"]
    five_score = ["k"]
    eight_score = ["j", "x"]
    ten_score = ["q", "z"]

    if letter in one_score:
        return 1
    elif letter in two_score:
        return 2
    elif letter in three_score:
        return 3
    elif letter in four_score:
        return 4
    elif letter in five_score:
        return 5
    elif letter in eight_score:
        return 6
    elif letter in ten_score:
        return 7
    else:
        return 0
    
# function 2
def scrabble_score(word):
    """returns the corresponding scrabble score of a word"""
    if len(word) == 1:
        return letter_score(word)
    else:
        return letter_score(word[0]) + scrabble_score(word[1:])

# function 3
def BUtify(s):
    """returns the string s but with all lowercase 'b's and 'u's uppercase"""
    if s == '':
        return ''
    else:
        s_rest = BUtify(s[1:])
        if s[0] == 'b':
            return 'B' + s_rest
        elif s[0] == 'u':
            return 'U' + s_rest
        else:
            return s[0] + s_rest

# function 4
def diff(vals1, vals2):
    """returns a list of containing the absolute value of the different between each lists' corresponding index, leaving any excess in difference between length of lists at the end"""
    if len(vals1) == 0 or len(vals2) == 0:
        if len(vals1) > len(vals2):
            return vals1
        elif len(vals2) > len(vals1):
            return vals2
        else:
            return[]
    else:
        diff_rest = diff(vals1[1:], vals2[1:])
        if vals1[0] - vals2[0] >= 0:
            return [vals1[0] - vals2[0]] + diff_rest
        else:
            return [(vals1[0] - vals2[0]) * -1] + diff_rest

