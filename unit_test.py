import unittest
from typed_list import TypedList

class TypedListTest(unittest.TestCase):
    def setUp(self):
        self.lst = TypedList()

    def test_length_empty(self):
        self.assertEqual(self.lst.get_length(), 0)

    def test_length_nonempty(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        self.assertEqual(self.lst.get_length(), 4)

    def test_append(self):
        self.lst.append('A')
        self.lst.append('B')
        self.assertEqual(self.lst.get_length(), 2)
        self.assertEqual(self.lst.get(0), 'A')
        self.assertEqual(self.lst.get(1), 'B')

    def test_insert_valid_index(self):
        self.lst.append('A')
        self.lst.insert('B', 0)
        self.assertEqual(self.lst.get_length(), 2)
        self.assertEqual(self.lst.get(0), 'B')
        self.assertEqual(self.lst.get(1), 'A')

    def test_insert_invalid_index(self):
        self.lst.append('A')
        with self.assertRaises(ValueError):
            self.lst.insert('X', 2)

    def test_delete_valid_index(self):
        self.lst.append('A')
        self.lst.append('B')
        deleted_item = self.lst.delete(0)
        self.assertEqual(deleted_item, 'A')
        self.assertEqual(self.lst.get_length(), 1)
        self.assertEqual(self.lst.get(0), 'B')

    def test_delete_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.delete(0)

    def test_deleteAll(self):
        self.lst = TypedList()
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.lst.deleteAll('A')
        self.assertEqual(self.lst.get_length(), 1)
        self.assertEqual(self.lst.get(0), 'B')

    def test_get_valid_index(self):
        self.lst.append('A')
        self.lst.append('B')
        item = self.lst.get(1)
        self.assertEqual(item, 'B')

    def test_get_invalid_index(self):
        with self.assertRaises(IndexError):
            self.lst.get(0)

    def test_clone(self):
        self.lst.append('A')
        self.lst.append('B')
        cloned_list = self.lst.clone()
        self.assertIsNot(cloned_list, self.lst)
        self.assertEqual(cloned_list.get_length(), self.lst.get_length())
        self.assertEqual(cloned_list.get(0), self.lst.get(0))
        self.assertEqual(cloned_list.get(1), self.lst.get(1))

    def test_reverse(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        self.lst.reverse()
        self.assertEqual(self.lst.get(0), 'C')
        self.assertEqual(self.lst.get(1), 'B')
        self.assertEqual(self.lst.get(2), 'A')

    def test_findFirst_existing_element(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        index = self.lst.findFirst('A')
        self.assertEqual(index, 0)

    def test_findFirst_nonexisting_element(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        index = self.lst.findFirst('D')
        self.assertEqual(index, -1)

    def test_findLast_existing_element(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        index = self.lst.findLast('A')
        self.assertEqual(index, 2)

    def test_findLast_nonexisting_element(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        index = self.lst.findLast('D')
        self.assertEqual(index, -1)

    def test_clear(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.clear()
        self.assertEqual(self.lst.get_length(), 0)

    def test_extend(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.extend(['C', 'D'])
        self.assertEqual(self.lst.get_length(), 4)
        self.assertEqual(self.lst.get(2), 'C')
        self.assertEqual(self.lst.get(3), 'D')
    
    def test_insert_invalid_negative_index(self):
        self.lst.append('A')
        with self.assertRaises(ValueError):
            self.lst.insert('X', -1)

    def test_delete_invalid_negative_index(self):
        with self.assertRaises(IndexError):
            self.lst.delete(-1)

    def test_deleteAll_nonexisting_element(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('C')
        self.lst.deleteAll('D')
        self.assertEqual(self.lst.get_length(), 3)
        self.assertEqual(self.lst.get(0), 'A')
        self.assertEqual(self.lst.get(1), 'B')
        self.assertEqual(self.lst.get(2), 'C')

    def test_get_invalid_negative_index(self):
        with self.assertRaises(IndexError):
            self.lst.get(-1)

    def test_reverse_empty_list(self):
        self.lst.reverse()
        self.assertEqual(self.lst.get_length(), 0)

    def test_findFirst_existing_element_after_deletion(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.lst.delete(0)
        index = self.lst.findFirst('A')
        self.assertEqual(index, 1)

    def test_findLast_existing_element_after_deletion(self):
        self.lst.append('A')
        self.lst.append('B')
        self.lst.append('A')
        self.lst.delete(2)
        index = self.lst.findLast('A')
        self.assertEqual(index, 0)
        
if __name__ == '__main__':
    unittest.main()
