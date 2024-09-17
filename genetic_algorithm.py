import math
import random

from Character import Character
from crossover import one_point_crossover, two_point_crossover, uniform_crossover, circular_crossover
from eve_calc import eve_calculate
from mutation import gen_mutation, multigen_mutation
from selection import elite_selection, roulette_selection, universal_selection, boltzmann_selection, \
    deterministic_tournament_selection, probabilistic_tournament_selection, ranking_selection


def _check_termination_criteria(population, evaluate_fun, config):
    fitness = [evaluate_fun(*i.to_list()) for i in population]
    # rounded_fitness = [i for i in fitness]
    if 'structure' in config:
        pass
    if 'content' in config and len(set(fitness)) == 1:
        # print(fitness)
        # print('CONTENT REACHED')
        return True
    if 'acceptable_fitness' in config and max(fitness) >= config['acceptable_fitness']:
        return True
    return False


def _best_solution(population, evaluate_fun):
    best_index = max(range(len(population)), key=lambda i: evaluate_fun(*population[i].to_list()))
    return population[best_index]


def _replace_population(population, offspring, evaluation_fun, config):
    new_generation = []
    num_individuals_for_method1 = math.floor(config.get('proportion_for_method1', 1.0) * len(population))
    num_individuals_for_method2 = len(population) - num_individuals_for_method1

    def evaluate_selection(method, num_individuals):
        match method:
            case 'elite':
                new_generation.extend(elite_selection(population + offspring, evaluation_fun, num_individuals))
            case 'roulette':
                new_generation.extend(roulette_selection(population + offspring, evaluation_fun, num_individuals))
            case 'universal':
                new_generation.extend(universal_selection(population + offspring, evaluation_fun, num_individuals))
            case 'boltzmann':
                new_generation.extend(boltzmann_selection(population + offspring, evaluation_fun, num_individuals, 0.8))
            case 'deterministic_tournament':
                new_generation.extend(
                    deterministic_tournament_selection(population + offspring, evaluation_fun, num_individuals))
            case 'probabilistic_tournament':
                new_generation.extend(
                    probabilistic_tournament_selection(population + offspring, evaluation_fun, num_individuals))
            case 'ranking':
                new_generation.extend(ranking_selection(population + offspring, evaluation_fun, num_individuals))

    evaluate_selection(config['method1'], num_individuals_for_method1)
    if 'method2' in config:
        evaluate_selection(config['method2'], num_individuals_for_method2)

    return new_generation


def _mutate_offspring(offspring, config, total_points_available):
    match config['type']:
        case 'gen':
            return gen_mutation(offspring, config['probability'], total_points_available)
        case 'multigen':
            return multigen_mutation(offspring, config['probability'], total_points_available)
        case _:
            raise ValueError('Invalid mutation type')


def _cross_parents(parents, config, total_points_available):
    match config['type']:
        case 'one_point':
            return one_point_crossover(parents, total_points_available)
        case 'two_point':
            return two_point_crossover(parents, total_points_available)
        case 'uniform':
            return uniform_crossover(parents, total_points_available)
        case 'circular':
            return circular_crossover(parents, total_points_available)
        case _:
            raise ValueError('Invalid crossover type')


def _select_parents(population, evaluation_fun, config):
    parents = []
    num_parents = math.floor(config.get('ratio_of_parenthood', 2.0) * len(population)) // 2 * 2
    # print('PARENTS: ' + str(num_parents))
    num_parents_for_method1 = math.floor(config.get('proportion_for_method1', 1.0) * num_parents)
    num_parents_for_method2 = num_parents - num_parents_for_method1

    def evaluate_selection(method, n_parents):
        match method:
            case 'elite':
                parents.extend(elite_selection(population, evaluation_fun, n_parents))
            case 'roulette':
                parents.extend(roulette_selection(population, evaluation_fun, n_parents))
            case 'universal':
                parents.extend(universal_selection(population, evaluation_fun, n_parents))
            case 'deterministic_tournament':
                parents.extend(deterministic_tournament_selection(population, evaluation_fun, n_parents))
            case 'probabilistic_tournament':
                parents.extend(probabilistic_tournament_selection(population, evaluation_fun, n_parents))
            case 'ranking':
                parents.extend(ranking_selection(population, evaluation_fun, n_parents))

    evaluate_selection(config['method1'], num_parents_for_method1)
    if 'method2' in config:
        evaluate_selection(config['method2'], num_parents_for_method2)

    return parents


def initialize_population(character_class, points_available, population_size):
    population = []

    for _ in range(population_size):
        attributes = []
        points_left = points_available

        for i in range(Character.attribute_amount):
            attributes.append(random.randint(0, points_left))
            points_left -= attributes[i]
        random.shuffle(attributes)
        height = random.uniform(1.3, 2.0)

        population.append(Character.from_list([character_class, *attributes, height]))

    return population


def genetic_algorithm(character_class, points_available, config, ret):
    population = initialize_population(character_class, points_available, config['population_size'])
    termination_config = config['termination_criteria']
    i = 0
    ret.put(None)
    solution = None

    while not 'max_generations' in termination_config or i < termination_config['max_generations']:
        # print('GENERATION: ' + str(i))
        parents = _select_parents(population, eve_calculate, config['parents_selection'])
        offspring = _cross_parents(parents, config['crossover'], points_available)
        offspring = _mutate_offspring(offspring, config['mutation'], points_available)
        population = _replace_population(population, offspring, eve_calculate, config['new_generation_selection'])
        solution = _best_solution(population, eve_calculate)
        ret.get()
        ret.put(solution)
        if _check_termination_criteria(population, eve_calculate, termination_config):
            print('Exiting: ' + str(i))
            print(str(solution) + ' IS ' + str(eve_calculate(*solution.to_list())))
            return
        i += 1

    print(str(solution) + ' IS ' + str(eve_calculate(*solution.to_list())))
    print([eve_calculate(*i.to_list()) for i in population])
