import visualize as vis
import callSA

import start_greedy_perhouse
import start
import start_greedy_fullwijk
import helpers

"""
Hier komt een tekst te staan
"""

HOUSES_NUMBER = 20
BREADTH = 320
HEIGHT = 360
ITERATIONS = 1000
startmethods = [start, start_greedy_fullwijk, start_greedy_perhouse]
startmethod = startmethods[2]

if __name__ == "__main__":

    # initieer wijk, plot , visualiseer en geef waarde aan huizen en wijk
    houses_list = startmethod.init(HOUSES_NUMBER, BREADTH, HEIGHT)
    #print(houses_list)
    houses_list = helpers.omlig_ruimte(houses_list, BREADTH, HEIGHT)
    #print(houses_list)
    houses_list, curr_waarde = helpers.waarde(houses_list)
    #print(f"Waarde wijk: {curr_waarde}")
    best_worth = curr_waarde
    vis.grid(houses_list, best_worth)

    callSA.callSA(HOUSES_NUMBER, houses_list, BREADTH, HEIGHT, curr_waarde, best_worth)