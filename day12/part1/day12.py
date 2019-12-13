from Planet import Planet


def main():
    # < x = -9, y = 10, z = -1 >
    # < x = -14, y = -8, z = 14 >
    # < x = 1, y = 5, z = 6 >
    # < x = -19, y = 7, z = 8 >
    io = Planet(pos_x=-9, pos_y=10, pos_z=-1)
    europa = Planet(pos_x=-14, pos_y=-8, pos_z=14)
    ganymede = Planet(pos_x=1, pos_y=5, pos_z=6)
    callisto = Planet(pos_x=-19, pos_y=7, pos_z=8)

    # < x = -1, y = 0, z = 2 >
    # < x = 2, y = -10, z = -7 >
    # < x = 4, y = -8, z = 8 >
    # < x = 3, y = 5, z = -1 >
    # io = Planet(pos_x=-1, pos_y=0, pos_z=2)
    # europa = Planet(pos_x=2, pos_y=-10, pos_z=-7)
    # ganymede = Planet(pos_x=4, pos_y=-8, pos_z=8)
    # callisto = Planet(pos_x=3, pos_y=5, pos_z=-1)

    # < x = -8, y = -10, z = 0 >
    # < x = 5, y = 5, z = 10 >
    # < x = 2, y = -7, z = 3 >
    # < x = 9, y = -8, z = -3 >
    # io = Planet(pos_x=-8, pos_y=-10, pos_z=0)
    # europa = Planet(pos_x=5, pos_y=5, pos_z=10)
    # ganymede = Planet(pos_x=2, pos_y=-7, pos_z=3)
    # callisto = Planet(pos_x=9, pos_y=-8, pos_z=-3)

    planets = [io, europa, ganymede, callisto]

    for i in range(1000):
        print()
        print('Step ', i)
        for base_planet in planets:
            print('pos=', base_planet.position, ' vel=', base_planet.velocity)
            for planet in planets:
                if planet == base_planet:
                    continue
                base_planet.add_gravity_for_planet(planet)

        for planet in planets:
            planet.apply_velocity_to_position()

    total_energy = 0
    for planet in planets:
        total_energy += planet.calculate_total_energy()

    print(total_energy)
    exit(1)


if __name__ == '__main__':
    main()
