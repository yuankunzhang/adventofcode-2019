#!/usr/bin/env python
# -*- coding: utf-8 -*-

OP_ADD = 1
OP_MUL = 2
OP_HLT = 99


def run(code):
    ip = 0

    while True:
        if code[ip] not in (OP_ADD, OP_MUL, OP_HLT):
            raise Exception('Invalid input')

        if code[ip] == OP_HLT:
            return

        pos_input1, pos_input2, pos_output = code[ip+1:ip+4]

        if code[ip] == OP_ADD:
            code[pos_output] = code[pos_input1] + code[pos_input2]
        elif code[ip] == OP_MUL:
            code[pos_output] = code[pos_input1] * code[pos_input2]

        ip += 4


def part1():
    data = [x.strip() for x in open('input').readlines()]
    code = [int(x) for x in data[0].split(',')]
    code[1] = 12
    code[2] = 2

    run(code)
    return code[0]


def part2():
    data = [x.strip() for x in open('input').readlines()]
    initial_mem = [int(x) for x in data[0].split(',')]

    for noun, verb in [(x, y) for x in range(0, 100) for y in range(0, 100)]:
        code = initial_mem.copy()
        code[1] = noun
        code[2] = verb

        run(code)
        if code[0] == 19690720:
            return 100 * noun + verb


print(part2())
