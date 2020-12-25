#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fuel(mass):
    return mass // 3 - 2


def part1():
    masses = [int(x) for x in open('input').readlines()]
    return sum([fuel(mass) for mass in masses])


def fuel_recursive(mass):
    if mass < 9:
        return 0
    return fuel(mass) + fuel_recursive(fuel(mass))


def part2():
    masses = [int(x) for x in open('input').readlines()]
    return sum([fuel_recursive(mass) for mass in masses])


print(part2())
