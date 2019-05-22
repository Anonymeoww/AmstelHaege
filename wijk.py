import visualize as vis
import callSA

import start_greedy_perhouse
import start
import start_greedy_fullwijk
import helpers
import HC
import start_greedy_wijkquadrants

"""
Hier komt een tekst te staan
"""

HOUSES_NUMBER = 20
BREADTH = 320
HEIGHT = 360
HILL_ITERATIONS = 500
ITERATIONS = 1000
startmethods = [start, start_greedy_fullwijk, start_greedy_perhouse, start_greedy_wijkquadrants]
startmethod = startmethods[2]

if __name__ == "__main__":

    # initieer wijk, plot, visualiseer en geef waarde aan huizen en wijk
    print("Initiate AmstelHaege...")
    houses_list = startmethod.init(HOUSES_NUMBER, BREADTH, HEIGHT)
    houses_list = helpers.omlig_ruimte(houses_list, BREADTH, HEIGHT)
    for house in houses_list:
        house.update_worth()
    current_worth = helpers.waarde(houses_list)
    init_worth = current_worth
    # best_worth = current_worth
    vis.grid(houses_list, current_worth)

    # for i in range (3):
    print("Running HillClimber..")
    houses_list = HC.call_HC(HILL_ITERATIONS, HOUSES_NUMBER, houses_list, BREADTH, HEIGHT, current_worth)

    current_worth = helpers.waarde(houses_list)

    print("Running Simulated Annealing..")
    houses_list = callSA.call_SA(HOUSES_NUMBER, ITERATIONS, houses_list, BREADTH, HEIGHT, current_worth)

    current_worth = helpers.waarde(houses_list)

    vis.grid(houses_list, current_worth)
    print(f"Change from {init_worth} to {current_worth}")
