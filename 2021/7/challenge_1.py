FILE_PATH = 'test_input.txt'
MAX_OFFSET = 1000

with open(FILE_PATH, 'r') as file:
    positions_lst = list(map(int, file.read().split(',')))
    
min_fuel = float('Inf')
mean_position = round(sum(positions_lst) / len(positions_lst))
for new_position in range(mean_position, mean_position + MAX_OFFSET + 1, 1):
    fuel_sum = 0
    for position in positions_lst:
        fuel_sum += abs(position - new_position)
    if (fuel_sum < min_fuel):
        print(new_position, min_fuel)
        min_fuel = fuel_sum

for new_position in range(mean_position - 1, mean_position - MAX_OFFSET - 1, -1):
    fuel_sum = 0
    for position in positions_lst:
        fuel_sum += abs(position - new_position)
    if (fuel_sum < min_fuel):
        print(new_position, min_fuel)
        min_fuel = fuel_sum
        
print(min_fuel)