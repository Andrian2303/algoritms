import sys
from queue import PriorityQueue

from graph import Graph


def dijkstra_algorithm(graph: Graph, start_index: int):
    distances = {vertex_index: sys.maxsize for vertex_index in graph.relations}
    distances[start_index] = 0

    available_vertexes_queue = PriorityQueue()
    available_vertexes_queue.put((0, start_index))

    if start_index not in graph.relations:
        raise ValueError('Unbounded graph (not found start index)')

    while not available_vertexes_queue.empty():
        parent_vertex = available_vertexes_queue.get()[1]

        for child_vertex_tuple in graph.relations[parent_vertex]:
            distance = distances[parent_vertex] + child_vertex_tuple[1]
            child_vertex_id = child_vertex_tuple[0]

            if distance < distances[child_vertex_id]:
                distances[child_vertex_id] = distance
                available_vertexes_queue.put((distance, child_vertex_id))

    return distances
