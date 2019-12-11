import math


def main():
    reader = open('input.txt', 'r')
    input_list = list(map(list, reader.read().split('\n')))
    # input = reader.readlines()
    asteroids = []

    for y in range(len(input_list)):
        for x in range(len(input_list[0])):
            if input_list[y][x] == '#':
                asteroids.append((x, y))

    max_asteroids = {'asteroid': (0, 0), 'number_of_asteroids_visible': 0}

    for asteroid1 in asteroids:
        angles = []
        for asteroid2 in asteroids:
            if asteroid1 == asteroid2:
                continue

            angle = math.atan2(asteroid2[1] - asteroid1[1], asteroid2[0] - asteroid1[0])
            if angle not in angles:
                angles.append(angle)

        if len(angles) > max_asteroids['number_of_asteroids_visible']:
            max_asteroids = {'asteroid': asteroid1, 'number_of_asteroids_visible': len(angles)}

    print(max_asteroids)


if __name__ == '__main__':
    main()