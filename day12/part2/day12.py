from Planet import Planet
from math import gcd
from functools import reduce


def check_if_initial(planet: Planet, initial, axis):
    return planet.position[axis] == initial[axis] and planet.velocity[axis] == 0


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    # < x = -9, y = 10, z = -1 >
    # < x = -14, y = -8, z = 14 >
    # < x = 1, y = 5, z = 6 >
    # < x = -19, y = 7, z = 8 >
    io_initial = [-9, 10, -1]
    europa_initial = [-14, -8, 14]
    ganymede_initial = [1, 5, 6]
    callisto_initial = [-19, 7, 8]

    io = Planet(pos_x=io_initial[0], pos_y=io_initial[1], pos_z=io_initial[2])
    europa = Planet(pos_x=europa_initial[0], pos_y=europa_initial[1], pos_z=europa_initial[2])
    ganymede = Planet(pos_x=ganymede_initial[0], pos_y=ganymede_initial[1], pos_z=ganymede_initial[2])
    callisto = Planet(pos_x=callisto_initial[0], pos_y=callisto_initial[1], pos_z=callisto_initial[2])

    planets = [io, europa, ganymede, callisto]
    x_steps = y_steps = z_steps = None
    i = 0
    while True:
        if (i != 0 and x_steps is None
                and check_if_initial(ganymede, ganymede_initial, 0)
                and check_if_initial(europa, europa_initial, 0)
                and check_if_initial(io, io_initial, 0)
                and check_if_initial(callisto, callisto_initial, 0)
        ):
            x_steps = i

        if (i != 0 and y_steps is None
                and check_if_initial(ganymede, ganymede_initial, 1)
                and check_if_initial(europa, europa_initial, 1)
                and check_if_initial(io, io_initial, 1)
                and check_if_initial(callisto, callisto_initial, 1)
        ):
            y_steps = i

        if (i != 0 and z_steps is None
                and check_if_initial(ganymede, ganymede_initial, 2)
                and check_if_initial(europa, europa_initial, 2)
                and check_if_initial(io, io_initial, 2)
                and check_if_initial(callisto, callisto_initial, 2)
        ):
            z_steps = i

        for base_planet in planets:
            for planet in planets:
                if planet == base_planet:
                    continue
                base_planet.add_gravity_for_planet(planet)

        for planet in planets:
            planet.apply_velocity_to_position()

        if x_steps and y_steps and z_steps:
            print(x_steps, y_steps, z_steps)
            print(reduce(lcm, [x_steps, y_steps, z_steps]))
            exit(1)

        i += 1


if __name__ == '__main__':
    main()
