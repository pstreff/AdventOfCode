class Computer:
    def __init__(self, phase):
        self.phase = phase
        self.halted = False
        self.finished = False
        self.input_list = []
        self.input_list = self.get_input_list()
        self.pointer = 0
        self.program_inputs = []
        self.program_inputs.append(phase)
        self.output = 0
        self.relative_base = 0

    def get_input_list(self):
        additional_memory = [0] * 1000000
        return list(map(int, open('input.txt', 'r').read().split(','))) + additional_memory

    def run(self):
        while not (self.finished or self.halted):
            self.run_int_code_program()

    def set_thrust_input(self, thrust_input):
        self.program_inputs.append(thrust_input)
        self.un_halt()

    def un_halt(self):
        self.halted = False

    def run_int_code_program(self):
        opcode, m1, m2, m3 = self.get_op_code_and_modes()
        param1, param2, param3 = self.get_params(m1, m2, m3)
        if opcode == 1:  # addition
            self.op_code_1(param1, param2, param3)
            self.pointer += 4
        elif opcode == 2:  # multiplication
            self.op_code_2(param1, param2, param3)
            self.pointer += 4
        elif opcode == 3:  # save
            try:
                program_input = self.program_inputs.pop(0)
            except IndexError:
                program_input = 0
            self.op_code_3(program_input, m1)
            self.pointer += 2
        elif opcode == 4:  # output
            self.output = self.op_code_4(param1)
            self.pointer += 2
            self.halted = True
        elif opcode == 5:  # jump if true
            returned = self.op_code_5(param1, param2)
            self.pointer = returned
        elif opcode == 6:  # jump if false
            returned = self.op_code_6(param1, param2)
            self.pointer = returned
        elif opcode == 7:  # less than
            self.op_code_7(param1, param2, param3)
            self.pointer += 4
        elif opcode == 8:  # equals
            self.op_code_8(param1, param2, param3)
            self.pointer += 4
        elif opcode == 9:  # adjust relative base
            self.op_code_9(param1)
            self.pointer += 2
        elif opcode == 99:  # finished
            self.finished = True

    def get_op_code_and_modes(self):
        instruction = str(self.input_list[self.pointer])
        opcode = int(instruction[-2:])

        try:
            m1 = int(instruction[-3])
        except IndexError:
            m1 = 0

        try:
            m2 = int(instruction[-4])
        except IndexError:
            m2 = 0

        try:
            m3 = int(instruction[-5])
        except IndexError:
            m3 = 0

        return opcode, m1, m2, m3

    def get_params(self, m1, m2, m3):
        try:
            if m1 == 0:
                param1 = self.input_list[self.input_list[self.pointer + 1]]
            elif m1 == 1:
                param1 = self.input_list[self.pointer + 1]
            elif m1 == 2:
                address = self.relative_base + self.input_list[self.pointer + 1]
                param1 = self.input_list[address]
        except IndexError:
            param1 = 0

        try:
            if m2 == 0:
                param2 = self.input_list[self.input_list[self.pointer + 2]]
            elif m2 == 1:
                param2 = self.input_list[self.pointer + 2]
            elif m2 == 2:
                address = self.relative_base + self.input_list[self.pointer + 2]
                param2 = self.input_list[address]
        except IndexError:
            param2 = 0

        try:
            if m3 == 0:
                param3 = self.input_list[self.pointer + 3]
            elif m3 == 1:
                print('This should not happen apparently!!!')
                exit(123)
            elif m3 == 2:
                param3 = self.relative_base + self.input_list[self.pointer + 3]
        except IndexError:
            param3 = 0

        return param1, param2, param3

    # addition
    def op_code_1(self, param1, param2, param3):
        output = param1 + param2
        self.input_list[param3] = output

    # multiply
    def op_code_2(self, param1, param2, param3):
        output = param1 * param2
        self.input_list[param3] = output

    # save
    def op_code_3(self, program_input, m1):
        if m1 == 0:
            param1 = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            param1 = self.input_list[self.pointer + 1]
        elif m1 == 2:
            param1 = self.relative_base + self.input_list[self.pointer + 1]
        self.input_list[param1] = program_input

    # output
    def op_code_4(self, param1):
        return param1

    # jump if true
    def op_code_5(self, param1, param2):
        if param1 != 0:
            return param2
        else:
            return self.pointer + 3

    # jump if false
    def op_code_6(self, param1, param2):
        if param1 == 0:
            return param2
        else:
            return self.pointer + 3

    # less than
    def op_code_7(self, param1, param2, param3):
        if param1 < param2:
            self.input_list[param3] = 1
        else:
            self.input_list[param3] = 0

    # equals
    def op_code_8(self, param1, param2, param3):
        if param1 == param2:
            self.input_list[param3] = 1
        else:
            self.input_list[param3] = 0

    # adjust relative base
    def op_code_9(self, param1):
        self.relative_base += param1
