"""Day 1 Code"""
def main():
    """the code"""    
    with open('Day1/input.txt', 'r', encoding='utf-8') as f:
        input_data = f.read()

    data = [[],[]]
    for i, line in enumerate(input_data.split('\n')):
        line_parts = line.split('   ')
        data[0].append(int(line_parts[0]))
        data[1].append(int(line_parts[1]))


    data[0].sort()
    data[1].sort()


    part_1 = 0
    part_2 = 0
    for i in range(len(data[0])):
        part_1 += abs(data[0][i] - data[1][i])
        part_2 += data[0][i] * len([x for x in data[1]if x == data[0][i]])

    print('Part 1:', part_1)
    print('Part 2:', part_2)

main()
