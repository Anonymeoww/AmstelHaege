import visualize as vis
import mainfunctions
import locale
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
              "1: Random \n2: Greedy fullwijk \n3: Greedy per house \n4:Greedy quadrants")

        methods1 = [1, 2, 3, 4]
        start = int(input("Startmethod: "))
        while (start not in methods1):
            print("Please choose between the given methods")
            start = int(input("Startmethod: "))

        smethod = mainfunctions.get_start(start)
        print("\nInitiate AmstelHaege using {}...".format(smethod))

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

    print("\nPlease choose the amount of runs and iterations.")

    runs = int(input("Runs: "))
    ITERATIONS = int(input("Iterations: "))

    print("\nRunning ...")
    row = -1
    for run in range(runs):
        row = row + 1
        solve1 = 1
        solve2 = 2
        waardes1 = mainfunctions.mainsolve(solve1, ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, init_worth)
        waardes2 = mainfunctions.mainsolve(solve2, ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, init_worth)
        max1 = mainfunctions.write_results(waardes1, row + 1)
        row = row + 1
        max2 = mainfunctions.write_results(waardes2, row + 1)
        print(f"{run+1}/{runs} runs complete")
        vis.linegraph_compare(ITERATIONS+1, waardes1, waardes2)
    locale.setlocale(locale.LC_ALL, '')
    value1 = locale.currency(max1*1000000, grouping=True)
    value2 = locale.currency(max2*1000000, grouping=True)
    init_value = locale.currency(init_worth, grouping=True)
    print(f"AmstelHaege HC changed from {init_value} to {value1}")
    print(f"AmstelHaege SA changed from {init_value} to {value2}")
