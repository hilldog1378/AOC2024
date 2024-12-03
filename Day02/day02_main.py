# day02_main.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    return [x for x in puzzle_input.splitlines()]

def direction(report: list) -> bool:
    """
    Check to see if all the leveles in a report are either decending or acending

    Parameters
    ----------
    report : str
        The report, which is made up of diffrent levels.

    Returns
    -------
    bool
        Returns true if the report if all decending or acending.

    """
    #temp = [int(x) for x in report.split()]
    postive = 0
    negtive = 0
    nutrual = 0
    for x in range(len(report) - 1):
        if report[x+1] > report[x]:
            postive += 1
        elif report[x+1] < report[x]:
            negtive += 1
        else:
            nutrual += 1
    if postive == len(report)-1 or negtive == len(report)-1:
        return True
    else:
        return False
            
def diffrence(report: list) -> bool:
    """
    Check to see if the diffrence between all the levels in a report is between 1 and 3

    Parameters
    ----------
    report : str
        The report, which is made up of diffrent level .

    Returns
    -------
    bool
        returns TRUE if all level are between 1 to 3 diffrence.  Else returns FALSE

    """
    #temp = [int(x) for x in report.split()]
    for x in range(len(report) - 1):
        if 1 <= abs(report[x] - report[x+1]) <= 3:
            continue
        else:
            return False
    return True

def part1(data):
    """Solve part 1."""

    safe = 0
    unsafe = 0
    for report in data:
        temp = [int(x) for x in report.split()]
        if diffrence(temp) and direction(temp):
            safe += 1
        else:
            unsafe += 1
    return safe
    

def part2(data):
    """Solve part 2."""
    safe = 0
    safe_list = []
    unsafe = 0
    unsafe_list = []
    safe_tolerate = 0
    safe_tolerate_list = []
    unsafe_tolerate = 0
    unsafe_tolerate_list = []
    for report in range(len(data)):
        temp = [int(x) for x in data[report].split()]
        if diffrence(temp) and direction(temp):
            safe += 1
            safe_list.append(report)
        else:
            unsafe += 1
            unsafe_list.append(report)
    
    for y in range(len(unsafe_list)):
        test = unsafe_list[y]
        temp = [int(x) for x in data[test].split()]
        
        for z in range(len(temp)):
            temp_copy = temp.copy()
            temp_copy.pop(z)
            if diffrence(temp_copy) and direction(temp_copy):
                safe_tolerate += 1
                safe_tolerate_list.append(test)
                break
        else:
            unsafe_tolerate += 1
            unsafe_tolerate_list.append(test)
    
    return safe + safe_tolerate
    

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