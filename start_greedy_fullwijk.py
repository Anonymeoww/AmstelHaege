import helpers
import start

def init(houses_number, BREADTH, HEIGHT):
    """
    Initializes 10 random neighbourhoods, picks the best one as starting solution
    """
    worth = 0
    final_houses_list = []
    final_water_list = []

    # initialize 10 random neighbourhoods
    for i in range(10):
        water_list, houses_list = start.init(houses_number, BREADTH, HEIGHT)
        new_worth = helpers.waarde(houses_list)

        # if the new worth is higher than the current one, save solution
        if new_worth > worth:
            worth = new_worth
            final_water_list = water_list
            final_houses_list = houses_list

    return final_water_list, final_houses_list
