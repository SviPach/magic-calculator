import re

def perform_math():
    run = True
    equation = None
    previous = ''

    print("Welcome to the calculator.")
    print("Type 'quit' to exit.")

    while run:
        if previous == '':
            equation = input("Starting with: ")
        else:
            equation = input(f"{str(previous)}")

        if equation == "quit":
            run = False
        else:
            equation = re.sub('[a-zA-Z,:()" "]', '', equation)
            if equation == '':
                print("You typed: ", equation)
            else:
                previous = eval(str(previous) + equation)
                print("You typed:", equation)

    print("Exiting...")
    return

if __name__ == '__main__':
    perform_math()