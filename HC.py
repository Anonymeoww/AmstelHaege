import SA
import helpers
import visualize as vis

def call_HC(ITERATIONS, HOUSES_NUMBER, houses_list, BREADTH, HEIGHT, current_worth, best_worth):
    done_iterations = 0
    waardes = []
    waardes.append(current_worth)

    while done_iterations < ITERATIONS:
        buur_houses_list = SA.random_replace(HOUSES_NUMBER, houses_list, BREADTH, HEIGHT)
        buur_houses_list = helpers.omlig_ruimte(buur_houses_list, BREADTH, HEIGHT)
        for buur in buur_houses_list:
            buur.update_worth()
        next_worth = helpers.waarde(buur_houses_list)
        if next_worth > current_worth:
            waardes.append(next_worth)
            houses_list = buur_houses_list
            current_worth = next_worth
            if current_worth > best_worth:
                best_worth = current_worth
        done_iterations = done_iterations + 1

    print(waardes)
    vis.linegraph(waardes)
    vis.grid(houses_list, current_worth)
