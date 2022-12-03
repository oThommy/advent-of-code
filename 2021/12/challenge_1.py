FILE_PATH = 'input.txt'

with open(FILE_PATH, 'r') as file:
    graph = {}
    for line in file:
        node, adjecent_node = line.strip().split('-')
        graph[node] = graph.get(node, []) + [adjecent_node]
        
new_graph = graph.copy()
for node, adjecent_node_lst in graph.items():
    for adjecent_node in adjecent_node_lst:
        if (node in new_graph.get(adjecent_node, [])):
            continue
        new_graph[adjecent_node] = new_graph.get(adjecent_node, []) + [node]

def traverse(graph, path):
    count = 0
    current_node = path[-1]
    # print(f'path: {path}')
    for adjecent_node in graph[current_node]:
        # print(f'current_node: {current_node} en adjecent_node: {adjecent_node} en current path: {path}')
        if (adjecent_node == 'start'):
            # print('found start, returning 0...')
            continue
        elif (adjecent_node.islower() and adjecent_node in path):
            # print('found small cave twice, returning 0...')
            continue
        elif (adjecent_node == 'end'):
            # print('found end, returning 1...')
            count += 1
            continue
        # print('ik ga door...')
        count += traverse(graph, path + [adjecent_node])
            
    return count

print(traverse(new_graph, ['start']))