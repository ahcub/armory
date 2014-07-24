
def wave(graph, start, end):
    graph_state = {element: 0 for element in graph.keys()}
    graph_state[start] = -1
    recently_changed_elements = [start]
    new_recently_changed_elements = []
    while not graph_state[end] and recently_changed_elements:
        for el in recently_changed_elements:
            for link in graph[el]:
                if link in graph_state and not graph_state[link]:
                    graph_state[link] = el
                    new_recently_changed_elements.append(link)
        recently_changed_elements = new_recently_changed_elements
        new_recently_changed_elements = []

    path = []
    path_el = end
    while path_el != -1:
        path.append(path_el)
        path_el = graph_state[path_el]

    return path[::-1]