
def main():
    global user_input
    user_input = 1

    reader = open('input.txt', 'r')
    input_list = list(map(int, reader.read().split(',')))
    pointer = 0

    while True:
        opcode, m1, m2, m3 = get_op_code_and_modes(input_list, pointer)

        if opcode == 1:
            op_code_1(input_list, pointer, m1, m2, m3)
            pointer += 4
        elif opcode == 2:
            op_code_2(input_list, pointer, m1, m2, m3)
            pointer += 4
        elif opcode == 3:
            op_code_3(input_list, pointer)
            pointer += 2
        elif opcode == 4:
            op_code_4(input_list, pointer, m1)
            pointer += 2
        elif opcode == 99:
            print('Opcode 99 halting!')
            exit(99)


def get_op_code_and_modes(input_list, pointer):
    instruction = str(input_list[pointer])
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


def op_code_1(input_list, pointer, m1, m2, m3):
    if m1 == 0:
        input1 = input_list[input_list[pointer+1]]
    elif m1 == 1:
        input1 = input_list[pointer+1]

    if m2 == 0:
        input2 = input_list[input_list[pointer+2]]
    elif m2 == 1:
        input2 = input_list[pointer+2]

    if m3 == 0:
        output_position = input_list[pointer + 3]
    elif m3 == 1:
        print('This should not happen apparently!!!')
        exit(123)

    output = input1 + input2
    input_list[output_position] = output


def op_code_2(input_list, pointer, m1, m2, m3):
    if m1 == 0:
        input1 = input_list[input_list[pointer + 1]]
    elif m1 == 1:
        input1 = input_list[pointer + 1]

    if m2 == 0:
        input2 = input_list[input_list[pointer + 2]]
    elif m2 == 1:
        input2 = input_list[pointer + 2]

    if m3 == 0:
        output_position = input_list[pointer + 3]
    elif m3 == 1:
        print('This should not happen apparently!!!')
        exit(234)

    output = input1 * input2
    input_list[output_position] = output


def op_code_3(input_list, pointer):
    input_list[input_list[pointer+1]] = user_input


def op_code_4(input_list, pointer, m1):
    if m1 == 0:
        output = input_list[input_list[pointer+1]]
    elif m1 == 1:
        output = input_list[pointer+1]

    print(output)


if __name__ == '__main__':
    main()
