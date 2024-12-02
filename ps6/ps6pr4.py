#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the max price and its day')
    print('(5) Find the min single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    ## Add the new menu options here.

    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.

# function 1
def avg_price(prices):
    """returns the average price from a list containing prices as ints"""
    sum = 0
    for x in prices:
        sum += x
    return sum/len(prices)

# function 2
def max_day(prices):
    """returns the index of maximum price in a list of prices"""
    maximum = 0
    for x in range(len(prices)):
        if prices[x] >= prices[maximum]:
            maximum = x
    return maximum

# function 3
def min_change_day(prices):
    """returns the index of the day with the smallest absolute change in price """
    min_change = 1
    for x in range(1, len(prices)):
        print(f"first {prices[x-1] - prices[x]}")
        print(f"min_var {prices[min_change - 1] - prices[min_change - 1]}")
        if abs(prices[x-1] - prices[x]) < abs(prices[min_change - 1] - prices[min_change]):
            min_change = x
    return min_change

# function 4
def any_above(prices, value):
    for x in prices:
        if x > value:
            return True
    return False


# function 5
def find_tts(prices):
    """returns the best buy & sell date (index) given a list of prices along with the profit"""
    highest_profit = prices[1] - prices[0]
    buy_day = 0
    sell_day = 1
    for x in range(len(prices)-1):
        for i in range(x + 1, len(prices)):
            if prices[i] - prices[x] > highest_profit:
                buy_day = x
                sell_day = i
                highest_profit = prices[i] - prices[x]
    return [buy_day, sell_day, highest_profit]


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        
        ## add code to process the other choices here

        elif choice == 3:
            avg = avg_price(prices)
            print('The average price is', avg)
        elif choice == 4:
            maximum = max_day(prices)
            print('The max price is', prices[maximum])
            print("on day", maximum)
        elif choice == 5:
            change = min_change_day(prices)
            print("The min single-day change occurs on day", change)
            print("when the price goes from", prices[change - 1], "to", prices[change])
        elif choice == 6:
            thresh_val = int(choice("Enter the threshold: "))
            if any_above(prices, thresh_val):
                print("There is at least one price above", thresh_val)
            else:
                print("There are no prices above", thresh_val)
        elif choice == 7:
            result = find_tts(prices)
            print("Buy on day", result[0], "at price", prices[result[0]])
            print("Sell on day", result[1], "at price", prices[result[1]])
            print("Total profit:", result[2])
            
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
