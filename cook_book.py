import os


FILENAME = 'recipes.txt'
DISHES = ['Фахитос', 'Омлет']
COUNT = 3


def get_from_file(file_name):
    file = os.path.join('files', file_name)
    with open(file, 'r', encoding='UTF-8') as receipes_file:
        file_lines = receipes_file.readlines()
    return file_lines

def create_ingredient(file_line):
    first = file_line.find('|')
    last = file_line.rfind('|')
    ingredient = ([{'ingredient_name': file_line[:first].strip(),
        'quantity': int(file_line[first + 1:last].strip()),
        'measure': file_line[last+1:].strip()}])
    return ingredient

def write_cook_book(file_lines):
    cook_book = {}
    x = 0
    while x < len(file_lines):
        dish_name = file_lines[x].strip()
        x += 1
        ingredients = []
        for y in range(int(file_lines[x].strip())):
            ingredients += create_ingredient(file_lines[x + y + 1])
        x += y + 3
        cook_book[dish_name] = ingredients
    return cook_book

def get_shop_list_by_dishes(dishes, count):
    cook_book = write_cook_book(get_from_file(FILENAME))
    shop_list = {}
    for dish_name in dishes:
        ingredients = cook_book[dish_name]
        for ingredient in ingredients:
            ingredient_name = ingredient['ingredient_name']
            try:
                quantity = shop_list[ingredient_name]['quantity']
                shop_list[ingredient_name] = ({
                    'measure': ingredient['measure'],
                    'quantity': quantity + ingredient['quantity'] * count})
            except:
                shop_list[ingredient_name] = ({
                    'measure': ingredient['measure'],
                    'quantity': ingredient['quantity'] * count})
    return shop_list


print(get_shop_list_by_dishes(DISHES, COUNT))