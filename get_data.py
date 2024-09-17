import subprocess

# Define the command template and the arguments
command_template = 'python3'
arguments = ['main.py --character-class warrior --points-available 100 --timeout 25 --config-file /configs/config_prototype.json --output-file data1.csv'
             , 'main.py --character-class mage --points-available 100 --timeout 25 --config-file /configs/config_prototype.json --output-file data2.csv'
             , 'main.py --character-class guardian --points-available 100 --timeout 25 --config-file /configs/config_prototype.json --output-file data3.csv'
             , 'main.py --character-class archer --points-available 100 --timeout 25 --config-file /configs/config_prototype.json --output-file data4.csv', ]

# Number of repetitions
num_repetitions = 100


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