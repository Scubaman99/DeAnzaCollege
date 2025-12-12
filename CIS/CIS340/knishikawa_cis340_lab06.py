"""
***************************************************************************
Filename: knishikawa_cis340_lab06.py
Author: Kenichi Nishikawa
Date:2025.12.09
Modifications: None
Description: This module reads cake orders from a text file and
writes the ingredient lists for each cake order to
an output text file in a formatted report. The cake
recipes are based on percentage weights for each
ingredient for Chocolate, Red Velvet, and Lemon
cakes and use regular (4 lb / 64 oz) and large
(7 lb / 112 oz) sizes.

***************************************************************************
"""

# ------------------------------------------------------------------------
# Constants for cake sizes (total weight in ounces)
# ------------------------------------------------------------------------

REGULAR_CAKE_OZ = 64.0 # 4 lb cake
LARGE_CAKE_OZ = 112.0# 7 lb cake

# ------------------------------------------------------------------------
# Chocolate Cake Recipe Percentages
# ------------------------------------------------------------------------

CHOC_FLOUR_PCT = 15.8
CHOC_SUGAR_PCT = 24.5
CHOC_COCOA_PCT = 5.6
CHOC_BAKING_POWDER_PCT = 0.4
CHOC_BAKING_SODA_PCT = 0.6
CHOC_SALT_PCT = 0.4
CHOC_EGG_PCT = 9.0
CHOC_BUTTERMILK_PCT = 18.0
CHOC_OIL_PCT = 8.1
CHOC_VANILLA_PCT= 0.6
CHOC_WATER_PCT = 17.0

# ------------------------------------------------------------------------
# Red Velvet Cake Recipe Percentages
# ------------------------------------------------------------------------

RV_FLOUR_PCT = 22.4
RV_SUGAR_PCT = 22.4
RV_BAKING_SODA_PCT = 0.7
RV_SALT_PCT= 0.4
RV_COCOA_PCT = 0.4
RV_OIL_PCT = 24.0
RV_BUTTERMILK_PCT = 17.9
RV_EGG_PCT = 9.0
RV_RED_FOOD_COLOR_PCT= 2.1
RV_VANILLA_PCT = 0.3
RV_VINEGAR_PCT = 0.4

# ------------------------------------------------------------------------
# Lemon Cake Recipe Percentages
# Base cake + filling
# ------------------------------------------------------------------------

LEMON_BUTTER_PCT= 8.5
LEMON_SUGAR_PCT = 15.0
LEMON_EGG_PCT = 9.0
LEMON_FLOUR_PCT = 15.6
LEMON_BUTTERMILK_PCT = 9.0
LEMON_VANILLA_PCT = 0.2

LEMON_FILL_EGG_YOLK_PCT = 17.9
LEMON_FILL_SUGAR_PCT = 11.3
LEMON_FILL_BUTTER_PCT= 2.1
LEMON_FILL_LEMON_PCT = 11.4

# ------------------------------------------------------------------------
# Helper function to print to screen and write to file
# ------------------------------------------------------------------------

def print_and_write(line, out_file):
"""
***************************************************************************
Function: print_and_write(line, out_file)

Parameters: line- string to be printed and written
out_file - file object already opened for writing

Outputs: Prints the line to the screen and writes the same line
to the output file with a newline at the end.

Returns: None
Author: Kenichi Nishikawa
Date: 2025.12.09
Modifications: NoneDescription:
This function helps keep the screen output and the file output
synchronized. It prints the text line to the console and writes
the same text line to the output file, followed by a newline
character in the file.

***************************************************************************
"""
print(line)
out_file.write(line + "\n")

# ------------------------------------------------------------------------
# Functions to process each cake type
# ------------------------------------------------------------------------

def process_chocolate_cake(size_code, out_file):
"""
***************************************************************************
Function: process_chocolate_cake(size_code, out_file)
Parameters: size_code - 'L' or 'R' indicating Large or Regular cake
out_file - file object already opened for writing
Outputs: Prints and writes the ingredient list for a Chocolate
cake of the requested size.
Returns: None
Author: Kenichi Nishikawa
Date: 2025.12.09
Modifications: None
Description:
This function calculates the ingredient weights in ounces for a
Chocolate cake using the recipe percentages and the total cake
weight for either a regular (64 oz) or large (112 oz) cake. It then
prints the ingredient list to the screen and writes the same list
to the output file.***************************************************************************
"""
# Decide total weight based on size
if size_code.upper() == "L":
total_oz = LARGE_CAKE_OZ
header = "Large Chocolate Cake Ingredient List"
else:
total_oz = REGULAR_CAKE_OZ
header = "Regular Chocolate Cake Ingredient List"

