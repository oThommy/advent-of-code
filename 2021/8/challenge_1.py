FILE_PATH = 'input.txt'

with open(FILE_PATH, 'r') as file:
    signal_pattern_lst = []
    digit_output_lst = []
    for line in file:
        signal_pattern, digit_output = line.split(' | ')
        signal_pattern_lst.append(signal_pattern.split(' '))
        digit_output_lst.append(digit_output.strip().split(' '))

count = 0
for digit_output in digit_output_lst:
    for digit in digit_output:
        if (len(digit) in [2, 4, 3, 7]):
            count += 1
            
print(count)