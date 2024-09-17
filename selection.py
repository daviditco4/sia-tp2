import math
import random


def roulette_selection(population, evaluation_fun, num_individuals):
    fitness = [evaluation_fun(*i.to_list()) for i in population]
    total_fitness = sum(fitness)
    individuals = []

    for _ in range(num_individuals):
        pick = random.uniform(0, total_fitness)
        current = 0
        picked = False

        for individual, fit in zip(population, fitness):
            current += fit
            if current > pick:
                picked = True
                individuals.append(individual)
                break

        if not picked:
            individuals.append(population[-1])

    return individuals


def elite_selection(population, evaluation_fun, num_individuals):
    elite_indices = sorted(range(len(population)), key=lambda i: evaluation_fun(*population[i].to_list()),
                           reverse=True)[:num_individuals]
    individuals = []

    for j, elite_index in enumerate(elite_indices):
        n = math.ceil((num_individuals - j) / len(population))
        if len(individuals) + n > num_individuals:
            n = num_individuals - len(individuals)

        individuals.extend([population[elite_index]] * n)
        # print('Adding: ' + str(n))

        if len(individuals) == num_individuals:
            break

    return individuals


def universal_selection(population, evaluation_fun, num_individuals):
    fitness = [evaluation_fun(*i.to_list()) for i in population]
    total_fitness = sum(fitness)
    probabilities = [i / total_fitness for i in fitness]

    cumulative_probs = []
    cumulative_sum = 0
    for prob in probabilities:
        cumulative_sum += prob
        cumulative_probs.append(cumulative_sum)

    selected_indices = []
    step = 1.0 / num_individuals
    start = random.uniform(0, step)

    for i in range(num_individuals):
        pick = start + i * step
        for index, cum_prob in enumerate(cumulative_probs):
            if pick <= cum_prob:
                selected_indices.append(index)
                break

    return [population[i] for i in selected_indices]


def boltzmann_selection(population, evaluation_fun, num_individuals, temperature):
    fitness = [evaluation_fun(*i.to_list()) for i in population]
    scaled_fitness = [math.exp(i / temperature) for i in fitness]
    total_scaled_fitness = sum(scaled_fitness)
    probabilities = [i / total_scaled_fitness for i in scaled_fitness]
    selected_indices = random.choices(range(len(population)), weights=probabilities, k=num_individuals)
    return [population[i] for i in selected_indices]


def deterministic_tournament_selection(population, evaluation_fun, num_individuals):
    individuals = []
    population_fit = zip(population, [evaluation_fun(*i.to_list()) for i in population])

    for _ in range(num_individuals):
        t_round = random.sample(population_fit, 2)
        individuals.append(max(t_round, key=lambda i: i[1])[0])

    return individuals


def probabilistic_tournament_selection(population, evaluation_fun, num_individuals):
    individuals = []
    population_fit = zip(population, [evaluation_fun(*i.to_list()) for i in population])

    for _ in range(num_individuals):
        t_round = random.sample(population_fit, 2)
        if random.random() < 0.8:
            individuals.append(max(t_round, key=lambda i: i[1])[0])
        else:
            individuals.append(min(t_round, key=lambda i: i[1])[0])

    return individuals


def ranking_selection(population, evaluation_fun, num_individuals):
    ranked_indices = sorted(range(len(population)), key=lambda i: evaluation_fun(*population[i].to_list()),
                            reverse=True)
    ranks = list(range(1, len(population) + 1))
    rank_probabilities = [(len(population) - rank / len(population)) for rank in ranks]
    total_prob = sum(rank_probabilities)
    rank_probabilities = [i / total_prob for i in rank_probabilities]
    selected_indices = random.choices(ranked_indices, weights=rank_probabilities, k=num_individuals)
    return [population[i] for i in selected_indices]
