
class Planet:
    def __init__(self, pos_x, pos_y, pos_z):
        self.velocity = [0, 0, 0]
        self.gravity = [0, 0, 0]
        self.position = [pos_x, pos_y, pos_z]

    def add_gravity_for_planet(self, planet: 'Planet'):
        if self.position[0] < planet.position[0]:
            self.velocity[0] += 1
        elif self.position[0] > planet.position[0]:
            self.velocity[0] -= 1
        else:
            self.velocity[0] += 0  # do nothing basically

        if self.position[1] < planet.position[1]:
            self.velocity[1] += 1
        elif self.position[1] > planet.position[1]:
            self.velocity[1] -= 1
        else:
            self.velocity[1] += 0  # do nothing basically

        if self.position[2] < planet.position[2]:
            self.velocity[2] += 1
        elif self.position[2] > planet.position[2]:
            self.velocity[2] -= 1
        else:
            self.velocity[2] += 0  # do nothing basically

    def apply_velocity_to_position(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]
        self.position[2] += self.velocity[2]

    def calculate_potential_energy(self):
        return abs(self.position[0]) + abs(self.position[1]) + abs(self.position[2])

    def calculate_kinetic_energy(self):
        return abs(self.velocity[0]) + abs(self.velocity[1]) + abs(self.velocity[2])

    def calculate_total_energy(self):
        return self.calculate_potential_energy() * self.calculate_kinetic_energy()