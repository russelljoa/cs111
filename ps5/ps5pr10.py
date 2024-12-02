# 
# ps5pr10.py - Problem Set 5, Problem 10
#
# Choosing the correct type of loop
#

# funciton 1
def get_even_val():
    """Returns a user's input, repeating until the input is even, then returns that"""
    user_input = int(input("Enter an even integer:  "))
    while user_input % 2 != 0:
        user_input = int(input("The input must be even. Try again:  "))
    return user_input

def add_powers(m, n):
    """returns the sum of the first m powers of n"""
    sum = 0
    for x in range(m):
        sum += n ** x
        print(n, "**", x, "=", n ** x)
    return sum

