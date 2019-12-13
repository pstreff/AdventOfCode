from Computer import Computer
from PIL import Image


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
position = (100, 100)
visited_colors = {}
facing = 'up'
visited = 0

img = Image.new('1', (200, 200), 0)
pixels = img.load()
pixels[100, 100] = 1

comp = Computer()
comp.set_input(1)
while not comp.finished:
    comp.run()

    if position not in visited_colors:
        visited += 1

    visited_colors[position] = comp.output
    pixels[position[0], position[1]] = comp.output

    comp.un_halt()
    comp.run()

    # turn robpt
    facing = turn_robot(facing, comp.output)
    # move robot
    position = move_robot(position, facing)

    if position in visited_colors.keys():
        color = visited_colors[position]
    else:
        color = 0

    comp.set_input(color)
    comp.un_halt()


img = img.resize((200*25, 200*25))
img = img.transpose(Image.FLIP_TOP_BOTTOM)
img.show()

print(visited_colors)
print(visited)
