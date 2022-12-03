FILE_PATH = 'input.txt'
DAYS = 80

with open(FILE_PATH, 'r') as file:
    fish_timers_lst = list(map(int, file.read().split(',')))
    
for _ in range(DAYS):
    new_fish_timers_lst = []
    new_fish_timers_count = 0
    for fish_timer in fish_timers_lst:
        new_fish_timer = fish_timer - 1
        if (new_fish_timer == -1):
            new_fish_timers_count += 1
            new_fish_timers_lst.append(6)
        else:
            new_fish_timers_lst.append(new_fish_timer)
    new_fish_timers_lst += [8 for _ in range(new_fish_timers_count)]
    fish_timers_lst = new_fish_timers_lst
    
answer = len(fish_timers_lst)
print(answer)

