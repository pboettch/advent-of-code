#!/usr/bin/env python3

from typing import List, Dict
from math import isqrt
import sys


def to_int(line: str):
    assert len(line) == 10

    num = 0
    for i, v in enumerate(reversed(line)):
        if v == '#':
            num += 1 << i
    return num


class Tile:
    def __init__(self, id: int, n, s, w, e, image):
        self._id = id
        self._north = n
        self._south = s
        self._east = e
        self._west = w
        self._image = image

    @property
    def n(self):
        return self._north

    @property
    def s(self):
        return self._south

    @property
    def e(self):
        return self._east

    @property
    def w(self):
        return self._west

    @property
    def image(self):
        return self._image

    def print(self):
        print(f" {self.n:>010b}")
        for e, w in zip(f"{self.e:>010b}", f"{self.w:>010b}"):
            print(f"{w}          {e}")
        print(f" {self.s:>010b}")

    @property
    def id(self):
        return self._id

    def __repr__(self):
        return f"Tile-{self._id}({self.n}, {self.w}, {self.s}, {self.e})"

    def __str__(self):
        return self.__repr__()


class TileGenerator:
    def __init__(self, id: int, data: List[str]):
        self._id = id
        self._data = data

    @property
    def id(self):
        return self._id

    @property
    def data(self):
        return self._data

    # 90° - clockwise
    def rotate(self):
        # https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
        self._data = list(zip(*self._data[::-1]))

    def flip(self):
        self._data = [list(reversed(line)) for line in self._data]

    def get_tile(self):
        north = self._data[0]
        south = self._data[-1]
        west = [line[0] for line in self._data]
        east = [line[-1] for line in self._data]

        image = [line[1:-1] for line in self._data[1:-1]]

        return Tile(self.id, to_int(north), to_int(south), to_int(west), to_int(east), image)


def test():
    data = [
        '........#.',
        '..........',
        '..........',
        '..........',
        '#.........',
        '..........',
        '..........',
        '.........#',
        '..........',
        '...#......',
    ]

    # data = [list(line) for line in data]
    # for l in data:
    #     print(''.join(l))

    tile_gen = TileGenerator(1337, data)

    tile = tile_gen.get_tile()
    tile.print()

    assert tile.n == 2 and tile.w == 32 and tile.s == 64 and tile.e == 4

    tile_gen.rotate()
    tile = tile_gen.get_tile()
    tile.print()

    assert tile.n == 16 and tile.e == 2 and tile.s == 128 and tile.w == 64


def tile_fits(tile: Tile, grid: List[List[Tile]], x: int, y: int):
    if y - 1 >= 0:
        if grid[y - 1][x] is not None and tile.n != grid[y - 1][x].s:
            return False

    # if y + 1 < len(grid):
    #     if grid[y + 1][x] is not None and tile.s != grid[y + 1][x].n:
    #         print('failed south')
    #         return False

    if x - 1 >= 0:
        if grid[y][x - 1] is not None and tile.w != grid[y][x - 1].e:
            return False

    # if x + 1 < len(grid[0]):
    #     if grid[y][x + 1] is not None and tile.e != grid[y][x + 1].w:
    #         print('failed east')
    #         return False

    return True


matched_grid = None


def find_solution(grid: List[List[Tile]], index: int, dim: int, tiles: Dict[int, List[Tile]], available: List[int]):
    global matched_grid

    if matched_grid is not None:
        return

    if index == dim * dim:
        sol = grid[0][0].id * grid[-1][0].id * grid[0][-1].id * grid[-1][-1].id
        print('done found solution', sol)
        matched_grid = []
        for line in grid:
            matched_grid.append(line.copy())
        return

    x = index % dim
    y = index // dim

    for id, variants in tiles.items():
        if id not in available:
            continue

        available.remove(id)

        for tile in variants:
            if tile_fits(tile, grid, x, y):
                grid[y][x] = tile
                find_solution(grid, index + 1, dim, tiles, available)
                grid[y][x] = None

        available.append(id)


if __name__ == '__main__':
    test()

    tiles = {}
    data = open('20.input').read(30000)
    for tile in data.split('\n\n'):
        lines = tile.split('\n')
        if len(lines[-1]) == 0:  # kludge
            lines = lines[0:-1]

        tile_gen = TileGenerator(int(lines[0][5:-1]), lines[1:])

        tiles[tile_gen.id] = []
        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())
        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())
        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())
        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())

        tile_gen.flip()

        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())
        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())
        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())
        tile_gen.rotate()
        tiles[tile_gen.id].append(tile_gen.get_tile())

    print('tile variants', len(tiles) * len(tiles[list(tiles.keys())[0]]))

    dim = isqrt(len(tiles))
    assert dim * dim == len(tiles)
    print(f'grid dim: {dim}x{dim}')

    grid = []
    for i in range(dim):
        grid.append([None for _ in range(dim)])

    find_solution(grid, 0, dim, tiles, [*tiles.keys()])

    image = []
    for line in matched_grid:
        for i in range(len(line[0].image[0])):  # all images are squares
            image.append(''.join([''.join(tile.image[i]) for tile in line]))

    class Monster:
        def __init__(self, monster: List[str]):
            self._height = len(monster)
            self._width = len(monster[0])

            self._coords = []

            for y, line in enumerate(monster):
                for x, ch in enumerate(line):
                    if ch == '#':
                        self._coords.append((x, y))

        @property
        def height(self):
            return self._height

        @property
        def width(self):
            return self._width

        @property
        def coords(self):
            return self._coords


    def get_roughness(image: List[str], monster: Monster):
        monster_count = 0

        image = image.copy()
        for y in range(len(image) - monster.height):
            for x in range(len(image[0]) - monster.width):
                matches = 0
                for coord in monster.coords:
                    if image[coord[1] + y][coord[0] + x] == '#':
                        matches += 1

                if matches == len(monster.coords):
                    monster_count += 1
                    print('monster found at', x, y)
                    for coord in monster.coords:
                        nl = list(image[coord[1] + y])
                        nl[coord[0] + x] = 'O'
                        image[coord[1] + y] = ''.join(nl)

        roughness = 0
        for line in image:
            roughness += line.count('#')
        return roughness, monster_count


    monster_str = ["                  # ",
                   "#    ##    ##    ###",
                   " #  #  #  #  #  #   "]
    m = Monster(monster_str)

    tgen = TileGenerator(0, image)

    print('roughness', get_roughness(tgen.data, m))
    tgen.rotate()
    print('roughness', get_roughness(tgen.data, m))
    tgen.rotate()
    print('roughness', get_roughness(tgen.data, m))
    tgen.rotate()
    print('roughness', get_roughness(tgen.data, m))

    tgen.flip()

    print('roughness', get_roughness(tgen.data, m))
    tgen.rotate()
    print('roughness', get_roughness(tgen.data, m))
    tgen.rotate()
    print('roughness', get_roughness(tgen.data, m))
    tgen.rotate()
    print('roughness', get_roughness(tgen.data, m))
