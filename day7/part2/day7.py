from itertools import permutations
from Computer import Computer


loops = []
phase_settings = list(permutations(range(5, 10)))

for phase_setting in phase_settings:
    compA = Computer(phase_setting[0])
    compA.set_thrust_input(0)
    compA.run()
    compB = Computer(phase_setting[1])
    compB.set_thrust_input(compA.output)
    compB.run()
    compC = Computer(phase_setting[2])
    compC.set_thrust_input(compB.output)
    compC.run()
    compD = Computer(phase_setting[3])
    compD.set_thrust_input(compC.output)
    compD.run()
    compE = Computer(phase_setting[4])
    compE.set_thrust_input(compD.output)
    compE.run()

    while not compE.finished:
        compA.set_thrust_input(compE.output)
        compA.run()

        compB.set_thrust_input(compA.output)
        compB.run()

        compC.set_thrust_input(compB.output)
        compC.run()

        compD.set_thrust_input(compC.output)
        compD.run()

        compE.set_thrust_input(compD.output)
        compE.run()

    loops.append(compE.output)

print(loops)
print(max(loops))
