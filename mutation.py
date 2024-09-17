import random

from Character import Character


def gen_mutation(offspring, mutation_rate, total_points_available):
    mutants = []

    for individual in offspring:
        if random.random() < mutation_rate:
            index = random.randint(1, Character.attribute_amount + 1)
            individual_list = individual.to_list()
            delta = None

            if index != Character.attribute_amount + 2 - 1:
                while not delta or delta > Character.unassigned_points_from_list(individual_list,
                                                                                 total_points_available):
                    rand = random.random()
                    delta = random.choice([-1, 1]) * int(
                        ((total_points_available / Character.attribute_amount) / 2) * (rand ** 2))
                individual_list[index] = max(0, individual_list[index] + delta)
            else:
                while not delta or individual_list[index] + delta < 1.3 or individual_list[index] + delta > 2.0:
                    rand = random.random()
                    delta = random.choice([-1, 1]) * ((2.0 - 1.3) / 2) * (rand ** 2)
                individual_list[index] = min(2.0, max(1.3, individual_list[index] + delta))
            mutants.append(Character.from_list(individual_list))
        else:
            mutants.append(individual)

            return mutants


def multigen_mutation(offspring, mutation_rate, total_points_available):
    mutants = []

    for individual in offspring:
        individual_list = individual.to_list()
        deltas = []
        attr_delta = None

        while attr_delta is None or attr_delta > Character.unassigned_points_from_list(individual_list,
                                                                                       total_points_available):
            deltas.clear()
            attr_delta = 0
            for i in range(1, Character.attribute_amount + 1):
                if random.random() < mutation_rate:
                    rand = random.random()
                    choice = random.choice([-1, 1]) * int(
                        ((total_points_available / Character.attribute_amount) / 2) * (
                                rand ** 2))
                    deltas.append(choice)
                    if individual_list[i] + choice < 0:
                        attr_delta -= individual_list[i]
                    else:
                        attr_delta += choice
                else:
                    deltas.append(0)
            if random.random() < mutation_rate:
                rand = random.random()
                deltas.append(random.choice([-1, 1]) * ((2.0 - 1.3) / 2) * (rand ** 2))
            else:
                deltas.append(0)
        for i in range(1, Character.attribute_amount + 1):
            individual_list[i] = max(0, individual_list[i] + deltas[i - 1])
        individual_list[Character.attribute_amount + 1] = min(2.0, max(1.3, individual_list[
            Character.attribute_amount + 1] + deltas[Character.attribute_amount]))

        mutants.append(Character.from_list(individual_list))

    return mutants
