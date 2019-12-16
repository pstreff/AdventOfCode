from Computer import Computer


block_tiles = 0
output = []
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

    if output[2] == 2:
        block_tiles += 1
    output.clear()

print(block_tiles)
