import visualize as vis
import mainfunctions
import sys

HOUSES_NUMBER = 0
BREADTH = 320
HEIGHT = 360
ITERATIONS = 0
houses_list = []
water_list = []
maxis1 = []
maxis2 = []
waardes1 = 0
waardes2 = 0
init_worth = 0
max1 = 0
max2 = 0
maxi1 = 0
maxi2 = 0
initiating = True

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

    while initiating == True:

        print("Choose method of initiating: \n"
              "1: Random \n2: Greedy fullwijk \n3: Greedy per house \n 4:Greedy quadrants")

        methods1 = [1, 2, 3, 4]
        start = int(input("Startmethod: "))
        while (start not in methods1):
            print("Please choose between the given methods")
            start = int(input("Startmethod: "))

        smethod = mainfunctions.get_start(start)
        print("Initiate AmstelHaege using {}...".format(smethod))

        houses_list, water_list, init_worth = mainfunctions.mainstart(start, HOUSES_NUMBER, BREADTH, HEIGHT)

        answers = [1, 2]
        print("This is the initial neighbourhood. Would you like to \n"
              "1: Generate a new neighbourhood \n2: Optimize the current neighbourhood")
        answer = int(input("Option: "))
        while (answer not in answers):
            print("Please choose between the given options")
            answer = int(input("Option: "))

        if answer == 1:
            initiating = True
        elif answer == 2:
            break
        else:
            print("ERROR")

    print("Please choose the amount of runs and iterations.")

    runs = int(input("Runs: "))
    ITERATIONS = int(input("Iterations: "))

    print("Running ...")

    for run in range(runs):
        solve = 1
        waardes1 = mainfunctions.mainsolve(solve, ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, init_worth)
        waardes2 = mainfunctions.mainsolve(solve, ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, init_worth)
        maxi1 = mainfunctions.write_results(waardes1, run+1)
        maxi2 = mainfunctions.write_results(waardes2, run + 1)
        maxis1.append(maxi)
        if maxi1 > max1:
            max1 = maxi
        if maxi2 > max2:
            max2 = maxi
        # print(waardes1)
    print(f"AmstelHaege HC changed from {init_worth/1000000} to {max1}")
    print(f"AmstelHaege SA changed from {init_worth/1000000} to {max2}")


    # print("This is the optimized map! Do you want to use another algorithm on this map?")
    # answer2 = input("Y/N: ")
