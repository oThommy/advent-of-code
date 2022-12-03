file_path = 'input.txt'
bit_len = len('011101101110')

# file_path = 'test_input.txt'
# bit_len = len('00100')

with open(file_path, 'r') as file:
    count_bit_lst = [[0, 0] for _ in range(bit_len)]
    for line in file:
        line = line.split('\n')[0]
        for index, bit in enumerate(line):
            count_bit_lst[index][int(bit)] += 1
    
gamma_rate = ''
epsilon_rate = ''            
for count_0, count_1 in count_bit_lst:
    if (count_0 > count_1):
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'
gamma_rate = int(gamma_rate, base=2)
epsilon_rate = int(epsilon_rate, base=2)
answer = gamma_rate * epsilon_rate
print(f'  gamma rate: {gamma_rate}')
print(f'epsilon rate: {epsilon_rate}')
print(f'      answer: {answer}')