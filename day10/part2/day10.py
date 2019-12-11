import math


def main():
    reader = open('input.txt', 'r')
    input_list = list(map(list, reader.read().split('\n')))
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

    shifted_asteroids = []
    base_asteroid = max_asteroids['asteroid']

    for asteroid in asteroids:
        if asteroid == base_asteroid:
            continue
        shifted_asteroids.append((asteroid[0] - base_asteroid[0], -(asteroid[1] - base_asteroid[1])))

    information = []
    for asteroid in shifted_asteroids:
        angle = math.degrees(math.pi/2 - math.atan2(asteroid[1], asteroid[0]))
        if angle < 0:
            angle += 360
        distance = math.sqrt(asteroid[0]**2 + asteroid[1]**2)
        information.append({'asteroid': asteroid, 'angle': angle, 'distance': distance})

    sort = sorted(information, key=lambda i: (i['angle'], i['distance']))

    destroyed = []
    while sort:
        previous_angle = None
        rotation_destroy = []
        for asteroid in sort:
            if asteroid['angle'] == previous_angle:
                continue
            previous_angle = asteroid['angle']
            rotation_destroy.append(asteroid)
        for a in rotation_destroy:
            sort.remove(a)
        destroyed += rotation_destroy

    bet_winner = (destroyed[199]['asteroid'][0] + base_asteroid[0], -(destroyed[199]['asteroid'][1]) + base_asteroid[1])

    print('200th asteroid vaporized: ', bet_winner)
    print('Solution: ', bet_winner[0] * 100 + bet_winner[1])


if __name__ == '__main__':
    main()