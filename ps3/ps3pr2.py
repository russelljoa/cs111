# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design
#

# funciton 1

def cube_all_lc(values):
    "returns a list values with all its values cubed using list comprehension"
    return [x**3 for x in values]

# function 2
def cube_all_rec(values):
    "returns a list values with all its values cubed using recursion"
    if values == []:
        return []
    else:
        values_rest = cube_all_rec(values[1:])
        return [values[0]**3] + values_rest

# function 3
def consonants(s):
    "returns a list values with all letters of a string s that are consonants"
    vowels = ["a", "e", "i", "o", "u"]
    return [x for x in s if x not in vowels]


# function 4
def num_consonants(s):
    "returns the number of consonants in a string s by taking the length of the value from the above consonants() function"
    return len(consonants(s))

# fucntion 5
def most_consonants(wordlist):
    "returns the string with the most consonants from a list [wordlist] using num_consonants()"
    return max([num_consonants(x), x] for x in wordlist)[1]

