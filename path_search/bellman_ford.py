
def bellman_ford(graph, start, end):
    graph_state = {element: None for element in graph.keys()}
    graph_state[start] = (None, 0)

    for i in range(len(graph.keys()) - 1):
        for vertex_index, vertex_relaxed_info in get_edges_can_be_relaxed(graph, graph_state):
            graph_state[vertex_index] = vertex_relaxed_info

    for _, _ in get_edges_can_be_relaxed(graph, graph_state):
        return []

    path = []
    path_el = end
    while path_el is not None and graph_state[path_el] is not None:
        path.append(path_el)
        path_el = graph_state[path_el][0]

    return path[::-1]


def get_edges_can_be_relaxed(graph, graph_state):
    for el, data in graph_state.items():
        if data is not None:
            for index, weight in graph[el]:
                if graph_state[index] is None or graph_state[index][1] > data[1] + weight:
                    yield index, (el, data[1] + weight)