
def main():
    reader = open('input.txt', 'r')
    input = reader.readlines()

    sum = 0

    for module in input:
        sum = sum + (int((int(module) / 3)) - 2)

    print(sum)

if __name__ == '__main__':
    main()