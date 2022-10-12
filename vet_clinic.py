cats = [('Снейп', 1, 'Марина', 'Апраксина'),
        ('Лютик', 4, 'Виталий', 'Соломин'),
        ('Снежок', 3, 'Марина', 'Апраксина')]

cat_1 = f'{cats[0][0]}, {cats[0][1]}'
cat_2 = f'{cats[1][0]}, {cats[1][1]}'
cat_3 = f'{cats[2][0]}, {cats[2][1]}'

cat_dictionary = {}

cat_dictionary.setdefault(' '.join(cats[0][2:]), []).append(cat_1)
cat_dictionary.setdefault(' '.join(cats[1][2:]), []).append(cat_2)
cat_dictionary.setdefault(' '.join(cats[2][2:]), []).append(cat_3)

name = input('Owner:')

print(f'{name}:{"; ".join(cat_dictionary[name])}')