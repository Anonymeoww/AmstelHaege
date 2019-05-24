import start
import start_greedy_perhouse
import start_greedy_fullwijk
import start_greedy_wijkquadrants
import helpers
import HC
import SA
import visualize as vis

def mainstart(starter, HOUSES_NUMBER, BREADTH, HEIGHT):

    startmethods = [start, start_greedy_fullwijk, start_greedy_perhouse, start_greedy_wijkquadrants]
    startmethod = startmethods[starter-1]

    # Create first solution, determine surrounding space and show the map
    water_list, first_houses_list = startmethod.init(HOUSES_NUMBER, BREADTH, HEIGHT)
    houses_list = helpers.omlig_ruimte(water_list, first_houses_list, BREADTH, HEIGHT)
    for house in houses_list:
        house.update_worth()
    current_worth = helpers.waarde(houses_list)
    init_worth = current_worth
    vis.grid(water_list, houses_list, current_worth)

    return houses_list, water_list, init_worth


def mainsolve(solver, ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth):

    solvemethods = [HC, SA]
    solvemethod = solvemethods[solver - 1]

    # Optimize AmstelHaege
    houses_list = solvemethod.call(ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth)
    current_worth = helpers.waarde(houses_list)

    vis.grid(water_list, houses_list, current_worth)

def get_start(start):

    if start == 1:
        smethod = 'Random algorithm'
    elif start == 2:
        smethod = 'Greedy fullwijk algorithm'
    elif start == 3:
        smethod = 'Greedy per house algorithm'
    elif start == 4:
        smethod = 'Greedy quadrant algorithm'
    else:
        smethod = 'ERROR'

    return smethod

def get_solve(solve):

    if solve == 1:
        solmethod = 'Hillclimber algorithm'
    elif solve == 2:
        solmethod = 'Simulated Annealing algorithm'
    else:
        solmethod = 'ERROR'

    return solmethod