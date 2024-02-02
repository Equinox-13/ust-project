import os
from concurrent.futures import ThreadPoolExecutor
from program1 import generate_numbers_divisible_by_5_and_7
from program2 import interleave_strings


def run_program1(n):
    """
    Run Program 1 with the given input 'n'.

    :param n: The upper limit for the range of numbers.
    """
    result = generate_numbers_divisible_by_5_and_7(int(n))
    output = ",".join(map(str, result))
    print("Output from program 1:", output)

def run_program2(string_1, string_2):
    """
    Run Program 2 with the given input strings.

    :param string_1: first input string
    :param string_2: second input string
    """
    output = interleave_strings(string_1, string_2)
    print("Output from program 2:", output)

def main():
    """
    The main function that reads input from a file, executes two programs concurrently using ThreadPoolExecutor,
    and prints the respective outputs.
    """
    file_path = os.path.join("inputs", "input.txt")
    with open(file_path, 'r') as file:
        lines = file.read().splitlines()

    with ThreadPoolExecutor() as executor:
        future_program1 = executor.submit(run_program1, lines[0])
        future_program2 = executor.submit(run_program2, lines[1], lines[2])

        future_program1.result()
        future_program2.result()


if __name__ == "__main__":
    main()
