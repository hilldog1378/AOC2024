# day01_main.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    left = []
    right = []
    for x in puzzle_input.splitlines():
        temp = x.split('   ')
        left.append(int(temp[0]))
        right.append(int(temp[1]))
    left.sort()
    right.sort()
    return {'left':left,'right':right}
        

def part1(data):
    """Solve part 1."""
    output = 0
    for x in range(len(data['left'])):
        output = output + abs(data['left'][x]-data['right'][x])
    return output

    

def part2(data):
    """Solve part 2."""
    output = 0
    for x in range(len(data['left'])):
        left = data['left'][x]
        output = output + (left * data['right'].count(left) )
    return output
       

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        data = parse(puzzle_input)
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
