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
        # If there has been a previous calculation ->
        if previous == '':
            equation = input("Starting with: ")
        else:
            equation = input(f"{str(previous)}")

        # If user quits ->
        if equation == "quit":
            run = False

        # If user clears the previous calculation ->
        elif equation == "clear":
            previous = ''
            print("You cleared the previous calculation.")
            continue
        else:
            # Cleaning the input string ->
            equation =  re.sub('[a-zA-Z,:()" \\\\]', '', equation)

            if previous == '':
                # Deleting '*' and '/' if it's the first symbol ->
                while equation[0] == '*' or equation[0] == '/':
                    equation = equation[1:]

            i = 0

            # Check for "*/" and "/*" and if found, delete the second character ->
            equation = list(equation)
            while i != len(equation) - 1:
                for i in range(len(equation)):
                    if i == len(equation) - 1:
                        break
                    if (
                            equation[i] + equation[i + 1] == '/*'
                            or
                            equation[i] + equation[i + 1] == '*/'
                    ):
                        equation[i+1] = ''
                        equation = ''.join(equation)
                        equation = list(equation)
                        i = 0
                        break
            equation = ''.join(equation)

            # Check if the last character of the equation is '*' or '/':
            while (
                    equation[len(equation) - 1] == '/'
                    or
                    equation[len(equation) - 1] == '*'
            ):
                equation = equation[:len(equation) - 1]

            # Check for "...***..." and "...///..." and if found, delete until 2 of them left ->
            if len(equation) > 1:
                equation = list(equation)
                while i != 1:
                    for i in range(len(equation) - 1, -1, -1):
                        if i == 1:
                            break
                        if (
                                equation[i] + equation[i - 1] + equation[i - 2] == '***'
                                or
                                equation[i] + equation[i - 1] + equation[i - 2] == '///'
                        ):
                            equation[i] = ''
                            equation = ''.join(equation)
                            equation = list(equation)
                            i = len(equation) - 1
                            break
                equation = ''.join(equation)

            # Deleting "." if it's a first symbol ->
            if len(equation)>0 and equation[0] == '.':
                equation = equation[1:]

            # Printing the result ->
            if equation == '':
                print("You typed: ", equation)
            else:
                previous = eval(str(previous) + equation)
                print("You typed:", equation)

    print("Exiting...")
    return

if __name__ == '__main__':
    perform_math()