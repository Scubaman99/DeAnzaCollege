"""
***************************************************************************
Filename: knishikawa_cis340_lab05.py
Author: Ken Nishikawa
Date: 2025.12.09
Modifications: 2025.12.09

Description:
This module implements the "More Cakes" program. It takes repeated cake
orders (type and size) from the user, calculates ingredient weights using
the real recipes for Chocolate, Red Velvet, and Lemon cakes, and prints
a formatted ingredient list for each order. The program uses a sentinel
value to allow the user to quit.
***************************************************************************
"""

# ----------------------------- Constants ---------------------------------

# conversion and cake sizes
LB_TO_OZ = 16.0
REGULAR_LB = 4.0
LARGE_LB = 7.0
REGULAR_OZ = REGULAR_LB * LB_TO_OZ
LARGE_OZ = LARGE_LB * LB_TO_OZ

# Chocolate recipe percentages
CHOC_FLOUR_PCT = 15.8
CHOC_SUGAR_PCT = 24.5
CHOC_COCOA_PCT = 5.6
CHOC_BAKING_POWDER_PCT = 0.4
CHOC_BAKING_SODA_PCT = 0.6
CHOC_SALT_PCT = 0.4
CHOC_EGG_PCT = 9.0
CHOC_BUTTERMILK_PCT = 18.0
CHOC_OIL_PCT = 8.1
CHOC_VANILLA_PCT = 0.6
CHOC_WATER_PCT = 17.0

# Red Velvet recipe percentages
RV_FLOUR_PCT = 22.4
RV_SUGAR_PCT = 22.4
RV_BAKING_SODA_PCT = 0.7
RV_SALT_PCT = 0.4
RV_COCOA_PCT = 0.4
RV_OIL_PCT = 24.0
RV_BUTTERMILK_PCT = 17.9
RV_EGG_PCT = 9.0
RV_RED_COLOR_PCT = 2.1
RV_VANILLA_PCT = 0.3
RV_VINEGAR_PCT = 0.4

# Lemon recipe percentages
LEMON_BUTTER_PCT = 8.5
LEMON_SUGAR_PCT = 15.0
LEMON_EGG_PCT = 9.0
LEMON_FLOUR_PCT = 15.6
LEMON_BUTTERMILK_PCT = 9.0
LEMON_VANILLA_PCT = 0.2
LEMON_FILL_EGG_YOLK_PCT = 17.9
LEMON_FILL_SUGAR_PCT = 11.3
LEMON_FILL_BUTTER_PCT = 2.1
LEMON_FILL_LEMON_PCT = 11.4

# ----------------------------- Functions ---------------------------------

def compute_ingredients(cake_type, size_choice):
"""
***************************************************************************
Function: compute_ingredients(cake_type, size_choice)

Parameters:
cake_type - integer: 1 for Chocolate, 2 for Red Velvet, 3 for Lemon
size_choice - string: 'L' or 'l' for Large, 'R' or 'r' for Regular

Outputs:
None (this function does not print directly)

Returns:
cake_name - name of the cake type as a string
size_name - "Large" or "Regular" as a string
ingredients - list of (ingredient_name, weight_in_oz) tuples
total_oz- total cake weight in ounces (float)

Author:Ken Nishikawa
Date: 2025.12.09
Modifications: 2025.12.09

Description:
This function determines the total cake weight based on the selected
size (Regular or Large), then uses the real recipe percentages for the
selected cake type to calculate the amount of each ingredient in ounces.
It returns the cake name, size name, ingredient list, and total weight.
***************************************************************************
"""
# determine cake size in ounces
if size_choice == "L" or size_choice == "l":
size_name = "Large"
total_oz = LARGE_OZ
else:
size_name = "Regular"
total_oz = REGULAR_OZ

ingredients = []

# Chocolate Cake
if cake_type == 1:
cake_name = "Chocolate Cake"

flour_oz = total_oz * CHOC_FLOUR_PCT / 100.0
sugar_oz = total_oz * CHOC_SUGAR_PCT / 100.0
cocoa_oz = total_oz * CHOC_COCOA_PCT / 100.0
bake_powder_oz = total_oz * CHOC_BAKING_POWDER_PCT / 100.0
bake_soda_oz = total_oz * CHOC_BAKING_SODA_PCT / 100.0
salt_oz = total_oz * CHOC_SALT_PCT / 100.0
egg_oz = total_oz * CHOC_EGG_PCT / 100.0
buttermilk_oz = total_oz * CHOC_BUTTERMILK_PCT / 100.0
oil_oz = total_oz * CHOC_OIL_PCT / 100.0
vanilla_oz = total_oz * CHOC_VANILLA_PCT / 100.0
water_oz = total_oz * CHOC_WATER_PCT / 100.0

ingredients.append(("Flour:", flour_oz))
ingredients.append(("Sugar:", sugar_oz))
ingredients.append(("Unsweetened Cocoa Powder:", cocoa_oz))
ingredients.append(("Baking Powder:", bake_powder_oz))
ingredients.append(("Baking Soda:", bake_soda_oz))
ingredients.append(("Salt:", salt_oz))
ingredients.append(("Egg:", egg_oz))
ingredients.append(("Buttermilk:", buttermilk_oz))
ingredients.append(("Oil:", oil_oz))
ingredients.append(("Vanilla Extract:", vanilla_oz))
ingredients.append(("Boiling Water:", water_oz))

# Red Velvet Cake
elif cake_type == 2:
cake_name = "Red Velvet Cake"

