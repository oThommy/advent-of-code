import json

segments = {0: 6,#
            1: 2,
            2: 5,#
            3: 5,#
            4: 4,
            5: 5,#
            6: 6,#
            7: 3,
            8: 7,
            9: 6}#
LEN_OPTIONS = {2: ['bottom_right', 'top_right'], # 1
                4: ['top_left', 'middle', 'top_right', 'bottom_right'], # 4
                3: ['top', 'top_right', 'bottom_right'], # 7
                7: ['top', 'middle', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right'], # 8
                5: ['top', 'middle', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right'], # 2, 3, 5
                6: ['top', 'middle', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right']} # 0, 6, 9


# signal_pattern = ['ab', 'dab']
signal_pattern = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab'.split(' ')

def is_substring(s, sub_str):
    for ch in sub_str:
        if (ch not in s):
            return False
    return True    

def set_to_str(str_set):
    output_str = ''
    for ch in str_set:
        output_str += ch
    return output_str

class InfoMap(dict):
    def is_done(self):
        keys = self.keys()
        for ch in 'abcdefg':
            if (ch not in keys) or (len(self[ch]) > 1):
                return False
        return True
        
info_map = InfoMap()
for pattern in signal_pattern:
    info_map[pattern] = LEN_OPTIONS[len(pattern)]

while (not info_map.is_done()):
    keys = tuple(info_map.keys())
    for index_offset, pattern in enumerate(keys):
        for index in range(index_offset + 1, len(keys)):
            sub_pattern = keys[index]
            if (set(pattern) == set(sub_pattern)):
                continue
            
            if (is_substring(pattern, sub_pattern)):
                new_pattern = set_to_str(set(pattern) - set(sub_pattern))
                
                
                
                
                # if (new_pattern == 'a'):
                #     print('hoi')
                #     print(pattern)
                #     print(sub_pattern)
                
                
                
                
                new_options = list(set(info_map[pattern]) - set(info_map[sub_pattern]))
                if (len(new_options) == 0):
                    pass
                elif (new_pattern not in keys):
                    info_map[new_pattern] = new_options
                elif (len(new_options) < len(info_map[new_pattern])):
                    info_map[new_pattern] = new_options
                    
                
            if (is_substring(sub_pattern, pattern)):
                new_pattern = set_to_str(set(sub_pattern) - set(pattern))
                new_options = list(set(info_map[sub_pattern]) - set(info_map[pattern]))
                if (len(new_options) == 0):
                    pass
                elif (new_pattern not in keys):
                    info_map[new_pattern] = new_options
                elif (len(new_options) < len(info_map[new_pattern])):
                    info_map[new_pattern] = new_options
    # while True:
    #     user_input = input('key: ')
    #     if (user_input == ''):
    #         break
    #     try:
    #         print(json.dumps(info_map[user_input], indent=4))
    #     except:
    #         print('couldnt find lol')
    # print(json.dumps(info_map, indent=4))
    print(json.dumps({x: y for x, y in info_map.items() if len(x) == 1}, indent=4))
    input()

print(json.dumps(info_map, indent=4))
print(info_map.is_done())
# print(list(map(lambda x: len(x), signal_pattern)))