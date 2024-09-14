import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from CharacterClass import CharacterClass
from eve_calc import eve_calculate
from genetic_algorithm import initialize_population

if __name__ == '__main__':
    population = initialize_population(CharacterClass.WARRIOR, 100, 10000000)
    best_index = max(range(len(population)), key=lambda i: eve_calculate(*population[i].to_list()))
    print(str(population[best_index].to_list()) + ' IS ' + str(eve_calculate(*population[best_index].to_list())))