# [Calculate] - compute each ingredient amount
flour_oz = total_oz * CHOC_FLOUR_PCT / 100.0
sugar_oz = total_oz * CHOC_SUGAR_PCT / 100.0
cocoa_oz = total_oz * CHOC_COCOA_PCT / 100.0
baking_pow_oz = total_oz * CHOC_BAKING_POWDER_PCT / 100.0
baking_soda_oz = total_oz * CHOC_BAKING_SODA_PCT / 100.0
salt_oz = total_oz * CHOC_SALT_PCT / 100.0
egg_oz = total_oz * CHOC_EGG_PCT / 100.0
buttermilk_oz = total_oz * CHOC_BUTTERMILK_PCT / 100.0
oil_oz = total_oz * CHOC_OIL_PCT / 100.0
vanilla_oz= total_oz * CHOC_VANILLA_PCT / 100.0
water_oz = total_oz * CHOC_WATER_PCT / 100.0

# Recalculate total to show at the bottom
total_calc_oz = (flour_oz + sugar_oz + cocoa_oz + baking_pow_oz +
baking_soda_oz + salt_oz + egg_oz + buttermilk_oz +
oil_oz + vanilla_oz + water_oz)

# [Output] - formatted printing and writing
print_and_write("", out_file)
print_and_write(header, out_file)
print_and_write("", out_file)

print_and_write("Flour:{:>27.1f} Oz".format(flour_oz), out_file)
print_and_write("Sugar:{:>27.1f} Oz".format(sugar_oz), out_file)
print_and_write("Unsweetened Cocoa Powder:{:>9.1f} Oz".format(cocoa_oz), out_file)
print_and_write("Baking Powder:{:>19.1f} Oz".format(baking_pow_oz), out_file)
print_and_write("Baking Soda:{:>21.1f} Oz".format(baking_soda_oz), out_file)
print_and_write("Salt:{:>28.1f} Oz".format(salt_oz), out_file)
print_and_write("Egg:{:>29.1f} Oz".format(egg_oz), out_file)
print_and_write("Buttermilk:{:>23.1f} Oz".format(buttermilk_oz), out_file)
print_and_write("Oil:{:>29.1f} Oz".format(oil_oz), out_file)
print_and_write("Vanilla Extract:{:>18.1f} Oz".format(vanilla_oz), out_file)
print_and_write("Boiling Water:{:>20.1f} Oz".format(water_oz), out_file)
print_and_write("", out_file)
print_and_write("Total:{:>27.1f} Oz".format(total_calc_oz), out_file)
print_and_write("", out_file)


