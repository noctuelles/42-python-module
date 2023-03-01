cookbook = {
    'Sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': '10'
    },
    'Cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': '60'
    },
    'Salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': '15'
    }
}

def printRecipe(name):
    recipe = cookbook[name]
    print(f"""Recipe for {name}
    Ingredients list: {recipe['ingredients']}
    To be eaten for {recipe['meal']}.
    Takes {recipe['prep_time']} minutes of cooking.""")

def printRecipes():
    for recipe in cookbook:
        printRecipe(recipe)

def deleteRecipe(name):
    cookbook.pop(name)

def addRecipe(name, ingredients, meal_type, prep_time):
    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal_type,
        'prep_time': prep_time
    }

if __name__ == "__main__":
    addRecipe('Prout', ['caca', 'haricot'], 'lunch', '30')
    printRecipes()
