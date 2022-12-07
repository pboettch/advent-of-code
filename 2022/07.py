#!/usr/bin/env python3

import sys
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Path:
    name: str
    parent: Optional['Path'] = None
    directories: dict[str, 'Path'] = field(default_factory=dict)
    size: int = 0
    total: int = 0


if __name__ == "__main__":

    root = Path('/')
    path = None

    for l in open(sys.argv[1] if len(sys.argv) > 1 else '07-input'):
        c = l.strip().split()
        if c[0] == '$':
            if c[1] == 'cd':
                if c[2] == '/':
                    path = root
                elif c[2] == '..':
                    path = path.parent
                else:
                    path = path.directories[c[2]]
            elif c[1] == 'ls':
                pass
        else:
            if c[0] == 'dir':
                path.directories.update({c[1]: Path(c[1], path)})
            else:
                path.size += int(c[0])


    def total_sizes(p: Path):
        p.total = p.size
        for _, d in p.directories.items():
            subdir_size = total_sizes(d)
            p.total += subdir_size
        return p.total


    total_sizes(root)


    def part1(p: Path):
        if p.total <= 100000:
            yield p.total
        for _, d in p.directories.items():
            yield from part1(d)


    print('part1', sum(part1(root)))

    needed_space = 30000000 - (70000000 - root.total)


    def part2(p: Path):
        if p.total >= needed_space:
            yield p.total
        for _, d in p.directories.items():
            yield from part2(d)


    print('part2', min(part2(root)))
