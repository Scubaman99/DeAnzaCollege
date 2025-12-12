"""
*******************************************************************************
Filename: knishikawa_cis340_lab08_final.py
Author: Kenichi Nishikawa
Date: 2025.12.10
Modifications:
    - Full implementation of Lab08 using OOP.
    - Cake class with attributes, calc_ingrd(), __str__().
    - Uses 2D nested ingredient list.
    - Uses Lab07 formatting and docstring style.

Description:
Implements Cake class with OOP approach. Creates 6 cake objects and prints
ingredient listings in exact Lab05/Lab07 formatting.
*******************************************************************************
"""

REGULAR_OZ = 64.0
LARGE_OZ = 112.0

CHOCOLATE_RECIPE = {
    "Flour": 15.8, "Sugar": 24.5, "Unsweetened Cocoa Powder": 5.6,
    "Baking Powder": 0.4, "Baking Soda": 0.6, "Salt": 0.4,
    "Egg": 9.0, "Buttermilk": 18.0, "Oil": 8.1,
    "Vanilla Extract": 0.6, "Boiling Water": 17.0
}

RED_VELVET_RECIPE = {
    "Flour": 22.4, "Sugar": 22.4, "Unsweetened Cocoa Powder": 0.4,
    "Baking Soda": 0.7, "Salt": 0.4, "Egg": 9.0,
    "Buttermilk": 17.9, "Oil": 24.0, "Vanilla Extract": 0.3,
    "Red Food Coloring": 2.1, "Distilled Vinegar": 0.4
}

LEMON_RECIPE = {
    "Sugar": 15.0, "Egg": 9.0, "Buttermilk": 9.0,
    "Vanilla Extract": 0.2, "Butter": 8.5,
    "Sifted Self-Rising Flour": 15.6, "Filling - Egg Yolk": 17.9,
    "Filling - Sugar": 11.3, "Filling - Butter": 2.1,
    "Filling - Lemon Zest": 11.4
}

INGREDIENT_NAMES = [
    "Flour","Sugar","Unsweetened Cocoa Powder","Baking Powder",
    "Baking Soda","Salt","Egg","Buttermilk","Oil","Vanilla Extract",
    "Boiling Water","Red Food Coloring","Distilled Vinegar",
    "Sifted Self-Rising Flour","Butter","Filling - Egg Yolk",
    "Filling - Sugar","Filling - Butter","Filling - Lemon Zest"
]

class Cake:
    """
    Cake class implementing OOP version of cake ingredient calculation.
    """

    def __init__(self, type, size):
        """
        Initializes cake object, assigns recipe, name, weight, and builds ingredient list.
        """
        self.type = type
        self.size = size.upper()
        self.weight = LARGE_OZ if self.size == 'L' else REGULAR_OZ

        if type == 1:
            self.name = "Chocolate Cake"
            self.recipe = CHOCOLATE_RECIPE
        elif type == 2:
            self.name = "Red Velvet Cake"
            self.recipe = RED_VELVET_RECIPE
        else:
            self.name = "Lemon Cake"
            self.recipe = LEMON_RECIPE

        self.ingrd_list = [INGREDIENT_NAMES, []]
        self.calc_ingrd(self.weight, self.recipe)

    def calc_ingrd(self, weight, recipe):
        """
        Populates ingredient weights into the nested list structure.
        """
        for name in INGREDIENT_NAMES:
            if name in recipe:
                wt = weight * recipe[name] / 100.0
                self.ingrd_list[1].append(wt)
            else:
                self.ingrd_list[1].append(None)

    def __str__(self):
        """
        Returns formatted ingredient list as string.
        """
        size_label = "Large" if self.size == 'L' else "Regular"
        output = f"\nIngredient Quantities for {size_label} {self.name}\n\n"

        total = 0.0
        for label, wt in zip(self.ingrd_list[0], self.ingrd_list[1]):
            if wt is not None:
                output += f"{label + ':':<30s}{wt:>10.1f} Oz\n"
                total += wt

        output += f"\n{'Total:':<30s}{total:>10.1f} Oz\n"
        return output


# ---------------------- TEST CODE BLOCK ------------------------------

reg_chocolate_cake = Cake(1,'R')
lrg_chocolate_cake = Cake(1,'L')
reg_red_velvet_cake = Cake(2,'R')
lrg_red_velvet_cake = Cake(2,'L')
reg_lemon_cake = Cake(3,'R')
lrg_lemon_cake = Cake(3,'L')

print(reg_chocolate_cake)
print(lrg_chocolate_cake)
print(reg_red_velvet_cake)
print(lrg_red_velvet_cake)
print(reg_lemon_cake)
print(lrg_lemon_cake)

# -------------------- RECORD OF EXECUTION --------------------
"""
Paste your execution transcript here.
"""