flour_oz = total_oz * RV_FLOUR_PCT / 100.0
sugar_oz = total_oz * RV_SUGAR_PCT / 100.0
cocoa_oz = total_oz * RV_COCOA_PCT / 100.0
baking_soda_oz = total_oz * RV_BAKING_SODA_PCT / 100.0
salt_oz = total_oz * RV_SALT_PCT / 100.0
egg_oz = total_oz * RV_EGG_PCT / 100.0
buttermilk_oz = total_oz * RV_BUTTERMILK_PCT / 100.0
oil_oz = total_oz * RV_OIL_PCT / 100.0
vanilla_oz = total_oz * RV_VANILLA_PCT / 100.0
color_oz = total_oz * RV_RED_COLOR_PCT / 100.0
vinegar_oz = total_oz * RV_VINEGAR_PCT / 100.0

ingredients.append(("Flour:", flour_oz))
ingredients.append(("Sugar:", sugar_oz))
ingredients.append(("Unsweetened Cocoa Powder:", cocoa_oz))
ingredients.append(("Baking Soda:", baking_soda_oz))
ingredients.append(("Salt:", salt_oz))
ingredients.append(("Egg:", egg_oz))
ingredients.append(("Buttermilk:", buttermilk_oz))
ingredients.append(("Oil:", oil_oz))
ingredients.append(("Vanilla Extract:", vanilla_oz))
ingredients.append(("Red Food Coloring:", color_oz))
ingredients.append(("Distilled Vinegar:", vinegar_oz))

# Lemon Cake
else:
cake_name = "Lemon Cake"

butter_oz = total_oz * LEMON_BUTTER_PCT / 100.0
sugar_oz = total_oz * LEMON_SUGAR_PCT / 100.0
egg_oz = total_oz * LEMON_EGG_PCT / 100.0
flour_oz = total_oz * LEMON_FLOUR_PCT / 100.0
buttermilk_oz = total_oz * LEMON_BUTTERMILK_PCT / 100.0
vanilla_oz = total_oz * LEMON_VANILLA_PCT / 100.0
fill_egg_yolk_oz = total_oz * LEMON_FILL_EGG_YOLK_PCT / 100.0
fill_sugar_oz = total_oz * LEMON_FILL_SUGAR_PCT / 100.0
fill_butter_oz = total_oz * LEMON_FILL_BUTTER_PCT / 100.0
fill_lemon_oz = total_oz * LEMON_FILL_LEMON_PCT / 100.0

# Order of ingredients matches sample output
ingredients.append(("Sugar:", sugar_oz))
ingredients.append(("Egg:", egg_oz))
ingredients.append(("Buttermilk:", buttermilk_oz))
ingredients.append(("Vanilla Extract:", vanilla_oz))
ingredients.append(("Butter:", butter_oz))
ingredients.append(("Sifted Self Rising Flour:", flour_oz))
ingredients.append(("Filling - Egg Yolk:", fill_egg_yolk_oz))
ingredients.append(("Filling - Sugar:", fill_sugar_oz))
ingredients.append(("Filling - Butter:", fill_butter_oz))
ingredients.append(("Filling - Lemon Zest:", fill_lemon_oz))

return cake_name, size_name, ingredients, total_oz

def print_ingredients(size_name, cake_name, ingredients, total_oz):
"""
***************************************************************************
Function: print_ingredients(size_name, cake_name, ingredients, total_oz)

Parameters:
size_name - string: "Large" or "Regular"
cake_name - string: full name of the cake type
ingredients - list of (ingredient_name, weight_in_oz) tuples
total_oz- float: total cake weight in ounces

Outputs:
Prints the ingredient list and total weight formatted in aligned
columns, similar to the sample output given in the lab assignment.

Returns:
None

Author:Ken Nishikawa
Date:  2025.12.09
Modifications: 2025.12.09

Description:
This function prints a header line that shows the cake size and type.
Then, it prints each ingredient name and its weight in ounces using
formatted output so that the numbers line up in a neat column. Finally,
it prints the total cake weight at the bottom.
***************************************************************************
"""
# print header
print()
print(size_name + " " + cake_name + " Ingredient List")
print()

# print each ingredient line with formatting
for name, amount in ingredients:
# name left-aligned in 28 spaces, amount right-aligned with 1 decimal
print("{:<28s}{:>7.1f} Oz".format(name, amount))

# print total
print()
print("{:<28s}{:>7.1f} Oz".format("Total:", total_oz))
print()

def main():
"""
***************************************************************************
Function: main()

Parameters:
None

Outputs:
Repeatedly prompts the user for cake type and size, prints the
ingredient list for each valid order, and ends when the user
enters 'q' or 'Q' for cake type.

Returns:
None

Author:Ken Nishikawa
Date:  2025.12.09
Modifications: 2025.12.09

Description:
This is the main control function for the "More Cakes" program. It uses
a sentinel-controlled loop to accept as many cake orders as the user
wants. For each order, it asks for cake type and size, calls the helper
function to compute ingredients, and then prints the formatted list.
When the user enters 'q' to quit, the program prints "Bye!" and ends.
***************************************************************************
"""
# sentinel-controlled loop
while True:
cake_choice_text = input(
"Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, "
"3 for Lemon, q to quit: "
)

# check for sentinel
if cake_choice_text == "q" or cake_choice_text == "Q":
print("Bye!")
break

# convert cake type to integer
cake_type = int(cake_choice_text)

# prompt for cake size
size_choice = input("Please Select Cake Size; Enter L for large, R for regular: ")

# calculate ingredients
cake_name, size_name, ingredients, total_oz = compute_ingredients(
cake_type,
size_choice
)

# output ingredient list
print_ingredients(size_name, cake_name, ingredients, total_oz)

# ------------------------------ Main Guard --------------------------------

if __name__ == "__main__":
main()


