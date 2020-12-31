#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Computer:
    def __init__(self, code, stdin, stdout):
        self.code = code
        self.stdin = stdin
        self.stdout = stdout
        self.ip = 0

        self.basic = {
            1: self.add,
            2: self.mul,
            3: self.inp,
            4: self.out,
            99: self.hlt,
        }

        self.advanced = self.basic.copy()
        self.advanced.update({
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equal,
        })

    def run_code(self, advanced=False):
        while self.ip < len(self.code):
            halt = self.run_instruction(advanced)
            if halt:
                return

    def run_instruction(self, advanced):
        opcode, mode = self.get_opcode_and_mode()
        if advanced:
            self.advanced[opcode](mode)
        else:
            self.basic[opcode](mode)

        if opcode == 99:
            return True
        else:
            return False

    def get_opcode_and_mode(self):
        instruction = str(self.code[self.ip])
        opcode = int(instruction[-2:])
        mode = instruction[-3::-1].ljust(3, '0')
        return opcode, mode

    def add(self, mode):
        oprand0 = self.get_oprand(self.ip + 1, mode[0])
        oprand1 = self.get_oprand(self.ip + 2, mode[1])
        oprand2 = self.code[self.ip+3]
        self.code[oprand2] = oprand0 + oprand1
        self.ip += 4

    def mul(self, mode):
        oprand0 = self.get_oprand(self.ip + 1, mode[0])
        oprand1 = self.get_oprand(self.ip + 2, mode[1])
        oprand2 = self.code[self.ip+3]
        self.code[oprand2] = oprand0 * oprand1
        self.ip += 4

    def inp(self, mode):
        oprand0 = self.code[self.ip+1]
        self.code[oprand0] = self.stdin.pop()
        self.ip += 2

    def out(self, mode):
        oprand0 = self.get_oprand(self.ip + 1, mode[0])
        self.stdout.append(oprand0)
        self.ip += 2

    def jump_if_true(self, mode):
        oprand0 = self.get_oprand(self.ip + 1, mode[0])
        oprand1 = self.get_oprand(self.ip + 2, mode[1])
        if oprand0 != 0:
            self.ip = oprand1
        else:
            self.ip += 3

    def jump_if_false(self, mode):
        oprand0 = self.get_oprand(self.ip + 1, mode[0])
        oprand1 = self.get_oprand(self.ip + 2, mode[1])
        if oprand0 == 0:
            self.ip = oprand1
        else:
            self.ip += 3

    def less_than(self, mode):
        oprand0 = self.get_oprand(self.ip + 1, mode[0])
        oprand1 = self.get_oprand(self.ip + 2, mode[1])
        oprand2 = self.code[self.ip+3]
        self.code[oprand2] = 1 if oprand0 < oprand1 else 0
        self.ip += 4

    def equal(self, mode):
        oprand0 = self.get_oprand(self.ip + 1, mode[0])
        oprand1 = self.get_oprand(self.ip + 2, mode[1])
        oprand2 = self.code[self.ip+3]
        self.code[oprand2] = 1 if oprand0 == oprand1 else 0
        self.ip += 4

    def hlt(self, mode):
        self.ip += 2

    def get_oprand(self, pos, mode):
        if mode == '0':
            return self.code[self.code[pos]]
        return self.code[pos]


def part1():
    data = [x.strip() for x in open('input').readlines()]
    code = [int(x) for x in data[0].split(',')]

    stdout = []
    computer = Computer(code, [1], stdout)
    computer.run_code(False)

    return stdout[-1]


def part2():
    data = [x.strip() for x in open('input').readlines()]
    code = [int(x) for x in data[0].split(',')]

    stdout = []
    computer = Computer(code, [5], stdout)
    computer.run_code(True)

    return stdout[-1]


print('part1:', part1())
print('part2:', part2())
