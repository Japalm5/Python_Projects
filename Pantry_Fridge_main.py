# SMART FOOD SOURCE CODE
import shelve
from pathlib import Path

current_directory = Path.cwd()
path_persistent = current_directory.joinpath("smart_inventory_persistent_files")
path_smart_pantry = str(path_persistent.joinpath("smart_pantry_inventory"))
path_smart_fridge = str(path_persistent.joinpath("smart_fridge_inventory"))
path_smart_selection = str(path_persistent.joinpath("smart_selection"))
path_smart_recipes = str(path_persistent.joinpath("smart_recipes"))
if not Path.exists(path_persistent):
    Path.mkdir(path_persistent)

    smart_pantry_inventory = shelve.open(path_smart_pantry)

    smart_pantry_inventory["oatmeal"] = '30'
    smart_pantry_inventory["banana"] = '5'
    smart_pantry_inventory["blueberry"] = '30'
    smart_pantry_inventory["apple"] = '0'
    smart_pantry_inventory["kiwi"] = '6'
    smart_pantry_inventory["strawberry"] = '10'
    smart_pantry_inventory["potato"] = '3'

    smart_pantry_inventory.close()

    smart_fridge_inventory = shelve.open(path_smart_fridge)

    smart_fridge_inventory["milk"] = "1"
    smart_fridge_inventory["steak"] = "2"
    smart_fridge_inventory["butter"] = "4"

    smart_fridge_inventory.close()

    smart_selection = shelve.open(path_smart_selection)

    smart_selection['1'] = "Apple Oatmeal"
    smart_selection["2"] = "Strawberry Oatmeal"
    smart_selection["3"] = "Blueberry Oatmeal"
    smart_selection["4"] = "Banana Oatmeal"
    smart_selection["5"] = "Kiwi Oatmeal"
    smart_selection["6"] = "Apple Oatmeal with Steak"
    smart_selection["7"] = "Kiwi Oatmeal with Steak and Potatoes"
    smart_selection["8"] = "Potatoes and Steak"
    smart_selection["9"] = "Blueberry Oatmeal and Potatoes"

    smart_selection.close()

    smart_recipes = shelve.open(path_smart_recipes)

    smart_recipes["Apple Oatmeal"] = [".5 apple", "3 oatmeal", ".1 milk"]
    smart_recipes["Strawberry Oatmeal"] = ["3 strawberry", "3 oatmeal", ".1 milk"]
    smart_recipes["Blueberry Oatmeal"] = ["12 blueberry", "3 oatmeal", ".1 milk"]
    smart_recipes["Banana Oatmeal"] = [".5 banana", "3 oatmeal", ".1 milk"]
    smart_recipes["Kiwi Oatmeal"] = ["1 kiwi", "3 oatmeal", ".1 milk"]
    smart_recipes["Apple Oatmeal with Steak"] = [".5 apple", "3 oatmeal", ".1 milk", "1 steak"]
    smart_recipes["Kiwi Oatmeal with Steak and Potatoes"] = ["1 kiwi", "3 oatmeal", ".1 milk", "1 steak", "2 potatoes"]
    smart_recipes["Potatoes and Steak"] = ["2 potatoes", "1 steak"]
    smart_recipes["Blueberry Oatmeal and Potatoes"] = ["12 blueberry", "3 oatmeal", ".1 milk", "2 potatoes"]

    smart_recipes.close()


def check_dict(dictionary, items_passed_in) -> bool:
    """
    checks if adequate quantities of ingredients are available. if not, the variable 'switch' is set to
    false and returned
    :param dictionary: the dictionary containing the required ingredient
    :param items_passed_in: the ingredients and their quantities needed
    :return: whether adequate amounts of the ingredient are available
    """

    # for key2, value2 in dictionary.items():
    value_to_compare = dictionary.get(items_passed_in[1])
    # if items[1] == key2 and float(items[0]) <= float(value2):
    if float(items_passed_in[0]) <= float(value_to_compare):
        print(f"adequate amount of {items_passed_in[1]}")
        return True
    # elif items[1] == key2 and float(items[0]) > float(value2):
    elif float(items_passed_in[0]) > float(value_to_compare):
        print(f"there is not enough {items_passed_in[1]}")
        return False


