import random

from Character import Character


def mutate_gen(offspring, mutation_rate, unassigned_points_available, total_points_available):
    mutants = []

    for individual in offspring:
        if random.random() < mutation_rate:
            index = random.randint(1, Character.attribute_amount + 2 - 1)
            delta = 0

            while delta == 0 or delta > unassigned_points_available:
                rand = random.random()
                delta = random.choice([-1, 1]) * int(((total_points_available / Character.attribute_amount) / 2) * (rand ** 2))

            individual_list = individual.to_list()
            individual_list[index] = max(0, individual_list[index] + delta)
            mutants.append(Character.from_list(individual_list))
        mutants.append(individual)

    return mutants


def mutate_multigen(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = random.choice(range(len(individual)))
    return individual
