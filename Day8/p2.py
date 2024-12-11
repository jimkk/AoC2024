import math
from pprint import pp as pprint

def slope(point1, point2):
    """
    Get the slope as a 2D vector between two points
    """
    return (point2[0] - point1[0], point2[1] - point1[1])

def get_antinodes(point1, point2, max_x, max_y):
    """
    Get the points from point1 to point2
    that are on the line between the two points
    and half the distance from one point than the other
    """
    slope_between_points = slope(point1, point2)
    first_point = point1
    while first_point[0] >= 0 and first_point[1] >= 0 and first_point[0] < max_x and first_point[1] < max_y:
        first_point = (first_point[0] - slope_between_points[0], first_point[1] - slope_between_points[1])
    point = (first_point[0] + slope_between_points[0], first_point[1] + slope_between_points[1])
    points = [point]
    while point[0] < max_x and point[1] < max_y:
        point = (point[0] + slope_between_points[0], point[1] + slope_between_points[1])
        points.append(point)
    return points

        
with open('Day8/input.txt', 'r', encoding='utf-8') as f:
    data = [list(x.strip()) for x in f.readlines()]

antennas = {}
for i, row in enumerate(data):
    for j, loc in enumerate(row):
        if loc == '.':
            continue
        if loc in antennas:
            antennas[loc].append((i,j))
        else:
            antennas[loc] = [(i,j)]

antinodes = []

for key, antenna in antennas.items():
    for i, a in enumerate(antenna):
        for b in antenna[i+1:]:
            antenna_antinodes = [x for x in get_antinodes(a, b, len(data), len(data[0])) if x[0] >= 0 and x[1] >= 0 and x[0] < len(data) and x[1] < len(data[0])]
            antinodes += antenna_antinodes

print('Part 2:', len(set(antinodes)))

# For visualizing the result for debugging
# answer = []
# for i, row in enumerate(data):
#     answer_row = []
#     for j, loc in enumerate(row):
#         if (i,j) in antinodes:
#             answer_row.append('#')
#         else:
#             answer_row.append(loc)
#     answer.append(answer_row)

# print('\n'.join([''.join(x) for x in answer]))
