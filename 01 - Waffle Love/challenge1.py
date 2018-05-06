#!/usr/bin/env python3

INPUT_FILE = 'submitInput.txt'
OUTPUT_FILE = 'submitOutput.txt'


def get_number_of_holes(vertical_lines, horizontal_lines):
    return (vertical_lines-1) * (horizontal_lines-1)

with open(INPUT_FILE, 'r') as f:
    cases = int(f.readline())
    lines = f.readlines()

with open(OUTPUT_FILE, 'w') as f:
    for case in range(cases):
        v, h = map(int, lines[case].split())
        result = 'Case #' + str(case + 1) + ': ' + str(get_number_of_holes(v, h)) + '\n'
        print(result)
        f.write(result)
