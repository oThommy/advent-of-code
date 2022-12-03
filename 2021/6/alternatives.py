FILE_PATH = 'test_input.txt'
DAYS = 256

with open(FILE_PATH, 'r') as file:
    fish_timers_lst = list(map(int, file.read().split(',')))
    fish_timers_dict = {timer_num: fish_timers_lst.count(timer_num) for timer_num in range(9)}
    
for _ in range(DAYS):
    print(_)
    new_fish_counter = 0
    for index, fish_timer in enumerate(fish_timers_lst):
        new_fish_timer = fish_timer - 1
        if (new_fish_timer == -1):
            fish_timers_lst[index] = 6
            new_fish_counter += 1
        else:
            fish_timers_lst[index] = new_fish_timer
    fish_timers_lst += [8 for _ in range(new_fish_counter)]
    
answer = len(fish_timers_lst)
print(answer)


