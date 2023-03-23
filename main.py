from pprint import pprint

with open('list-recipe.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        recipe_name = line.strip()
        num_ingr = int(file.readline())
        ingredients = []
        for id in range(num_ingr):
            ingr_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingr_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[recipe_name] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    order = {}
    for dish, ingredients in cook_book.items():
        if dish in dishes:
            for ingredient in ingredients:
                order[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': int(ingredient['quantity']) * person_count}
    print(order)

get_shop_list_by_dishes('Запеченный картофель', 2)

