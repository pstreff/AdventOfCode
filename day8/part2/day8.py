from PIL import Image


def main():
    wide = 25
    tall = 6
    reader = open('input.txt', 'r')
    input_list = list(map(int, reader.read()))

    # tall = 2
    # wide = 2
    # input_list = [0, 2, 2, 2, 1, 1, 2, 2, 2, 2, 1, 2, 0, 0, 0, 0]

    layers = {}
    i = 0
    n = wide * tall

    while input_list:
        layers[i] = input_list[:n]
        del input_list[:n]
        i += 1

    image_data = []

    for pixel in range(wide*tall):
        for layer in layers.values():
            if layer[pixel] == 2:
                continue
            elif layer[pixel] == 0 or layer[pixel] == 1:
                image_data.append(layer[pixel])
                break
            else:
                image_data.append(0)
                break

    img = Image.new('1', (wide, tall), 1)
    img.putdata(image_data)
    img = img.resize((wide*25, tall*25))
    img.show()

    exit(1)


if __name__ == '__main__':
    main()
