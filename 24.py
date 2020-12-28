#!/usr/bin/env python3


class Tile:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
        self._c = 'W'
        self._nc = None

    def nw(self):
        return self._x - 1, self._y - 1

    def ne(self):
        return self._x + 1, self._y - 1

    def sw(self):
        return self._x - 1, self._y + 1

    def se(self):
        return self._x + 1, self._y + 1

    def w(self):
        return self._x - 2, self._y

    def e(self):
        return self._x + 2, self._y

    def flip(self):
        self._c = 'B' if self._c == 'W' else 'W'

    def flip_later(self):
        assert self._nc is None
        self._nc = 'B' if self._c == 'W' else 'W'
        # print('flipping later', self._x, self._y, 'to', self._nc)

    def commit(self):
        if self._nc is not None:
            self._c = self._nc
        self._nc = None

    @property
    def color(self):
        return self._c


class Floor:
    def __init__(self):
        self._f = {}

    def get(self, x, y):
        if not (x, y) in self._f:
            self._f[(x, y)] = Tile(x, y)
        return self._f[(x, y)]

    def count(self, c: str):
        count = 0
        for tile in self._f.values():
            if tile.color == c:
                count += 1
        return count

    def x_lim(self):
        max, min = None, None
        for coord in self._f:
            if max is None or coord[0] > max:
                max = coord[0]
            if min is None or coord[0] < min:
                min = coord[0]

        return min, max

    def y_lim(self):
        max, min = None, None
        for coord in self._f:
            if max is None or coord[1] > max:
                max = coord[1]
            if min is None or coord[1] < min:
                min = coord[1]

        return min, max

    def count_adj(self, tile: Tile, c: str):
        count = 0
        count += int(self.get(*tile.ne()).color == c)
        count += int(self.get(*tile.nw()).color == c)
        count += int(self.get(*tile.e()).color == c)
        count += int(self.get(*tile.w()).color == c)
        count += int(self.get(*tile.se()).color == c)
        count += int(self.get(*tile.sw()).color == c)
        return count

    def flip(self):
        # for coord, tile in dict(self._f).items():

        x_min, x_max = self.x_lim()
        y_min, y_max = self.x_lim()
        for x in range(x_min - 1, x_max + 2):
            for y in range(y_min - 1, y_max + 2):
                tile = self.get(x,y)

                if tile.color == 'B' and self.count_adj(tile, 'B') in [0, 3, 4, 5, 6]:
                    tile.flip_later()

                if tile.color == 'W' and self.count_adj(tile, 'B') == 2:
                    tile.flip_later()

        for _, tile in self._f.items():
            tile.commit()


floor = Floor()

for seq in open('24.input').readlines():
    tile = floor.get(0, 0)

    c_iter = iter(seq)
    while True:
        c = next(c_iter)
        if c == 'n':
            c = next(c_iter)
            if c == 'e':
                x, y = tile.ne()
            elif c == 'w':
                x, y = tile.nw()
            else:
                raise ValueError('unknown north')
        elif c == 's':
            c = next(c_iter)
            if c == 'e':
                x, y = tile.se()
            elif c == 'w':
                x, y = tile.sw()
            else:
                raise ValueError('unknown south')
        elif c == 'e':
            x, y = tile.e()
        elif c == 'w':
            x, y = tile.w()
        elif c == '\n':
            break
        else:
            raise ValueError('unknown direction', c)

        tile = floor.get(x, y)

    tile.flip()

black = floor.count('B')
print('initial black tiles', black)

for day in range(1, 101):
    floor.flip()
    print(day, floor.count('B'))

