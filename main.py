import argparse
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
    parser.add_argument('--output-file', type=str, default='output/temp.out', help='The file to write the output to')
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')

    # Parse arguments
    return parser.parse_args()


def run_with_timeout(char_class, points_available, timeout, conf):
    ret = multiprocessing.Queue()

    p = multiprocessing.Process(target=genetic_algorithm, args=(char_class, points_available, conf, ret))
    p.start()
    p.join(timeout)

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
    res = run_with_timeout(character_class, args.points_available, args.timeout, config)

    log_path = Path(args.output_file)
    info = {'CharacterClass': args.character_class, 'PointsAvailable': args.points_available,
            'ElapsedSeconds': time() - starting_time, 'PopulationSize': config['population_size'],
            'TerminationCriteria': list(config['termination_criteria'].items())[1],
            'ParentsSelection': config['parents_selection']['method1'], 'Crossover': config['crossover']['type'],
            'Mutation': config['mutation']['type'],
            'NewGenerationSelection': config['new_generation_selection']['method1'],
            'SolutionScoreForEVE': eve_calculate(*res.to_list())}
    print(str(res.to_list()) + ' IS ' + str(eve_calculate(*res.to_list())))

    with open(args.output_file, mode='a', newline='') as log_file:
        writer = DictWriter(log_file, fieldnames=list(info.keys()))
        if not log_path.exists() or not log_path.stat().st_size:
            writer.writeheader()
        writer.writerow(info)
