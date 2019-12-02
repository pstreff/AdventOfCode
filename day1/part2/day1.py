
def main():
    reader = open('input.txt', 'r')
    input = reader.readlines()

    sum = 0

    for weight in input:
        sum = sum + fuel_calculation(int((int(weight) / 3)) - 2)

    print(sum)


def fuel_calculation(weight):
    if int((int(weight) / 3)) - 2 > 0:
        return weight + fuel_calculation(int((int(weight) / 3)) - 2)
    else:
        return weight


if __name__ == '__main__':
    main()
