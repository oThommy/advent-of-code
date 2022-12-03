FILE_PATH = 'input.txt'
OPENING_CH = {'(', '[', '{', '<'}
CLOSING_CH = {')', ']', '}', '>'}
OPEN_CLOSE_MAP = {'(': ')',
                  '[': ']',
                  '{': '}',
                  '<': '>'}
CH_POINTS = {')': 3,
             ']': 57,
             '}': 1197,
             '>': 25137}

total_points = 0

with open(FILE_PATH, 'r') as file:
    for index, line in enumerate(file):
        stack = []
        first_illegal_ch = ''
        for ch in line:
            if (ch in OPENING_CH):
                stack.append(ch)
            elif (ch in CLOSING_CH):
                opening_ch = stack.pop()
                if (OPEN_CLOSE_MAP[opening_ch] == ch):
                    continue
                elif (not first_illegal_ch):
                    first_illegal_ch = ch
                
                if (ch == first_illegal_ch):
                    total_points += CH_POINTS[ch]
        print(index, total_points)

print(total_points )