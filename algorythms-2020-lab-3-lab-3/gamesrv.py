from info import get_info, print_info
from dijkstra import dijkstra_algorithm


def main():
    n, m, clients, graph = get_info('exmp/in-1')
    latency = None

    for vertex_index in graph.relations:
        if vertex_index not in clients:
            current_latencies = dijkstra_algorithm(graph, vertex_index)
            current_max_latency = max([current_latencies[client] for client in clients])
            if latency is None:
                latency = current_max_latency
            elif current_max_latency < latency:
                latency = current_max_latency

    print_info('exmp/out-1', latency)

    return latency


if __name__ == '__main__':
    print(main())
