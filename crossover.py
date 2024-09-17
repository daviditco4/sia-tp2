import random

from Character import Character


def one_point_crossover(parents, total_points_available):
    offspring = []

    for i in range(0, len(parents), 2):
        point = random.randint(2, Character.attribute_amount + 1)
        parent1_list = parents[i].to_list()
        parent2_list = parents[i + 1].to_list()
        child1_list = []
        child2_list = []
        counter = 0

        while not Character.is_valid_from_list(child1_list, total_points_available) or not Character.is_valid_from_list(
                child2_list, total_points_available):
            child1_list.clear()
            child2_list.clear()
            if counter >= 10:
                break
            counter += 1
            for j in range(Character.attribute_amount + 2):
                child1_list.append(parent1_list[j] if i < point else parent2_list[j])
                child2_list.append(parent2_list[j] if i < point else parent1_list[j])

        if child1_list and child2_list:
            offspring.extend([Character.from_list(child1_list), Character.from_list(child2_list)])
        else:
            # print('Crossover failed')
            offspring.extend([Character.from_list(parent1_list), Character.from_list(parent1_list)])

    return offspring


def two_point_crossover(parents, total_points_available):
    offspring = []

    for i in range(0, len(parents), 2):
        point1, point2 = sorted(random.sample(range(2, Character.attribute_amount + 1), 2))
        parent1_list = parents[i].to_list()
        parent2_list = parents[i + 1].to_list()
        child1_list = []
        child2_list = []
        counter = 0

        while not Character.is_valid_from_list(child1_list, total_points_available) or not Character.is_valid_from_list(
                child2_list, total_points_available):
            child1_list.clear()
            child2_list.clear()
            if counter >= 10:
                break
            counter += 1
            for j in range(Character.attribute_amount + 2):
                child1_list.append(
                    parent1_list[j] if j < point1 else parent2_list[j] if point1 <= j < point2 else parent1_list[j])
                child2_list.append(
                    parent2_list[j] if j < point1 else parent1_list[j] if point1 <= j < point2 else parent2_list[j])

        if child1_list and child2_list:
            offspring.extend([Character.from_list(child1_list), Character.from_list(child2_list)])
        else:
            # print('Crossover failed')
            offspring.extend([Character.from_list(parent1_list), Character.from_list(parent1_list)])

    return offspring


def uniform_crossover(parents, total_points_available):
    offspring = []

    for i in range(0, len(parents), 2):
        parent1_list = parents[i].to_list()
        # print('PARENT2: ' + str(i + 1))
        parent2_list = parents[i + 1].to_list()
        child1_list = []
        child2_list = []
        counter = 0

        while not Character.is_valid_from_list(child1_list, total_points_available) or not Character.is_valid_from_list(
                child2_list, total_points_available):
            child1_list.clear()
            child2_list.clear()
            if counter >= 10:
                break
            counter += 1
            for j in range(Character.attribute_amount + 2):
                value = random.random()
                child1_list.append(parent1_list[j] if value >= 0.5 else parent2_list[j])
                child2_list.append(parent2_list[j] if value >= 0.5 else parent1_list[j])

        if child1_list and child2_list:
            offspring.extend([Character.from_list(child1_list), Character.from_list(child2_list)])
        else:
            # print('Crossover failed')
            offspring.extend([Character.from_list(parent1_list), Character.from_list(parent1_list)])

    return offspring


def circular_crossover(parents, total_points_available):
    offspring = []

    for i in range(0, len(parents), 2):
        point = random.randint(1, Character.attribute_amount + 1)
        size = random.randint(1, Character.attribute_amount + 1)
        parent1_list = parents[i].to_list()
        parent2_list = parents[i + 1].to_list()
        child1_list = []
        child2_list = []
        counter = 0

        while not Character.is_valid_from_list(child1_list, total_points_available) or not Character.is_valid_from_list(
                child2_list, total_points_available):
            child1_list.clear()
            child2_list.clear()
            if counter >= 10:
                break
            counter += 1
            for j in range(Character.attribute_amount + 2):
                child1_list.append(
                    parent2_list[j] if point <= j < point + size or (
                            point > j and j < point + size - Character.attribute_amount + 2) else parent1_list[j])
                child2_list.append(
                    parent1_list[j] if point <= j < point + size or (
                            point > j and j < point + size - Character.attribute_amount + 2) else parent2_list[j])

        if child1_list and child2_list:
            offspring.extend([Character.from_list(child1_list), Character.from_list(child2_list)])
        else:
            # print('Crossover failed')
            offspring.extend([Character.from_list(parent1_list), Character.from_list(parent1_list)])

    return offspring
