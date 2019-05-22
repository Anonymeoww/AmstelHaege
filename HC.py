import helpers
import visualize as vis

def call_HC(ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth):
    done_iterations = 0
    waardes = []
    waardes.append(current_worth/1000000)
    best_worth = current_worth

    while done_iterations < ITERATIONS:
        buur_houses_list = helpers.random_replace(HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT)
        buur_houses_list = helpers.omlig_ruimte(water_list, houses_list, BREADTH, HEIGHT)
        for buur in buur_houses_list:
            buur.update_worth()
        next_worth = helpers.waarde(buur_houses_list)

        if next_worth > current_worth:
            houses_list = buur_houses_list
            current_worth = next_worth

            if current_worth > best_worth:
                best_worth = current_worth
        done_iterations = done_iterations + 1
        waardes.append(best_worth / 1000000)
        # print(done_iterations)
    # wijk_id = 1
    # wijk = Wijk(wijk_id, current_worth, HOUSES_NUMBER, houses_list)
    # print(wijk)

    # vis.linegraph(done_iterations, waardes)
    vis.grid(water_list, houses_list, current_worth)

    return houses_list
