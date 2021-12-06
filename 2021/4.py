#!/usr/bin/env python3


class Bingo:
    def __init__(self, file):
        self.board = []
        self.hits = [False] * 25

        file.readline()
        for c in range(5):
            l = f.readline().split()
            if len(l) != 5:
                raise IOError("could not read bingo-line")
            self.board += map(int, l)

        print("NEW BINGO", self.board)

    def add_number(self, n: int):
        if n in self.board:
            i = self.board.index(n)
            self.hits[i] = True

    def solved(self):
        for i in range(5):
            if sum(self.hits[i * 5:(i + 1) * 5]) == 5 or sum(self.hits[i:25:5]) == 5:
                return True
        return False

    def sum(self):
        return sum(n for i, n in enumerate(self.board) if not self.hits[i])


if __name__ == "__main__":
    part1 = 0
    part2 = 0

    bingos = []

    with open('4-input') as f:
        *numbers, = map(int, f.readline().split(','))
        while True:
            try:
                bingos += [Bingo(f)]
            except IOError:
                break

    for n in numbers:
        bingos_solved = sum(b.solved() for b in bingos)

        for bingo in bingos:
            # one unsolved bingo and it is this one
            last_one = None

            if bingos_solved == len(bingos) - 1 and \
                not bingo.solved():
                last_one = bingo

            bingo.add_number(n)
            if bingo.solved() and part1 == 0:
                part1 = bingo.sum() * n

            if last_one and bingo.solved():
                part2 = bingo.sum() * n

    print('part1', part1)
    print('part2', part2)
