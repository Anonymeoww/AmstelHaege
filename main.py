import visualize as vis
from wijken import Wijk
import mainfunctions
import sys

HOUSES_NUMBER = 0
BREADTH = 320
HEIGHT = 360
ITERATIONS = 0
wijk_list = []
solving = True

if __name__ == "__main__":
    """
    Ask user for methods, and create AmstelHaege
    """
    print("Welcome to the AmstelHaege generator. Please choose the amount of houses (20, 40 or 60) and the method"
          "for generating the first neighbourhood. For more information on the methods and algorithms please look at "
          "the README.\n")

    sizes = [20, 40, 60]
    HOUSES_NUMBER = int(input("Size (20, 40, 60): "))
    while (HOUSES_NUMBER not in sizes):
        print("Please choose between 20, 40 or 60 houses.")
        HOUSES_NUMBER = int(input("Size (20, 40, 60): "))

    print("1: Random \n 2: Greedy fullwijk \n 3: Greedy per house \n 4: Greedy quadrants")

    methods1 = [1, 2, 3, 4]
    start = int(input("Startmethod: "))
    while (start not in methods1):
        print("Please choose between the given methods")
        start = int(input("Startmethod: "))

    smethod = mainfunctions.get_start(start)
    print("Initiate AmstelHaege using {}...".format(smethod))

    houses_list, water_list, init_worth = mainfunctions.mainstart(start, HOUSES_NUMBER, BREADTH, HEIGHT)

    print("This is the initial neighbourhood. Would you like to optimize this neighbourhood?")
    answer = input("Y/N: ")

    if answer == 'N':
        solving = False
        print("Goodbye!")
        sys.exit(0)

    elif answer == 'Y':
        solving = True

    while solving == True:

        print("Please choose an algorithm. \n1: Hillclimber \n2: Simulated Annealing \n")
        methods2 = [1, 2]
        solve = int(input("Solvemethod: "))
        while (solve not in methods2):
            print("Please choose between the given methods")
            solve = int(input("Solve method: "))

        ITERATIONS = int(input("Iterations: "))

        solmethod = mainfunctions.get_solve(solve)
        print("Running {}...".format(solmethod))

        mainfunctions.mainsolve(solve, ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, init_worth)
        wijk = Wijk(1, current_worth, HOUSES_NUMBER, houses_list)
        wijk_list.append(wijk)

        print(wijk_list)
        print(f"AmstelHaege changed from {init_worth} to {current_worth}")

        print("This is the optimized map! Do you want to use another algorithm on this map?")
        answer2 = input("Y/N: ")

        if answer2 == 'N':
            solving = False
            print("Goodbye!")
            sys.exit(0)

        elif answer2 == 'Y':
            solving = True