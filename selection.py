import math
import random


def roulette_selection(population, evaluation_fun, num_parents):
    fitness = [evaluation_fun(*i.to_list()) for i in population]
    total_fitness = sum(fitness)
    parents = []

    for _ in range(num_parents):
        pick = random.uniform(0, total_fitness)
        current = 0
        picked = False

        for individual, fit in zip(population, fitness):
            current += fit
            if current > pick:
                picked = True
                parents.append(individual)
                break

        if not picked:
            parents.append(population[-1])

    return parents


def elite_selection(population, evaluation_fun, num_parents):
    elite_indices = sorted(range(len(population)), key=lambda i: evaluation_fun(*population[i].to_list()),
                           reverse=True)[:num_parents]
    parents = []

    for j, elite_index in enumerate(elite_indices):
        n = math.ceil((num_parents - j) / len(population))
        if len(parents) + n > num_parents:
            n = num_parents - len(parents)

        parents.extend([population[elite_index]] * n)
        # print('Adding: ' + str(n))

        if len(parents) == num_parents:
            break

    return parents
