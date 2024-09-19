# sia-tp2

Implementation of RPG-like character generation from genetic algorithm based on Python

## System requirements

Python 3.10+

## How to use

* Clone or download this repository in the folder you desire
* In a new terminal, navigate to the repository using `cd`
* When you are ready, enter a command as follows:
```sh
python3 main.py [--character-class <c>] [--points-available <p>] [--timeout <t>] [--config-file <f>] [--output-file <o>]
```

### Arguments

* `--character-class`: The RPG-like class from which the character will be made
* `--points-available`: The amount of points to distribute among the character's skills
* `--timeout`: The time limit in seconds to reach the optimal character
* `--config-file`: The config file to determine algorithm hyperparameters (as described below)
* `--output-file`: The file to write the output to

### Hyperparameters

The configuration for the algorithm's options is a JSON file with the following structure:

* `"population_size"`: The amount of individuals of each new generation
* `"termination_criteria"`:
  * `"max_generations"`: The amount of generations before the algorithm exits
  * `"acceptable_fitness"` (optional): The fitness amount for a result to be provided sooner than the exit by generation
  * `"content"` (optional): If set, it also provides the result when a generation's individuals have all reached the
  same fitness
* `"parents_selection"`:
  * `"ratio_of_parenthood"`: The average amount of times an individual will be a parent (e.g. one child for each couple
  is 1.0)
  * `"proportion_for_method1"` (optional): The proportion of the selection that will be done with 'method1' (default
  1.0)
  * `"method1"`: The first method of selection ('elite', 'roulette', 'universal', 'boltzmann',
  'deterministic_tournament', 'probabilistic_tournament' or 'ranking')
  * `"method2"` (optional): The second method of selection (idem)
* `"crossover"`:
  * `"type"`: The type of crossover the algorithm will use ('one_point', 'two_point', 'uniform' or 'circular')
* `"mutation"`:
  * `"type"`: The type of mutation the algorithm will use ('gen' or 'multigen')
  * `"probability"`: The rate of mutation the algorithm will use
* `"new_generation_selection"`:
  * `"proportion_for_method1"` (optional): The proportion of the selection that will be done with 'method1' (default
  1.0)
  * `"method1"`: The first method of selection ('elite', 'roulette', 'universal', 'boltzmann',
  'deterministic_tournament', 'probabilistic_tournament' or 'ranking')
  * `"method2"` (optional): The second method of selection (idem)

## License

This project is licensed under the MIT License - see the LICENSE file for details.