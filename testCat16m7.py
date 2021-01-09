from Cat16m7 import Cat

cat_1 = Cat('Сэм', 'мальчик', '2')
cat_2 = Cat('Барон', 'мальчик', '2')

pets = [cat_1, cat_2]

for pet in pets:
    pet.print_list()