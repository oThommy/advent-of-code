FILE_PATH = 'input.txt'

with open(FILE_PATH, 'r') as file:
    height_map = []
    for line in file:
        height_map.append([int(num) for num in line.split('\n')[0]])

basin_lst = []
rows = len(height_map)
columns = len(height_map[0])
for i in range(rows):
    for j in range(columns):
        base_num = height_map[i][j] 
        low_point_flag = True
        for i_offset, j_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            adjecent_i = i + i_offset
            adjecent_j = j + j_offset
            if (not 0 <= adjecent_i <= rows - 1) or (not 0 <= adjecent_j <= columns - 1):
                continue
            elif (base_num >= height_map[adjecent_i][adjecent_j]):
                low_point_flag = False
                break
        if low_point_flag:
            basin_lst.append((i, j))

def traverse(point, basin_point_set, height_map):
    rows = len(height_map)
    columns = len(height_map[0])
    i, j = point
    if (point in basin_point_set) or (height_map[i][j] == 9):
        return basin_point_set
    basin_point_set.add(point)
    for i_offset, j_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        adjecent_i = i + i_offset
        adjecent_j = j + j_offset
        if (not 0 <= adjecent_i <= rows - 1) or (not 0 <= adjecent_j <= columns - 1):
            continue
        basin_point_set = traverse((adjecent_i, adjecent_j), basin_point_set, height_map)
    return basin_point_set
        
large_basin_lst = []
for basin in basin_lst:
    basin_point_set = traverse(basin, set(), height_map)
    basin_size = len(basin_point_set)
    large_basin_lst.append(basin_size)

large_basin_lst.sort()
print(large_basin_lst[len(large_basin_lst) - 3:])