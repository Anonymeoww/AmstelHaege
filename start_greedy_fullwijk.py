import helpers
import start

def init(houses_number, BREADTH, HEIGHT):
    """
    Initialiseert 3 random wijken, neemt de beste daarvan als startoplossing
    """
    worth = 0
    final_houses_list = []
    final_water_list = []
    for i in range(10):
        water_list, houses_list = start.init(houses_number, BREADTH, HEIGHT)
        new_worth = helpers.waarde(houses_list)

        if new_worth > worth:
            worth = new_worth
            final_water_list = water_list
            final_houses_list = houses_list

    return final_water_list, final_houses_list
