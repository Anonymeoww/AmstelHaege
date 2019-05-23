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
    HOUSES_NUMBER = int(input("Size (20, 40, 60): "))
    start = int(input("Startmethod: "))
    startmethod = startmethods[start-1]
    if start == 1:
        smethod = 'Random algorithm'
    elif start == 2:
        smethod = 'Greedy fullwijk algorithm'
    elif start == 3:
        smethod = 'Greedy per house algorithm'
    elif start == 4:
        smethod = 'Greedy quadrant algorithm'

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

    if solvemethod == 1:
        solmethod = 'Hillclimber algorithm'
    elif solvemethod == 2:
        solmethod = 'Simulated Annealing algorithm'

    #print("Running {}...".format(solmethod))

    # Optimize AmstelHaege
    houses_list = solvemethod.call(ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth)
    current_worth = helpers.waarde(houses_list)
    wijk = Wijk(1, current_worth, HOUSES_NUMBER, houses_list)
    wijk_list.append(wijk)
    vis.grid(water_list, houses_list, current_worth)
    print(wijk_list)
    print(f"Change from {init_worth} to {current_worth}")

