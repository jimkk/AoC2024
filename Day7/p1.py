import itertools
import re

with open('Day7/input.txt', 'r', encoding='utf-8') as f:
    data = [x.strip().split(': ') for x in f.readlines()]

def eval_options(goal, options, numbers):
    for option in options:
        option_total = int(numbers[0])
        for i in range(1, len(numbers)):
            option_total = eval(str(option_total) + option[i-1] + numbers[i])
        if option_total == goal:
            return goal
        if option_total > goal:
            continue
    return 0


total = 0
for equation in data:
    goal = int(equation[0])
    numbers = equation[1].split(' ')
    options = list(itertools.product(['+', '*'], repeat=len(numbers)-1))
    total += eval_options(goal, options, numbers)

print('Part 1:', total)