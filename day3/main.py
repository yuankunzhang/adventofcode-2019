#!/usr/bin/env python
# -*- coding: utf-8 -*-


def wire(path):
    wire = set()
    steps = {}

    x, y = 0, 0
    z = 0

    for segment in path.split(','):
        direction = segment[0]
        distance = int(segment[1:])

        if direction == 'R':
            for r in range(y + 1, y + distance + 1):
                wire.add((x, r))
                if (x, r) not in steps:
                    steps[(x, r)] = z + r - y
            y += distance
            z += distance
        elif direction == 'D':
            for d in range(x + 1, x + distance + 1):
                wire.add((d, y))
                if (d, y) not in steps:
                    steps[(d, y)] = z + d - x
            x += distance
            z += distance
        elif direction == 'L':
            for l in range(y - 1, y - distance - 1, -1):
                wire.add((x, l))
                if (x, l) not in steps:
                    steps[(x, l)] = z + y - l
            y -= distance
            z += distance
        elif direction == 'U':
            for u in range(x - 1, x - distance - 1, -1):
                wire.add((u, y))
                if (u, y) not in steps:
                    steps[(u, y)] = z + x - u
            x -= distance
            z += distance

    return wire, steps


def part1():
    data = [x.strip() for x in open('input').readlines()]
    wire1, _ = wire(data[0])
    wire2, _ = wire(data[1])

    crosses = wire1.intersection(wire2)
    return sum(min([[abs(x), abs(y)] for (x, y) in crosses]))


def part2():
    data = [x.strip() for x in open('input').readlines()]
    wire1, steps1 = wire(data[0])
    wire2, steps2 = wire(data[1])

    crosses = wire1.intersection(wire2)
    nearest = min(crosses, key=lambda point: steps1[point] + steps2[point])
    return steps1[nearest] + steps2[nearest]


print(part2())
