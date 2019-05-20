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

HOUSES_NUMBER = 60
BREADTH = 320
HEIGHT = 360
ITERATIONS = 500
startmethods = [start, start_greedy_fullwijk, start_greedy_perhouse, start_greedy_wijkquadrants]
startmethod = startmethods[3]

if __name__ == "__main__":

    # initieer wijk, plot, visualiseer en geef waarde aan huizen en wijk
    print("Initiate AmstelHaege...")
    houses_list = startmethod.init(HOUSES_NUMBER, BREADTH, HEIGHT)
    houses_list = helpers.omlig_ruimte(houses_list, BREADTH, HEIGHT)
    current_worth = helpers.waarde(houses_list)
    best_worth = current_worth
    vis.grid(houses_list, best_worth)

    print("Running HillClimber..")
    # HC.call_HC(ITERATIONS, HOUSES_NUMBER, houses_list, BREADTH, HEIGHT, current_worth, best_worth)

    print("Running Simulated Annealing..")
    # callSA.call_SA(HOUSES_NUMBER, ITERATIONS, houses_list, BREADTH, HEIGHT, current_worth, best_worth)
