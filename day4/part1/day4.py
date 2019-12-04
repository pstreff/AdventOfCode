
def main():
    lower_boundary = 236491
    upper_boundary = 713787
    number_of_passwords = 0
    for number in range(lower_boundary, upper_boundary + 1):
        if is_valid_number(str(number)):
            number_of_passwords += 1
            print('Valid Password: ' + str(number))

    print()
    print('Number of passwords: ' + str(number_of_passwords))


def is_valid_number(number: str):
    valid = True
    same = 1
    pairs = []
    for index, digit in enumerate(number[:-1]):
        if number[index] > number[index+1]:
            valid = False
            break
        if number[index] == number[index+1]:
            same += 1
        else:
            pairs.append(same)
            same = 1
    pairs.append(same)

    if not any(value >= 2 for value in pairs):
        valid = False

    return valid


if __name__ == '__main__':
    main()
