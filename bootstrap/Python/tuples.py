recipe1 = ("Veg Sandwich", "15 minutes", "Easy")
recipe2 = ("Veg Burger", "25 minutes", "Medium")
print("Recipe 1:", recipe1)
print("Recipe 2:", recipe2)
print()
ingredients1 = {
    "Bread",
    "Butter",
    "Tomato",
    "Onion",
    "Cheese",
    "Salt"
}
ingredients2 = {
    "Burger Bun",
    "Tomato",
    "Cheese",
    "Lettuce"
    "Salt"
    "Mayonnaise"
}
print("Ingredients of Recipe 1")
print(ingredients1)
print()
print("Ingredients of Recipe 2")
print(ingredients2)
print("All Ingredients (Union)")
print(ingredients1.union(ingredients2))
print()
print("Common ingredients")
print(ingredients1.intersection(ingredients2))
print()
print("Only in Recipe 1")
print(ingredients1.difference(ingredients2))
print()
print("Only in Recipe 2")
print(ingredients2.difference(ingredients1))
print()
print("Unique ingredients in both recipes")
print(ingredients1.symmetric_difference(ingredients2))
