import unittest
from Binary_Search_Tree import Binary_Search_Tree

class Binary_Search_Tree_Tester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()

    def test_traverse_empty_tree(self):
        self.assertEqual('[ ]', self.__tree.in_order())
        self.assertEqual('[ ]', self.__tree.pre_order())
        self.assertEqual('[ ]', self.__tree.post_order())

    def test_insert_none(self):
        self.assertRaises(ValueError, self.__tree.insert_element, None)

    def test_insert_into_empty_tree(self):
        self.__tree.insert_element(1)
        self.assertEqual("[ 1 ]", self.__tree.in_order())
        self.assertEqual("[ 1 ]", self.__tree.pre_order())
        self.assertEqual("[ 1 ]", self.__tree.post_order())

    def test_insert_at_left_pos(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.assertEqual('[ 1, 2 ]', self.__tree.in_order())
        self.assertEqual('[ 2, 1 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 2 ]', self.__tree.post_order())

    def test_insert_at_right_pos(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 2 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 1 ]', self.__tree.post_order())

    def test_insert_at_root_dot_left_dot_left(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.assertEqual('[ 1, 2, 3 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 2, 1 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 2, 3 ]', self.__tree.post_order())

    def test_insert_at_root_dot_left_dot_right(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2, 3 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 1, 2 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 1, 3 ]', self.__tree.post_order())

    def test_insert_at_root_dot_right_dot_left(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.assertEqual('[ 1, 2, 3 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 3, 2 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 1 ]', self.__tree.post_order())

    def test_insert_at_root_dot_right_dot_right(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(3)
        self.assertEqual('[ 1, 2, 3 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 2, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 2, 1 ]', self.__tree.post_order())

    def test_insert_value_already_contained_at_root(self):
        self.__tree.insert_element(0)
        self.assertRaises(ValueError, self.__tree.insert_element, 0)

    def test_insert_value_already_in_intermediate_position(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertRaises(ValueError, self.__tree.insert_element, 1)

    def test_insert_value_already_in_leaf_pos(self):
        self.__tree.insert_element(0)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertRaises(ValueError, self.__tree.insert_element, 2)

    def test_remove_from_tree_with_one_node(self):
        self.__tree.insert_element(1)
        self.__tree.remove_element(1)
        self.assertEqual('[ ]', self.__tree.in_order())
        self.assertEqual('[ ]', self.__tree.pre_order())
        self.assertEqual('[ ]', self.__tree.post_order())

    def test_remove_from_empty_tree(self):
        self.assertRaises(ValueError, self.__tree.remove_element, 0)

    def test_remove_none_from_empty_tree(self):
        self.assertRaises(ValueError, self.__tree.remove_element, None)

    def test_remove_none_from_non_empty_tree(self):
        self.__tree.insert_element(1)
        self.assertRaises(ValueError, self.__tree.remove_element, None)

    def test_remove_value_not_in_tree_of_height_one(self):
        self.__tree.insert_element(1)
        self.assertRaises(ValueError, self.__tree.remove_element, 2)
        self.assertRaises(ValueError, self.__tree.remove_element, 0)

    def test_remove_value_not_in_tree_of_height_two(self):
        self.__tree.insert_element(4)
        self.__tree.insert_element(2)
        self.__tree.insert_element(6)
        self.assertRaises(ValueError, self.__tree.remove_element, 1)
        self.assertRaises(ValueError, self.__tree.remove_element, 3)
        self.assertRaises(ValueError, self.__tree.remove_element, 5)
        self.assertRaises(ValueError, self.__tree.remove_element, 7)
        #Test removal of non-included value which takes each logarithmic path down tree

    def test_remove_root_of_one_node_tree(self):
        self.__tree.insert_element(1)
        self.__tree.remove_element(1)
        self.assertEqual('[ ]', self.__tree.in_order())
        self.assertEqual('[ ]', self.__tree.post_order())
        self.assertEqual('[ ]', self.__tree.pre_order())

    def test_remove_right_leaf_height_two(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual('[ 0, 1 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 0 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 1 ]', self.__tree.post_order())

    def test_remove_left_leaf_height_two(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(0)
        self.assertEqual('[ 1, 2 ]', self.__tree.in_order())
        self.assertEqual('[ 2, 1 ]', self.__tree.post_order())
        self.assertEqual('[ 1, 2 ]', self.__tree.pre_order())

    def test_remove_root_dot_left_dot_left(self):
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(2)
        self.__tree.insert_element(4)
        self.__tree.insert_element(6)
        self.__tree.insert_element(8)
        self.__tree.remove_element(2)
        self.assertEqual('[ 3, 4, 5, 6, 7, 8 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 4, 7, 6, 8 ]', self.__tree.pre_order())
        self.assertEqual('[ 4, 3, 6, 8, 7, 5 ]', self.__tree.post_order())

    def test_remove_root_dot_left_dot_right(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual('[ 1, 3 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 1 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 3 ]', self.__tree.post_order())

    def test_remove_root_dot_right_dot_right(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 4 ]', self.__tree.in_order())
        self.assertEqual('[ 4, 3 ]', self.__tree.post_order())
        self.assertEqual('[ 3, 4 ]', self.__tree.pre_order())

    def test_remove_root_dot_right_dot_left(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(5)
        self.__tree.insert_element(4)
        self.assertEqual('[ 3, 4, 5 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 5, 4 ]', self.__tree.pre_order())
        self.assertEqual('[ 4, 5, 3 ]', self.__tree.post_order())

    def test_remove_right_intermediate_pos_with_one_child(self):
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.insert_element(5)
        self.__tree.remove_element(4)
        self.assertEqual('[ 3, 5 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 5 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 3 ]', self.__tree.post_order())

    def test_remove_right_intermediate_pos_with_two_children(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(4)
        self.__tree.insert_element(3)
        self.__tree.insert_element(5)
        self.__tree.remove_element(4)
        self.assertEqual('[ 1, 3, 5 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 5, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 1 ]', self.__tree.post_order())

    def test_remove_left_intermediate_pos_with_one_child(self):
        self.__tree.insert_element(7)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 7 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 7 ]', self.__tree.post_order())
        self.assertEqual('[ 7, 3 ]', self.__tree.pre_order())

    def test_remove_left_intermediate_pos_with_two_children(self):
        self.__tree.insert_element(7)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(6)
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 6, 7 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 6, 7 ]', self.__tree.post_order())
        self.assertEqual('[ 7, 6, 3 ]', self.__tree.pre_order())

    def test_remove_root_when_root_dot_right_is_none(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0 ]', self.__tree.in_order())
        self.assertEqual('[ 0 ]', self.__tree.pre_order())
        self.assertEqual('[ 0 ]', self.__tree.post_order())

    def test_remove_root_when_root_dot_right_is_not_none(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ 2 ]', self.__tree.in_order())

    def test_remove_root_with_two_children_height_2(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0, 2 ]', self.__tree.in_order())
        self.assertEqual('[ 2, 0 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 2 ]', self.__tree.post_order())

    def test_remove_root_with_recursive_find_min_one(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0, 2, 3 ]', self.__tree.in_order())
        self.assertEqual('[ 2, 0, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 3, 2 ]', self.__tree.post_order())

    def test_remove_root_with_recursive_find_min_two(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0, 2, 3, 5 ]', self.__tree.in_order())
        self.assertEqual('[ 2, 0, 5, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 3, 5, 2 ]', self.__tree.post_order())

    def test_remove_root_with_recursive_find_min_elbow(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(7)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(4)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0, 3, 4, 5, 7 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 0, 7, 5, 4 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 4, 5, 7, 3 ]', self.__tree.post_order())

    #MANY OF THESE HEIGHT TESTS ARE ALSO GOOD OPPORTUNITIES TO TEST CORNER CASES ON TRAVERSALS
    #CONSIDER ADDING SUCH TRAVERSALS.

    def test_get_height_of_empty_tree(self):
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_get_height_of_tree_with_one_node(self):
        self.__tree.insert_element(1)
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_for_change_in_height_on_removal_from_empty_tree(self):
        #Test whether erroneous insert and remove calls can change height
        with self.assertRaises(ValueError):
            self.__tree.remove_element(2)
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_for_change_in_height_on_removal_of_nonsense_value(self):
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.remove_element(None)
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_for_change_in_height_on_insertion_of_nonsense_value_in_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__tree.insert_element(None)
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_height_after_insertion_of_nonsense_value_in_nonempty_tree(self):
        self.__tree.insert_element(5)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(None)
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_height_after_insertion_of_nonsense_value_in_tree_height_2(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(None)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_height_after_insertion_of_value_already_right_leaf_pos(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(2)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_height_after_insertion_of_value_already_in_left_leaf_pos(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(0)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_height_after_insertion_of_value_already_at_root_height_2(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.insert_element(2)
        with self.assertRaises(ValueError):
            self.__tree.insert_element(1)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_height_after_insertion_of_value_already_at_root_height_1(self):
        self.__tree.insert_element(1)
        self.assertRaises(ValueError, self.__tree.insert_element, 1)
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_height_after_removal_from_empty_tree(self):
        with self.assertRaises(ValueError):
            self.__tree.remove_element(-1)
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_height_of_empty_tree(self):
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_height_of_empty_tree_that_was_once_nonempty_height_1(self):
        self.__tree.insert_element(1)
        self.__tree.remove_element(1)
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_height_of_empty_tree_that_was_once_height_2(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(0)
        self.__tree.remove_element(0)
        self.__tree.remove_element(1)
        self.__tree.remove_element(2)
        self.assertEqual('0', str(self.__tree.get_height()))

    #BELOW, TEST THAT ALL POSSIBLE CONFIGURATIONS OF TREES OF HEIGHTS 1, 2, AND 3 HAVE
    #THE CORRECT HEIGHTS

    def test_height_of_one_node_tree(self):
        self.__tree.insert_element(1)
        self.assertEqual('1', str(self.__tree.get_height()))
        self.assertEqual('[ 1 ]', self.__tree.in_order())
        self.assertEqual('[ 1 ]', self.__tree.pre_order())
        self.assertEqual('[ 1 ]', self.__tree.post_order())

    def test_height_of_two_node_tree_left_child(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.assertEqual('2', str(self.__tree.get_height()))
        self.assertEqual('[ 0, 1 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 0 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 1 ]', self.__tree.post_order())

    def test_tree_height_2_right_child(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.assertEqual('2', str(self.__tree.get_height()))
        self.assertEqual('[ 1, 2 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 2 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 1 ]', self.__tree.post_order())

    def test_height_of_tree_height_two_two_chidren(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(2)
        self.__tree.insert_element(0)
        self.assertEqual('2', str(self.__tree.get_height()))
        self.assertEqual('[ 0, 1, 2 ]', self.__tree.in_order())
        self.assertEqual('[ 1, 0, 2 ]', self.__tree.pre_order())
        self.assertEqual('[ 0, 2, 1 ]', self.__tree.post_order())

    def test_height_of_three_config_1(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 2, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 2 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 5, 10 ]', self.__tree.post_order())

    def test_height_of_three_config_2(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(12)
        self.__tree.insert_element(15)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 10, 12, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 12, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 15, 12, 10 ]', self.__tree.post_order())

    def test_height_of_three_config_3(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 10 ]', self.__tree.post_order())

    def test_height_of_three_config_4(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(12)
        self.__tree.insert_element(11)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 10, 11, 12 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 12, 11 ]', self.__tree.pre_order())
        self.assertEqual('[ 11, 12, 10 ]', self.__tree.post_order())

    def test_height_of_three_config_5(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(8)
        self.__tree.insert_element(6)
        self.__tree.insert_element(12)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 6, 8, 10, 12 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 8, 6, 12 ]', self.__tree.pre_order())
        self.assertEqual('[ 6, 8, 12, 10 ]', self.__tree.post_order())

    def test_height_of_three_config_6(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(8)
        self.__tree.insert_element(6)
        self.__tree.insert_element(9)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 6, 8, 9, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 8, 6, 9 ]', self.__tree.pre_order())
        self.assertEqual('[ 6, 9, 8, 10 ]', self.__tree.post_order())

    def test_height_of_three_config_7(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(7)
        self.__tree.insert_element(12)
        self.__tree.insert_element(14)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 7, 10, 12, 14 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7, 12, 14 ]', self.__tree.pre_order())

        self.assertEqual('[ 7, 14, 12, 10 ]', self.__tree.post_order())
    def test_height_of_three_config_8(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(12)
        self.__tree.insert_element(17)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual("[ 10, 12, 15, 17 ]", self.__tree.in_order())
        self.assertEqual("[ 10, 15, 12, 17 ]", self.__tree.pre_order())
        self.assertEqual("[ 12, 17, 15, 10 ]", self.__tree.post_order())

    def test_height_of_three_config_9(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(8)
        self.__tree.insert_element(6)
        self.__tree.insert_element(9)
        self.__tree.insert_element(12)
        self.assertEqual('[ 6, 8, 9, 10, 12 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 8, 6, 9, 12 ]', self.__tree.pre_order())
        self.assertEqual('[ 6, 9, 8, 12, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_height_of_three_config_10(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(12)
        self.__tree.insert_element(14)
        self.__tree.insert_element(8)
        self.__tree.insert_element(11)
        self.assertEqual('[ 8, 10, 11, 12, 14 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 8, 12, 11, 14 ]', self.__tree.pre_order())
        self.assertEqual('[ 8, 11, 14, 12, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_height_of_three_config_11(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)
        self.__tree.insert_element(3)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.assertEqual('[ 3, 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

        #there is no config. 12. my apologies.

    def test_height_of_three_config_13(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.insert_element(27)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 13, 15, 17, 20, 25, 27 ]', self.__tree.in_order())
        self.assertEqual('[ 20, 15, 13, 17, 25, 27 ]', self.__tree.pre_order())
        self.assertEqual('[ 13, 17, 15, 27, 25, 20 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_height_of_three_config_14(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(5)
        self.__tree.insert_element(17)
        self.__tree.insert_element(3)
        self.__tree.insert_element(13)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 3, 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_height_of_three_config_15(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(5)
        self.__tree.insert_element(17)
        self.__tree.insert_element(3)
        self.assertEqual('3', str(self.__tree.get_height()))
        self.assertEqual('[ 3, 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 17, 15, 10 ]', self.__tree.post_order())


    #TESTS OF HEIGHT UPDATE AFTER REMOVAL
    #TRAVERSALS MAY BE ADDED WHERE APPROPRIATE

    def test_remove_intermediate_node_no_change_in_height_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)
        self.__tree.insert_element(3)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(15)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_remove_at_intermediate_node_no_change_in_height_left(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(7)
        self.__tree.insert_element(3)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(5)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_remove_intermediate_node_and_change_height_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(5)
        self.__tree.insert_element(20)
        self.__tree.remove_element(15)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_remove_intermediate_node_and_change_height_left(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(12)
        self.__tree.remove_element(5)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_remove_root_and_change_height_right_heavy(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.remove_element(10)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_remove_root_and_do_not_change_height_left_heavy(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(2)
        self.__tree.insert_element(15)
        self.__tree.remove_element(10)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_remove_root_and_do_not_change_height_perfect(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(15)
        self.assertEqual("2", str(self.__tree.get_height()))
    def test_remove_root_height_one_and_set_height_to_zero(self):

        self.__tree.insert_element(1)
        self.__tree.remove_element(1)
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_remove_leaf_and_do_not_change_height_left_height_2(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(10)
        self.assertEqual("2", str(self.__tree.get_height()))

    def test_remove_leaf_and_do_not_change_height_right_height_2(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual("2", str(self.__tree.get_height()))

    def test_remove_leaf_and_do_not_change_height_left_height_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(5)
        self.__tree.remove_element(5)
        self.assertEqual("3", str(self.__tree.get_height()))

    def test_remove_leaf_and_do_not_change_height_right_height_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(5)
        self.__tree.remove_element(25)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_remove_leaf_and_change_height_right_height_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.remove_element(25)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_remove_leaf_and_change_height_right_height_2(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.remove_element(20)
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_remove_leaf_and_change_height_left_height_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(20)
        self.__tree.remove_element(5)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_remove_leaf_and_change_height_left_height_2(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.remove_element(10)
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_insert_in_empty_tree_and_update_height(self):
        self.__tree.insert_element(1)
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_insert_at_right_and_do_not_change_height_height_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        h = self.__tree.get_height()
        self.__tree.insert_element(20)
        self.assertEqual(str(self.__tree.get_height()), str(h))

    def test_insert_at_right_and_do_not_change_height_height_2(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        h = self.__tree.get_height()
        self.__tree.insert_element(20)
        self.assertEqual(str(self.__tree.get_height()), str(h))

    def test_insert_at_left_and_do_not_change_height_height_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.__tree.insert_element(25)
        self.__tree.insert_element(10)
        h = self.__tree.get_height()
        self.__tree.insert_element(5)
        self.assertEqual(str(self.__tree.get_height()), str(h))

    def test_insert_at_left_and_do_not_change_height_height_2(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        h = self.__tree.get_height()
        self.__tree.insert_element(10)
        self.assertEqual(str(self.__tree.get_height()), str(h))

    def test_insert_at_left_and_change_height_to_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.assertEqual(str(self.__tree.get_height()), '2')
        self.__tree.insert_element(5)
        self.assertEqual(str(self.__tree.get_height()), '3')

    def test_insert_at_left_and_change_height_to_2(self):
        self.__tree.insert_element(15)
        self.assertEqual('1', str(self.__tree.get_height()))
        self.__tree.insert_element(10)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_insert_at_right_and_change_height_to_3(self):
        self.__tree.insert_element(15)
        self.__tree.insert_element(10)
        self.__tree.insert_element(20)
        self.assertEqual('2', str(self.__tree.get_height()))
        self.__tree.insert_element(25)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_insert_at_right_and_change_height_to_2(self):
        self.__tree.insert_element(15)
        self.assertEqual('1', str(self.__tree.get_height()))
        self.__tree.insert_element(25)
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_deep_insertion_without_height_change_at_root_left(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(35)
        self.__tree.insert_element(37)
        self.assertEqual('4', str(self.__tree.get_height()))
        self.__tree.insert_element(3)
        self.assertEqual('4', str(self.__tree.get_height()))

    def test_deep_insertion_without_height_change_at_root_right(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertEqual('4', str(self.__tree.get_height()))
        self.__tree.insert_element(37)
        self.assertEqual('4', str(self.__tree.get_height()))

    def test_deep_removal_without_height_change_left(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(35)
        self.__tree.insert_element(37)
        self.assertEqual('4', str(self.__tree.get_height()))
        self.__tree.remove_element(3)
        self.assertEqual('4', str(self.__tree.get_height()))

    def test_deep_removal_without_height_change_right(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(30)
        self.__tree.insert_element(35)
        self.__tree.insert_element(37)
        self.__tree.insert_element(25)
        self.assertEqual('4', str(self.__tree.get_height()))
        self.__tree.remove_element(37)
        self.assertEqual('4', str(self.__tree.get_height()))

    def test_test_chain_height_update_removal_right(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)
        self.__tree.insert_element(35)
        self.__tree.insert_element(37)
        self.assertEqual('4', str(self.__tree.get_height()))
        self.__tree.remove_element(37)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_chain_height_update_on_removal_left(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.assertEqual('4', str(self.__tree.get_height()))
        self.__tree.remove_element(3)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_chain_height_update_removal_right(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(30)
        self.__tree.insert_element(35)
        self.__tree.insert_element(37)
        self.assertEqual('4', str(self.__tree.get_height()))
        self.__tree.remove_element(37)
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_remove_and_decrement_height_one_side_right_and_traverse(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 17, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))
        self.__tree.remove_element(17)
        self.assertEqual('2', str(self.__tree.get_height()))
        self.assertEqual('[ 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 15 ]', self.__tree.pre_order())

    def test_remove_and_decrement_height_one_side_left_and_traverse(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))
        self.__tree.remove_element(3)
        self.assertEqual('2', str(self.__tree.get_height()))
        self.assertEqual('[ 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 10 ]', self.__tree.post_order())

    def test_remove_node_with_left_child_from_intermediate_position(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 3, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 15, 10 ]', self.__tree.post_order())

    def test_remove_node_with_right_child_only_at_intermediate_pos(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(15)
        self.assertEqual('[ 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 5, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 5, 7, 15 ]', self.__tree.pre_order())
        self.__tree.remove_element(5)
        self.assertEqual('[ 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 7, 15 ]', self.__tree.pre_order())

    def test_remove_node_with_left_and_right_children_at_int_pos_left(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 10 ]', self.__tree.post_order())

    def test_remove_node_with_left_and_right_children_at_int_pos_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.assertEqual('[ 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 17, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 15, 13, 17 ]', self.__tree.pre_order())
        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 13, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 17, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 13, 17, 10 ]', self.__tree.post_order())

    def test_remove_root_with_left_child_no_granchildren_or_right_child(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.assertEqual('[ 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(10)
        self.assertEqual('[ 5 ]', self.__tree.in_order())
        self.assertEqual('[ 5 ]', self.__tree.pre_order())
        self.assertEqual('[ 5 ]', self.__tree.post_order())

    def test_remove_root_with_right_child_no_grandchildren_or_left_child(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.assertEqual('[ 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(10)
        self.assertEqual('[ 15 ]', self.__tree.in_order())
        self.assertEqual('[ 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 15 ]', self.__tree.post_order())

    def test_remove_root_with_four_grandchildren(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.assertEqual('[ 3, 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(10)
        self.assertEqual('[ 3, 5, 7, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 5, 3, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 17, 15, 13 ]', self.__tree.post_order())

    def test_remove_root_and_replace_with_elbow_min_below(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(13)
        self.__tree.insert_element(14)
        self.__tree.insert_element(9)
        self.assertEqual('[ 9, 10, 13, 14, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 9, 15, 13, 14 ]', self.__tree.pre_order())
        self.assertEqual('[ 9, 14, 13, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(10)
        self.assertEqual('[ 9, 13, 14, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 9, 15, 14 ]', self.__tree.pre_order())
        self.assertEqual('[ 9, 14, 15, 13 ]', self.__tree.post_order())

    def test_remove_value_not_included_in_a_large_tree(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(25)
        self.__tree.insert_element(35)
        self.assertRaises(ValueError, self.__tree.remove_element, 36)

    def test_of_find_min_1_remove_root_no_right_child(self):
        self.__tree.insert_element(1)
        self.__tree.insert_element(0)
        self.__tree.remove_element(1)
        self.assertEqual('[ 0 ]', self.__tree.in_order())
        self.assertEqual('[ 0 ]', self.__tree.pre_order())
        self.assertEqual('[ 0 ]', self.__tree.post_order())

    def test_of_find_min_2_remove_root_with_childless_right_child(self):
        self.__tree.insert_element(2)
        self.__tree.insert_element(1)
        self.__tree.insert_element(3)
        self.__tree.remove_element(2)
        self.assertEqual('[ 3, 1 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, 3 ]', self.__tree.post_order())
        self.assertEqual('[ 1, 3 ]', self.__tree.in_order())

    def test_of_find_min_3_remove_right_min_with_right_child(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(20)
        self.assertEqual('[ 5, 10, 15, 20 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 20 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 20, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 15, 20 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 5, 20 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 20, 15 ]', self.__tree.post_order())

    def test_of_find_min_4_search_left_one_for_min(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(13)
        self.assertEqual('[ 5, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_of_find_min_5_search_left_two_for_min(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(13)
        self.__tree.insert_element(12)
        self.assertEqual('[ 5, 10, 12, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13, 12 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 12, 13, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 12, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 12, 5, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 15, 12 ]', self.__tree.post_order())

    def test_of_find_min_5_search_left_2_for_elbow_min(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(25)
        self.__tree.insert_element(23)
        self.__tree.insert_element(24)
        self.assertEqual('[ 10, 20, 23, 24, 25, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 20, 10, 30, 25, 23, 24 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 24, 23, 25, 30, 20 ]', self.__tree.post_order())
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 23, 24, 25, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 24, 25, 30, 23 ]', self.__tree.post_order())
        self.assertEqual('[ 23, 10, 30, 25, 24 ]', self.__tree.pre_order())

    def test_of_find_min_6_search_left_2_for_elbow_min_ignoring_branches(self):
        self.__tree.insert_element(40)
        self.__tree.insert_element(20)
        self.__tree.insert_element(60)
        self.__tree.insert_element(50)
        self.__tree.insert_element(65)
        self.__tree.insert_element(55)
        self.__tree.insert_element(45)
        self.__tree.insert_element(47)
        self.assertEqual('[ 20, 40, 45, 47, 50, 55, 60, 65 ]', self.__tree.in_order())
        self.assertEqual('[ 40, 20, 60, 50, 45, 47, 55, 65 ]', self.__tree.pre_order())
        self.assertEqual('[ 20, 47, 45, 55, 50, 65, 60, 40 ]', self.__tree.post_order())
        self.__tree.remove_element(40)
        self.assertEqual('[ 20, 45, 47, 50, 55, 60, 65 ]', self.__tree.in_order())
        self.assertEqual('[ 45, 20, 60, 50, 47, 55, 65 ]', self.__tree.pre_order())
        self.assertEqual('[ 20, 47, 55, 50, 65, 60, 45 ]', self.__tree.post_order())

    def test_of_find_min_7_search_left_three_for_min(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(29)
        self.__tree.insert_element(28)
        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 20, 27, 28, 29, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 20, 10, 30, 29, 28, 27 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 27, 28, 29, 30, 20 ]', self.__tree.post_order())
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 27, 28, 29, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 27, 10, 30, 29, 28 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 28, 29, 30, 27 ]', self.__tree.post_order())

    def test_of_find_min_8_search_left_three_for_elbow_min(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(29)
        self.__tree.insert_element(28)
        self.__tree.insert_element(26)
        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 20, 26, 27, 28, 29, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 20, 10, 30, 29, 28, 26, 27 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 27, 26, 28, 29, 30, 20 ]', self.__tree.post_order())
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 26, 27, 28, 29, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 26, 10, 30, 29, 28, 27 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 27, 28, 29, 30, 26 ]', self.__tree.post_order())

    def test_smallest_search_for_elbow_min(self):
        self.__tree.insert_element(20)
        self.__tree.insert_element(10)
        self.__tree.insert_element(30)
        self.__tree.insert_element(25)
        self.__tree.insert_element(27)
        self.assertEqual('[ 10, 20, 25, 27, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 20, 10, 30, 25, 27 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 27, 25, 30, 20 ]', self.__tree.post_order())
        self.__tree.remove_element(20)
        self.assertEqual('[ 10, 25, 27, 30 ]', self.__tree.in_order())
        self.assertEqual('[ 25, 10, 30, 27 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 27, 30, 25 ]', self.__tree.post_order())

        #TESTS OF LEFT AND RIGHT SEARCH FUNCTIONALITY OF self.__rec_remov :

    def test_search_left_then_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.assertEqual('[ 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(7)
        self.assertEqual('[ 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 10 ]', self.__tree.post_order())

    def test_search_double_left(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(7)
        self.__tree.insert_element(5)
        self.assertEqual('[ 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7, 5 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 7, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(5)
        self.assertEqual('[ 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 10 ]', self.__tree.post_order())

    def test_search_double_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 17, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(17)
        self.assertEqual('[ 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 15, 10 ]', self.__tree.post_order())

    def test_remove_intermediate_left(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 10 ]', self.__tree.post_order())

    def test_remove_intermediate_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 17, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 17, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 17 ]', self.__tree.pre_order())

    def test_seven_node_tree_test_1_root_removal(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.assertEqual('[ 3, 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(10)
        self.assertEqual('[ 3, 5, 7, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 5, 3, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 17, 15, 13 ]', self.__tree.post_order())

    def test_seven_node_tree_test_2_root_dot_left_removal(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7, 3, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_seven_node_tree_test_3_root_dot_right_removal(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(15)
        self.assertEqual('[ 3, 5, 7, 10, 13, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 17, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 17, 10 ]', self.__tree.post_order())

    def test_seven_node_tree_test_4_root_dot_left_dot_left_removal(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_seven_node_tree_test_5_root_dot_left_dot_right_removal(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(7)
        self.assertEqual('[ 3, 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_seven_node_tree_test_6_root_dot_right_dot_left_removal(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(13)
        self.assertEqual('[ 3, 5, 7, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_seven_node_tree_test_7_root_dot_right_dot_right_removal(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.__tree.remove_element(17)
        self.assertEqual('[ 3, 5, 7, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_remove_the_left_elbow(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(7)
        self.assertEqual('[ 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(5)
        self.assertEqual('[ 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 10 ]', self.__tree.post_order())

    def test_remove_the_right_elbow(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(13)
        self.assertEqual('[ 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 13, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(15)
        self.assertEqual('[ 10, 13 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 13 ]', self.__tree.pre_order())

    def test_remove_intermediate_node_of_full_tree_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(13)
        self.__tree.insert_element(17)
        self.assertEqual('[ 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 17, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(15)
        self.assertEqual('[ 5, 10, 13, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 17, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 17, 10 ]', self.__tree.post_order())

    def test_remove_intermediate_node_of_full_tree_left(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(7)
        self.__tree.insert_element(15)
        self.assertEqual('[ 3, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 7, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 7, 3, 15 ]', self.__tree.pre_order())

    def test_remove_intermediate_node_two_down_left(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.assertEqual('[ 2, 3, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 2, 3, 5, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 5, 3, 2 ]', self.__tree.pre_order())
        self.__tree.remove_element(3)
        self.assertEqual('[ 10, 5, 2 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 5, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 2, 5, 10 ]', self.__tree.in_order())

    def test_remove_intermediate_node_down_two_right(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.__tree.insert_element(18)
        self.assertEqual('[ 10, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15, 17, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 18, 17, 15, 10 ]', self.__tree.post_order())
        self.__tree.remove_element(17)
        self.assertEqual('[ 10, 15, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 15, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 18, 15, 10 ]', self.__tree.post_order())

    def test_remove_left_three_down(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(3)
        self.__tree.insert_element(2)
        self.__tree.remove_element(2)
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.post_order())

    def test_remove_right_three_down(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.__tree.insert_element(18)
        self.__tree.remove_element(18)
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 17, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.pre_order())

    def test_remove_leaf_node_after_zigzag(self):
        self.__tree.insert_element(50)
        self.__tree.insert_element(25)
        self.__tree.insert_element(49)
        self.__tree.insert_element(26)
        self.__tree.insert_element(48)
        self.__tree.insert_element(27)
        self.__tree.insert_element(47)
        self.__tree.insert_element(28)
        self.__tree.insert_element(46)
        self.assertEqual('[ 25, 26, 27, 28, 46, 47, 48, 49, 50 ]', self.__tree.in_order())
        self.assertEqual('[ 50, 25, 49, 26, 48, 27, 47, 28, 46 ]', self.__tree.pre_order())
        self.assertEqual('[ 46, 28, 47, 27, 48, 26, 49, 25, 50 ]', self.__tree.post_order())
        self.__tree.remove_element(46)
        self.assertEqual('[ 25, 26, 27, 28, 47, 48, 49, 50 ]', self.__tree.in_order())
        self.assertEqual('[ 50, 25, 49, 26, 48, 27, 47, 28 ]', self.__tree.pre_order())
        self.assertEqual('[ 28, 47, 27, 48, 26, 49, 25, 50 ]', self.__tree.post_order())

    def test_remove_root_and_search_left_two_for_min(self):
        self.__tree.insert_element(10)
        self.__tree.insert_element(5)
        self.__tree.insert_element(15)
        self.__tree.insert_element(17)
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 5, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 17, 15 ]', self.__tree.post_order())










    #TEST CASES:
    #INSERTION AND TRAVERSAL METHODS
    #REMOVAL METHODS
if __name__ == '__main__':
    unittest.main()
