import os

with open(os.path.join('files', 'recipes.txt'), 'r',\
    encoding='UTF-8') as receipes_file:
    file_lines = receipes_file.readlines()