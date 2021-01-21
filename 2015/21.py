#!/usr/bin/env python3

class Modifier:
    def __init__(self, name: str, gold: int, damage: int, armor: int):
        self.name = name
        self.gold = gold
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return self.name


class Char:
    def __init__(self, hp: int, damage: int, armor: int):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def alive(self):
        return self.hp > 0

    def attack(self, opponent):
        damage = self.damage - opponent.armor
        if damage <= 0:
            damage = 1
        opponent.hp -= damage


def fight(p1: Char, p2: Char):
    while p1.alive() and p2.alive():
        p1.attack(p2)
        if p2.alive():
            p2.attack(p1)


if __name__ == "__main__":
    # test
    boss = Char(12, 7, 2)
    me = Char(8, 5, 5)

    fight(me, boss)

    assert me.alive()
    assert me.hp == 2
    assert not boss.alive()
    assert boss.hp == 0

    weapons = [
        Modifier("dagger", 8, 4, 0),
        Modifier("shortsword", 10, 5, 0),
        Modifier("warhammer", 25, 6, 0),
        Modifier("longsword", 40, 7, 0),
        Modifier("greataxe", 74, 8, 0),
    ]

    armors = [
        Modifier("None", 0, 0, 0),
        Modifier("Leather", 13, 0, 1),
        Modifier("Chainmail", 31, 0, 2),
        Modifier("Splintmail", 53, 0, 3),
        Modifier("Bandedmail", 75, 0, 4),
        Modifier("Platemail", 102, 0, 5),
    ]

    rings = [
        Modifier("None", 0, 0, 0),
        Modifier("Damage + 1", 25, 1, 0),
        Modifier("Damage + 2", 50, 2, 0),
        Modifier("Damage + 3", 100, 3, 0),
        Modifier("Defense + 1", 20, 0, 1),
        Modifier("Defense + 2", 40, 0, 2),
        Modifier("Defense + 3", 80, 0, 3),
    ]

    part1 = 10000
    part2 = 0

    for weapon in weapons:
        for armor in armors:
            for ring1 in rings:
                for ring2 in rings:
                    if ring1.gold != 0 and ring1 == ring2:
                        continue

                    spent = weapon.gold + armor.gold + ring1.gold + ring2.gold

                    boss = Char(104, 8, 1)

                    me = Char(100,
                              ring1.damage + ring2.damage + weapon.damage,
                              ring1.armor + ring2.armor + armor.armor)

                    fight(me, boss)

                    if me.alive():
                        if part1 > spent:
                            print('new part1', weapon, armor, ring1, ring2, spent)
                            part1 = spent

                    if not me.alive():
                        if part2 < spent:
                            print('new part2', weapon, armor, ring1, ring2, spent)
                            part2 = spent

    print('part1', part1)
    print('part2', part2)
