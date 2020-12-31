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
    def __init__(self, id: int, n, s, w, e):
        self._id = id
        self._north = n
        self._south = s
        self._east = e
        self._west = w

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

        assert len(data) == 10
        assert len(data[0]) == 10


        self._north = data[0]
        self._south = data[-1]
        self._west = [line[0] for line in data]
        self._east = [line[-1] for line in data]

        # print(self._north, self._east, self._south, self._west)

    @property
    def id(self):
        return self._id

    # 90° - counter-clockwise
    def rotate(self):
        self._east, self._south, self._west, self._north = \
            self._south[::-1], self._west, self._north[::-1], self._east

    def flip(self):
        self._east, self._south, self._west, self._north = \
             self._west, self._south[::-1], self._east, self._north[::-1]
        pass

    def get_tile(self):
        return Tile(self.id, to_int(self._north), to_int(self._south), to_int(self._west), to_int(self._east))


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

    data = [list(line) ]

    tile_gen = TileGenerator(1337, data)

    tile = tile_gen.get_tile()
    tile.print()

    assert tile.n == 2 and tile.w == 32 and tile.s == 64 and tile.e == 4

    tile_gen.rotate()
    tile = tile_gen.get_tile()
    tile.print()

    print(tile)
    assert tile.n == 4 and tile.e == 8 and tile.s == 32 and tile.w == 256


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
        matched_grid = grid.copy()
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
    # test()

    tiles = {}
    data = open('20-ex.input').read(30000)
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



