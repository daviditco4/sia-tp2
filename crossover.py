import random

from Character import Character


def one_point_crossover(parent1, parent2):
    point = random.randint(2, Character.attribute_amount + 2 - 1)
    parent1_list = parent1.to_list()
    parent2_list = parent2.to_list()
    child1_list = []
    child2_list = []

    for i in range(Character.attribute_amount + 2):
        child1_list.append(parent1_list[i] if i < point else parent2_list[i])
        child2_list.append(parent2_list[i] if i < point else parent1_list[i])

    return Character.from_list(child1_list), Character.from_list(child2_list)


def two_point_crossover(parent1, parent2):
    point1, point2 = sorted(random.sample(range(2, Character.attribute_amount + 2), 2))
    parent1_list = parent1.to_list()
    parent2_list = parent2.to_list()
    child1_list = []
    child2_list = []

    for i in range(Character.attribute_amount + 2):
        child1_list.append(
            parent1_list[i] if i < point1 else parent2_list[i] if point1 <= i < point2 else parent1_list[i])
        child2_list.append(
            parent2_list[i] if i < point1 else parent1_list[i] if point1 <= i < point2 else parent2_list[i])

    return Character.from_list(child1_list), Character.from_list(child2_list)


def uniform_crossover(parent1, parent2):
    parent1_list = parent1.to_list()
    parent2_list = parent2.to_list()
    child1_list = []
    child2_list = []

    for i in range(Character.attribute_amount + 2):
        value = random.random()
        child1_list.append(parent1_list[i] if value >= 0.5 else parent2_list[i])
        child2_list.append(parent2_list[i] if value >= 0.5 else parent1_list[i])

    return Character.from_list(child1_list), Character.from_list(child2_list)
