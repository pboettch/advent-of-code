#!/usr/bin/env python3


if __name__ == "__main__":
    # lines = ["acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"]
    lines = open('8-input')
    # lines = open('8-example')

    part1 = 0
    part2 = 0

    for data in lines:
        notes, display = data.split(' | ')
        notes = [set(n) for n in notes.split()]
        display = [set(n) for n in display.split()]

        configs = [None] * 10

        for n in notes:
            if len(n) == 2:
                configs[1] = n
            elif len(n) == 3:
                configs[7] = n
            elif len(n) == 4:
                configs[4] = n
            elif len(n) == 7:
                configs[8] = n

        while None in configs:
            for n in notes:
                if n in configs:
                    continue

                if len(n) == 6:
                    if n & configs[4] == configs[4]:
                        configs[9] = n
                    elif len(n & configs[1]) == 2:
                        configs[0] = n
                    else:
                        configs[6] = n
                elif len(n - configs[7]) == 2:
                    configs[3] = n
                elif configs[9] is not None:
                    if n & configs[9] == n:
                        configs[5] = n
                    else:
                        configs[2] = n

        s = 0
        for n in display:
            if len(n) in [2, 3, 4, 7]:
                part1 += 1
            s *= 10
            s += configs.index(n)
        part2 += s

    print('part1', part1)
    print('part2', part2)
