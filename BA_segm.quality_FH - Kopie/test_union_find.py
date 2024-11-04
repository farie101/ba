import unittest
from union_find import UnionFind


class TestUnionFind(unittest.TestCase):

    def setUp(self):
        self.union = UnionFind(10)

    def test_nothing_connected(self):
        self.assertFalse(self.union.connected(0, 1))
        self.assertFalse(self.union.connected(2, 3))

    def test_union_and_connected(self):
        # Test union and connection logic
        self.union.union(0, 1)
        self.assertTrue(self.union.connected(0, 1))
        self.assertEqual(self.union.find(0),self.union.find(1))
        self.union.union(1, 2)
        self.assertTrue(self.union.connected(0, 2))
        self.assertFalse(self.union.connected(0, 3))

    def test_multiple_unions(self):
        def test_union_with_multiple_groups(self):
            self.union.union(3, 4)
            self.assertTrue(self.union.connected(3, 4))
            self.assertFalse(self.union.connected(0, 3))

            self.union.union(2, 3)
            self.assertTrue(self.union.connected(0, 4))

    def test_multiple_unions(self):
        self.union.union(4, 3)
        self.union.union(3, 0)
        self.union.union(1,2)
        self.union.union(1,3)
        self.union.connected(2,4)
        print(self.union.find(5))


if __name__ == '__main__':
    unittest.main()