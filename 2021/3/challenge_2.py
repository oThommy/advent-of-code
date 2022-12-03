import copy

file_path = 'input.txt'
bit_len = len('011101101110')

# file_path = 'test_input.txt'
# bit_len = len('00100')

input_bit_oxygen_lst = []
with open(file_path, 'r') as file:
    input_bit_oxygen_lst = file.read().split('\n')
input_bit_co2_lst = copy.copy(input_bit_oxygen_lst)
    
for i in range(bit_len):
    if len(input_bit_oxygen_lst) == 1:
        break
    
    count_0 = 0
    count_1 = 0
    for input_bit in input_bit_oxygen_lst:
        exec(f'count_{input_bit[i]} += 1')
    if count_1 >= count_0:
        input_bit_oxygen_lst = [input_bit for input_bit in input_bit_oxygen_lst if input_bit[i] == '1']
    elif count_1 < count_0:
        input_bit_oxygen_lst = [input_bit for input_bit in input_bit_oxygen_lst if input_bit[i] == '0']
        
for i in range(bit_len):
    if len(input_bit_co2_lst) == 1:
        break
    
    count_0 = 0
    count_1 = 0
    for input_bit in input_bit_co2_lst:
        exec(f'count_{input_bit[i]} += 1')
    if count_0 <= count_1:
        input_bit_co2_lst = [input_bit for input_bit in input_bit_co2_lst if input_bit[i] == '0']
    elif count_0 > count_1:
        input_bit_co2_lst = [input_bit for input_bit in input_bit_co2_lst if input_bit[i] == '1']
        
oxygen_rate = int(input_bit_oxygen_lst[0], base=2)
co2_rate = int(input_bit_co2_lst[0], base=2)
life_support_rate = oxygen_rate * co2_rate
print(life_support_rate)