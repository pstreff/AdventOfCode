from Computer import Computer

comp = Computer(2)
while not comp.finished:
    comp.un_halt()
    comp.run()

print(comp.output)
