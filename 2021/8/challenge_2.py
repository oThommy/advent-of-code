import json

DISPLAY_MAP = {('top', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right'): 0,
               ('top_right', 'bottom_left'): 1,
               ('top', 'top_right', 'middle', 'bottom_left', 'bottom'): 2,
               ('top', 'top_right', 'middle', 'bottom_right', 'bottom'): 3,
               ('top_left', 'middle', 'top_right', 'bottom_right'): 4,
               ('top', 'top_left', 'middle', 'bottom_right', 'bottom'): 5,
               ('top', 'top_left', 'middle', 'bottom_right', 'bottom', 'bottom_left'): 6,
               ('top', 'top_right', 'bottom_left'): 7,
               ('top', 'middle', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right'): 8,
               ('top', 'top_left', 'top_right', 'middle', 'bottom_right', 'bottom'): 9}
DISPLAY_SEGMENTS = ('top', 'middle', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right')

signal = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split(' ')
count = 0
for a in range(7):
    for b in range(7):
        for c in range(7):
            for d in range(7):
                for e in range(7):
                    for f in range(7):
                        for g in range(7):
                            if (not len({a, b, c, d, e, f, g}) == 7):
                                continue
                            ch_map = {ch: DISPLAY_SEGMENTS[eval(ch)] for ch in 'abcdefg'}
                            number_set = set()
                            for pattern in signal:
                                segment_lst = []
                                for ch in pattern:
                                    segment_lst.append(ch_map[ch])
                                    
                                    
                                for key, val in DISPLAY_MAP.items():
                                    if (set(segment_lst) == set(key)):
                                        num = val
                                        break
                                number_set.add(num)
                            if (len(number_set) == 7):
                                for pattern in signal:
                                    if (len(pattern) in ['idek']):
                                        for ch in pattern:
                                            
# ch_map = 
for pattern in signal:
    pass

print(count)