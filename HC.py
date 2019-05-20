import helpers
import visualize as vis

def call_HC(ITERATIONS, HOUSES_NUMBER, houses_list, BREADTH, HEIGHT, current_worth, best_worth):
    done_iterations = 0
    waardes = []
    waardes.append(current_worth/1000000)

    while done_iterations < ITERATIONS:
        buur_houses_list = helpers.random_replace(HOUSES_NUMBER, houses_list, BREADTH, HEIGHT)
        buur_houses_list = helpers.omlig_ruimte(buur_houses_list, BREADTH, HEIGHT)
        for buur in buur_houses_list:
            buur.update_worth()
        next_worth = helpers.waarde(buur_houses_list)
        waardes.append(next_worth / 1000000)
        if next_worth > current_worth:
            houses_list = buur_houses_list
            current_worth = next_worth
            if current_worth > best_worth:
                best_worth = current_worth
        done_iterations = done_iterations + 1
        print(done_iterations)
    # wijk_id = 1
    # wijk = Wijk(wijk_id, current_worth, HOUSES_NUMBER, houses_list)
    # print(wijk)
    iter = len(waardes)
    vis.linegraph(iter, waardes)
    vis.grid(houses_list, current_worth)
