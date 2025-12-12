"""
*******************************************************************************
Filename:      make_more_cake_enhanced_sln.py

Author:        Victor Lau

Date:          2019.02.18

Modifications: 2022.06.04

Description:   This module performs the first stage of a cake making process.
               It's tasks includes:
               1) Query a cake order
               2) Calculate the amounts, in oz, needed for each ingredient
               3) print the ingredients list with the amounts for each
               4) Repeat Step 1 - 3 until user enter 'q' or 'Q' to quit; a while loop using sentinel
*******************************************************************************
"""

def print_ingrd(flour_wt,sugar_wt,unsweetened_cocoa_powder_wt,baking_powder_wt,
                baking_soda_wt,salt_wt,egg_wt,buttermilk_wt,oil_wt,
                vanilla_extract_wt,boiling_water_wt,red_food_coloring_wt,
                distilled_vinegar_wt,butter_wt,sifted_self_rising_flour_wt,
                fill_egg_yolk_wt,fill_sugar_wt,fill_butter_wt,
                fill_lemon_zest_wt):
    """
    ***************************************************************************

    Function:   print_ingrd( )

    Parameters: flour_wt                # calculated weights of ingredient in oz
                sugar_wt
                unsweetened_cocoa_powder_wt
                baking_powder_wt
                baking_soda_wt
                salt_wt
                egg_wt
                buttermilk_wt
                oil_wt
                vanilla_extract_wt
                boiling_water_wt
                red_food_coloring_wt
                distilled_vinegar_wt
                butter_wt
                sifted_self_rising_flour_wt
                fill_egg_yolk_wt
                fill_sugar_wt
                fill_butter_wt
                fill_lemon_zest_wt

    Inputs:     None

    Outputs:    print the ingredients list with weight for each ingredient

    Returns:    None

    Author:     Victor Lau

    Date:       2019.02.18

    Modifications:

    Description:
        This function prints the ingredient list with each amount in oz. Tasks:
        1. Check the value of every parameter(possible ingredient)
        2. If the wt value is greater zero, print the ingredient name and its weight
        3. Calculate and print the total weight
    ***************************************************************************
    """

    if flour_wt != 0:
        print("%-28s%5.1f Oz" % ("Flour:", flour_wt))
    if sugar_wt != 0:
        print("%-28s%5.1f Oz" % ("Sugar: ", sugar_wt))
    if unsweetened_cocoa_powder_wt != 0:
        print("%-28s%5.1f Oz" % ("Unsweetened Cocoa Powder: ", unsweetened_cocoa_powder_wt))
    .
    .
    .

    if sifted_self_rising_flour_wt != 0:
        print("%-28s%5.1f Oz" % ("Sifted Self Rising Flour: ", sifted_self_rising_flour_wt))
    # filling
    if fill_egg_yolk_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Egg Yolk: ", fill_egg_yolk_wt))
    if fill_sugar_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Sugar: ", fill_sugar_wt))
    if fill_butter_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Butter: ", fill_butter_wt))
    if fill_lemon_zest_wt != 0:
        print("%-28s%5.1f Oz" % ("Filling - Lemon Zest: ", fill_lemon_zest_wt))

    # Verification - back calcuation to get total weight
    print("%-28s%5.1f Oz" % ("Total: ", flour_wt + ...
        ...
        ...
        ...
        + fill_lemon_zest_wt) )

    print()
    print()


