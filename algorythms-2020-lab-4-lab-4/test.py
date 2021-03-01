import unittest
from ijones import get_paths_number


class IJonesTest(unittest.TestCase):

    def test_get_paths_number(self):
        self.assertEqual(get_paths_number('exmp/in-1'), 5)

    def test_get_paths_number2(self):
        self.assertEqual(get_paths_number('exmp/in-2'), 2)

    def test_get_paths_number3(self):
        self.assertEqual(get_paths_number('exmp/in-3'), 201684)

        print('Tests passed, covering the basic logic of the task')


if __name__ == '__main__':
    unittest.main()
