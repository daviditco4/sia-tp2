import math
import random


def roulette_selection(population, fitness, num_parents):
    total_fitness = sum(fitness)
    parents = []

    for _ in num_parents:
        pick = random.uniform(0, total_fitness)
        current = 0
        picked = False

        for individual, fit in zip(population, fitness):
            current += fit
            if current > pick:
                picked = True
                parents.append(individual)

        if not picked:
            parents.append(population[-1])

    return parents


def elite_selection(population, fitness, num_parents):
    elite_indices = sorted(range(len(fitness)), key=lambda i: fitness[i], reverse=True)
    parents = []

    for j, elite_index in enumerate(elite_indices):
        n = math.ceil((num_parents - j) / len(population))
        # if len(parents) + n > num_parents:
        #     n = num_parents - len(parents)

        parents.extend([population[elite_index]] * n)

        # if len(parents) == num_parents:
        #     break

    return parents
