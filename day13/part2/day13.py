from Computer import Computer


block_tiles = 0
score = 0
paddle_pos = (0, 0)
ball_pos = (0, 0)
output = []
cycle = 0
comp = Computer()
while not comp.finished:
    comp.run()
    output.append(comp.output)
    comp.un_halt()
    comp.run()
    output.append(comp.output)
    comp.un_halt()
    comp.run()
    output.append(comp.output)
    comp.un_halt()

    if comp.needsInputs:
        if ball_pos[0] > paddle_pos[0]:
            comp.set_input(1)
        elif ball_pos[0] < paddle_pos[0]:
            comp.set_input(-1)
        else:
            comp.set_input(0)

    if output[0] == -1 and output[1] == 0:
        score = output[2]

    if output[2] == 4:
        ball_pos = (output[0], output[1])

    if output[2] == 3:
        paddle_pos = (output[0], output[1])

    output.clear()

    cycle += 1

print('cycles ', cycle)

print('Score: ', score)
