from pprint import pp as pprint
import numpy as np

def rotate_facing(vector):
    # Rotation matrix for 90 degrees to the right
    rotation_matrix = np.array([[0, 1],
                                [-1, 0]])
    
    # Perform the rotation
    rotated_vector = np.dot(rotation_matrix, vector)
    
    return [int(x) for x in rotated_vector]

def get_facing_symbol(facing):
    match facing:
        case [-1,0]:
            return '^'
        case [0,1]:
            return '>'
        case [1,0]:
            return 'v'
        case [0,-1]:
            return '<'
    return '-'

with open('Day6/input.txt', 'r', encoding='utf-8') as f:
    original_data = f.readlines()
    data = [list(x.strip()) for x in original_data]

#find guard
guard_loc = [-1,-1]
guard_facing = [-1,0]
for i, row in enumerate(data):
    for j, col in enumerate(row):
        if col == '^':
            guard_loc = [i,j]
            break
    if guard_loc[0] != -1:
        break
original_loc = guard_loc.copy()
print('Start location:', guard_loc)
on_map = True
path = [f'%d,%d' % (guard_loc[0], guard_loc[1])]
while on_map:
    new_loc = list(map(lambda x,y: x+y, guard_loc, guard_facing))
    if new_loc[0] < 0 or new_loc[1] < 0 or new_loc[0] >= len(data) or new_loc[1] >= len(data[0]):
        on_map = False
        break

    if data[new_loc[0]][new_loc[1]] != '#':
        data[new_loc[0]][new_loc[1]] = get_facing_symbol(guard_facing)
        guard_loc = new_loc
        path.append(f'%d,%d' % (guard_loc[0], guard_loc[1]))
    else:
        guard_facing = rotate_facing(guard_facing)


pprint(data)
print('Unique locations in path:', len(set(path)))
