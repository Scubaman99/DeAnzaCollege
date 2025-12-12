"""
*******************************************************************************
Filename: knishikawa_cis340_lab07_final.py
Author: Kenichi Nishikawa
Date: 2025.12.10
Modifications:
    - Full implementation of Lab07 Part II.
    - Uses dictionaries and lists for flexible recipe management.
    - Replaces three separate ingredient calculators with one generic function.
    - Uses zip() to iterate ingredient names with calculated weights.
    - EXACT Lab05 formatting preserved.

Description:
This program enhances the Cake Program by using lists and dictionaries
to improve flexibility, readability, and maintainability. It accepts
unlimited cake orders, computes ingredient weights based on recipe
dictionaries, and prints ingredient lists in the exact formatting style
required in Lab05. This file represents the full submission for Lab07.
*******************************************************************************
"""

# ----------------------------- CONSTANTS ---------------------------------

REGULAR_OZ = 64.0
LARGE_OZ = 112.0

# --------------------------- RECIPE DICTIONARIES -------------------------

CHOCOLATE_RECIPE = {
    "Flour": 15.8,
    "Sugar": 24.5,
    "Unsweetened Cocoa Powder": 5.6,
    "Baking Powder": 0.4,
    "Baking Soda": 0.6,
    "Salt": 0.4,
    "Egg": 9.0,
    "Buttermilk": 18.0,
    "Oil": 8.1,
    "Vanilla Extract": 0.6,
    "Boiling Water": 17.0
}

RED_VELVET_RECIPE = {
    "Flour": 22.4,
    "Sugar": 22.4,
    "Unsweetened Cocoa Powder": 0.4,
    "Baking Soda": 0.7,
    "Salt": 0.4,
    "Egg": 9.0,
    "Buttermilk": 17.9,
    "Oil": 24.0,
    "Vanilla Extract": 0.3,
    "Red Food Coloring": 2.1,
    "Distilled Vinegar": 0.4
}

LEMON_RECIPE = {
    "Sugar": 15.0,
    "Egg": 9.0,
    "Buttermilk": 9.0,
    "Vanilla Extract": 0.2,
    "Butter": 8.5,
    "Sifted Self-Rising Flour": 15.6,
    "Filling - Egg Yolk": 17.9,
    "Filling - Sugar": 11.3,
    "Filling - Butter": 2.1,
    "Filling - Lemon Juice and Zest": 11.4
}

# --------------------------- COMMON INGREDIENT ORDER ---------------------

# Ingredient name order for printing (Lab05 format)
INGREDIENT_NAMES = [
    "Flour",
    "Sugar",
    "Unsweetened Cocoa Powder",
    "Baking Powder",
    "Baking Soda",
    "Salt",
    "Egg",
    "Buttermilk",
    "Oil",
    "Vanilla Extract",
    "Boiling Water",
    "Red Food Coloring",
    "Distilled Vinegar",
    "Sifted Self-Rising Flour",
    "Butter",
    "Filling - Egg Yolk",
    "Filling - Sugar",
    "Filling - Butter",
    "Filling - Lemon Juice and Zest"
]


# ------------------------- INGREDIENT CALCULATOR -------------------------

def calc_ingrd(cake_weight, recipe_dic):
    """
    Calculates ingredient weights for a given cake weight and recipe dictionary.
    Returns a list of ingredient weights in the same order as INGREDIENT_NAMES.
    """
    wt_list = []
    for name in INGREDIENT_NAMES:
        if name in recipe_dic:
            wt = cake_weight * recipe_dic[name] / 100.0
            wt_list.append(wt)
        else:
            wt_list.append(None)  # Ingredient not used by this recipe
    return wt_list


# ----------------------------- PRINT FUNCTION ----------------------------

def print_ingrd(type_label, size_label, wt_list, label_list):
    """
    Prints ingredient list in EXACT Lab05 alignment using zip().
    """
    print(f"\n{size_label} {type_label} Ingredient List\n")

    for name, wt in zip(label_list, wt_list):
        if wt is not None:
            print(f"{name + ':':<30s}{wt:>10.1f} Oz")

    total = sum(filter(lambda x: x is not None, wt_list))
    print(f"\n{'Total:':<30s}{total:>10.1f} Oz\n")


# ----------------------------- MAIN LOOP ---------------------------------

def main():
    """
    Main sentinel loop for processing cake orders.
    """
    while True:
        type_choice = input(
            "Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, "
            "3 for Lemon, q to quit: "
        )

        if type_choice.lower() == "q":
            print("Bye!")
            break

        size_choice = input("Please Select Cake Size; Enter L for large, R for regular: ")

        if size_choice.upper() == "L":
            cake_weight = LARGE_OZ
            size_label = "Large"
        else:
            cake_weight = REGULAR_OZ
            size_label = "Regular"

        if type_choice == "1":
            recipe = CHOCOLATE_RECIPE
            type_label = "Chocolate Cake"
        elif type_choice == "2":
            recipe = RED_VELVET_RECIPE
            type_label = "Red Velvet Cake"
        elif type_choice == "3":
            recipe = LEMON_RECIPE
            type_label = "Lemon Cake"
        else:
            print("Invalid cake type!")
            continue

        ingrd_list = calc_ingrd(cake_weight, recipe)
        print_ingrd(type_label, size_label, ingrd_list, INGREDIENT_NAMES)


# -------------------------- EXECUTION GUARD ------------------------------

if __name__ == "__main__":
    main()


# ----------------------- RECORD OF EXECUTION ------------------------------
"""
Paste your test run for these 6 cases:

1. Large Red Velvet
2. Regular Lemon
3. Large Lemon
4. Regular Chocolate
5. Regular Red Velvet
6. Large Chocolate
"""
