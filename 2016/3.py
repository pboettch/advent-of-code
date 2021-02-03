#!/usr/bin/env python3


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    numbers = [int(i) for i in open('3.input').read(50000).replace('\n', '').split()]

    for i in range(0, len(numbers), 3):
        a, b, c = numbers[i:i + 3]
        if a + b > c and a + c > b and b + c > a:
            part1 += 1

    for i in range(0, len(numbers), 9):
        for j in range(3):
            a, b, c = numbers[i + j:i + j + 9:3]
            if a + b > c and a + c > b and b + c > a:
                part2 += 1

    print('part1', part1)
    print('part2', part2)
