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
   
    mul = p.compile("mul({first:d},{second:d})")
    pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)")
    output = re.findall(pattern, data)
    
    head = True
    answer = 0
    for x in output:
        if x == 'do()':
            head = True
        elif x == "don't()":
            head = False
        else:
            if head:
                temp = [results["first"] * results["second"] for results in mul.findall(x)]
                answer += temp[0]
    
    return answer

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