import re

with open('Day3/input.txt', 'r', encoding='utf-8') as f:
    data = f.read()

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
part_1 = 0
for match in matches:
    numbers = re.findall(r'\d{1,3}', match)
    part_1 += int(numbers[0]) * int(numbers[1])

part_2 = 0
enabled = True
matches = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', data)
print(matches)
for match in matches:
    operation = match.split('(')[0]
    
    match operation:
        case 'do':
            enabled = True
        case 'don\'t':
            enabled = False
        case 'mul':
            if enabled:
                numbers = [int(x) for x in re.findall(r'\d{1,3}', match)]
                part_2 += numbers[0] * numbers[1]

print('Part 1:', part_1)
print('Part 2:', part_2)
