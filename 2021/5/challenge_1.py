import re
import math

FILE_PATH = 'input.txt'

with open(FILE_PATH, 'r') as file:
    input_str = file.read()
input_num_lst = list(map(int, re.findall('\d+', input_str)))
x_max = max(input_num_lst)
y_max = max(input_num_lst)
grid = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]

for line in input_str.split('\n'):
    x1, y1, x2, y2 = map(int, line.replace(' -> ', ',').split(','))
    if (not (x1 == x2 or y1 == y2)):
        continue
    elif (x1 == x2):
        sign = int(math.copysign(1, y2 - y1))
        for dy in range(y1, y2 + sign, sign):
            grid[dy][x1] += 1
    elif (y1 == y2):
        sign = int(math.copysign(1, x2 - x1))
        for dx in range(x1, x2 + sign, sign):
            grid[y1][dx] += 1
            
count = 0
grid_str = ''
for y in range(y_max + 1):
    for x in range(x_max + 1):
        if (grid[y][x] == 0):
            grid_str += '.'
        else:
            grid_str += str(grid[y][x])
        if (grid[y][x] > 1):
            count += 1
    grid_str += '\n'
print(count)
print(grid_str)