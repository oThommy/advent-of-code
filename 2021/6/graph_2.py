import matplotlib.pyplot as plt

DAYS = 80
INITIAL_SIZE = 4

x_lst = range(1, DAYS + 1)
y_lst = list(False for _ in range(DAYS))
y_lst[0] = INITIAL_SIZE
for index, x in enumerate(x_lst):
    if (index == 0):
        continue
    
    y_lst[index] = 1.23**((x % 3) + (x % 6) + (x % 2)) # y_lst[index - 1] + 

plt.plot(x_lst, y_lst)