
def main():
    for noun in range(0, 100):
        for verb in range(0, 100):
            input_list, pointer = reset_memory()

            input_list[1] = noun
            input_list[2] = verb

            while input_list[pointer] != 99:
                opcode, first_input, output_position, second_input = get_instructions(input_list, pointer)

                if opcode == 1:
                    output = first_input + second_input
                elif opcode == 2:
                    output = first_input * second_input
                elif opcode == 3:
                    print('Opcode 3 halting!')
                    exit(3)

                input_list[output_position] = output
                pointer += 4

            if input_list[0] == 19690720:
                print(input_list)
                print('Noun: ' + str(input_list[1]))
                print('Verb: ' + str(input_list[2]))
                print('Output :' + str(input_list[0]))
                print('Answer 100+ noun + verb = ' + str((100 * input_list[1]) + input_list[2]))


def get_instructions(input_list, pointer):
    opcode = input_list[pointer]
    output_position = input_list[pointer + 3]
    first_input = input_list[input_list[pointer + 1]]
    second_input = input_list[input_list[pointer + 2]]
    return opcode, first_input, output_position, second_input


def reset_memory():
    reader = open('input.txt', 'r')
    input_list = list(map(int, reader.read().split(',')))
    reader.close()
    pointer = 0
    return input_list, pointer

def restore_1202_program_alarm_state(input_list):
    input_list[1] = 12
    input_list[2] = 2


if __name__ == '__main__':
    main()
