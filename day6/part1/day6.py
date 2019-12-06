class Node:
    def __init__(self, name):
        self.name = name
        self.parent = []
        self.children = []
        if name == 'COM':
            self.direct = 0
        else:
            self.direct = 1
        self.indirect = 0

    def add_parent(self, parent):
        self.parent.append(parent)

    def add_child(self, child):
        self.children.append(child)

    def parent(self):
        return self.parent

    def children(self):
        return self.children

    def calculate_indirect(self, orbit_map):
        try:
            parent_node = orbit_map[self.parent[0]]
            self.indirect = parent_node.direct + parent_node.calculate_indirect(orbit_map)
            return self.indirect
        except IndexError:
            self.indirect = 0
            return self.indirect

    def __str__(self):
        return 'Instance: ' + self.name + '\n' \
               + 'Parent: ' + str(self.parent) + '\n' \
               + 'Children: ' + str(self.children) + '\n' \
               + 'Direct: ' + str(self.direct) + '\n' \
               + 'Indirect: ' + str(self.indirect) + '\n'


def main():
    reader = open('input.txt', 'r')
    input_list = list(reader.read().split('\n'))
    #
    #
    # input_list = [
    #     'COM)B',
    #     'B)C',
    #     'C)D',
    #     'D)E',
    #     'E)F',
    #     'B)G',
    #     'G)H',
    #     'D)I',
    #     'E)J',
    #     'J)K',
    #     'K)L',
    # ]
    # print(input_list)

    orbit_map = {}

    for relation in input_list:
        tmp = relation.split(')')
        a = tmp[0]
        b = tmp[1]
        if a not in orbit_map.keys():
            node = Node(a)
            node.add_child(b)
            orbit_map[a] = node
        else:
            node = orbit_map[a]
            node.add_child(b)

        if b not in orbit_map.keys():
            node2 = Node(b)
            node2.add_parent(a)
            orbit_map[b] = node2
        else:
            node2 = orbit_map[b]
            node2.add_parent(a)

    total = 0
    for node in orbit_map.values():
        node.calculate_indirect(orbit_map)
        total += node.direct + node.indirect

    print()
    print(total)


if __name__ == '__main__':
    main()


