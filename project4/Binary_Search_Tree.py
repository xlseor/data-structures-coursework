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

  def __rec_ins(self, node, value):
      if node is None:
          return self.__BST_Node(value)
      if node.value == value:
          raise ValueError
      if value > node.value:
          node.right = self.__rec_ins(node.right, value)
          self.__update_height(node)
          return node
      if value < node.value:
          node.left = self.__rec_ins(node.left, value)
          self.__update_height(node)
          return node

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
          return node
      if value < node.value:
          node.left = self.__rec_remov(node.left, value)
          self.__update_height(node)
          return node
      if value == node.value:
          if node.left is None and node.right is None:
              return None
          if node.left is not None and node.right is None:
              return node.left
          if node.left is None and node.right is not None:
              return node.right
          if node.left is not None and node.right is not None:
              val = find_min(node.right)
              node = self.__rec_remov(node, val)
              node.value = val
              return node






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
    pass

  #pass #unit tests make the main section unnecessary.
