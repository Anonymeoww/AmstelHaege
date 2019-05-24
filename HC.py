import helpers
import visualize as vis

def call(ITERATIONS, HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT, current_worth):
    """
    Executes a hillclimber algorithm on houses_list
    """

    done_iterations = 0
    waardes = []
    waardes.append(current_worth/1000000)
    best_worth = current_worth


    while done_iterations < ITERATIONS:

        # Create neighbouring solution (a random house moved 0,5 meter to a random direction)
        buur_houses_list = helpers.random_replace(HOUSES_NUMBER, water_list, houses_list, BREADTH, HEIGHT)

        # calculate free space for neighbouring solution and calculate worth
        buur_houses_list = helpers.omlig_ruimte(water_list, houses_list, BREADTH, HEIGHT)
        for buur in buur_houses_list:
            buur.update_worth()
        next_worth = helpers.waarde(buur_houses_list)

        # if the new worth is higher than or equal to the current worth, accept the solution
        if next_worth >= current_worth:
            houses_list = buur_houses_list
            current_worth = next_worth

            # if the newly accepted worth is also the highest ever, save it
            if current_worth > best_worth:
                best_worth = current_worth
        done_iterations = done_iterations + 1
        waardes.append(best_worth / 1000000)

    return waardes, houses_list
