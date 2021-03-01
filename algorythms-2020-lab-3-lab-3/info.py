from graph import Graph


def get_info(file_name: str):
    graph = Graph()
    with open(file_name, 'r') as file:
        lines = file.readlines()
        n, m = tuple(int(x) for x in lines[0].split())
        clients = tuple(int(x) for x in lines[1].split())
        for line in lines[2:]:
            start, end, weight = tuple(int(x) for x in line.split())
            graph.add_edges_from_vertexes(start, end, weight)

    return n, m, clients, graph


def print_info(file_name, info):
    info = str(info)
    with open(file_name, 'w') as file:
        file.write(info)
