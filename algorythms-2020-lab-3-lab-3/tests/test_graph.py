import unittest

from graph import Graph


class GraphTest(unittest.TestCase):
    def setUp(self) -> None:
        self.first_graph = Graph()
        self.first_graph.add_edges_from_vertexes(1, 2, 10)
        self.first_graph.add_edges_from_vertexes(1, 3, 20)
        self.first_graph.add_edges_from_vertexes(2, 3, 5)

        self.second_graph = Graph()
        self.second_graph.add_edges_from_vertexes(1, 2, 20)
        self.second_graph.add_edges_from_vertexes(2, 3, 70)
        self.second_graph.add_edges_from_vertexes(3, 5, 40)
        self.second_graph.add_edges_from_vertexes(4, 1, 30)
        self.second_graph.add_edges_from_vertexes(5, 2, 90)
        self.second_graph.add_edges_from_vertexes(5, 4, 10)

    def test_graph_vertexes(self):
        self.assertEqual([1, 2, 3], list(self.first_graph.relations.keys()))
        self.assertEqual([1, 2, 3, 5, 4], list(self.second_graph.relations.keys()))

    def test_graphs_relations(self):
        self.assertEqual(
            {1: [(2, 10), (3, 20)],
             2: [(1, 10), (3, 5)],
             3: [(1, 20), (2, 5)]},
            self.first_graph.relations
        )

        self.assertEqual(
            {1: [(2, 20), (4, 30)],
             2: [(1, 20), (3, 70), (5, 90)],
             3: [(2, 70), (5, 40)],
             4: [(1, 30), (5, 10)],
             5: [(3, 40), (2, 90), (4, 10)]},
            self.second_graph.relations
        )


if __name__ == '__main__':
    unittest.main()