def calc_n_print_chocolate_ingrd(cake_wt, size_label):
    """
    ***************************************************************************

    Function:   calc_n_print_chocolate_ingrd( )

    Parameters: cake_wt - cake weight in oz
                size_label - either "Large" or "Regular"

    Inputs:     None

    Outputs:    1. print the header indicating cake type and size
                2. print the ingredients list with weight for each ingredient;
                by calling print_ingrd( )

    Returns:    None

    Author:     Victor Lau

    Date:       2019.02.18

    Modifications:

    Description:
        This function calculates the weight of each ingredient for a
        Chocolate Cake according to the recipe. Tasks:
        1. Use constants to define the Chocolate Cake recipe
        2. Initialize all ingredient weights to zero
        3. Calculate the weights for each ingredient
        4. Print the Header and, Call print_ingrd( ) to print the ingredients list
    ***************************************************************************
    """

    # Chocolate cake recipe; in percentage of total weight
    CHOC_FLOUR_PCT = 15.8
    CHOC_SUGAR_PCT = 24.5
    CHOC_UNSWEETENED_COCOA_POWDER_PCT = 5.6
    CHOC_BAKING_POWER_PCT = 0.4
    CHOC_BAKING_SODA_PCT = 0.6
    CHOC_SALT_PCT = 0.4
    CHOC_EGG_PCT = 9.0
    CHOC_BUTTERMILK_PCT = 18.0
    CHOC_OIL_PCT = 8.1
    CHOC_VANILLA_EXTRACT_PCT = 0.6
    CHOC_BOILING_WATER_PCT = 17.0

    # zero every ingredient wt
    flour_wt = 0
    .
    .
    .
    sifted_self_rising_flour_wt = 0

    # Filling
    fill_egg_yolk_wt = 0
    .
    .
    .
    fill_lemon_zest_wt = 0

    #calculate ingredient wts for choclate cake
    flour_wt = cake_wt * CHOC_FLOUR_PCT/100
    .
    .
    .
    boiling_water_wt = cake_wt * CHOC_BOILING_WATER_PCT/100

    """
    ***************************************************************************
                                    OUTPUT
    ***************************************************************************
    """
    # First, print the header
    header = "Ingredient Quantities for %s Chocolate Cake" % (size_label)
    print(header)

    print_ingrd(flour_wt, sugar_wt, unsweetened_cocoa_powder_wt,
                baking_powder_wt, baking_soda_wt, salt_wt, egg_wt,
                buttermilk_wt, oil_wt, vanilla_extract_wt, boiling_water_wt,
                red_food_coloring_wt, distilled_vinegar_wt, butter_wt,
                sifted_self_rising_flour_wt, fill_egg_yolk_wt, fill_sugar_wt,
                fill_butter_wt, fill_lemon_zest_wt)


def calc_n_print_red_velvet_ingrd(cake_wt, size_label):
    """
    ***************************************************************************

    Function:   calc_n_print_red_velvet_ingrd( )

    Parameters: cake_wt - cake weight in oz
                size_label - either "Large" or "Regular"

    Inputs:     None

    Outputs:    1. print the header indicating cake type and size
                2. print the ingredients list with weight for each ingredient;
                by calling print_ingrd( )

    Returns:    None

    Author:     Victor Lau

    Date:       2019.02.18

    Modifications:

    Description:
        This function calculates the weight of each ingredient for a
        Red Velvet Cake according to the recipe. Tasks:
        1. Use constants to define the Chocolate Cake recipe
        2. Initialize all ingredient weights to zero
        3. Calculate the weights for each ingredient
        4. Print the Header and, Call print_ingrd( ) to print the ingredients list
    ***************************************************************************
    """

    # Red Velvet cake recipe; in percentage of total weight
    REDV_FLOUR_PCT = 22.4
    .
    .
    .
    REDV_DISTILLED_VINEGAR_PCT = 0.4

    # zero every ingredient wt
    flour_wt = 0
    .
    .
    .
    sifted_self_rising_flour_wt = 0

    # Filling
    fill_egg_yolk_wt = 0
    .
    .
    .
    fill_lemon_zest_wt = 0

    # Calculate the ingredient wts for Red Velvet Cake
    flour_wt = cake_wt * REDV_FLOUR_PCT/100
    .
    .
    .
    distilled_vinegar_wt = cake_wt * REDV_DISTILLED_VINEGAR_PCT/100

    """
    ***************************************************************************
                                    OUTPUT
    ***************************************************************************
    """
    # First, print the header
    header = "Ingredient Quantities for %s Red Velvet Cake" % (size_label)
    print(header)

    print_ingrd(flour_wt, sugar_wt, unsweetened_cocoa_powder_wt,
                baking_powder_wt, baking_soda_wt, salt_wt, egg_wt,
                buttermilk_wt, oil_wt, vanilla_extract_wt, boiling_water_wt,
                red_food_coloring_wt, distilled_vinegar_wt, butter_wt,
                sifted_self_rising_flour_wt, fill_egg_yolk_wt, fill_sugar_wt,
                fill_butter_wt, fill_lemon_zest_wt)
    # *****************************************************
    #           End of calc_red_velvet_ingrd()
    # *****************************************************


