#TODO add the height pointers to removal function

class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class
  __root = None
  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class
    # must be public to be reachable from the the methods.
    value = None
    height = 1
    left = None
    right = None

    def __init__(self, value):
      self.value = value

    def get_height(self):
        return self.height
  def __init__(self):
      self.__root = None

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation
    if self.__root is None:
        return 0
    return self.__root.height

  def __update_height(self, node):

      if node.left is None and node.right is None:
          node.height = 1

      if node.left is None and node.right is not None:
          node.height = node.right.height + 1

      if node.left is not None and node.right is None:
          node.height = node.left.height + 1

      if node.left is not None and node.right is not None:
          if node.left.height == node.height:
              node.height += 1
          if node.right.height == node.height:
              node.height += 1
          if node.right.height < node.height - 1 and node.left.height < node.height -1:
              node.height -= 1

  #Recursive insertion and removal functions:
  def __rotate_right(self, node):
      if node.left.right is None:
          new_root = node.left
          new_root.right = node
          node.left = None
          return new_root

      if node.left.right is not None:
          new_root = node.left
          node.left = node.left.right
          new_root.right = node
          return new_root

  def __rotate_left(self, node):
       if node.right.left is None:
           new_root = node.right
           new_root.left = node
           node.right = None
           return new_root

       if node.right.left is not None:
           new_root = node.right
           node.right = node.right.left
           new_root.left = node
           return new_root

  def __get_balance(self, node):

      if node.left is None and node.right is None:
          return 0
      if node.left is not None and node.right is None:
          return (-1)*node.left.get_height()
      if node.right is not None and node.left is None:
          return node.right.get_height()
      if node.right is not None and node.left is not None:
          return node.right.get_height() - node.left.get_height()

  def __balance(self, node):

      if self.__get_balance(node) > (-2) and self.__get_balance(node) < (2):
          return node
      if self.__get_balance(node) is 2:
          if self.__get_balance(node.right) is 1 or self.__get_balance(node.right) is 0:
              return self.__rotate_left(node)
          if self.__get_balance(node.right) is -1:
              node.right = self.__rotate_right(node.right)
              return self.__rotate_left(node)
      if self.__get_balance(node) is -2:
          if self.__get_balance(node.left) is -1 or self.__get_balance(node.left) is 0:
              return self.__rotate_right(node)
          if self.__get_balance(node.left) is 1:
              node.left = self.__rotate_left(node.left)
              return self.__rotate_right(node)



  def __rec_ins(self, node, value):
      if node is None:
          return self.__BST_Node(value)
      if node.value == value:
          raise ValueError
      if value > node.value:
          node.right = self.__rec_ins(node.right, value)
          self.__update_height(node)
          return self.__balance(node)
      if value < node.value:
          node.left = self.__rec_ins(node.left, value)
          self.__update_height(node)
          return self.__balance(node)

  def __rec_remov(self, node, value):
    #find_min is a recursive function for finding the minimum value in a subtree.
      def find_min(node):
          if node.left is not None:
              return find_min(node.left)
          if node.left is None:
              return node.value

      if node is None:
          raise ValueError
          #In test cases, make sure that this error does not alter tree. I don't think it should...
      if value > node.value:
          node.right = self.__rec_remov(node.right, value)
          self.__update_height(node)
          return self.__balance(node)
      if value < node.value:
          node.left = self.__rec_remov(node.left, value)
          self.__update_height(node)
          return self.__balance(node)
      if value == node.value:
          if node.left is None and node.right is None:
              return None
          if node.left is not None and node.right is None:
              return node.left
          if node.left is None and node.right is not None:
              return node.right
          if node.left is not None and node.right is not None:
              val = find_min(node.right)
              node.right = self.__rec_remov(node.right, val)
              node.value = val
              return self.__balance(node)






  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if value is None:
        raise ValueError
    if self.__root is None:
        self.__root = self.__BST_Node(value)
        return
    self.__root = self.__rec_ins(self.__root, value)

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some
    # implementations). Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if value is None:
        raise ValueError
    if self.__root is None:
        raise ValueError
    self.__root = self.__rec_remov(self.__root, value)


    #Recursive traversal methods:

  def __rec_pre_order(self, node):
       #string which will be updated by recursion
       #base cases:
       #allowance for Node is None avoids three-branch recursive case
       #by accounting for situation where node has one child instead of two.
       if(node is None):
           return ""
       if((node.left is None) and (node.right is None)):
           return str(node.value) + ", "
       #recursive case:
       if((node.left is not None) or (node.right is not None)):
           rec_str = ""
           rec_str = rec_str + str(node.value) + ", "
           rec_str = rec_str + self.__rec_pre_order(node.left)
           rec_str = rec_str + self.__rec_pre_order(node.right)
           return rec_str

  def __rec_post_order(self, node):

       if(node is None):
           return ""
       if((node.left is None) and (node.right is None)):
           return str(node.value) + ", "
       if((node.left is not None) or (node.right is not None)):
           rec_str = ""
           rec_str = rec_str + self.__rec_post_order(node.left)
           rec_str = rec_str + self.__rec_post_order(node.right)
           rec_str = rec_str + str(node.value) + ", "
           return rec_str

  def __rec_in_order(self, node):

       if(node is None):
           return ""
       if((node.left is None) and (node.right is None)):
           return str(node.value) + ", "
       if((node.left is not None) or (node.right is not None)):
           rec_str = ""
           rec_str = rec_str + self.__rec_in_order(node.left)
           rec_str = rec_str + str(node.value) + ", "
           rec_str = rec_str + self.__rec_in_order(node.right)
           return rec_str

  def __rec_to_list(self, node):
      rec_list = []
      if node is None:
          return rec_list
      rec_list.extend(self.__rec_to_list(node.left))
      rec_list.append(node.value)
      rec_list.extend(self.__rec_to_list(node.right))
      return rec_list

  def to_list(self):
       if self.get_height() == 0:
           return []
       the_list = []
       the_list.extend(self.__rec_to_list(self.__root))
       return the_list
#traversal methods:

  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control
    # variable.
    if(self.get_height() == 0):
        return "[ ]"
    string_rep = "[ "
    string_rep = string_rep + self.__rec_in_order(self.__root)
    if(len(string_rep) >= 5):
        string_rep = string_rep[0:len(string_rep)-2] #slice off trailing comma
    string_rep = string_rep + " ]"
    return string_rep

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control
    # variable.
    if self.get_height() == 0:
        return "[ ]"
    string_rep = "[ "
    string_rep = string_rep + self.__rec_pre_order(self.__root)
    if(len(string_rep) >= 5):
        string_rep = string_rep[0:len(string_rep)-2] #slice trailing comma
    string_rep = string_rep + " ]"
    return string_rep

  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control
    # variable.
    if self.get_height() == 0:
        return "[ ]"
    string_rep = "[ "
    string_rep = string_rep + self.__rec_post_order(self.__root)
    if(len(string_rep) >= 5):
        string_rep = string_rep[0:len(string_rep)-2] #slice trailing comma
    string_rep = string_rep + " ]"
    return string_rep

  def __str__(self):
      return self.in_order()

if __name__ == '__main__':
    bobke = [10, 5, 15, 3, 7, 17, 2]
    the_tree = Binary_Search_Tree()
    for bob in bobke:
        the_tree.insert_element(bob)
    the_tree.remove_element(10)
    print(the_tree.in_order())
    print(the_tree.pre_order())
    print(the_tree.post_order())



  #pass #unit tests make the main section unnecessary.
