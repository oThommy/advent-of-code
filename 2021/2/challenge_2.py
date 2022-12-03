horizontal_pos = 0
depth = 0
aim = 0
with open('input.txt', 'r') as f:
    for line in f:
        cmd, x = line.split(' ')
        x = int(x)
        if cmd == 'down':
            aim += x
        elif cmd == 'up':
            aim -= x
        elif cmd == 'forward':
            horizontal_pos += x
            depth += aim * x

print(f'horizontal position: {horizontal_pos}')
print(f'              depth: {depth}')
print(f'                aim: {aim}')
print(f'         multiplied: {horizontal_pos * depth}')