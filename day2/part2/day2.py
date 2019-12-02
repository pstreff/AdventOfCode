
def main():
    reader = open('input.txt', 'r')
    input_list = list(map(int, reader.read().split(',')))
    pointer = 0

    restore_1202_program_alarm_state(input_list)

    print(input_list)

    while input_list[pointer] != 99:
        opcode, first_input, output_position, second_input = get_instructions(input_list, pointer)

        if opcode == 1:
            output = first_input + second_input
        elif opcode == 2:
            output = first_input * second_input
        elif opcode == 3:
            print('Opcode 3 halting!')
            exit(3)
        elif opcode == 99:
            print('Opcode 99 halting!')
            print(input_list)
            exit(99)

        input_list[output_position] = output
        pointer += 4

    print(input_list)
    print(input_list[0])


def get_instructions(input_list, pointer):
    opcode = input_list[pointer]
    output_position = input_list[pointer + 3]
    first_input = input_list[input_list[pointer + 1]]
    second_input = input_list[input_list[pointer + 2]]
    return opcode, first_input, output_position, second_input


def restore_1202_program_alarm_state(input_list):
    input_list[1] = 12
    input_list[2] = 2


if __name__ == '__main__':
    main()
