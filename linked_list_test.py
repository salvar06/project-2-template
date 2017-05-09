import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

list1 = Pair(1,Pair(2,Pair(3,Pair(4, None))))
list2 = Pair(4,Pair(2,Pair(1,Pair(3, None))))
list3 = Pair(2,Pair(3,Pair(1,Pair(4, None))))
list4 = Pair(1, Pair(-1, Pair(100, Pair(2, None))))
list5 = Pair(-1, Pair(1, Pair(2, Pair(100, None))))




class testCase(unittest.TestCase):

    def test_repr(self):
        self.assertEqual(repr(None), "None")
        self.assertEqual(repr(Pair(0, None)), 'Pair(0, None)')
        self.assertEqual(repr(Pair(0, Pair(1, None))), 'Pair(0, Pair(1, None))')

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add(self):
        self.assertRaises(IndexError, add, None, 1, 'first')
        self.assertRaises(IndexError, add, Pair(1, None), -1, 'last')
        self.assertEqual(add(None, 0, 1), Pair(1, None))
        self.assertEqual(add(Pair(1, None), 0, 'first'), Pair('first', Pair(1, None)))
        self.assertEqual(add(Pair(1, Pair('two', None)), 1, 'second'), Pair(1, Pair('second', Pair('two', None))))
        self.assertEqual(add(Pair(1, Pair('two', None)), 2, 3), Pair(1, Pair('two', Pair(3, None))))
        self.assertRaises(IndexError, add, Pair(1, None), 2, 2)

    def test_length(self):
        self.assertEqual(length(None), 0)
        self.assertEqual(length(Pair(0, Pair('a', Pair([], None)))), 3)
        self.assertEqual(length(Pair(0, Pair(Pair(1, None), None))), 2)

    def test_get(self):
        self.assertRaises(IndexError, get, None, 1)
        self.assertRaises(IndexError, get, None, 0)
        self.assertRaises(IndexError, get, Pair(1, None), -1)
        self.assertRaises(IndexError, get, Pair(1, None), 2)
        self.assertEqual(get(Pair(1, None), 0), 1)
        self.assertEqual(get(Pair(1, Pair('two', None)), 1), 'two')
        self.assertEqual(get(Pair(1, Pair('two', Pair(3, None))), 2), 3)

    def test_set(self):
        self.assertRaises(IndexError, set, None, 1, 1)
        self.assertRaises(IndexError, set, None, 0, 1)
        self.assertRaises(IndexError, set, Pair(1, None), -1, 2)
        self.assertRaises(IndexError, set, Pair(1, None), 2, 2)
        self.assertEqual(set(Pair(1, None), 0, 'a'), Pair('a', None))
        self.assertEqual(set(Pair(1, Pair(2, None)), 1, 'a'), Pair(1, Pair('a', None)))

    def test_remove(self):
        self.assertRaises(IndexError, remove, Pair(1, None), -1)
        self.assertRaises(IndexError, remove, Pair(1, None), 1)
        self.assertRaises(IndexError, remove, None, 0)
        self.assertRaises(IndexError, remove, None, 1)
        self.assertEqual(remove(Pair(1, None), 0), (1, None))
        self.assertEqual(remove(Pair(0, Pair(1, None)), 1), (1, Pair(0, None)))

    def test_sort(self):
        self.assertEqual(sort(list2, comparator), list1)
        self.assertEqual(sort(list1, comparator), list1)
        self.assertEqual(sort(list3, comparator), list1)
        self.assertEqual(sort(list4, comparator), list5)

    def test_insert(self):
        self.assertEqual(insert(None, 0, comparator), Pair(0, None))
        self.assertEqual(insert(Pair(0, None), 1, comparator), Pair(0, Pair(1, None)))
        self.assertEqual(insert(Pair(0, Pair(1, Pair(2, Pair(3, None)))), 2, comparator), Pair(0 , Pair(1, Pair(2, Pair(2, Pair(3, None))))))
        self.assertEqual(insert(Pair(0, None), -1, comparator), Pair(-1, Pair(0, None)))

    def test_comparator(self):
        self.assertEqual(comparator(0,1), False)
        self.assertEqual(comparator(1,1), False)
        self.assertEqual(comparator(1,0), True)
        self.assertEqual(comparator(-1,1), False)


if __name__ == '__main__':
    unittest.main()
