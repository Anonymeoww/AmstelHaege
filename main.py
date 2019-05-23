import visualize as vis
import SA
import start_greedy_perhouse
import start
import start_greedy_fullwijk
import helpers
import HC
import start_greedy_wijkquadrants
from wijken import Wijk

HOUSES_NUMBER = 0
BREADTH = 320
HEIGHT = 360
ITERATIONS = 0
wijk_list = []
startmethods = [start, start_greedy_fullwijk, start_greedy_perhouse, start_greedy_wijkquadrants]
solvemethods = [HC, SA]

if __name__ == "__main__":
    """
    Ask user for methods, and create AmstelHaege
    """
    print("Welcome to the AmstelHaege generator. Please choose the amount of houses (20, 40 or 60) and the method"
          "for generating the first neighbourhood. For more information on the methods and algorithms please look at "
          "the README.\n")

    HOUSES_NUMBER = int(input("Size (20, 40, 60): "))
    while (HOUSES_NUMBER != 20):
        print("Please choose between 20, 40 or 60 houses.")
        HOUSES_NUMBER = int(input("Size (20, 40, 60): "))

    print("1: Random \n 2: Greedy fullwijk \n 3: Greedy per house \n 4: Greedy quadrants")
    start = int(input("Startmethod: "))
    startmethod = startmethods[start-1]
    smethod = helpers.get_start(start)

    ITERATIONS = int(input("Iterations: "))

    print("Initiate AmstelHaege using {}...".format(smethod))

    # Create first solution, determine surrounding space and show the map
    water_list, first_houses_list = startmethod.init(HOUSES_NUMBER, BREADTH, HEIGHT)
    houses_list = helpers.omlig_ruimte(water_list, first_houses_list, BREADTH, HEIGHT)
    for house in houses_list:
        house.update_worth()
    current_worth = helpers.waarde(houses_list)
    init_worth = current_worth
    vis.grid(water_list, houses_list, current_worth)

    solve = int(input("Solvemethod: "))
    solvemethod = solvemethods[solve-1]
    solmethod = helpers.get_solve(solve)

    ITERATIONS2 = int(input("Iterations: "))

    print("Running {}...".format(solmethod))

    # Optimize AmstelHaege
    houses_list = solvemethod.call(ITERATIONS2, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth)
    current_worth = helpers.waarde(houses_list)
    wijk = Wijk(1, current_worth, HOUSES_NUMBER, houses_list)
    wijk_list.append(wijk)
    vis.grid(water_list, houses_list, current_worth)
    print(wijk_list)
    print(f"Change from {init_worth} to {current_worth}")

