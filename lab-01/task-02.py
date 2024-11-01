def bfs_shortest_path(graph, start, end):
    queue = [[start]]
    visited = []

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.append(node)
            new_paths = [path + [neighbor] for neighbor in graph.get(node, []) if neighbor not in visited]
            queue.extend(new_paths)

    return None


graph = {
    '1': ['2', '3', '5'],
    '2': ['1', '4'],
    '3': ['1', '5', '6'],
    '4': ['2', '7'],
    '5': ['1', '3', '7'],
    '6': ['3', '8'],
    '7': ['4', '5', '8'],
    '8': ['6', '7']
}

start_node = '1'
end_node = '7'
shortest_path = bfs_shortest_path(graph, start_node, end_node)
print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
