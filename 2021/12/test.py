def is_valid_path(path):
    path = [node for node in path if node.islower()]
    node_count_dict = {node: 0 for node in path}
    for node in path:
        node_count_dict[node] += 1
        if (node_count_dict[node] > 2):
            return False
    print(list(node_count_dict.values()))
    print(list(node_count_dict.values()).count(2))
    return list(node_count_dict.values()).count(2) <= 1

print(is_valid_path(['start', 'A', 'c', 'A', 'b', 'd', 'b']))