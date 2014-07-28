from path_search.performance_tests.test_data import graphs_test_data


def bellman_ford(graph, start, end):
    graph_state = {element: None for element in graph.keys()}
    graph_state[start] = (None, None)

    for i in range(len(graph.keys()) - 1):
        for el in graph_state.keys():
            if graph_state[el]:
                for link_index, weight in graph[el]:
                    curr_element_weight = graph_state[el][1] if graph_state[el][1] else 0
                    if not graph_state[link_index] or (graph_state[link_index][1] is not None and graph_state[link_index][1] > curr_element_weight + weight):
                        graph_state[link_index] = (el, curr_element_weight + weight)

    for el in graph_state.keys():
        if graph_state[el]:
            for link_index, weight in graph[el]:
                curr_element_weight = graph_state[el][1] if graph_state[el][1] else 0
                if not graph_state[link_index] or (graph_state[link_index][1] is not None and graph_state[link_index][1] > curr_element_weight + weight):
                    return False

    path = []
    path_el = end
    while path_el:
        path.append(path_el)
        path_el = graph_state[path_el][0]
    return path


def relax_edges():
    pass


bellman_ford(**graphs_test_data['ordered_weighted'])