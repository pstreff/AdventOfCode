
def main():
    points_visited = {}

    reader = open('wire1.txt', 'r')
    wire1_path = list(reader.read().split(','))
    reader.close()
    reader = open('wire2.txt', 'r')
    wire2_path = list(reader.read().split(','))
    reader.close()

    # wire1_path = ['R75', 'D30', 'R83', 'U83', 'L12', 'D49', 'R71', 'U7', 'L72']
    # wire2_path = ['U62', 'R66', 'U55', 'R34', 'D71', 'R55', 'D58', 'R83']

    x = y = 0
    for instr in wire1_path:
        dx = 0
        dy = 0
        direction = instr[0]
        distance = int(instr[1:])
        if direction == 'U':
            dy += 1
            dx += 0
        elif direction == 'D':
            dy -= 1
            dx += 0
        elif direction == 'R':
            dy += 0
            dx += 1
        elif direction == 'L':
            dy += 0
            dx -= 1
        for _ in range(distance):
            x += dx
            y += dy

            points_visited[(x, y)] = 1

    x = y = 0
    for instr in wire2_path:
        dx = 0
        dy = 0
        direction = instr[0]
        distance = int(instr[1:])
        if direction == 'U':
            dy += 1
            dx += 0
        elif direction == 'D':
            dy -= 1
            dx += 0
        elif direction == 'R':
            dy += 0
            dx += 1
        elif direction == 'L':
            dy += 0
            dx -= 1
        for _ in range(distance):
            x += dx
            y += dy
            if (x, y) in points_visited and points_visited[(x, y)] == 1:
                points_visited[(x, y)] = 3
            else:
                points_visited[(x, y)] = 2

    distances = []
    for (x, y) in points_visited:
        if points_visited.get((x, y)) == 3:
            distance = abs(0 - x) + abs(0 - y)
            distances.append(distance)

    distances.sort()
    print(distances[0])


if __name__ == '__main__':
    main()
