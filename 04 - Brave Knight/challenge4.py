#!/usr/bin/env python3

from collections import deque

INPUT_FILE = 'submitInput.txt'
OUTPUT_FILE = 'submitOutput.txt'

def is_valid(grid, node):
    return node[0]>=0 and node[1]>=0 and node[0]<len(grid) and node[1]<len(grid[0]) and grid[node[0]][node[1]] != '#'


def find_neighbors(grid, node):
    neighbors = deque()
    row, column = node[0], node[1]
    jumps_ground = [(1, 2), (1, -2), (-1, -2), (-1, 2), (2, 1), (2, -1), (-2, -1), (-2, 1)]
    jumps_trampoline = [(2, 4), (2, -4), (-2, -4), (-2, 4), (4, 2), (4, -2), (-4, -2), (-4, 2)]
    if grid[row][column] in ('.', 'S', 'P', 'D'):
        candidates = list(map(lambda n: (n[0]+row, n[1]+column), jumps_ground))
    else: #asterisk
        candidates = list(map(lambda n: (n[0]+row, n[1]+column), jumps_trampoline))
    for candidate in candidates:
        if is_valid(grid, candidate):
            if grid[candidate[0]][candidate[1]] == '*':
                neighbors.appendleft(candidate)
            else:
                neighbors.append(candidate)
    return neighbors


def breadth_first_search(grid, start, end):
    checked = set()
    queue = deque([start, '-'])
    newLevel = False
    counter = 0
    while queue:
        node = queue.popleft()
        if node == end:
            return counter
        if node == '-':
            counter += 1
            newLevel = True
            continue
        checked.add(node)

        neighbors = find_neighbors(grid, node)
        if neighbors and newLevel:
            queue.append('-')
            newLevel = False
        for neighbor in neighbors:
            if neighbor in checked or neighbor in queue:
                continue
            else:
                queue.append(neighbor)
    return None


def main():
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        cases_count = int(lines[0])
        lines = lines[1:]

    with open(OUTPUT_FILE, 'w') as f:
        for case in range(cases_count):
            grid = []
            start, princess, destination = (), (), ()
            rows, columns = map(int, lines[0].split())
            for n in range(rows):
                row = list(lines[n+1].strip())
                grid.append(row)
                if 'S' in row: start = (n, row.index('S'))
                if 'P' in row: princess = (n, row.index('P'))
                if 'D' in row: destination = (n, row.index('D'))

            result = 'IMPOSSIBLE'
            to_princess = breadth_first_search(grid, start, princess)
            if to_princess:
                to_destination = breadth_first_search(grid, princess, destination)
                if to_destination:
                    result = to_princess + to_destination
            print('Case #' + str(case + 1) + ': ' + str(result) + '\n')
            f.write('Case #' + str(case + 1) + ': ' + str(result) + '\n')

            lines = lines[rows + 1:]

main()
