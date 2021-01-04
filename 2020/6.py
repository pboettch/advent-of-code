#!/usr/bin/env python3

content = open('6.input').read(100000)
groups = [group.split('\n') for group in content.split('\n\n')]

yes_any = 0
yes_all = 0

for group in groups:
    anyone = set()
    everyone = set()

    first_person_of_group = True

    for person in group:
        for a in person:
            anyone.add(a)
            if first_person_of_group:
                everyone.add(a)

        if not first_person_of_group:
            for a in list(everyone):
                if a not in person:
                    everyone.remove(a)

        first_person_of_group = False

    yes_any += len(anyone)
    yes_all += len(everyone)

print('anyone', yes_any)
print('everyone', yes_all)




