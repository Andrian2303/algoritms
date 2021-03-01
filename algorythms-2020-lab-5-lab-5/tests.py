import unittest
from rabin_karp_algorithm import search_pattern


class RabinKarpAlgo(unittest.TestCase):
    def test_rabin_karp(self):
        self.assertEqual(search_pattern("26", "3141592653589793", 130, 256), [('6', '7')])
        self.assertEqual(search_pattern("xx", "xxxxx", 131, 256),
                         [('0', '1'), ('1', '2'), ('2', '3'), ('3', '4')])
        self.assertEqual(search_pattern("ABC", "abcABCaBcCAB", 131, 256), [('3', '5')])
        self.assertEqual(search_pattern("it", "just do it, do it!", 131, 256), [('8', '9'), ('15', '16')])
        self.assertEqual(search_pattern("0", "123456789", 131, 256), [])

        # example with Cyrillic and Latin
        self.assertEqual(search_pattern("АСAB", "ACABDАСAB", 131, 256), [('5', '8')])

    def test_empty_string(self):
        self.assertEqual(search_pattern("2", "", 131, 256), [])
        self.assertEqual(search_pattern("", "123654", 131, 256), [])
