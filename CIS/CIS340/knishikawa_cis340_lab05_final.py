"""
*******************************************************************************
Filename: knishikawa_cis340_lab05_fixed.py
Author: Ken Nishikawa
Date: 2025.12.10
Modifications:
    2025.12.10 - Fully corrected version. Fixed indentation, formatting, 
    docstrings, ingredient names, and added required 5‑iteration test run.

Description:
Implements the Lab05 "More Cakes" program. Allows repeated cake orders using a
sentinel-controlled loop. Calculates ingredient weights using the real recipes
for Chocolate, Red Velvet, and Lemon cakes. Produces formatted ingredient lists
with aligned columns. Includes required 5-test-case run at the bottom.
*******************************************************************************
"""

# ---------------------------- CONSTANTS -------------------------------------

LB_TO_OZ = 16.0
REGULAR_OZ = 4.0 * LB_TO_OZ
LARGE_OZ = 7.0 * LB_TO_OZ

# Chocolate Recipe %
CHOC = {
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

# Red Velvet Recipe %
RED_VELVET = {
    "Flour": 22.4,
    "Sugar": 22.4,
    "Baking Soda": 0.7,
    "Salt": 0.4,
    "Unsweetened Cocoa Powder": 0.4,
    "Oil": 24.0,
    "Buttermilk": 17.9,
    "Egg": 9.0,
    "Red Food Coloring": 2.1,
    "Vanilla Extract": 0.3,
    "Distilled Vinegar": 0.4
}

# Lemon Recipe %
LEMON = {
    "Butter": 8.5,
    "Sugar": 15.0,
    "Egg": 9.0,
    "Sifted Self-Rising Flour": 15.6,
    "Buttermilk": 9.0,
    "Vanilla Extract": 0.2,
    "Filling - Egg Yolk": 17.9,
    "Filling - Sugar": 11.3,
    "Filling - Butter": 2.1,
    "Filling - Lemon Juice and Zest": 11.4
}


# ---------------------------- FUNCTIONS --------------------------------------

def compute_ingredients(cake_type, size_choice):
    """
    Compute ingredient weights for selected cake type and size.

    Parameters:
        cake_type (int): 1 = Chocolate, 2 = Red Velvet, 3 = Lemon
        size_choice (str): 'L' or 'l' = Large, 'R' or 'r' = Regular

    Returns:
        cake_name (str)
        size_name (str)
        ingredients (list of (ingredient_name, ounces))
        total_oz (float)

    Description:
        Based on cake type and size, calculates each ingredient weight
        using the real recipe percentages.
    """

    if size_choice.lower() == "l":
        total_oz = LARGE_OZ
        size_name = "Large"
    else:
        total_oz = REGULAR_OZ
        size_name = "Regular"

    if cake_type == 1:
        cake_name = "Chocolate Cake"
        recipe = CHOC
    elif cake_type == 2:
        cake_name = "Red Velvet Cake"
        recipe = RED_VELVET
    else:
        cake_name = "Lemon Cake"
        recipe = LEMON

    ingredients = []
    for name, pct in recipe.items():
        amount = total_oz * pct / 100.0
        ingredients.append((name, amount))

    return cake_name, size_name, ingredients, total_oz


def print_ingredients(size_name, cake_name, ingredients, total_oz):
    """
    Print formatted ingredient list in aligned columns.

    Parameters:
        size_name (str): "Large" or "Regular"
        cake_name (str)
        ingredients (list)
        total_oz (float)

    Returns:
        None
    """

    print()
    print(f"{size_name} {cake_name} Ingredient List
")

    for (name, amount) in ingredients:
        print("{:<32s}{:>7.1f} Oz".format(name + ":", amount))

    print()
    print("{:<32s}{:>7.1f} Oz".format("Total:", total_oz))
    print()


def main():
    """
    Sentinel-controlled loop for repeated cake orders.

    Parameters:
        None

    Returns:
        None
    """

    while True:
        cake_choice = input(
            "Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, "
            "3 for Lemon, q to quit: "
        )

        if cake_choice.lower() == "q":
            print("Bye!")
            break

        cake_type = int(cake_choice)

        size_choice = input("Please Select Cake Size; Enter L for large, R for regular: ")

        cake_name, size_name, ingredients, total_oz = compute_ingredients(cake_type, size_choice)

        print_ingredients(size_name, cake_name, ingredients, total_oz)


# ----------------------------- MAIN GUARD -------------------------------------

if __name__ == "__main__":
    main()


# ----------------------- REQUIRED 5‑ITERATION TEST RUN ------------------------
"""
TEST RUN (Required by Lab05)

Case 1: Large Red Velvet
Case 2: Regular Lemon
Case 3: Large Lemon
Case 4: Regular Chocolate
Case 5: Regular Chocolate

(Example transcript omitted here for length; instructor will run program.)
"""


# ---------------------- REQUIRED TEST RUN TRANSCRIPT ----------------------
# Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 2
# Please Select Cake Size; Enter L for large, R for regular: L
# 
# Large Red Velvet Cake Ingredient List
# 
# Flour:                             25.1 Oz
# Sugar:                             25.1 Oz
# Baking Soda:                        0.8 Oz
# Salt:                               0.4 Oz
# Unsweetened Cocoa Powder:           0.4 Oz
# Oil:                               26.9 Oz
# Buttermilk:                        20.0 Oz
# Egg:                               10.1 Oz
# Red Food Coloring:                  2.4 Oz
# Vanilla Extract:                    0.3 Oz
# Distilled Vinegar:                  0.4 Oz
# 
# Total:                            112.0 Oz
# 
# 
# Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
# Please Select Cake Size; Enter L for large, R for regular: R
# 
# Regular Lemon Cake Ingredient List
# 
# Butter:                             5.4 Oz
# Sugar:                              9.6 Oz
# Egg:                                5.8 Oz
# Sifted Self-Rising Flour:          10.0 Oz
# Buttermilk:                         5.8 Oz
# Vanilla Extract:                    0.1 Oz
# Filling - Egg Yolk:                11.5 Oz
# Filling - Sugar:                    7.2 Oz
# Filling - Butter:                   1.3 Oz
# Filling - Lemon Juice and Zest:     7.3 Oz
# 
# Total:                             64.0 Oz
# 
# 
# Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 3
# Please Select Cake Size; Enter L for large, R for regular: L
# 
# Large Lemon Cake Ingredient List
# 
# Butter:                             9.5 Oz
# Sugar:                             16.8 Oz
# Egg:                               10.1 Oz
# Sifted Self-Rising Flour:          17.5 Oz
# Buttermilk:                        10.1 Oz
# Vanilla Extract:                    0.2 Oz
# Filling - Egg Yolk:                20.0 Oz
# Filling - Sugar:                   12.7 Oz
# Filling - Butter:                   2.4 Oz
# Filling - Lemon Juice and Zest:    12.8 Oz
# 
# Total:                            112.0 Oz
# 
# 
# Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
# Please Select Cake Size; Enter L for large, R for regular: R
# 
# Regular Chocolate Cake Ingredient List
# 
# Flour:                             10.1 Oz
# Sugar:                             15.7 Oz
# Unsweetened Cocoa Powder:           3.6 Oz
# Baking Powder:                      0.3 Oz
# Baking Soda:                        0.4 Oz
# Salt:                               0.3 Oz
# Egg:                                5.8 Oz
# Buttermilk:                        11.5 Oz
# Oil:                                5.2 Oz
# Vanilla Extract:                    0.4 Oz
# Boiling Water:                     10.9 Oz
# 
# Total:                             64.0 Oz
# 
# 
# Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: 1
# Please Select Cake Size; Enter L for large, R for regular: R
# 
# Regular Chocolate Cake Ingredient List
# 
# Flour:                             10.1 Oz
# Sugar:                             15.7 Oz
# Unsweetened Cocoa Powder:           3.6 Oz
# Baking Powder:                      0.3 Oz
# Baking Soda:                        0.4 Oz
# Salt:                               0.3 Oz
# Egg:                                5.8 Oz
# Buttermilk:                        11.5 Oz
# Oil:                                5.2 Oz
# Vanilla Extract:                    0.4 Oz
# Boiling Water:                     10.9 Oz
# 
# Total:                             64.0 Oz
# 
# 
# Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: q
# Bye!