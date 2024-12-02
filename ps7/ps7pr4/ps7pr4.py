# 
# ps7pr4.py - Problem Set 7, Problem 4
#
# Processing databases
#

# funciton 1
def main():
    """contains the main user-interaction loop"""
    init_file = input("Enter the name of data file: ")
    while True:
        if init_file == "quit":
            break
        city_name = input("city: ")
        if city_name == "quit":
            break
        state = input("state abbreviation: ").upper()
        if state.lower() == "quit":
            break
        parse_file(init_file, city_name, state)

# function 2
def parse_file(init_file, city_name, state):
    """prints city data based on a given file, city name, and state abbreviation, and formats the data accordingly"""
    file = open(init_file, "r")
    line_count = 0
    for line in file:
        line = line[:-1]
        fields = line.split(",")
        if fields[2] == city_name and fields[3] == state:
            pop = int(float(fields[4]) * 1000)
            print(fields[0] + '\t' + fields[1] + '\t' + format(pop, '10,d'))
            line_count += 1
    if line_count == 0:
        print("no results found for", city_name +  "," , state)
    file.close()

main()