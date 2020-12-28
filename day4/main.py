#!/usr/bin/env python
# -*- coding: utf-8 -*-


def adjacent_digits_1(s):
    return s[0] == s[1] or s[1] == s[2] or \
        s[2] == s[3] or s[3] == s[4] or s[4] == s[5]


def adjacent_digits_2(s):
    if s[0] == s[1] and s[1] != s[2]:
        return True
    if s[1] == s[2] and s[0] != s[1] and s[2] != s[3]:
        return True
    if s[2] == s[3] and s[1] != s[2] and s[3] != s[4]:
        return True
    if s[3] == s[4] and s[2] != s[3] and s[4] != s[5]:
        return True
    if s[4] == s[5] and s[3] != s[4]:
        return True
    return False


def increase(s):
    return s[0] <= s[1] and s[1] <= s[2] and \
        s[2] <= s[3] and s[3] <= s[4] and s[4] <= s[5]


def is_valid_1(s):
    if not adjacent_digits_1(s):
        return False
    if not increase(s):
        return False
    return True


def is_valid_2(s):
    if not adjacent_digits_2(s):
        return False
    if not increase(s):
        return False
    return True


def part1():
    data = '153517-630395'
    lower, upper = [int(x) for x in data.split('-')]

    count = 0
    for x in range(lower, upper + 1):
        if is_valid_1(str(x)):
            count += 1

    return count


def part2():
    data = '153517-630395'
    lower, upper = [int(x) for x in data.split('-')]

    count = 0
    for x in range(lower, upper + 1):
        if is_valid_2(str(x)):
            count += 1

    return count


print(part2())