def process_red_velvet_cake(size_code, out_file):
"""
 ***************************************************************************
Function: process_red_velvet_cake(size_code, out_file)
Parameters: size_code - 'L' or 'R' indicating Large or Regular cake
out_file - file object already opened for writing
Outputs: Prints and writes the ingredient list for a Red Velvet
cake of the requested size.
Returns: None
Author: Kenichi Nishikawa
Date: 2025.12.09
Modifications: None

Description:
This function calculates the ingredient weights in ounces for a
Red Velvet cake using the recipe percentages and the total cake
weight for either a regular (64 oz) or large (112 oz) cake. It then
prints the ingredient list to the screen and writes the same list
to the output file.

***************************************************************************
Ò""
# Decide total weight based on size
if size_code.upper() == "L":
total_oz = LARGE_CAKE_OZ
header = "Large Red Velvet Cake Ingredient List"
else:
total_oz = REGULAR_CAKE_OZheader = "Regular Red Velvet Cake Ingredient List"
# [Calculate] - compute each ingredient amount
flour_oz = total_oz * RV_FLOUR_PCT / 100.0
sugar_oz = total_oz * RV_SUGAR_PCT / 100.0
baking_soda_oz = total_oz * RV_BAKING_SODA_PCT / 100.0
salt_oz = total_oz * RV_SALT_PCT / 100.0
cocoa_oz = total_oz * RV_COCOA_PCT / 100.0
oil_oz = total_oz * RV_OIL_PCT / 100.0
buttermilk_oz = total_oz * RV_BUTTERMILK_PCT / 100.0
egg_oz = total_oz * RV_EGG_PCT / 100.0
red_color_oz = total_oz * RV_RED_FOOD_COLOR_PCT / 100.0
vanilla_oz= total_oz * RV_VANILLA_PCT / 100.0vinegar_oz= total_oz * RV_VINEGAR_PCT / 100.0

total_calc_oz = (flour_oz + sugar_oz + baking_soda_oz + salt_oz +
cocoa_oz + oil_oz + buttermilk_oz + egg_oz +
red_color_oz + vanilla_oz + vinegar_oz)
# [Output]
print_and_write("", out_file)
print_and_write(header, out_file)
print_and_write("", out_file)

print_and_write("Flour:{:>27.1f} Oz".format(flour_oz), out_file)
print_and_write("Sugar:{:>27.1f} Oz".format(sugar_oz), out_file)
print_and_write("Unsweetened Cocoa Powder:{:>9.1f} Oz".format(cocoa_oz), out_file)
 print_and_write("Baking Soda:{:>21.1f} Oz".format(baking_soda_oz), out_file)
 print_and_write("Salt:{:>28.1f} Oz".format(salt_oz), out_file)
print_and_write("Egg:{:>29.1f} Oz".format(egg_oz), out_file)print_and_write("Buttermilk:{:>23.1f} Oz".format(buttermilk_oz), out_file)
print_and_write("Oil:{:>29.1f} Oz".format(oil_oz), out_file)
print_and_write("Vanilla Extract:{:>18.1f} Oz".format(vanilla_oz), out_file)
print_and_write("Red Food Coloring:{:>16.1f} Oz".format(red_color_oz), out_file)
print_and_write("Distilled Vinegar:{:>16.1f} Oz".format(vinegar_oz), out_file)
print_and_write("", out_file)
print_and_write("Total:{:>27.1f} Oz".format(total_calc_oz), out_file)
print_and_write("", out_file)


def process_lemon_cake(size_code, out_file):
"""
***************************************************************************
Function: process_lemon_cake(size_code, out_file)

Parameters: size_code - 'L' or 'R' indicating Large or Regular cake
out_file - file object already opened for writing

