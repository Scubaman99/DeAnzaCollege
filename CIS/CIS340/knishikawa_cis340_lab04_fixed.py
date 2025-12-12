"""
File name: knishikawa_cis340_lab04_fixed.py
Author: Ken Nishikawa
Date of Creation: 12/10/2025
History of Modification: 12/10/2025 - Complete rewrite to meet all Lab04 requirements.
Description: Fully functional Cake Program per Lab 04 specifications.
"""

POUND_TO_OUNCE = 16

REGULAR_WEIGHT = 4 * POUND_TO_OUNCE
LARGE_WEIGHT = 7 * POUND_TO_OUNCE

# Chocolate
CH_A = 0.158
CH_B = 0.245
CH_C = 0.056
CH_D = 0.541

# Red Velvet
RV_A = 0.224
RV_B = 0.224
RV_C = 0.24
RV_D = 0.179
RV_E = 0.133

# Lemon
LE_A = 0.385
LE_B = 0.358
LE_C = 0.257

def compute_ingredients(cake_type, size_choice):
    """Compute ingredient weights."""
    if size_choice.upper() == "R":
        total = REGULAR_WEIGHT
        size_name = "Regular"
    else:
        total = LARGE_WEIGHT
        size_name = "Large"

    if cake_type == 1:
        cake_name = "Chocolate"
        ingredients = [
            ("Ingredient A", total * CH_A),
            ("Ingredient B", total * CH_B),
            ("Ingredient C", total * CH_C),
            ("Ingredient D", total * CH_D)
        ]
    elif cake_type == 2:
        cake_name = "Red Velvet"
        ingredients = [
            ("Ingredient A", total * RV_A),
            ("Ingredient B", total * RV_B),
            ("Ingredient C", total * RV_C),
            ("Ingredient D", total * RV_D),
            ("Ingredient E", total * RV_E)
        ]
    else:
        cake_name = "Lemon"
        ingredients = [
            ("Ingredient A", total * LE_A),
            ("Ingredient B", total * LE_B),
            ("Ingredient C", total * LE_C)
        ]

    return cake_name, size_name, ingredients

def print_ingredients(size_name, cake_name, items):
    """Print formatted ingredient list."""
    print(f"\n{size_name} {cake_name} Ingredient list:")
    for label, amount in items:
        print(f"{label}:  {amount:5.1f} Oz")

def main():
    type_text = input("Please select cake type; Enter 1 for Chocolate, 2 for Red Velvet and 3 for Lemon: ")
    size_text = input("\nPlease select cake size; Enter L for large, R for regular: ")

    cake_type = int(type_text)
    size_choice = size_text

    cake_name, size_name, items = compute_ingredients(cake_type, size_choice)

    print_ingredients(size_name, cake_name, items)

if __name__ == "__main__":
    main()
