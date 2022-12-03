file_contents = ''
with open('input.txt', 'r') as f:
    file_contents = f.read()
horizontal_pos = 0
depth = 0
for old_str, new_str in [('forward', 'horizontal_pos +='),
                         ('up', 'depth -='),
                         ('down', 'depth +=')]:
    file_contents = file_contents.replace(old_str, new_str)
exec(file_contents)
print(f'horizontal position: {horizontal_pos}')
print(f'              depth: {depth}')
print(f'         multiplied: {horizontal_pos * depth}')