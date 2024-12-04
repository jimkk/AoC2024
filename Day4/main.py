with open('Day4/input.txt', 'r', encoding='utf-8') as f:
    data = [x.replace('\n', '') for x in f.readlines()]

KEY = 'XMAS'
part_1 = 0
keys = []
for i, row in enumerate(data):
    for j,_ in enumerate(row):
        if j < len(row)-3:
            if row[j:j+4] == KEY:
                keys.append(['right:', i, j])
                part_1 += 1
        if j > 2:
            if ''.join([row[j], row[j-1], row[j-2], row[j-3]]) == KEY:
                keys.append(['left:', i, j])
                part_1 += 1
        if i < len(data) - 3:
            if ''.join([data[i][j], data[i+1][j], data[i+2][j], data[i+3][j]]) == KEY:
                keys.append(['down:', i, j])
                part_1 += 1
        if i > 2:
            if ''.join([data[i][j], data[i-1][j], data[i-2][j], data[i-3][j]]) == KEY:
                keys.append(['up:', i, j])
                part_1 += 1
        #ul
        if i > 2 and j > 2:
            if ''.join([data[i][j], data[i-1][j-1], data[i-2][j-2], data[i-3][j-3]]) == KEY:
                keys.append(['ul', i, j])
                part_1 += 1
        #ur
        if i > 2 and j < len(row) - 3:
            if ''.join([data[i][j], data[i-1][j+1], data[i-2][j+2], data[i-3][j+3]]) == KEY:
                keys.append(['ur', i, j])
                part_1 += 1
        #dl
        if i < len(data) - 3 and j > 2:
            if ''.join([data[i][j], data[i+1][j-1], data[i+2][j-2], data[i+3][j-3]]) == KEY:
                keys.append(['dl', i, j])
                part_1 += 1
        #dr
        if i < len(data) - 3 and j < len(row) - 3:
            if ''.join([data[i][j], data[i+1][j+1], data[i+2][j+2], data[i+3][j+3]]) == KEY:
                keys.append(['dr', i, j])
                part_1 += 1

#part 2
part_2 = 0
for i in range(1, len(data)-1):
    for j in range(1,len(data[i])-1):
        if data[i][j] != 'A':
            continue
        diags = [data[i-1][j-1],data[i-1][j+1],data[i+1][j-1],data[i+1][j+1]]
        if diags[0] == diags[3]:
            continue
        diags.sort()
        if ''.join(diags) == 'MMSS':
            part_2 += 1


print('Part 1:', part_1)
print('Part 2:', part_2)