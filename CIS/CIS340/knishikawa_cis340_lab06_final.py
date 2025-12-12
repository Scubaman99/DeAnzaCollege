"""
*******************************************************************************
Filename: knishikawa_cis340_lab06_final.py
Author: Kenichi Nishikawa
Date: 2025.12.10
Modifications:
    - Fully corrected Lab06 implementation.
    - Meets ALL requirements for Part 1 and Part 2.
    - Writes formatted ingredient lists to cake_ingredients_list.txt.
    - Reads cake orders from cake_orders.txt using .read(n).
    - Correct docstrings, formatting, spacing, and column alignment.

Description:
This program extends Lab05 by interfacing the Cake Program with files.
Part 1: Writes ingredient lists to a file in correct Lab05 format.
Part 2: Reads cake orders from a text file using .read(n) and processes
        each order using the correct recipes and formatting.
*******************************************************************************
"""

# ----------------------------- CONSTANTS ---------------------------------

REGULAR_OZ = 64.0
LARGE_OZ = 112.0

# Chocolate
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

# Red Velvet
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

# Lemon
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

# ------------------------- HELPER FUNCTION -------------------------------

def print_and_write(line, out_file):
    """
    Prints a line to the console AND writes the same line to the
    output file with a newline.
    """
    print(line)
    out_file.write(line + "\n")

# ------------------------- PROCESS FUNCTIONS ------------------------------

def process_generic_cake(size_code, recipe_dict, cake_name, out_file):
    """
    Generic processor for all cake types.
    """
    total_oz = LARGE_OZ if size_code.upper() == "L" else REGULAR_OZ
    size_name = "Large" if size_code.upper() == "L" else "Regular"
    header = f"{size_name} {cake_name} Ingredient List"

    print_and_write("", out_file)
    print_and_write(header, out_file)
    print_and_write("", out_file)

    total_calc = 0.0

    for name, pct in recipe_dict.items():
        amt = total_oz * pct / 100.0
        total_calc += amt
        print_and_write(f"{name + ':':<32s}{amt:>7.1f} Oz", out_file)

    print_and_write("", out_file)
    print_and_write(f"{'Total:':<32s}{total_calc:>7.1f} Oz", out_file)
    print_and_write("", out_file)

# ----------------------- FILE INPUT PROCESSOR -----------------------------

def process_cake_orders_from_file():
    """
    Reads cake orders from cake_orders.txt using .read(n) and processes
    each one, writing formatted ingredient lists to cake_ingredients_list.txt.
    """

    orders_file = open("cake_orders.txt", "r")
    out_file = open("cake_ingredients_list.txt", "w")

    cake_type_char = orders_file.read(1)

    while cake_type_char != "":
        _ = orders_file.read(3)  # skip spaces
        size_char = orders_file.read(1)
        _ = orders_file.read(1)  # skip newline

        if cake_type_char == "1":
            process_generic_cake(size_char, CHOC, "Chocolate Cake", out_file)
        elif cake_type_char == "2":
            process_generic_cake(size_char, RED_VELVET, "Red Velvet Cake", out_file)
        elif cake_type_char == "3":
            process_generic_cake(size_char, LEMON, "Lemon Cake", out_file)

        cake_type_char = orders_file.read(1)

    orders_file.close()
    out_file.close()

# ----------------------------- MAIN ---------------------------------------

def main():
    """
    Main driver: processes cake orders from file.
    """
    process_cake_orders_from_file()

if __name__ == "__main__":
    main()
