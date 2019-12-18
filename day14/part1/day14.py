from collections import defaultdict
from math import ceil


def calculate_ores(name, target_amount):
    reaction = dictionary[name]
    smallest_amount = reaction['amount']

    # check if material is in storage?
    if storage[name] >= target_amount:
        storage[name] -= target_amount
        return
    else:
        target_amount -= storage[name]
        storage[name] = 0

    repetitions = ceil(target_amount / smallest_amount)
    repetition_produces_amount = repetitions * smallest_amount

    wasted = repetition_produces_amount - target_amount
    storage[name] += wasted

    for needed, amount_needed in reaction['needed'].items():
        amount_needed = amount_needed * repetitions

        if needed == 'ORE':
            ore['ORE'] += amount_needed
        else:
            calculate_ores(needed, amount_needed)


reader = open('input.txt', 'r')
data = reader.read().split('\n')
reader.close()

dictionary = {}

for eq in data:
    needed, product = eq.split(' => ')
    product_amount, product_name = product.split(' ')
    needed_dict = {}
    for need in needed.split(', '):
        need_amount, need_name = need.split(' ')
        needed_dict[need_name] = int(need_amount)

    dictionary[product_name] = {'amount': int(product_amount), 'needed': needed_dict}

storage = defaultdict(int)
ore = defaultdict(int)

calculate_ores('FUEL', 1)
print(ore['ORE'])
