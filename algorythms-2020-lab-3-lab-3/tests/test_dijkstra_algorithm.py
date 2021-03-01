import unittest

from dijkstra import dijkstra_algorithm
from graph import Graph


class DijkstraTest(unittest.TestCase):
    def setUp(self) -> None:
        self.first_graph = Graph()
        self.first_graph.add_edges_from_vertexes(1, 3, 10)
        self.first_graph.add_edges_from_vertexes(3, 4, 80)
        self.first_graph.add_edges_from_vertexes(4, 5, 50)
        self.first_graph.add_edges_from_vertexes(5, 6, 20)
        self.first_graph.add_edges_from_vertexes(2, 3, 40)
        self.first_graph.add_edges_from_vertexes(2, 4, 100)

    def test_dijkstra_algorithm(self):
        self.assertRaises(ValueError, dijkstra_algorithm, self.first_graph, 0)
        self.assertEqual({1: 0, 3: 10, 4: 90, 5: 140, 6: 160, 2: 50},
                         dijkstra_algorithm(self.first_graph, 1))
        self.assertEqual({1: 50, 3: 40, 4: 100, 5: 150, 6: 170, 2: 0},
                         dijkstra_algorithm(self.first_graph, 2))
        self.assertEqual({1: 10, 3: 0, 4: 80, 5: 130, 6: 150, 2: 40},
                         dijkstra_algorithm(self.first_graph, 3))
        self.assertEqual({1: 90, 3: 80, 4: 0, 5: 50, 6: 70, 2: 100},
                         dijkstra_algorithm(self.first_graph, 4))
        self.assertEqual({1: 140, 3: 130, 4: 50, 5: 0, 6: 20, 2: 150},
                         dijkstra_algorithm(self.first_graph, 5))
        self.assertEqual({1: 160, 3: 150, 4: 70, 5: 20, 6: 0, 2: 170},
                         dijkstra_algorithm(self.first_graph, 6))


if __name__ == '__main__':
    unittest.main()
