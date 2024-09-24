import argparse
import ctypes
import os
import json
import multiprocessing
from csv import DictWriter
from pathlib import Path
from time import time

from CharacterClass import CharacterClass
from eve_calc import eve_calculate
from genetic_algorithm import genetic_algorithm


def parse_arguments():
    # Create the parser
    parser = argparse.ArgumentParser(
        description='Project for RPG-like character generation from genetic algorithm based on Python.')

    # Add arguments
    parser.add_argument('--character-class', type=str, default='warrior',
                        help='The RPG-like class from which the character will be made')
    parser.add_argument('--points-available', type=int, default=100,
                        help="The amount of points to distribute among the character's skills")
    parser.add_argument('--timeout', type=int, default=1800,
                        help='The time limit in seconds to reach the optimal character')
    parser.add_argument('--config-file', type=str, default='configs/config.json',
                        help='The config file to determine algorithm hyperparameters')
    parser.add_argument('--output-file', type=str, default='outputs/temp.csv', help='The file to write the output to')
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')

    # Parse arguments
    return parser.parse_args()


def run_with_timeout(char_class, points_available, timeout, conf, fit_scores):
    ret = multiprocessing.Queue()
    aux1 = multiprocessing.Array(ctypes.c_float, 2 * (conf['termination_criteria']['max_generations'] + 1))
    

    p = multiprocessing.Process(target=genetic_algorithm, args=(char_class, points_available, conf, ret, aux1))
    p.start()
    p.join(timeout)
    
    for i in range(len(aux1)):
        fit_scores[i] = aux1[i]

    if p.is_alive():
        result = ret.get()
        p.terminate()
        p.join()
        return result
    else:
        return ret.get()


def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
def give_separating_index(array):
    for i in range(len(array)):
        if(array[i] == 0.0):
            return i
    return 0


if __name__ == '__main__':
    args = parse_arguments()

    # if args.verbose:
    #     print('Loading config...')
    config = load_config(args.config_file)
    match args.character_class:
        case 'warrior':
            character_class = CharacterClass.WARRIOR
        case 'archer':
            character_class = CharacterClass.ARCHER
        case 'guardian':
            character_class = CharacterClass.GUARDIAN
        case 'mage':
            character_class = CharacterClass.MAGE
        case _:
            raise ValueError('Invalid character class')

    starting_time = time()
    fit_scores = multiprocessing.Array(ctypes.c_float, 2 * (config['termination_criteria']['max_generations'] + 1))
    res = run_with_timeout(character_class, args.points_available, args.timeout, config, fit_scores)
    index_val = give_separating_index(fit_scores)
    index_val = 0
    best_array=[]
    avg_array=[]
    
    if index_val==0:
        for i in range(len(fit_scores) - 1):
            if(i < (config['termination_criteria']['max_generations'] + 1)):
                best_array.append(fit_scores[i])
            else:
                avg_array.append(fit_scores[i])
    else:
        for i in range(len(fit_scores)):
            if(i < index_val):
                best_array.append(fit_scores[i])
            elif(i >=  config['termination_criteria']['max_generations'] and i < (config['termination_criteria']['max_generations'] + index_val)):
                avg_array.append(fit_scores[i])
    
    log_path = Path(args.output_file)
    info = {'CharacterClass': args.character_class, 'PointsAvailable': args.points_available,
            'ElapsedSeconds': time() - starting_time, 'PopulationSize': config['population_size'],
            'MaxGenerations': config['termination_criteria']['max_generations'],
            'ParentsSelection': config['parents_selection']['method1'], 'Crossover': config['crossover']['type'],
            'Mutation': config['mutation']['type'],
            'NewGenerationSelection': config['new_generation_selection']['method1'],
            'SolutionScoreForEVE': eve_calculate(*res.to_list())}
    # print(str(res.to_list()) + ' IS ' + str(eve_calculate(*res.to_list())))

    best_dict = {f"Generation{i}":num for i, num in enumerate(best_array)}
    avg_dict = {f"Generation{i}":num for i, num in enumerate(avg_array)}
    
    path_to_file = args.output_file
    last_inx = path_to_file.rfind('/')
    if last_inx != -1:
        best_fit_path = path_to_file[:last_inx + 1] + "best_array_" + path_to_file[last_inx + 1:]
        avg_fit_path = path_to_file[:last_inx + 1] + "avg_array_" + path_to_file[last_inx + 1:]
    else:
        best_fit_path = "best_array_" + path_to_file  # If there is no '/', just prepend the string
        avg_fit_path = "avg_array_" + path_to_file

    os.makedirs(os.path.dirname(best_fit_path), exist_ok=True)
    os.makedirs(os.path.dirname(avg_fit_path), exist_ok=True)

    
    with open(best_fit_path, mode='a', newline='') as f1:
        writer = DictWriter(f1, fieldnames=best_dict.keys())
        # Write the header only once
        if f1.tell() == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow(best_dict)

    with open(avg_fit_path, mode='a', newline='') as f2:
        writer = DictWriter(f2, fieldnames=avg_dict.keys())
        # Write the header only once
        if f2.tell() == 0:  # Check if file is empty
            writer.writeheader()
        writer.writerow(avg_dict)

    with open(args.output_file, mode='a', newline='') as log_file:
        writer = DictWriter(log_file, fieldnames=list(info.keys()))
        if not log_path.exists() or not log_path.stat().st_size:
            writer.writeheader()
        writer.writerow(info)