def apply_meal_cost(dictionary):
    """
    applies changes to quantities if ingredients of specified recipe are available
    :param dictionary: the dictionary containing the required ingredient
    """
    value_to_compare = dictionary.get(items[1])
    if float(items[0]) <= float(value_to_compare):
        dictionary[items[1]] = float(value_to_compare) - float(items[0])


def print_dict(dictionary) -> str:
    """
    user specifies dictionary and item to change quantity of. User can specify new item. item is returned.
    :param dictionary: the dictionary containing the item to change quantity of.
    :return: the item in the dictionary to change quantity of.
    """
    counter = 1
    grocery_choice = None
    temp_grocery_table = {}
    item_to_change_assign = ''

    for key3, value3 in dictionary.items():
        temp_grocery_table[counter] = key3
        counter += 1
    temp_grocery_table[counter] = "Enter a new ingredient"
    temp_grocery_table[0] = "Exit to previous screen"

    while grocery_choice not in temp_grocery_table.keys() and grocery_choice != 0:
        for key5, value5 in temp_grocery_table.items():
            print(f"{key5}: {value5}")  # prints indexed fridge or pantry dict keys
        grocery_choice = (input("What is your selection: "))
        validation2 = validation_check(grocery_choice, int, counter)
        if validation2 is False:
            continue
        grocery_choice = int(grocery_choice)
        if grocery_choice in range(1, counter):  # counter - 1 is maximum valid values to return
            item_to_change_assign = temp_grocery_table[grocery_choice]
        elif grocery_choice == counter:
            grocery_choice = input("what item would you like to add? (please use the singular noun of the item): ") \
                .lower()
            item_to_change_assign = temp_grocery_table[counter] = grocery_choice
            print(f"added {grocery_choice} to your inventory.")
            break
        elif grocery_choice == 0:
            break
        else:
            print("Enter a valid selection")
    # item_to_change_assign = temp_grocery_table[grocery_choice]
    return item_to_change_assign


def check_for_key_to_delete(dictionary) -> str:
    """
    Validates ingredient selection to delete
    :param dictionary: The dictionary to check if the ingredient exists
    :return: either '0' to back out of selection or the ingredient name to delete from specified dictionary
    """
    dict_counter = 1
    temp_grocery_table = {}
    delete_ingredient_number = None

    for dict_key in dictionary.keys():
        temp_grocery_table[dict_counter] = dict_key
        dict_counter += 1
    temp_grocery_table[0] = "Exit to previous screen"

    while delete_ingredient_number not in temp_grocery_table.keys() and delete_ingredient_number != 0:
        for key5, value5 in temp_grocery_table.items():
            print(f"{key5}: {value5}")  # prints indexed fridge or pantry dict keys
        delete_ingredient_number = input("What item do you want to delete?: ")
        validation1 = validation_check(delete_ingredient_number, int, dict_counter)
        if validation1 is False:
            print("this is an invalid selection")
            continue
        delete_ingredient_number = int(delete_ingredient_number)
        if delete_ingredient_number in range(1, dict_counter):  # dict_counter -1 is maximum valid choice
            delete_ingredient_key = temp_grocery_table[delete_ingredient_number]
            return delete_ingredient_key
        elif delete_ingredient_number == 0:
            return str(delete_ingredient_number)


def check_ingredient_in_recipes(dictionary, ingredient) -> bool:
    """
    checks if the specified ingredient is in a current recipe.
    :param dictionary: the recipe dictionary
    :param ingredient: the ingredient in question
    :return: returns true if ingredient is in the dictionary.
    """
    active_ingredients_list = []
    for value7 in dictionary.values():
        for contents in value7:
            active_ingredients = contents.split(" ")
            active_ingredients = active_ingredients[1::1]
            active_ingredients = ''.join(active_ingredients)
            active_ingredients_list.append(active_ingredients)
    active_ingredients_set = set(active_ingredients_list)
    if ingredient in active_ingredients_set:
        return True
    else:
        return False


