'''
    Program: Magical Calculator
    Author: Sviatoslav Balema
    Copyright: 2025
'''


import re

def perform_math():
    run = True
    equation = None
    previous = ''

    print("Welcome to the calculator.")
    print("Type 'clear' to clear previous calculation.")
    print("Type 'quit' to exit.")

    while run:
        # If there has been a previous calculation:
        if previous == '':
            equation = input("Starting with: ")
        else:
            equation = input(f"{str(previous)}")

        # If user quits:
        if equation == "quit":
            run = False
        # If user clears the previous calculation:
        elif equation == "clear":
            previous = ''
            print("You cleared the previous calculation.")
            continue
        else:
            # Cleaning the input string:
            if previous == '':
                equation =  re.sub('[a-zA-Z,:()" "/*]', '', equation)
            else:
                equation = re.sub('[a-zA-Z,:()" "]', '', equation)

            # Deleting "." if it's a first symbol:
            if len(equation)>0 and equation[0] == '.':
                equation = equation[1:]

            # Printing the result:
            if equation == '':
                print("You typed: ", equation)
            else:
                previous = eval(str(previous) + equation)
                print("You typed:", equation)

    print("Exiting...")
    return

if __name__ == '__main__':
    perform_math()