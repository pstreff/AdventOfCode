
def main():
    wide = 25
    tall = 6
    reader = open('input.txt', 'r')
    input_list = list(map(int, reader.read()))

    # tall = 3
    # wide = 2
    # input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]

    layers = {}
    i = 0
    n = wide * tall

    while input_list:
        layers[i] = input_list[:n]
        del input_list[:n]
        i += 1

    layer_number_digits = {}
    i = 0
    for layer in layers.values():
        zeros = 0
        ones = 0
        twos = 0
        for digit in layer:
            if digit == 0:
                zeros += 1
            elif digit == 1:
                ones += 1
            else:
                twos += 1
        layer_number_digits[i] = {0: zeros, 1: ones, 2: twos}
        i +=1

    layer_fewest_zeros = min(layer_number_digits, key=lambda k: int(layer_number_digits[k][0]))
    solution = layer_number_digits[layer_fewest_zeros][1] * layer_number_digits[layer_fewest_zeros][2]

    print(solution)


if __name__ == '__main__':
    main()
