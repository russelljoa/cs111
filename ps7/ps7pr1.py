# 
# ps7pr1.py - Problem Set 7, Problem 1
#
# String-method puzzles
#

s1 = 'Hickory Dickory Dock!'
s2 = 'The mouse ran up the clock.'

# Puzzle 0 (example)
answer0 = s2.lower().count('t')    


# Put your solutions to the remaining string puzzles below.

# Puzzle 1
answer1 = s1.replace('ck', 'll')

# Puzzle 2
answer2 = s2.split('e')

# Puzzle 3
answer3 = s1.lower().split('ck')

# Puzzle 4
answer4 = s1.upper().replace('HICK', '').replace('DICK', '').replace('D', 'H')

# Puzzle 5
answer5 = s2.upper().split("E ")



# The code below tests the values of your expressions. DO NOT MODIFY IT!
if __name__ == '__main__':    
    for n in range(0, 6):
        answer_var = 'answer' + str(n)
        if answer_var in dir():
            print(answer_var, '=', eval(answer_var))