def update_dict(dictionary, item_to_change_passed_in) -> dict:
    """
    Takes key returned in function "print_dict) and the dictionary where it resides. asks user to provide new quantity
    for the key and returns updated dictionary.
    :param dictionary: The current specified dictionary containing item with quantity to change
    :param item_to_change_passed_in: the item to change quantity of.
    :return: updated dictionary.
    """
    error_tracker = 0
    if item_to_change_passed_in in dictionary.keys():
        print(f"the current quantity for {item_to_change_passed_in} is {dictionary[item_to_change_passed_in]}")
        while error_tracker == 0:
            new_quantity = input(f"How many units of {item_to_change_passed_in} are available? ")
            try:
                float(new_quantity)
                error_tracker = 1
            except ValueError:
                print("this is not a valid number")
            dictionary[item_to_change_passed_in] = new_quantity
    for key6, value6 in dictionary.items():
        print(f"{key6}: {value6}")
    return dictionary


def validation_check(variable_to_check, variable_type, max_selection) -> bool:
    """
    Performs checks to ensure user input convertible to the correct variable type and is within desired range
    :param variable_to_check: the user input in question
    :param variable_type: The type that the variable should be able to convert to without a ValueError
    :param max_selection: An integer 1 number higher than the maximum input expected in the variable
    :return: False is checks on variable failed, True if checks on variable passed
    """
    try:
        variable_to_check = variable_type(variable_to_check)
    except ValueError:
        print("This is not a valid selection")
        return False
    if variable_to_check not in range(0, int(max_selection + 1)):
        print("This is not a valid selection")
        return False
    return True


update_choice = None
choice = None
active_list = []
del_counter = 0

