from Computer import Computer


def turn_robot(facing, direction):
    if facing == 'up':
        if direction == 0:
            return 'left'
        else:
            return 'right'
    if facing == 'right':
        if direction == 0:
            return 'up'
        else:
            return 'down'
    if facing == 'down':
        if direction == 0:
            return 'right'
        else:
            return 'left'
    if facing == 'left':
        if direction == 0:
            return 'down'
        else:
            return 'up'


def move_robot(position, facing):
    if facing == 'up':
        return (position[0], position[1] + 1)
    if facing == 'right':
        return (position[0] + 1, position[1])
    if facing == 'down':
        return (position[0], position[1] - 1)
    if facing == 'left':
        return (position[0] - 1, position[1])


# 0 = black, 1 = white
position = (0, 0)
visited_colors = {}
facing = 'up'
visited = 0
comp = Computer()
while not comp.finished:
    if position in visited_colors.keys():
        color = visited_colors[position]
    else:
        color = 0

    comp.set_input(color)
    comp.run()

    if position not in visited_colors:
        visited += 1

    visited_colors[position] = comp.output

    comp.un_halt()
    comp.run()

    # turn robpt
    facing = turn_robot(facing, comp.output)
    # move robot
    position = move_robot(position, facing)

    comp.un_halt()

print(visited_colors)
print(visited)
