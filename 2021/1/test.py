num_lst = []

with open('input.txt', 'r') as file:
    for line in file:
        num_lst.append(int(line))
        
print(num_lst)