while choice != "0":
    smart_selection = shelve.open(path_smart_selection)
    smart_recipes = shelve.open(path_smart_recipes)
    more_ingredient_validation = False
    del_counter = 0
    switch = True  # is true until quantity needed for item in recipe is not in inventory

    for key, value in smart_selection.items():
        print(f"{key}: {value}")
    print("Enter 'a' to add groceries or recipes")
    print("Enter 'd' to delete ingredient items or recipes")
    print("Enter '0' to exit")

    choice = input("what is your selection? ")

    while choice in smart_selection.keys():

        print(f"You selected: {smart_selection[choice]}")
        print("checking inventory...")
        identified_value = smart_recipes.get(smart_selection[choice])
        smart_selection.close()
        smart_recipes.close()

        for items in identified_value:
            quantity_identifier = items.split(" ")
            active_list.append(quantity_identifier)  # recipe ingredients are separated from quantity to use

        inadequateAmount = False  # is false until the first time switch becomes false

        smart_pantry_inventory = shelve.open(path_smart_pantry)
        smart_fridge_inventory = shelve.open(path_smart_fridge)

        for items in active_list:
            if items[1] in smart_pantry_inventory:
                switch = check_dict(smart_pantry_inventory, items)
                # if ingredient quantity is insufficient, switch returns false

            elif items[1] in smart_fridge_inventory:
                switch = check_dict(smart_fridge_inventory, items)
                # if ingredient quantity is insufficient, switch returns false

            if switch is False:
                inadequateAmount = True

        smart_selection = shelve.open(path_smart_selection)

        if inadequateAmount is False:  # is false if switch never becomes false
            print("-" * 40)
            print(f"preparing {smart_selection[choice]}")
            print("-" * 40)
            for items in active_list:
                if items[1] in smart_pantry_inventory:
                    apply_meal_cost(smart_pantry_inventory)
                    # performs changes to pantry dictionary if 'switch' not false
                elif items[1] in smart_fridge_inventory:
                    apply_meal_cost(smart_fridge_inventory)
                    # performs changes to fridge dictionary if 'switch' not false
            active_list.clear()
            smart_pantry_inventory.close()
            smart_fridge_inventory.close()
            smart_selection.close()
            print(input("press enter to continue "))
            break

        else:
            print("-" * 60)
            print(f"cannot prepare {smart_selection[choice]} due to missing ingredient(s)")
            print("-" * 60)
            active_list.clear()
            print(input("press enter to continue "))
            smart_pantry_inventory.close()
            smart_fridge_inventory.close()
            smart_selection.close()
            break

    else:
        while choice == 'a' and more_ingredient_validation is False:
            print("What would you like to add?\n1: Pantry ingredient\n2: Fridge ingredient\n3: New Recipe\n0: Exit")
            update_choice = (input("what is your selection? "))
            validation = validation_check(update_choice, int, 4)
            if validation is False:
                continue
            update_choice = int(update_choice)
            if update_choice == 0:
                print("you have exited the inventory menu")
                break
            elif update_choice == 1:
                smart_pantry_inventory = shelve.open(path_smart_pantry)
                item_to_change = print_dict(smart_pantry_inventory)
                if item_to_change == '':
                    continue
                elif item_to_change not in smart_pantry_inventory.keys():
                    smart_pantry_inventory[item_to_change] = 0
                pantry_inventory = update_dict(smart_pantry_inventory, item_to_change)
                smart_pantry_inventory.close()

            elif update_choice == 2:
                smart_fridge_inventory = shelve.open(path_smart_fridge)
                item_to_change = print_dict(smart_fridge_inventory)
                if item_to_change == '':
                    break
                elif item_to_change not in smart_fridge_inventory.keys():
                    smart_fridge_inventory[item_to_change] = 0
                fridge_inventory = update_dict(smart_fridge_inventory, item_to_change)
                smart_fridge_inventory.close()

            elif update_choice == 3:
                new_recipe_list = []
                new_ingredient_list = []
                ingredient_type = 0
                more_ingredient_check = 1

                smart_recipes = shelve.open(path_smart_recipes)
                smart_selection = shelve.open(path_smart_selection)
                smart_pantry_inventory = shelve.open(path_smart_pantry)
                smart_fridge_inventory = shelve.open(path_smart_fridge)
                new_recipe_name = input("What should this recipe be named? (Type `0` to cancel): ")
                if new_recipe_name in smart_recipes.keys():
                    print("This recipe already exists.\nExiting recipe creation")
                    break
                elif new_recipe_name == "0":
                    print("canceling new recipe creation")
                    break
                elif not all(char.isalpha() or char.isspace() for char in new_recipe_name):
                    print("The recipe name should only have alphabetic characters\nExiting recipe creation")
                    continue
                while more_ingredient_check != 0:
                    ingredient_type = 0
                    more_ingredient_validation = False
                    if more_ingredient_check == 1:
                        print("-" * 60)
                        print("Instructions:\nBe sure to proofread for spelling. First, you will be asked to name your "
                              "recipe. Next, you will enter ingredients one at a time followed by a decimal amount \n"
                              "of a unit of ingredient used for the recipe. The ingredient name should be in "
                              "singular noun form. A unit is an entire package of an ingredient. \n"
                              "For instance, if a recipe will use a tenth of a carton of milk, you will enter .1")

                        ingredient_name = input("Enter ingredient name (use singular noun form): ").lower()
                        if not all(char.isalpha() or char.isspace() for char in ingredient_name):
                            print("Ingredient name should only contain alphabetic characters")
                            print("starting over ingredient specification")
                            continue
                        quantity_used = input("Enter decimal amount of a unit used for the recipe: ")
                        try:
                            quantity_used = float(quantity_used)
                        except ValueError:
                            print("This is not a valid quantity to be used\nstarting over ingredient specification")
                            continue
                        while ingredient_type not in range(1, 3) and more_ingredient_validation is False:
                            print("Which storage type does this item belong?\n1: Pantry item\n2: Fridge item")
                            ingredient_type = input("what type of ingredient is this? ")
                            try:
                                ingredient_type = int(ingredient_type)
                            except ValueError:
                                print("This is not a valid selection")
                                continue
                            if ingredient_type == 1 or ingredient_type == 2:
                                quantity_used = str(quantity_used)
                                update_string = quantity_used + ' ' + ingredient_name
                                print(f"{ingredient_name} was added to your {new_recipe_name} recipe.")
                                new_ingredient_list.append([ingredient_name, ingredient_type])
                                new_recipe_list.append(update_string)
                                while True:
                                    print("1: Enter another ingredient\n0: Exit")
                                    more_ingredient_check = input("what is your selection? ")
                                    try:
                                        more_ingredient_check = int(more_ingredient_check)
                                    except ValueError:
                                        print("this is not a valid selection")
                                        continue
                                    if more_ingredient_check not in range(0, 2):
                                        print("This is not a valid selection")
                                    elif more_ingredient_check in range(0, 2):
                                        more_ingredient_validation = True
                                        break

                            else:
                                print("This is not a valid selection")
                                continue
                    else:
                        print("Enter a valid selection.")
                        print("1: Enter another ingredient\n0: Exit")
                        more_ingredient_check = input("what is your selection? ")

                smart_recipes[new_recipe_name] = new_recipe_list
                new_selection_key = str(len(smart_selection) + 1)
                smart_selection[new_selection_key] = new_recipe_name
                smart_recipes.close()
                smart_selection.close()
                # for each new ingredient, enter current number of units for update function
                for ingredient_details in new_ingredient_list:
                    inventory_item, inventory_type = ingredient_details
                    if inventory_type == 1:
                        if inventory_item not in smart_pantry_inventory.keys():
                            smart_pantry_inventory[inventory_item] = 0
                            update_dict(smart_pantry_inventory, inventory_item)
                    elif inventory_type == 2:
                        if inventory_item not in smart_fridge_inventory.keys():
                            smart_fridge_inventory[inventory_item] = 0
                            update_dict(smart_fridge_inventory, inventory_item)

                smart_pantry_inventory.close()
                smart_fridge_inventory.close()

        while choice == 'd' and del_counter == 0:
            print("what do you want to delete?\n1: Recipe\n2: Pantry item\n3: Fridge item\n0: Exit")
            delete_choice = input("What is your selection? ")
            validation = validation_check(delete_choice, int, 4)
            if validation is False:
                continue

            delete_choice = int(delete_choice)
            if delete_choice == 0:
                print("You exited the deletion menu")
                break
            elif delete_choice == 1:
                smart_recipes = shelve.open(path_smart_recipes)
                counter2 = 1
                grocery_choice = None
                temp_recipe_table = {}
                recipe_to_delete = ''

                print("Removing a recipe will delete it from possible recipes to make, but will not remove the "
                      "ingredients from your inventory")
                for key in smart_recipes.keys():
                    temp_recipe_table[counter2] = key
                    counter2 += 1
                for key in temp_recipe_table.keys():
                    print(f"{key}: {temp_recipe_table[key]}")
                print("0: Exit")
                delete_number = input("what recipe do you want to remove? ")
                validation = validation_check(delete_number, int, counter2)
                if validation is False:
                    print("This is not a valid selection\nExiting recipe deletion menu")
                    continue

                delete_number = int(delete_number)
                if delete_number == 0:
                    break
                elif delete_number in range(1, counter2):
                    delete_key = temp_recipe_table[delete_number]
                    delete_confirm = input(f"You selected {delete_key}. "
                                           f"press `Y` to confirm or `N` to cancel: ").upper()
                    if delete_confirm == 'Y':
                        new_key = 1
                        update_selection_dict = {}
                        smart_selection = shelve.open(path_smart_selection)
                        del smart_recipes[delete_key]
                        smart_recipes.close()

                        for key, value in smart_selection.items():
                            if value == delete_key:
                                del smart_selection[key]
                        for value in smart_selection.values():
                            updated_key_dict = {(str(new_key)): value}
                            new_key += 1
                            update_selection_dict.update(updated_key_dict)
                        smart_selection.clear()
                        smart_selection.update(update_selection_dict)

                        print(f"deleting the recipe '{delete_key}' from the recipe selection...")
                        del_counter = 1  # tells while loop deletion is completed
                        choice = ""
                        smart_selection.close()
                        break

                    elif delete_confirm == 'N':
                        print("Canceling recipe deletion")
                        smart_recipes.close()
                        continue

                else:
                    print("This is not a valid selection\nExiting recipe deletion menu")
                    smart_recipes.close()
                    smart_selection.close()
                    continue

            elif delete_choice == 2:
                delete_confirm = ''
                smart_pantry_inventory = shelve.open(path_smart_pantry)
                delete_key = check_for_key_to_delete(smart_pantry_inventory)
                if delete_key == "0":
                    smart_pantry_inventory.close()
                    break
                smart_recipes = shelve.open(path_smart_recipes)
                Active_ingredient_check = check_ingredient_in_recipes(smart_recipes, delete_key)
                if Active_ingredient_check is True:
                    enter_check = 0
                    print("This ingredient is part of a current recipe. Please delete the recipe first")
                    smart_pantry_inventory.close()
                    while enter_check != '':
                        enter_check = input("press enter to continue")
                        if enter_check == '':
                            break
                        else:
                            continue
                smart_recipes.close()

                while delete_confirm != 'Y' and Active_ingredient_check is False or \
                        delete_confirm != 'N' and Active_ingredient_check is False:
                    delete_confirm = input(f"You selected {delete_key}. press `Y` to confirm or `N` to cancel: "
                                           ).upper()
                    if delete_confirm == 'Y':
                        del smart_pantry_inventory[delete_key]
                        print(f"The Pantry item '{delete_key}' was removed")
                        smart_pantry_inventory.close()
                        break
                    elif delete_confirm == 'N':
                        print("Exiting ingredient deletion menu")
                        smart_pantry_inventory.close()
                        break
                    else:
                        print("This is an invalid selection")
                        continue
            elif delete_choice == 3:
                delete_confirm = ''
                smart_fridge_inventory = shelve.open(path_smart_fridge)
                delete_key = check_for_key_to_delete(smart_fridge_inventory)
                if delete_key == "0":
                    smart_fridge_inventory.close()
                    break
                smart_recipes = shelve.open(path_smart_recipes)
                Active_ingredient_check = check_ingredient_in_recipes(smart_recipes, delete_key)
                if Active_ingredient_check is True:
                    enter_check = 0
                    print("This ingredient is part of a current recipe. Please delete the recipe first")
                    smart_fridge_inventory.close()
                    while enter_check != '':
                        enter_check = input("press enter to continue")
                        if enter_check == '':
                            break
                        else:
                            continue
                smart_recipes.close()

                while delete_confirm != 'Y' and Active_ingredient_check is False or delete_confirm != 'N' \
                        and Active_ingredient_check is False:
                    delete_confirm = input(f"You selected {delete_key}. press `Y` to confirm or `N` to cancel: "
                                           ).upper()
                    if delete_confirm == 'Y':
                        del smart_fridge_inventory[delete_key]
                        print(f"The Fridge item '{delete_key}' was removed")
                        smart_fridge_inventory.close()
                        break
                    elif delete_confirm == 'N':
                        print("Exiting ingredient deletion menu")
                        smart_fridge_inventory.close()
                        break
                    else:
                        print("This is an invalid selection")
                        continue

        else:
            if del_counter == 1:
                continue
            elif choice == 'a' and more_ingredient_validation is True:
                print(input("Your new recipe is created! Press enter to continue"))
            elif choice == 'a' and more_ingredient_validation is False:
                continue
            elif choice != '0':
                print("this is not a valid selection")
                continue

if choice == "0":
    print("you quit the program")
elif del_counter == 0:
    print("select a valid option")
