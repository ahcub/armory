
def wave(graph, start, end):
    """
    :param graph: dictionary that represents unweighted, ordered graph where keys are vertex indexes
    and values is list of connections of current vertex with others
    example: {
        1: [4],
        2: [3],
        3: [2, 4, 7],
        4: [1, 3, 8],
        5: [3, 6],
        6: [5, 10],
    }
    :param start: index of vertex from what you want to find path
    :param end: index of vertex to what you want to find path
    :return: list of elements in shortest path from start index to end index
    if path don't exists an empty list will be returned
    """

    graph_state = {element: None for element in graph.keys()}
    graph_state[start] = 0
    recently_changed_elements = [start]
    new_recently_changed_elements = []
    while not graph_state[end] and recently_changed_elements:
        for el in recently_changed_elements:
            for link in graph[el]:
                if link in graph_state and graph_state[link] is None:
                    graph_state[link] = el
                    new_recently_changed_elements.append(link)
        recently_changed_elements = new_recently_changed_elements
        new_recently_changed_elements = []

    path = []
    path_el = end
    while path_el:
        path.append(path_el)
        path_el = graph_state[path_el]

    return path[::-1]