# import json
# from math import factorial

# PERMUTATIONS = 3

# range_lst = list(range(PERMUTATIONS))
# permutation_lst = []
# for i in range(factorial(PERMUTATIONS)):
#     permutation_lst.append([i % 3, i % 2, i % 1])
    
# # print(json.dumps(permutation_lst, indent=4))
# for lst in permutation_lst:
#     print(*lst, sep=', ')

import math

for i in range(1, 7):
    print(round(i / 2))