import subprocess

# Define the command template and the arguments
command_template = 'python3'
arguments = [
    'main.py --character-class warrior --points-available 100 --timeout 50 --config-file configs/config_prototype.json --output-file outputs/points_available.csv',
    'main.py --character-class warrior --points-available 130 --timeout 50 --config-file configs/config_prototype.json --output-file outputs/points_available.csv',
    'main.py --character-class warrior --points-available 160 --timeout 50 --config-file configs/config_prototype.json --output-file outputs/points_available.csv',
    'main.py --character-class warrior --points-available 200 --timeout 50 --config-file configs/config_prototype.json --output-file outputs/points_available.csv',

    'main.py --character-class warrior --points-available 100 --timeout 10 --config-file configs/config_prototype.json --output-file outputs/timeout.csv',
    'main.py --character-class warrior --points-available 100 --timeout 50 --config-file configs/config_prototype.json --output-file outputs/timeout.csv',
    'main.py --character-class warrior --points-available 100 --timeout 120 --config-file configs/config_prototype.json --output-file outputs/timeout.csv',
    'main.py --character-class warrior --points-available 100 --timeout 1800 --config-file configs/config_prototype.json --output-file outputs/timeout.csv',

    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_population_size.csv --config-file configs/config_population_size_20.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_population_size.csv --config-file configs/config_population_size_60.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_population_size.csv --config-file configs/config_population_size_120.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_population_size.csv --config-file configs/config_population_size_200.json',

    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_max_generations.csv --config-file configs/config_max_generations_40.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_max_generations.csv --config-file configs/config_max_generations_100.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_max_generations.csv --config-file configs/config_max_generations_500.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_max_generations.csv --config-file configs/config_max_generations_1000.json',

    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_parents_selection.csv --config-file configs/config_parents_selection_elite.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_parents_selection.csv --config-file configs/config_parents_selection_roulette.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_parents_selection.csv --config-file configs/config_parents_selection_universal.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_parents_selection.csv --config-file configs/config_parents_selection_boltzmann.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_parents_selection.csv --config-file configs/config_parents_selection_deterministic_tournament.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_parents_selection.csv --config-file configs/config_parents_selection_probabilistic_tournament.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_parents_selection.csv --config-file configs/config_parents_selection_ranking.json',

    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_crossover.csv --config-file configs/config_crossover_one_point.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_crossover.csv --config-file configs/config_crossover_two_point.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_crossover.csv --config-file configs/config_crossover_uniform.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_crossover.csv --config-file configs/config_crossover_circular.json',

    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_mutation.csv --config-file configs/config_mutation_gen_0-01.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_mutation.csv --config-file configs/config_mutation_gen_0-1.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_mutation.csv --config-file configs/config_mutation_gen_0-4.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_mutation.csv --config-file configs/config_mutation_multigen_0-01.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_mutation.csv --config-file configs/config_mutation_multigen_0-1.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_mutation.csv --config-file configs/config_mutation_multigen_0-4.json',

    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_new_generation_selection.csv --config-file configs/config_new_generation_selection_elite.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_new_generation_selection.csv --config-file configs/config_new_generation_selection_roulette.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_new_generation_selection.csv --config-file configs/config_new_generation_selection_universal.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_new_generation_selection.csv --config-file configs/config_new_generation_selection_boltzmann.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_new_generation_selection.csv --config-file configs/config_new_generation_selection_deterministic_tournament.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_new_generation_selection.csv --config-file configs/config_new_generation_selection_probabilistic_tournament.json',
    'main.py --character-class warrior --points-available 100 --timeout 50 --output-file outputs/output_new_generation_selection.csv --config-file configs/config_new_generation_selection_ranking.json']

# Number of repetitions
num_repetitions = 10


def run_command(command, args, repetitions):
    for arg in args:
        for _ in range(repetitions):
            # Construct the full command
            full_command = [command] + arg.split()
            try:
                # Execute the command
                result = subprocess.run(full_command, capture_output=True, text=True, check=True)
                print(f'Command executed: {result.args}')
                print('Output:')
                print(result.stdout.strip())
            except subprocess.CalledProcessError as e:
                print(f'Error executing command: {e}')
                print(f'Command: {e.cmd}')
                print(f'Output: {e.output}')
                print(f'Error: {e.stderr}')


if __name__ == "__main__":
    run_command(command_template, arguments, num_repetitions)
