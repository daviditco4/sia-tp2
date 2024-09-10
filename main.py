import argparse
import json


def parse_arguments():
    # Create the parser
    parser = argparse.ArgumentParser(
        description="Project for RPG-like character generation from genetic algorithm based on Python.")

    # Add arguments
    parser.add_argument('--character-class', type=str, default='warrior',
                        help='The RPG=like class from which the character will be made')
    parser.add_argument('--points-available', type=int, default=100,
                        help="The amount of points to distribute among the character's skills")
    parser.add_argument('--timeout', type=int, default=1800,
                        help='The time limit in seconds to reach the optimal character')
    parser.add_argument('--config-file', type=str, help='The config file to determine algorithm hyperparameters')
    parser.add_argument('--output-file', type=str, help='The file to write the output to')
    parser.add_argument('--verbose', action='store_true', help='Increase output verbosity')

    # Parse arguments
    return parser.parse_args()


def load_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)


if __name__ == '__main__':
    args = parse_arguments()
    if args.verbose:
        print('Loading config...')
    config = load_config(args.config_file)
