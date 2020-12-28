#!/usr/bin/env python3

input = [int(i) for i in '389125467']
input_len = len(input)

for move in range(0, 11):
    print(move, input)

    current = move % input_len
    three_cups = (input + input)[current + 1:current + 4]
    insert = input[current] - 1

    for cup in three_cups:
        input.remove(cup)


    while True:
        try:
            index = input.index(insert)
        except ValueError:
            insert -= 1
            if insert < 0:
                insert = input_len
            continue

        print('destination', input[index])
        input.insert(index + 1, three_cups[2])
        input.insert(index + 1, three_cups[1])
        input.insert(index + 1, three_cups[0])
        break

    current += 1
    if current > len(input):
        current = 0
