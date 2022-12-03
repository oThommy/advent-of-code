test = {8: 43,
        7: 30,
        6: 20,
        5: 29,
        4: 3,
        3: 49,
        2: 13,
        1: 14,
        0: 1}
print({num - 1: test[num] for num in range(8, -1, -1)})