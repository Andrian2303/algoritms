class Graph:

    def __init__(self):
        self.relations = {}

    def __add_edge(self, vertex_from: int, vertex_to: int, weight: int):
        if vertex_from in self.relations.keys():
            if (vertex_to, weight) not in self.relations[vertex_from]:
                self.relations[vertex_from].append((vertex_to, weight))

        else:
            self.relations[vertex_from] = [(vertex_to, weight)]

    def add_edges_from_vertexes(self, first_vertex: int, second_vertex: int, weight: int):
        self.__add_edge(first_vertex, second_vertex, weight)
        self.__add_edge(second_vertex, first_vertex, weight)

    def print_graph(self):
        for element in self.relations:
            print(element, self.relations[element])
