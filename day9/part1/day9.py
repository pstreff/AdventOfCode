from Computer import Computer

comp = Computer(1)
while not comp.finished:
    comp.un_halt()
    comp.run()

print(comp.output)
