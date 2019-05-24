import visualize as vis
import SA

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
ITERATIONS = 5000
startmethods = [start, start_greedy_fullwijk, start_greedy_perhouse, start_greedy_wijkquadrants]
startmethod = startmethods[0]

if __name__ == "__main__":

    # initieer wijk, plot, visualiseer en geef waarde aan huizen en wijk
    print("Initiate AmstelHaege...")
    water_list, houses_list = startmethod.init(HOUSES_NUMBER, BREADTH, HEIGHT)
    first_houses_list = helpers.omlig_ruimte(water_list, houses_list, BREADTH, HEIGHT)
    for house in houses_list:
        house.update_worth()
    current_worth = helpers.waarde(houses_list)
    init_worth = current_worth
    # best_worth = current_worth
    vis.grid(water_list, houses_list, current_worth)

    # for i in range (3):
    print("Running HillClimber..")
    waardes_HC, houses_list_HC = HC.call(ITERATIONS, HOUSES_NUMBER, water_list, first_houses_list, BREADTH, HEIGHT, init_worth)

    current_worth = helpers.waarde(houses_list)

    print("Running Simulated Annealing..")
    waardes_SA, houses_list_SA = SA.call(ITERATIONS, HOUSES_NUMBER, water_list, first_houses_list, BREADTH, HEIGHT, init_worth)

    vis.linegraph_compare(ITERATIONS, waardes_HC, waardes_SA)

    # current_worth = helpers.waarde(houses_list, houses_list_SA)

    # vis.grid(houses_list, current_worth)
    print(f"Change from {init_worth} to {current_worth}")
