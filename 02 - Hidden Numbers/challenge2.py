#!/usr/bin/env python3

INPUT_FILE = 'submitInput.txt'
OUTPUT_FILE = 'submitOutput.txt'

chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
         'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

def get_min(line):
    base = len(line)
    minimum = ['1', '0']
    for x in range(2, base):
        minimum.append(chars[x])
    return ''.join(minimum)

def get_max(line):
    base = len(line)
    maximum = [chars[base-1], chars[base-2]]
    for x in range(base-3, -1, -1):
        maximum.append(chars[x])
    return ''.join(maximum)

def get_result(line):
    min_in_certain_base = get_min(line)
    max_in_certain_base = get_max(line)
    min_in_decimal = int(min_in_certain_base, len(line))
    max_in_decimal = int(max_in_certain_base, len(line))
    return max_in_decimal - min_in_decimal


with open(INPUT_FILE, 'r') as f:
    cases = int(f.readline())
    lines = f.readlines()

with open(OUTPUT_FILE, 'w') as f:
    for case in range(cases):
        result = get_result(lines[case].rstrip('\n'))
        print("Case #" + str(case + 1) + ": " + str(result) + '\n')
        f.write("Case #" + str(case + 1) + ": " + str(result) + '\n')
