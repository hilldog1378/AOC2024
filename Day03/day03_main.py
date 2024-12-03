# day03_main.py

import pathlib
import sys
import parse as p
import re

def parse(puzzle_input):
    """Parse input."""
    return puzzle_input

def part1(data):
    """Solve part 1."""
    pattern = p.compile("mul({first:d},{second:d})")
    output = [results["first"] * results["second"] for results in pattern.findall(data)]
    return sum(output)

def part2(data):
    """Solve part 2."""
    pattern = p.compile("mul({first:d},{second:d})")
    do = re.compile(r"do\(\)")
    end = re.compile(r"don't\(\)")
    output = [results["first"] * results["second"] for results in pattern.findall(data)]
    start_index = [m.start() for m in do.finditer(data)]
    end_index = [m.start() for m in end.finditer(data)]
    start_index.insert(0,0)
    
    #need to edit the list to get rid of repeats
    
    return [len(start_index), len(end_index)]
    

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