def calc_n_print_lemon_ingrd(cake_wt, size_label):
    """
    ***************************************************************************

    Function:   calc_n_print_lemon_ingrd( )

    Parameters: cake_wt - cake weight in oz
                size_label - either "Large" or "Regular"

    Inputs:     None

    Outputs:    1. print the header indicating cake type and size
                2. print the ingredients list with weight for each ingredient;
                by calling print_ingrd( )

    Returns:    None

    Author:     Victor Lau

    Date:       2019.02.18

    Modifications:

    Description:
        This function calculates the weight of each ingredient for a
        Lemon Cake according to the recipe. Tasks:
        1. Use constants to define the Lemon Cake recipe
        2. Initialize all ingredient weights to zero
        3. Calculate the weights for each ingredient
        4. Print the Header and, Call print_ingrd( ) to print the ingredients list
    ***************************************************************************
    """

    # Lemon cake recipe; in percentage of total weight
    LEMO_BUTTER_PCT = 8.5
    .
    .
    .
    LEMO_FILL_LEMON_ZEST_PCT = 11.4

    # zero every ingredient wt
    flour_wt = 0
    .
    .
    .
    sifted_self_rising_flour_wt = 0
    # Filling
    fill_egg_yolk_wt = 0
    .
    .
    fill_lemon_zest_wt = 0

    # Calculate the ingredient wts for Lemon Cake
    butter_wt = cake_wt * LEMO_BUTTER_PCT/100
    .
    .
    .
    fill_lemon_zest_wt = cake_wt * LEMO_FILL_LEMON_ZEST_PCT/100

    """
    ***************************************************************************
                                    OUTPUT
    ***************************************************************************
    """
    # First, print the header
    header = "Ingredient Quantities for %s Lemon Cake" % (size_label)
    print(header)

    print_ingrd(flour_wt, sugar_wt, unsweetened_cocoa_powder_wt,
                baking_powder_wt, baking_soda_wt, salt_wt, egg_wt,
                buttermilk_wt, oil_wt, vanilla_extract_wt, boiling_water_wt,
                red_food_coloring_wt, distilled_vinegar_wt, butter_wt,
                sifted_self_rising_flour_wt, fill_egg_yolk_wt, fill_sugar_wt,
                fill_butter_wt, fill_lemon_zest_wt)
    # *****************************************************
    #               End of calc_lemon_ingrd()
    # *****************************************************


def make_cake_loop():
    """
    ***************************************************************************

    Function:   make_cake_loop( )

    Parameters: None

    Inputs:     cake_type       1 - Chocolate; 2 - Red Velvet; 3 - Lemon;
                cake_size       'L' - Large; 'R' - Regular

    Outputs: print the ingredients list with weight for each ingredient

    Returns: None

    Author:  Victor Lau

    Date:    2019.02.18

    Modifications:

    Description:
        This function is effectively the whole main program. It contains:
        1. All three recipes; Chocolate, Red Velvet and Lemon
        2. Initialization of all variables
        3. Query the cake order
        4. Calculate the ingredients amounts for the cake just order
        5. Print the ingredient list accompanied by weights
        6. Repeat Step 3 - 5 until user enter 'q' or 'Q' to quit
    ***************************************************************************
    """
    # Cake size - weight in oz
    LARGE_CAKE_WT = 7 * 16
    REGULAR_CAKE_WT = 4 * 16
    cake_wt = 0

    """
    *******************************************************************************
                                        INPUT
    *******************************************************************************
    """
    # query cake type; if 'q' or 'Q' was entered then quit the program
    cake_type_raw = input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")

    # *************************************************************************
    #                   Sentinel to take cake order input
    # *************************************************************************
    while not(cake_type_raw == 'q' or cake_type_raw == 'Q'):
        # query cake size
        cake_type = eval(cake_type_raw)
        cake_size = input("Please Select Cake Size; Enter L for large, R for regular: ")
        print()

        #Determine cake_wt and size_label
        if cake_size == 'R' or cake_size == 'r':
            cake_wt = REGULAR_CAKE_WT
            size_label = "Regular"
        elif cake_size == 'L' or cake_size == 'l':
            cake_wt = LARGE_CAKE_WT
            size_label = "Large"

        # if the cake selected is Chocolate Cake
        if cake_type == 1:
            if cake_size == 'R' or cake_size == 'r':
                cake_wt = REGULAR_CAKE_WT
                size_label = "Regular"
            elif cake_size == 'L' or cake_size == 'l':
                cake_wt = LARGE_CAKE_WT
                size_label = "Large"

            calc_n_print_chocolate_ingrd(cake_wt, size_label)

        elif cake_type == 2:
            ...
            ...
            ...

            calc_n_print_red_velvet_ingrd(cake_wt, size_label)

        # if the cake selected is Lemon Cake
        else:
            ...
            ...
            ...

            calc_n_print_lemon_ingrd(cake_wt, size_label)

        # take next order - query cake type; if 'q' or 'Q' was entered then quit the program
        cake_type_raw = input("Please Select Cake Type; Enter 1 for Chocolate, 2 for Red Velvet, 3 for Lemon, q to quit: ")

        # *************************************************************************
        #                          end of while loop
        # *************************************************************************

    print("Bye")

'''
*******************************************************************************
                            Program Starts Here
*******************************************************************************
'''
make_cake_loop()