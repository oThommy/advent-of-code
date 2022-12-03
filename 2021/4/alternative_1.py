import sys
FILE_PATH = 'test_input.txt'

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
            return True, sum(num for num, _ in line)
        
    # vertical checks
    for j in range(5):
        num_sum = 0
        bingo_flag = True
        for i in range(5):
            num, marked = bingo_card[i][j]
            if (not marked):
                bingo_flag = False
                break
            num_sum += num
        if bingo_flag:
            return True, num_sum
    
    return False, 0

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
        bingo_cards[index] = mark_bingo_card(bingo_card, drawn_num)
        bingo_flag, num_sum = validate_bingo_card(bingo_cards[index])
        if bingo_flag:
            print(num_sum, drawn_num)
            print(num_sum * drawn_num)
            sys.exit(0)
    # print(drawn_num)
    # for bingo_card in bingo_cards:
    #     for line in bingo_card:
    #         print(line)
    #     print('')
    # input()

# test = [[[3, False], [15, False], [0, False], [2, False], [22, False]],
#         [[9, False], [18, False], [13, False], [17, False], [5, False]],
#         [[19, False], [8, False], [7, False], [25, False], [23, False]],
#         [[20, False], [11, False], [10, False], [24, False], [4, False]],
#         [[14, False], [21, False], [16, False], [12, False], [6, False]]]
# print(mark_bingo_card(test, 7))
    
# # print(correct_nums)
# # print(bingo_cards)
# for bingo_card in bingo_cards:
#     print(bingo_card)
#     print('')
    
# # test = [[(14, True), (21, True), (17, False), (24, False), (4, False)],
# #         [(10, True), (16, True), (15, False), (9, False), (19, False)], 
# #         [(18, True), (8, True), (23, False), (26, False), (20, False)],
# #         [(22, True), (11, True), (13, False), (6, False), (5, False)], 
# #         [(2, False), (0, True), (12, True), (3, True), (7, True)]]
# test = [[[14, False], [21, False], [17, False], [24, False], [4, False]], 
#         [[10, False], [16, False], [15, False], [9, False], [19, False]],
#         [[18, False], [8, False], [23, False], [26, False], [20, False]],
#         [[22, False], [11, False], [13, False], [6, False], [5, False]], 
#         [[2, False], [0, False], [12, False], [3, False], [7, False]]]
# for line in mark_bingo_card(test, 7):
#     print(line)
