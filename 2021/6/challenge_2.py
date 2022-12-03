FILE_PATH = 'input.txt'
DAYS = 256

with open(FILE_PATH, 'r') as file:
    fish_timers_lst = list(map(int, file.read().split(',')))
    fish_timers_dict = {timer_num: fish_timers_lst.count(timer_num) for timer_num in range(9)}
    
for _ in range(DAYS):
    # print(_)
    new_fish_timers_dict = {timer_num - 1: fish_timers_dict[timer_num] for timer_num in range(8, 0, -1)}
    new_fish_timers_dict[8] = fish_timers_dict[0]
    new_fish_timers_dict[6] += fish_timers_dict[0]
    fish_timers_dict = new_fish_timers_dict
    # print(fish_timers_dict)
    
answer = sum(fish_timers_dict.values())
print(answer)


