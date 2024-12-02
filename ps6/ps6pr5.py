#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# 2-D Lists
#
# Computer Science 111
# 

import random

def create_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of 0s with the specified dimensions.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = []
    
    for r in range(num_rows):
        row = [0] * num_cols     # a row containing width 0s
        grid += [row]

    return grid

def print_grid(grid):
    """ prints the 2-D list specified by grid in 2-D form,
        with each row on its own line.
        input: grid is a 2-D list
    """
    num_rows = len(grid)
    for r in range(num_rows):
        if r == 0:
            print('[', end='')
        else:
            print(' ', end='')
        if r < num_rows - 1:
            print(str(grid[r]) + ',')
        else:
            print(str(grid[r]) + ']')

def random_grid(num_rows, num_cols):
    """ creates and returns a 2-D list with the specified dimensions
        in which each cell is assigned a random integer from 0-9.
        inputs: num_rows and num_cols are non-negative integers
    """
    grid = create_grid(num_rows, num_cols)

    for r in range(num_rows):
        for c in range(num_cols):
            grid[r][c] = random.choice(range(10))
            
    return grid

# function 1
def col_index_grid(num_rows, num_cols):
    """ creates and returns a 2-D list of numbers corresponding with the index of their column with the specified dimensions."""
    grid = []
    row = []
    col_count = 0
    for r in range(num_cols):
        row += [col_count]     # a row containing width 0s
        col_count += 1
    for x in range(num_rows):
        grid += [row]
    return grid

# function 2
def num_between(grid, n1, n2):
    """returns the number of values in grid that are in between (inclusive) n1 and n2"""
    count = 0
    for row in grid:
        for val in row:
            if n1 <= val <= n2:
                count += 1
    return count

# function 3
def copy(grid):
    """returns a 'deep copy' of a given grid"""
    newgrid = []
    for row in range(len(grid)):
        newrow = []
        for val in range(len(grid[row])):
            newrow += [grid[row][val]]
        newgrid += [newrow]
    return newgrid

# function 4
def double_with_cap(grid, cap):
    """modifies a 2-D grid by doubling every number within it, but capping the new values to be equal to or lower than int cap. Does not return anything, rather it just modifies the internals of the list"""
    for row in range(len(grid)):
        for item in range(len(grid[0])):
            if (grid[row][item] * 2) > cap:
                grid[row][item] = cap
            else:
                grid[row][item] *= 2

# function 5
def sum_evens_in_col(grid, colnum):
    """returns the sum of the even values in selected column colnum"""
    sum = 0
    for row in grid:
        if row[colnum] % 2 == 0:
            sum += row[colnum]
    return sum
