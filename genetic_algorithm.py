import math
import random

from Character import Character
from crossover import one_point_crossover, two_point_crossover, uniform_crossover
from eve_calc import eve_calculate
from selection import elite_selection, roulette_selection


def _mutate_offspring(offspring, config):
    match config['type']:
        case 'gen':
            return gen_mutation(offspring, config['probability'])
        case 'multigen':
            return multigen_mutation(offspring, config['probability'])
        case _:
            raise ValueError('Invalid mutation type')


def _cross_parents(parents, config):
    offspring = []

    for i in range(0, len(parents), 2):
        parent1 = parents[i]
        parent2 = parents[i + 1]

        match config['type']:
            case 'one_point':
                child1, child2 = one_point_crossover(parent1, parent2)
            case 'two_point':
                child1, child2 = two_point_crossover(parent1, parent2)
            case 'uniform':
                child1, child2 = uniform_crossover(parent1, parent2)
            case _:
                raise ValueError('Invalid crossover type')

        offspring.extend([child1, child2])

    return offspring


def _select_parents(population, fitness, config):
    parents = []
    num_parents = math.floor(config.get('ratio_of_parenthood', 1.0) * len(population)) // 2 * 2
    num_parents_for_method1 = math.floor(config.get('proportion_for_method_a', 1.0) * num_parents)
    num_parents_for_method2 = num_parents - num_parents_for_method1

    match config['method1']:
        case 'elite':
            parents.extend(elite_selection(population, fitness, num_parents_for_method1))
        case 'roulette':
            parents.extend(roulette_selection(population, fitness, num_parents_for_method1))
    if 'method2' in config:
        match config['method2']:
            case 'elite':
                parents.extend(elite_selection(population, fitness, num_parents_for_method2))
            case 'roulette':
                parents.extend(roulette_selection(population, fitness, num_parents_for_method2))

    return parents


def _evaluate_population(population):
    return [eve_calculate(*individual.to_list()) for individual in population]


def _initialize_population(character_class, points_available, population_size):
    population = []

    for _ in range(population_size):
        attributes = []
        points_left = points_available

        for i in range(Character.attribute_amount):
            attributes[i] = random.randint(0, points_left)
            points_left -= attributes[i]
        random.shuffle(attributes)
        height = random.uniform(1.3, 2.0)

        population.append(Character.from_list([character_class, *attributes, height]))

    return population


def genetic_algorithm(character_class, points_available, config):
    population = _initialize_population(character_class, points_available, config['population_size'])
    termination_config = config['termination_criteria']

    for generation in range(termination_config['max_generations']):
        fitness = _evaluate_population(population)
        parents = _select_parents(population, fitness, config['parents_selection'])
        offspring = _cross_parents(parents, config['crossover'])
        offspring = _mutate_offspring(offspring, config['mutation'])
        population = _replace_population(population, offspring, config['replacement'])
        if _check_termination_criteria(fitness):
            break

    return _best_solution(population)
