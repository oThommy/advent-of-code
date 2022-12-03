FILE_PATH = 'input.txt'
OPENING_CH = {'(', '[', '{', '<'}
CLOSING_CH = {')', ']', '}', '>'}
OPEN_CLOSE_MAP = {'(': ')',
                  '[': ']',
                  '{': '}',
                  '<': '>'}
CH_POINTS = {')': 1,
             ']': 2,
             '}': 3,
             '>': 4}

trailing_str_lst = []
with open(FILE_PATH, 'r') as file:
    for line in file:
        stack = []
        illegal_flag = False
        for ch in line:
            if (ch in OPENING_CH):
                stack.append(ch)
            elif (ch in CLOSING_CH):
                opening_ch = stack.pop()
                if (OPEN_CLOSE_MAP[opening_ch] == ch):
                    continue
                illegal_flag = True
                break

        if illegal_flag:
            continue
        trailing_str_lst.append(stack)

for index, stack in enumerate(trailing_str_lst):
    trailing_str = [OPEN_CLOSE_MAP[opening_ch] for opening_ch in stack[::-1]]
    score = 0
    for ch in trailing_str:
        score *= 5
        score += CH_POINTS[ch]
    trailing_str_lst[index] = score
    
trailing_str_lst.sort()
print(trailing_str_lst[(len(trailing_str_lst) - 1) // 2])
# import json
# print(json.dumps([''.join(lst) for lst in trailing_str_lst], indent=4))