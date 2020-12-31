#!/usr/bin/env python3

ingredients_amount = {}

al_in = {}

for line in open('21.input').readlines():
    ingredients, allergens = line.rstrip()[0:-1].split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.split(', ')

    for a in allergens:
        if a not in al_in:
            al_in[a] = ingredients
        else:
            al_in[a] = list(set(al_in[a]) & set(ingredients))

    for i in ingredients:
        ingredients_amount.setdefault(i, 0)
        ingredients_amount[i] += 1

# reduce impossible occurences due to uniquely assigned ingredients
while True:
    changed = False

    for a, i in al_in.items():
        if len(i) == 1:
            for i2 in al_in.values():
                if len(i2) > 1:
                    if i[0] in i2:
                        i2.remove(i[0])
                        changed = True

    if not changed:
        break

print('final')
for a, i in al_in.items():
    print(a, i)
    del ingredients_amount[i[0]]

print('occurrences of non-allergic ingredients', sum([count for _, count in ingredients_amount.items()]))

canon_list = []
for a in sorted(al_in.keys()):
    for i in al_in[a]:
        if i not in canon_list:
            canon_list.append(i)

print('canonical list:', ','.join(canon_list))
