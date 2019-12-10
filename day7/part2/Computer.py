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

    def get_input_list(self):
        return list(map(int, open('input.txt', 'r').read().split(',')))

    def run(self):
        while not (self.finished or self.halted):
            self.run_int_code_program()

    def set_thrust_input(self, thrust_input):
        self.program_inputs.append(thrust_input)
        self.halted = False

    def run_int_code_program(self):
        opcode, m1, m2, m3 = self.get_op_code_and_modes()
        if opcode == 1:
            self.op_code_1(m1, m2, m3)
            self.pointer += 4
        elif opcode == 2:
            self.op_code_2(m1, m2, m3)
            self.pointer += 4
        elif opcode == 3:
            try:
                program_input = self.program_inputs.pop(0)
            except IndexError:
                program_input = 0
            self.op_code_3(program_input)
            self.pointer += 2
        elif opcode == 4:
            self.output = self.op_code_4(m1)
            self.pointer += 2
            self.halted = True
        elif opcode == 5:
            returned = self.op_code_5(m1, m2)
            self.pointer = returned
        elif opcode == 6:
            returned = self.op_code_6(m1, m2)
            self.pointer = returned
        elif opcode == 7:
            self.op_code_7(m1, m2, m3)
            self.pointer += 4
        elif opcode == 8:
            self.op_code_8(m1, m2, m3)
            self.pointer += 4
        elif opcode == 99:
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

    # addition
    def op_code_1(self, m1, m2, m3):
        if m1 == 0:
            input1 = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            input1 = self.input_list[self.pointer + 1]

        if m2 == 0:
            input2 = self.input_list[self.input_list[self.pointer + 2]]
        elif m2 == 1:
            input2 = self.input_list[self.pointer + 2]

        if m3 == 0:
            output_position = self.input_list[self.pointer + 3]
        elif m3 == 1:
            print('This should not happen apparently!!!')
            exit(123)

        output = input1 + input2
        self.input_list[output_position] = output

    # multiply
    def op_code_2(self, m1, m2, m3):
        if m1 == 0:
            input1 = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            input1 = self.input_list[self.pointer + 1]

        if m2 == 0:
            input2 = self.input_list[self.input_list[self.pointer + 2]]
        elif m2 == 1:
            input2 = self.input_list[self.pointer + 2]

        if m3 == 0:
            output_position = self.input_list[self.pointer + 3]
        elif m3 == 1:
            print('This should not happen apparently!!!')
            exit(123)

        output = input1 * input2
        self.input_list[output_position] = output

    # save
    def op_code_3(self, program_input):
        self.input_list[self.input_list[self.pointer + 1]] = program_input

    # output
    def op_code_4(self, m1):
        if m1 == 0:
            output = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            output = self.input_list[self.pointer + 1]

        return output

    # jump if true
    def op_code_5(self, m1, m2):
        if m1 == 0:
            compare = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            compare = self.input_list[self.pointer + 1]

        if compare != 0:
            if m2 == 0:
                return self.input_list[self.input_list[self.pointer + 2]]
            elif m2 == 1:
                return self.input_list[self.pointer + 2]
        else:
            return self.pointer + 3

    # jump if false
    def op_code_6(self, m1, m2):
        if m1 == 0:
            compare = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            compare = self.input_list[self.pointer + 1]

        if compare == 0:
            if m2 == 0:
                return self.input_list[self.input_list[self.pointer + 2]]
            elif m2 == 1:
                return self.input_list[self.pointer + 2]
        else:
            return self.pointer + 3

    # less than
    def op_code_7(self, m1, m2, m3):
        if m1 == 0:
            input1 = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            input1 = self.input_list[self.pointer + 1]

        if m2 == 0:
            input2 = self.input_list[self.input_list[self.pointer + 2]]
        elif m2 == 1:
            input2 = self.input_list[self.pointer + 2]

        if m3 == 0:
            output_position = self.input_list[self.pointer + 3]
        elif m3 == 1:
            print('This should not happen apparently!!!')
            exit(123)

        if input1 < input2:
            self.input_list[output_position] = 1
        else:
            self.input_list[output_position] = 0

    # equals
    def op_code_8(self, m1, m2, m3):
        if m1 == 0:
            input1 = self.input_list[self.input_list[self.pointer + 1]]
        elif m1 == 1:
            input1 = self.input_list[self.pointer + 1]

        if m2 == 0:
            input2 = self.input_list[self.input_list[self.pointer + 2]]
        elif m2 == 1:
            input2 = self.input_list[self.pointer + 2]

        if m3 == 0:
            output_position = self.input_list[self.pointer + 3]
        elif m3 == 1:
            print('This should not happen apparently!!!')
            exit(123)

        if input1 == input2:
            self.input_list[output_position] = 1
        else:
            self.input_list[output_position] = 0