Outputs: Prints and writes the ingredient list for a Lemon cake
of the requested size, including the filling.
Returns: None
Author: Kenichi Nishikawa
Date: 2025.12.09
Modifications: None
Description:
This function calculates the ingredient weights in ounces for aLemon cake (base + filling) using the recipe percentages and the
total cake weight for either a regular (64 oz) or large (112 oz)
cake. It then prints the ingredient list to the screen and writes
the same list to the output file***************************************************************************
"""
# Decide total weight based on size
if size_code.upper() == "L":
total_oz = LARGE_CAKE_OZ
header = "Large Lemon Cake Ingredient List"
else:
total_oz = REGULAR_CAKE_OZ
header = "Regular Lemon Cake Ingredient List"
# [Calculate] - base cake
butter_oz = total_oz * LEMON_BUTTER_PCT / 100.0
sugar_oz = total_oz * LEMON_SUGAR_PCT / 100.0
egg_oz = total_oz * LEMON_EGG_PCT / 100.0
flour_oz = total_oz * LEMON_FLOUR_PCT / 100.0
buttermilk_oz = total_oz * LEMON_BUTTERMILK_PCT / 100.0
vanilla_oz = total_oz * LEMON_VANILLA_PCT / 100.0
# [Calculate] - filling
fill_egg_yolk_oz = total_oz * LEMON_FILL_EGG_YOLK_PCT / 100.0
fill_sugar_oz = total_oz * LEMON_FILL_SUGAR_PCT / 100.0
fill_butter_oz = total_oz * LEMON_FILL_BUTTER_PCT / 100.0
fill_lemon_oz = total_oz * LEMON_FILL_LEMON_PCT / 100.0

total_calc_oz = (butter_oz + sugar_oz + egg_oz + flour_oz +
buttermilk_oz + vanilla_oz + fill_egg_yolk_oz +
fill_sugar_oz + fill_butter_o
# [Output]
print_and_write("", out_file)print_and_write(header, out_file)
 print_and_write("", out_file)
# Order is chosen to look similar to sample output
 print_and_write("Sugar:{:>27.1f} Oz".format(sugar_oz), out_file)
print_and_write("Egg:{:>29.1f} Oz".format(egg_oz), out_file)
print_and_write("Buttermilk:{:>23.1f} Oz".format(buttermilk_oz), out_file)
print_and_write("Vanilla Extract:{:>18.1f} Oz".format(vanilla_oz), out_file)
print_and_write("Butter:{:>27.1f} Oz".format(butter_oz), out_file)
print_and_write("Sifted Self Rising Flour:{:>9.1f} Oz".format(flour_oz), out_file)
print_and_write("Filling - Egg Yolk:{:>17.1f} Oz".format(fill_egg_yolk_oz), out_file)
print_and_write("Filling - Sugar:{:>20.1f} Oz".format(fill_sugar_oz), out_file)print_and_write("Filling - Butter:{:>19.1f} Oz".format(fill_butter_oz), out_file)
 print_and_write("Filling - Lemon Zest:{:>14.1f} Oz".format(fill_lemon_oz), out_file)
print_and_write("", out_file)
print_and_write("Total:{:>27.1f} Oz".format(total_calc_oz), out_file)
print_and_write("", out_file)

# ------------------------------------------------------------------------
# Function to process cake orders from a text file
# ------------------------------------------------------------------------

def process_cake_orders_from_file():
"""
***************************************************************************
Function: process_cake_orders_from_file()
Parameters: Non
Outputs: Prints ingredient lists to the screen and writes the
same ingredient lists to the file "cake_ingredients_list.txt".
Returns: Non
Author: Kenichi Nishikawa
Date: 2025.12.09
Modifications: None
Description:
This function reads cake orders from the file "cake_orders.txt".
Each line in the file contains a cake type and size in the format:
[1 character: cake type] [3 spaces] [1 character: cake size
For example:
2 L -> Red Velvet, Large
3 R -> Lemon, Regular

The function uses .read(n) to read fixed numbers of characters and
a sentinel loop that stops when no more characters can be read
(char == ''). For each order, it calls the appropriate cake
processing function to print and write the ingredient list.
At the end, it closes both the input and output files.***************************************************************************
"""
# Open the input and output files
orders_file = open("cake_orders.txt", "r")
out_file = open("cake_ingredients_list.txt", "w")

# Read the first character for the cake type (sentinel-based loop)
cake_type_char = orders_file.read(1)

while cake_type_char != "":
# Read and discard the 3 spaces
_ = orders_file.read(3)

# Read the size character
cake_size_char = orders_file.read(1)
# Read and discard the newline character
= orders_file.read(1)
# Decide which cake to process based on cake_type_char
if cake_type_char == "1":
process_chocolate_cake(cake_size_char, out_file)
elif cake_type_char == "2":
process_red_velvet_cake(cake_size_char, out_file)
elif cake_type_char == "3":
process_lemon_cake(cake_size_char, out_file)
else:
# Unknown type code; simple beginner-level handling
print_and_write("", out_file)
print_and_write("Unknown cake type code: " + cake_type_char, out_file)
print_and_write("", out_file)

# Read the next cake type for the next iteration
cake_type_char = orders_file.read(1)

# Close the files after finishing
orders_file.close()
out_file.close()

# ------------------------------------------------------------------------
# Main function
# ------------------------------------------------------------------------
def main():
 """
***************************************************************************
Function: main()
Parameters: None
Outputs: Calls the function that processes cake orders from file.
Returns: NoneAuthor: Kenichi Nishikaw
Date: 2025.12.09
Modifications: None
Description:
This is the main driver function for Lab 6. It calls the function
that reads cake orders from the text file "cake_orders.txt" and
writes the formatted ingredient lists to "cake_ingredients_list.txt".
**************************************************************************
"""
process_cake_orders_from_file()

# ------------------------------------------------------------------------
# Standard Python idiom to call main()
# ------------------------------------------------------------------------
if __name__ == "__main__":
main()
