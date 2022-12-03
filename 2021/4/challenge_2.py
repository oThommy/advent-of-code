FILE_PATH = 'input.txt'

def mark_bingo_card(bingo_card, drawn_num):
    for i in range(5):
        for j in range(5):
            if (bingo_card[i][j][0] == drawn_num):
                bingo_card[i][j][1] = True
    return bingo_card

def validate_bingo_card(bingo_card):
    # horizontal checks
    for line in bingo_card:
        marked_lst = [marked for _, marked in line]
        if (all(marked_lst)):
            return True, sum_unmarked_nums(bingo_card)
        
    # vertical checks
    for j in range(5):
        bingo_flag = True
        for i in range(5):
            _, marked = bingo_card[i][j]
            if (not marked):
                bingo_flag = False
                break
        if bingo_flag:
            return True, sum_unmarked_nums(bingo_card)
    
    return False, 0

def sum_unmarked_nums(bingo_card):
    num_sum = 0
    for i in range(5):
        for j in range(5):
            num, marked = bingo_card[i][j]
            if (marked == False):
                num_sum += num
    return num_sum

with open(FILE_PATH, 'r') as file:
    correct_nums = list(map(int, file.readline().split(',')))
    file.readline()
    bingo_cards = file.read().split('\n\n')
    for index, bingo_card in enumerate(bingo_cards):
        bingo_cards[index] = bingo_card.split('\n')
        for i, line in enumerate(bingo_cards[index]):
            line_int_lst = []
            for j in range(1, len(line), 3):
                line_int_lst.append(int(line[j - 1] + line[j]))
            line_int_lst = [[num, False] for num in line_int_lst]
            bingo_cards[index][i] = line_int_lst
            
for drawn_num in correct_nums:    
    for index, bingo_card in enumerate(bingo_cards):
        if bingo_card == 'already won':
            continue
        bingo_cards[index] = mark_bingo_card(bingo_card, drawn_num)
        bingo_flag, num_sum = validate_bingo_card(bingo_cards[index])
        if bingo_flag:
            if (bingo_cards.count('already won') == len(bingo_cards) - 1):
                print(drawn_num, sum_unmarked_nums(bingo_card))
                print(drawn_num * sum_unmarked_nums(bingo_card))
            bingo_cards[index] = 'already won'