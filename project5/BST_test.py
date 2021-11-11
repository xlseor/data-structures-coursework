import unittest
from Binary_Search_Tree import Binary_Search_Tree


class Binary_Search_Tree_Tester(unittest.TestCase):
    def setUp(self):
        self.__tree = Binary_Search_Tree()

    def __make_tree(self, elem_list):
        for elem in elem_list:
            self.__tree.insert_element(elem)

    def test_traverse_empty_tree(self):
        self.assertEqual('[ ]', self.__tree.in_order())
        self.assertEqual('[ ]', self.__tree.pre_order())
        self.assertEqual('[ ]', self.__tree.post_order())
        self.assertEqual('0', str(self.__tree.get_height()))

    def test_insert_one_element(self):

        self.__tree.insert_element(1)
        self.assertEqual('[ 1 ]', self.__tree.in_order())
        self.assertEqual('[ 1 ]', self.__tree.pre_order())
        self.assertEqual('[ 1 ]', self.__tree.post_order())
        self.assertEqual('1', str(self.__tree.get_height()))

    def test_create_tree_of_two_elements_left(self):
        self.__make_tree([ 1, -1])
        self.assertEqual('[ -1, 1 ]', self.__tree.in_order())
        self.assertEqual('[ 1, -1 ]', self.__tree.pre_order())
        self.assertEqual('[ -1, 1 ]', self.__tree.post_order())
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_create_tree_of_two_elements_right(self):
        self.__make_tree([ -1, 1])
        self.assertEqual('[ -1, 1 ]', self.__tree.in_order())
        self.assertEqual('[ -1, 1 ]', self.__tree.pre_order())
        self.assertEqual('[ 1, -1 ]', self.__tree.post_order())
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_full_balanced_tree_of_three(self):
        self.__make_tree([0, -1, 1])
        self.assertEqual('[ -1, 0, 1 ]', self.__tree.in_order())
        self.assertEqual('[ 0, -1, 1 ]', self.__tree.pre_order())
        self.assertEqual('[ -1, 1, 0 ]', self.__tree.post_order())
        self.assertEqual('2', str(self.__tree.get_height()))

    def test_balanced_tree_of_height_3_no_rotations_config_1(self):
        self.__make_tree([1, -2, 3, -4])
        self.assertEqual('[ -4, -2, 1, 3 ]', self.__tree.in_order())
        self.assertEqual('[ 1, -2, -4, 3 ]', self.__tree.pre_order())
        self.assertEqual('[ -4, -2, 3, 1 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_balanced_tree_of_height_3_no_rotations_config_2(self):
        self.__make_tree([10, 5, 15, 3, 7])
        self.assertEqual('[ 3, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_balanced_tree_of_height_3_no_rotations_config_3(self):
        self.__make_tree([10, 5, 15, 3, 7, 13])
        self.assertEqual('[ 3, 5, 7, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_balanced_tree_of_height_3_no_rotations_config_4(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.assertEqual('[ 3, 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_balanced_tree_of_height_3_no_rotations_config_5(self):
        self.__make_tree([10, 5, 15, 13, 17])
        self.assertEqual('[ 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 17, 15, 10 ]', self.__tree.post_order())
        self.assertEqual('3', str(self.__tree.get_height()))

    def test_balanced_tree_of_height_3_no_rotations_config_6(self):
        self.__make_tree([10, 5, 15, 7, 13, 17])
        self.assertEqual('[ 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_balanced_tree_of_height_3_no_rotations_config_7(self):
        self.__make_tree([10, 5, 15, 17])
        self.assertEqual('[ 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_balanced_tree_of_height_3_no_rotations_config_8(self):
        self.__make_tree([10, 5, 15, 3, 17])
        self.assertEqual('[ 3, 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_balanced_tree_of_height_3_no_rotations_config_9(self):
        self.__make_tree([10, 5, 15, 3, 7, 17])
        self.assertEqual('[ 3, 5, 7, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_balanced_tree_of_height_3_no_rotations_config_10(self):
        self.__make_tree([10, 5, 15, 3, 13, 17])
        self.assertEqual('[ 3, 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    #ROTATIONS ON INSERTION.

    def test_rotation_on_insertion_config_1(self):
        self.__make_tree([10, 5, 3])
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 10 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 10, 5 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_2(self):
        self.__make_tree([10, 15, 17])
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 17, 15 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_3(self):
        self.__make_tree([10, 5, 7])
        self.assertEqual('[ 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 5, 10 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 10, 7 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_4(self):
        self.__make_tree([10, 15, 13])
        self.assertEqual('[ 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 15, 13 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_5(self):
        self.__make_tree([10, 5, 15, 3, 2])
        self.assertEqual('[ 2, 3, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 3, 2, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 5, 3, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_6(self):
        self.__make_tree([10, 5, 15, 3, 4])
        self.assertEqual('[ 3, 4, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 4, 3, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 4, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_7A(self):
        self.__make_tree([10, 5, 15, 3, 7, 2])
        self.assertEqual('[ 2, 3, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 2, 10, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 7, 15, 10, 5 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_7B(self):
        self.__make_tree([10, 5, 15, 3, 7, 4])
        self.assertEqual('[ 3, 4, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 4, 10, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 4, 3, 7, 15, 10, 5 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_7C(self):
        self.__make_tree([10, 5, 15, 3, 7, 6])
        self.assertEqual('[ 3, 5, 6, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 5, 3, 6, 10, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 6, 5, 15, 10, 7 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_7D(self):
        self.__make_tree([10, 5, 15, 3, 7, 8])
        self.assertEqual('[ 3, 5, 7, 8, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 5, 3, 10, 8, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 8, 15, 10, 7 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_8A(self):
        self.__make_tree([10, 5, 15, 13, 17, 12])
        self.assertEqual('[ 5, 10, 12, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 5, 12, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 12, 10, 17, 15, 13 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_8B(self):
        self.__make_tree([10, 5, 15, 13, 17, 14])
        self.assertEqual('[ 5, 10, 13, 14, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 10, 14, 17, 15, 13 ]', self.__tree.post_order())
        self.assertEqual('[ 13, 10, 5, 15, 14, 17 ]', self.__tree.pre_order())

    def test_rotation_on_insertion_config_8C(self):
        self.__make_tree([10, 5, 15, 13, 17, 16])
        self.assertEqual('[ 5, 10, 13, 15, 16, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 5, 13, 17, 16 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 10, 16, 17, 15 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_8D(self):
        self.__make_tree([10, 5, 15, 13, 17, 18])
        self.assertEqual('[ 5, 10, 13, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 5, 13, 17, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 10, 18, 17, 15 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_9(self):
        self.__make_tree([10, 5, 15, 17, 19])
        self.assertEqual('[ 5, 10, 15, 17, 19 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 17, 15, 19 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 19, 17, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_10(self):
        self.__make_tree([10, 5, 15, 17, 16])
        self.assertEqual('[ 5, 10, 15, 16, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 16, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 17, 16, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11A(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 2])
        self.assertEqual('[ 2, 3, 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 2, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11B(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 4])
        self.assertEqual('[ 3, 4, 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 4, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 4, 3, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11C(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 6])
        self.assertEqual('[ 3, 5, 6, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 6, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 6, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11D(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 8])
        self.assertEqual('[ 3, 5, 7, 8, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 8, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 8, 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11E(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 12])
        self.assertEqual('[ 3, 5, 7, 10, 12, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 12, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 12, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11F(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 14])
        self.assertEqual('[ 3, 5, 7, 10, 13, 14, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 14, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 14, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11G(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 16])
        self.assertEqual('[ 3, 5, 7, 10, 13, 15, 16, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 17, 16 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 16, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_config_11H(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17, 18])
        self.assertEqual('[ 3, 5, 7, 10, 13, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13, 17, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 18, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_12A(self):
        self.__make_tree([10, 5, 15, 17, 3])
        self.assertEqual('[ 3, 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_12B(self):
        self.__make_tree([ 10, 5, 15, 17, 7])
        self.assertEqual('[ 5, 7, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_12C(self):
        self.__make_tree([5, 10, 15, 17, 13])
        self.assertEqual('[ 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_13A(self):
        self.__make_tree([10, 5, 15, 3, 7])
        self.assertEqual('[ 3, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_13B(self):
        self.__make_tree([10, 5, 15, 3, 13])
        self.assertEqual('[ 3, 5, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_13C(self):
        self.__make_tree([10, 5, 15, 3, 17])
        self.assertEqual('[ 3, 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_14A(self):
        self.__make_tree([10, 5, 15, 3, 7, 13])
        self.assertEqual('[ 3, 5, 7, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_14B(self):
        self.__make_tree([10, 5, 15, 3, 7, 17])
        self.assertEqual('[ 3, 5, 7, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_15A(self):
        self.__make_tree([10, 5, 15, 13, 17, 3])
        self.assertEqual('[ 3, 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_after_insertion_15B(self):
        self.__make_tree([10, 5, 15, 13, 17, 7])
        self.assertEqual('[ 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_insertion_16A(self):
        self.__make_tree([10, 5, 15, 3])
        self.assertEqual('[ 3, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_insertion_16B(self):
        self.__make_tree([10, 5, 15, 7])
        self.assertEqual('[ 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_insertion_16C(self):
        self.__make_tree([10, 5, 15, 13])
        self.assertEqual('[ 5, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_insertion_16D(self):
        self.__make_tree([10, 5, 15, 17])
        self.assertEqual('[ 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_insertion_17(self):
        self.__make_tree([10, 5, 15])
        self.assertEqual('[ 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_insertion_18(self):
        self.__make_tree([10, 15, 5])
        self.assertEqual('[ 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_1(self):
        self.__make_tree([10, 5, 15, 3])
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_2(self):
        self.__make_tree([10, 5, 15, 17])
        self.__tree.remove_element(17)
        self.assertEqual('[ 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_3(self):
        self.__make_tree([10, 5, 15])
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 5 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_4(self):
        self.__make_tree([10, 5, 15, 17])
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 5, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 17, 15 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_5A(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_5B(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.__tree.remove_element(7)
        self.assertEqual('[ 3, 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config5C(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.__tree.remove_element(13)
        self.assertEqual('[ 3, 5, 7, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_5D(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.__tree.remove_element(17)
        self.assertEqual('[ 3, 5, 7, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_6A(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.__tree.remove_element(10)
        self.assertEqual('[ 3, 5, 7, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 5, 3, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 17, 15, 13 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config6B(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7, 3, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config6C(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 17])
        self.__tree.remove_element(15)
        self.assertEqual('[ 3, 5, 7, 10, 13, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 17, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 13, 17, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config7A(self):
        self.__make_tree([10, 5, 15, 3, 7])
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7, 3, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_7B(self):
        self.__make_tree([10, 5, 15, 3, 7])
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_7C(self):
        self.__make_tree([10, 5, 15, 3, 7])
        self.__tree.remove_element(7)
        self.assertEqual('[ 3, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_8A(self):
        self.__make_tree([10, 5, 15, 13, 17])
        self.__tree.remove_element(15)
        self.assertEqual('[ 5, 10, 13, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 17, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 17, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_8B(self):
        self.__make_tree([10, 5, 15, 13, 17])
        self.__tree.remove_element(13)
        self.assertEqual('[ 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_8C(self):
        self.__make_tree([10, 5, 15, 13, 17])
        self.__tree.remove_element(17)
        self.assertEqual('[ 5, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_8D(self):
        self.__make_tree([10, 5, 15, 13, 17])
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 5, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 17, 15, 13 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_9A(self):
        self.__make_tree([10, 5, 15, 7, 13, 17])
        self.__tree.remove_element(5)
        self.assertEqual('[ 7, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 7, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_9B(self):
        self.__make_tree([10, 5, 15, 7, 13, 17])
        self.__tree.remove_element(10)
        self.assertEqual('[ 5, 7, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 5, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 17, 15, 13 ]', self.__tree.post_order())

    def test_no_rotation_after_removal_config_9C(self):
        self.__make_tree([10, 5, 15, 7, 13, 17])
        self.__tree.remove_element(15)
        self.assertEqual('[ 5, 7, 10, 13, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 17, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 13, 17, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_9D(self):
        self.__make_tree([10, 5, 15, 7, 13, 17])
        self.__tree.remove_element(17)
        self.assertEqual('[ 5, 7, 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15, 13 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 13, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_9E(self):
        self.__make_tree([10, 5, 15, 7, 13, 17])
        self.__tree.remove_element(13)
        self.assertEqual('[ 5, 7, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 7, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 7, 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_9F(self):
        self.__make_tree([10, 5, 15, 7, 13, 17])
        self.__tree.remove_element(7)
        self.assertEqual('[ 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_10(self):
        #Omitted due to redundancy
        pass

        #I see you laughing
    def test_no_rotation_on_removal_config_11A(self):
        self.__make_tree([10, 5, 15, 3, 17])
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_11B(self):
        self.__make_tree([10, 5, 15, 3, 17])
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 3, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 17, 15, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_insertion_11C(self):
        self.__make_tree([10, 5, 15, 3, 17])
        self.__tree.remove_element(10)
        self.assertEqual('[ 3, 5, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 5, 3, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 17, 15 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_11D(self):
        self.__make_tree([10, 5, 15, 3, 17])
        self.__tree.remove_element(15)
        self.assertEqual('[ 3, 5, 10, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 17, 10 ]', self.__tree.post_order())

    def test_no_rotation_on_removal_config_11E(self):
        self.__make_tree([10, 5, 15, 3, 17])
        self.__tree.remove_element(17)
        self.assertEqual('[ 3, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 15, 10 ]', self.__tree.post_order())

    #Tests of rotation on insertion

    def test_rotation_on_insertion_config_1(self):
        self.__make_tree([10, 5, 3])
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 10 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 10, 5 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_2(self):
        self.__make_tree([10, 15, 17])
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 17, 15 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_3(self):
        self.__make_tree([10, 5, 7])
        self.assertEqual('[ 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 5, 10 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 10, 7 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_4(self):
        self.__make_tree([10, 15, 13])
        self.assertEqual('[ 10, 13, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 15, 13 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_5(self):
        self.__make_tree([10, 5, 15, 17, 18])
        self.assertEqual('[ 5, 10, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 17, 15, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 18, 17, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_6(self):
        self.__make_tree([10, 5, 15, 17, 16])
        self.assertEqual('[ 5, 10, 15, 16, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 16, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 15, 17, 16, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config7(self):
        self.__make_tree([10, 5, 15, 3, 4])
        self.assertEqual('[ 3, 4, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 4, 3, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 4, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_8(self):
        self.__make_tree([10, 5, 15, 3, 2])
        self.assertEqual('[ 2, 3, 5, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 3, 2, 5, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 5, 3, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_9A(self):
        self.__make_tree([10, 5, 15, 3, 7, 2])
        self.assertEqual('[ 2, 3, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 2, 10, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 7, 15, 10, 5 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_9B(self):
        self.__make_tree([10, 5, 15, 3, 7, 4])
        self.assertEqual('[ 3, 4, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 4, 10, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 4, 3, 7, 15, 10, 5 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_9C(self):
        self.__make_tree([10, 5, 15, 3, 7, 6])
        self.assertEqual('[ 3, 5, 6, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 6, 5, 15, 10, 7 ]', self.__tree.post_order())
        self.assertEqual('[ 7, 5, 3, 6, 10, 15 ]', self.__tree.pre_order())

    def test_rotation_on_insertion_config_9D(self):
        self.__make_tree([10, 5, 15, 3, 7, 8])
        self.assertEqual('[ 7, 5, 3, 10, 8, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 7, 8, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 5, 8, 15, 10, 7 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_10A(self):
        self.__make_tree([10, 5, 15, 13, 17, 12])
        self.assertEqual('[ 5, 10, 12, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 5, 12, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 12, 10, 17, 15, 13 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_10B(self):
        self.__make_tree([10, 5, 15, 13, 17, 14])
        self.assertEqual('[ 5, 10, 13, 14, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 5, 15, 14, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 10, 14, 17, 15, 13 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_10C(self):
        self.__make_tree([10, 5, 15, 13, 17, 16])
        self.assertEqual('[ 5, 10, 13, 15, 16, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 5, 13, 17, 16 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 10, 16, 17, 15 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_10D(self):
        self.__make_tree([10, 5, 15, 13, 17, 18])
        self.assertEqual('[ 5, 10, 13, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 5, 13, 17, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 10, 18, 17, 15 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_11A(self):
        self.__make_tree([10, 5, 15, 3, 17, 2])
        self.assertEqual('[ 2, 3, 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 3, 2, 5, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 5, 3, 17, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_11B(self):
        self.__make_tree([10, 5, 15, 3, 17, 4])
        self.assertEqual('[ 3, 4, 5, 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 4, 3, 5, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 4, 17, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_11C(self):
        self.__make_tree([10, 5, 15, 3, 17, 16])
        self.assertEqual('[ 3, 5, 10, 15, 16, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 16, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 15, 17, 16, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_11D(self):
        self.__make_tree([10, 5, 15, 3, 17, 18])
        self.assertEqual('[ 3, 5, 10, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 17, 15, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 15, 18, 17, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_12A(self):
        self.__make_tree([10, 5, 15, 3, 13, 17, 2])
        self.assertEqual('[ 2, 3, 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 3, 2, 5, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 5, 3, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_12B(self):
        self.__make_tree([10, 5, 15, 3, 13, 17, 4])
        self.assertEqual('[ 3, 4, 5, 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 4, 3, 5, 15, 13, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 4, 13, 17, 15, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_13A(self):
        self.__make_tree([10, 5, 15, 3, 7, 17, 16])
        self.assertEqual('[ 3, 5, 7, 10, 15, 16, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 16, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 15, 17, 16, 10 ]', self.__tree.post_order())

    def test_rotation_on_insertion_config_13B(self):
        self.__make_tree([10, 5, 15, 3, 7, 17, 18])
        self.assertEqual('[ 3, 5, 7, 10, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 7, 17, 15, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 5, 15, 18, 17, 10 ]', self.__tree.post_order())

    #Configurations 14 and 15 could be added, similar to 12 and 13 except with the insertion below an elbow. ommitted due to time constraintself.

    #TESTS OF REMOVALS WHICH RESULT IN REBALANCING:

    def test_removal_which_results_in_rebalance_config_1A(self):
        self.__make_tree([10, 5, 15, 3])
        self.__tree.remove_element(10)
        self.assertEqual('[ 3, 5, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 15, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_1B(self):
        self.__make_tree([10, 5, 15, 3])
        self.__tree.remove_element(15)
        self.assertEqual('[ 3, 5, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 10 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 10, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_2(self):
        self.__make_tree([10, 5, 15, 17])
        self.__tree.remove_element(5)
        self.assertEqual('[ 10, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 10, 17, 15 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_3(self):
        self.__make_tree([10, 5, 15, 13, 17])
        self.__tree.remove_element(5)
        self.assertEqual('[ 10, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 17, 15 ]', self.__tree.post_order())
        self.assertEqual('[ 15, 10, 13, 17 ]', self.__tree.pre_order())

    def test_removal_which_results_in_rebalance_config_4A(self):
        self.__make_tree([10, 5, 15, 3, 7])
        self.__tree.remove_element(10)
        self.assertEqual('[ 3, 5, 7, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 15, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 15, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_4B(self):
        self.__make_tree([10, 5, 15, 3, 7])
        self.__tree.remove_element(15)
        self.assertEqual('[ 3, 5, 7, 10 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 10, 7 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 7, 10, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_5A(self):
        self.__make_tree([10, 5, 15, 3, 7, 17, 8])
        self.__tree.remove_element(17)
        self.assertEqual('[ 3, 5, 7, 8, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 5, 3, 10, 8, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 8, 15, 10, 7 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_5B(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 8])
        self.__tree.remove_element(13)
        self.assertEqual('[ 3, 5, 7, 8, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 7, 5, 3, 10, 8, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 8, 15, 10, 7 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_6A(self):
        self.__make_tree([10, 5, 15, 3, 13, 17, 12])
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 10, 12, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 5, 12, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 12, 10, 17, 15, 13 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_6B(self):
        self.__make_tree([10, 5, 15, 7, 13, 17, 12])
        self.__tree.remove_element(7)
        self.assertEqual('[ 5, 10, 12, 13, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 13, 10, 5, 12, 15, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 12, 10, 17, 15, 13 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_7A(self):
        self.__make_tree([10, 5, 15, 3, 13, 17, 16, 18])
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 10, 13, 15, 16, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 5, 13, 17, 16, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 10, 16, 18, 17, 15 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_7B(self):
        self.__make_tree([10, 5, 15, 7, 13, 17, 16, 18])
        self.__tree.remove_element(7)
        self.assertEqual('[ 5, 10, 13, 15, 16, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 5, 13, 17, 16, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 10, 16, 18, 17, 15 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_8A(self):
        self.__make_tree([10, 5, 15, 3, 7, 13, 2, 4])
        self.__tree.remove_element(13)
        self.assertEqual('[ 2, 3, 4, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 2, 4, 10, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 4, 3, 7, 15, 10, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_8B(self):
        self.__make_tree([10, 5, 15, 3, 7, 17, 2, 4])
        self.__tree.remove_element(17)
        self.assertEqual('[ 2, 3, 4, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 2, 4, 10, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 4, 3, 7, 15, 10, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_9A(self):
        self.__make_tree([10, 5, 15, 3, 7, 17, 2])
        self.__tree.remove_element(10)
        self.assertEqual('[ 2, 3, 5, 7, 15, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 2, 15, 7, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 7, 17, 15, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_9B(self):
        self.__make_tree([10, 5, 15, 3, 7, 17, 2])
        self.__tree.remove_element(15)
        self.assertEqual('[ 2, 3, 5, 7, 10, 17 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 2, 10, 7, 17 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 7, 17, 10, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_9C(self):
        self.__make_tree([10, 5, 15, 3, 7, 17, 2])
        self.__tree.remove_element(17)
        self.assertEqual('[ 2, 3, 5, 7, 10, 15 ]', self.__tree.in_order())
        self.assertEqual('[ 5, 3, 2, 10, 7, 15 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 7, 15, 10, 5 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_10A(self):
        self.__make_tree([10, 5, 15, 3, 13, 17, 18])
        self.__tree.remove_element(10)
        self.assertEqual('[ 13, 5, 3, 17, 15, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 5, 13, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 3, 5, 15, 18, 17, 13 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_10B(self):
        self.__make_tree([10, 5, 15, 3, 13, 17, 18])
        self.__tree.remove_element(5)
        self.assertEqual('[ 3, 10, 13, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 3, 13, 17, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 13, 10, 18, 17, 15 ]', self.__tree.post_order())

    def test_removal_which_results_in_rebalance_config_10C(self):
        self.__make_tree([10, 5, 15, 3, 13, 17, 18])
        self.__tree.remove_element(3)
        self.assertEqual('[ 5, 10, 13, 15, 17, 18 ]', self.__tree.in_order())
        self.assertEqual('[ 15, 10, 5, 13, 17, 18 ]', self.__tree.pre_order())
        self.assertEqual('[ 5, 13, 10, 18, 17, 15 ]', self.__tree.post_order())

    #TEST OF REMOVAL WHICH RESULTS IN RECURSIVE DOUBLE REBALANCE

    def test_removal_which_results_in_recursive_double_rebalance_right_heavy(self):
        self.__make_tree([20, 10, 30, 5, 15, 25, 35, 3, 23, 33, 37, 38])
        self.__tree.remove_element(15)
        self.assertEqual('[ 3, 5, 10, 20, 23, 25, 30, 33, 35, 37, 38 ]', self.__tree.in_order())
        self.assertEqual('[ 30, 20, 5, 3, 10, 25, 23, 35, 33, 37, 38 ]', self.__tree.pre_order())
        self.assertEqual('[ 3, 10, 5, 23, 25, 20, 33, 38, 37, 35, 30 ]', self.__tree.post_order())

    def test_removal_which_results_in_recursive_double_rebalance_left_heavy(self):
        self.__make_tree([20, 10, 30, 5, 15, 25, 35, 3, 7, 17, 37, 2])
        self.__tree.remove_element(25)
        self.assertEqual('[ 2, 3, 5, 7, 10, 15, 17, 20, 30, 35, 37 ]', self.__tree.in_order())
        self.assertEqual('[ 10, 5, 3, 2, 7, 20, 15, 17, 35, 30, 37 ]', self.__tree.pre_order())
        self.assertEqual('[ 2, 3, 7, 5, 17, 15, 30, 37, 35, 20, 10 ]', self.__tree.post_order())

if __name__ == '__main__':
    unittest.main()
