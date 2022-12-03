FILE_PATH = 'input.txt'
OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def is_valid_coord(i, j, max_i, max_j):
    return (0 <= i <= max_i) and (0 <= j <= max_j)

with open(FILE_PATH, 'r') as file:
    energy_lst = []
    for line in file:
        line = line.split('\n')[0]
        energy_lst.append([int(num) for num in line])

max_i = len(energy_lst) - 1
max_j = len(energy_lst[0]) - 1
size = len(energy_lst) * len(energy_lst[0])  
step = 0

while True:
    # new step
    step += 1
    flash_count = 0
    
    # increment every energy level by 1
    for i, _ in enumerate(energy_lst):
        for j, _ in enumerate(energy_lst[0]):
            energy_lst[i][j] += 1
                
    # make octopuses flash
    while True:
        flash_flag = False
        
        for i, _ in enumerate(energy_lst):
            for j, _ in enumerate(energy_lst[0]):
                # octopus doesn't flash
                if (energy_lst[i][j] <= 9):
                    continue
                
                # octopus does flash
                energy_lst[i][j] = 0
                flash_flag = True
                flash_count += 1
                
                for i_offset, j_offset in OFFSETS:
                    adjecent_i = i + i_offset
                    adjecent_j = j + j_offset
                    if (not is_valid_coord(adjecent_i, adjecent_j, max_i, max_j)):
                        continue
                    elif (energy_lst[adjecent_i][adjecent_j] == 0):
                        continue
                    energy_lst[adjecent_i][adjecent_j] += 1
        
        if (not flash_flag):
            break
        
    if (flash_count == size):
        print(step)
        break