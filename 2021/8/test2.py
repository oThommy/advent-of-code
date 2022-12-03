x = set(['top', 'middle', 'bottom', 'top_left', 'bottom_left', 'top_right', 'bottom_right'])
y = set(['top', 'top_right', 'bottom_right'])
print(list(x-y))

# while (not info_map.is_done()):
#     keys = tuple(info_map.keys())
#     for index_offset, pattern in enumerate(keys):
#         for index in range(index_offset + 1, len(keys)):
#             sub_pattern = keys[index]
#             if (not is_substring(pattern, sub_pattern)):
#                 continue
#             new_pattern = set_to_str(set(pattern) - set(sub_pattern))
#             info_map[new_pattern] = list(set(info_map[pattern]) - set(info_map[sub_pattern]))
#     print(json.dumps(info_map, indent=4))
#     input()