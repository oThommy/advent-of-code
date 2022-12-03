FILE_PATH = 'input.txt'

with open(FILE_PATH, 'r') as file:
    height_map = []
    for line in file:
        height_map.append([int(num) for num in line.split('\n')[0]])

low_point_lst = []
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
            low_point_lst.append(base_num)

print(sum(low_point_lst) + len(low_point_lst))