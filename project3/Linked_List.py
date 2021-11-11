class Linked_List:
    class __Node:
        __slots__ = "val", "next", "prev"
        #streamline memory usage as on textbook page 262
        def __init__(self, val):
            # declare and initialize the private attributes
            self.val = val
            self.next = None
            self.prev = None
            # for objects of the Node class.

    def __init__(self):
        # declare and initialize the private attributes
        # for objects of the sentineled Linked_List class
        self.__length = 0
        self.__header = self.__Node(val = None)
        self.__trailer = self.__Node(val = None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__trailer.next = None
        self.__header.prev = None

    def __len__(self):
        # return the number of value-containing nodes in
        # this list.
        return self.__length

    def append_element(self, val):
        # increase the size of the list by one, and add a
        # node containing val at the new tail position. this
        # is the only way to add items at the tail position.
        newest = self.__Node(val = val)
        newest.next = self.__trailer
        newest.prev = self.__trailer.prev
        self.__trailer.prev.next = newest
        self.__trailer.prev = newest
        self.__length = self.__length + 1


    def insert_element_at(self, val, index):
        # assuming the head position (not the header node)
        # is indexed 0, add a node containing val at the
        # specified index. If the index is not a valid
        # position within the list, raise an IndexError
        # exception. This method cannot be used to add an
        # item at the tail position.
        if(val is None and index is None):
            raise TypeError
        if(index == None or type(index) is not int):
            raise IndexError
        if(index < 0 or index >= self.__length):
            raise IndexError
        newest = self.__Node(val = val)
        n = 0
        cur = self.__header
        while(n < index):
            cur = cur.next
            n = n + 1
        newest.next = cur.next
        newest.prev = cur
        cur.next.prev = newest
        cur.next = newest
        self.__length = self.__length + 1
        return


    def remove_element_at(self, index):
        # assuming the head position (not the header node)
        # is indexed 0, remove and return the value stored
        # in the node at the specified index. If the index
        # is invalid, raise an IndexError exception.

        #test for valid index type
        if(type(index) is not int):
            raise TypeError
        #test for index in valid range
        if(index < 0 or index >= self.__length):
            raise IndexError
        i = 0
        if(self.__length == 0):
            raise IndexError



        #begin current walk
        cur = self.__header
        while(i < index):
            cur = cur.next
            i = i + 1
        #retrieve value from removed node
        val = cur.next.val
        cur.next.next.prev = cur
        cur.next = cur.next.next
        self.__length = self.__length - 1
        return val

    def get_element_at(self, index):
        # assuming the head position (not the header node)
        # is indexed 0, return the value stored in the node
        # at the specified index, but do not unlink it from
        # the list. If the specified index is invalid, raise
        # an IndexError exception.
        if(type(index) is not int):
            raise TypeError
        if(index < 0 or index >= self.__length):
            raise IndexError
        if(self.__length == 0):
            raise IndexError
        k = 0
        cur = self.__header
        while(k < index):
            cur = cur.next
            k = k + 1
        return cur.next.val


    def rotate_left(self):
        # rotate the list left one position. Conceptual indices
        # should all decrease by one, except for the head, which
        # should become the tail. For example, if the list is
        # [ 5, 7, 9, -4 ], this method should alter it to
        # [ 7, 9, -4, 5 ]. This method should modify the list in
        # place and must not return a value.
        if(self.__length == 0 or self.__length == 1):
            return
        back_item = self.__header.next #Initialize an alias to store the head node,
        #instead of destroying it.
        #remove the head by updating references
        self.__header.next.next.prev = self.__header
        self.__header.next = self.__header.next.next
        #insert back_item at the back of the Linked_List
        back_item.prev = self.__trailer.prev
        back_item.next = self.__trailer
        self.__trailer.prev.next = back_item
        self.__trailer.prev = back_item
        return

    def __str__(self):
        # return a string representation of the list's
        # contents. An empty list should appear as [ ].
        # A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ].
        # You may assume that the values stored inside of the
        # node objects implement the __str__() method, so you
        # call str(val_object) on them to get their string
        # representations.
        string_rep = "[ "
        k = 0
        for item in self:
            string_rep += str(item)
            k += 1
            if k == self.__length:
                string_rep += " ]"
                return string_rep
            else:
                string_rep += ", "
        return "[ ]"



    def __iter__(self):
        # initialize a new attribute for walking through your list
        self.__iter = self.__header.next
        return self

    def __next__(self):
        # using the attribute that you initialized in __iter__(),
        # fetch the next value and return it. If there are no more
        # values to fetch, raise a StopIteration exception.
        current = self.__iter
        if current.next == None:
            raise StopIteration
        self.__iter = self.__iter.next
        return current.val


if __name__ == '__main__':
# Your test code should go here. Be sure to look at cases
# when the list is empty, when it has one element, and when
# it has several elements. Do the indexed methods raise exceptions
# when given invalid indices? Do they position items
# correctly when given valid indices? Does the string
# representation of your list conform to the specified format?
# Does removing an element function correctly regardless of that
# element's location? Does a for loop iterate through your list
# from head to tail? Your writeup should explain why you chose the
# test cases. Leave all test cases in your code when submitting.

#TEST CASES:
    #A Method-by-method testing approach is taken here
    #Initialize test list 1
    #Test __len__:
    test_list = Linked_List()
    print("Linked_List initialized.")
    print("Length of linked list:")
    print(len(test_list))
    print("String representation of Empty list:")
    print(test_list) #iterators and __str__ tested more rigorously later
#ONE: test append_element():
    print("1.  Test for append_element():")
    print("Appending elements 'foo', 'boo', [3], 5, 7.889, in that order:")

    try:
        #append a series of elements with different data types to the LL:
        test_list.append_element("foo")
        print("String representation of list with one item:")
        print(test_list, "\n")
        test_list.append_element("boo")
        test_list.append_element([3])
        test_list.append_element(5)
        test_list.append_element(7.889)
        print("Linked List:")
        print(test_list)
        print("Observe order of appended elements. \nIf it matches, append_element passes the test.\n\n")
        #We can see from the output that they have been appended in the correct order.
    except TypeError:
        #Handle exception. Nothing should have gone wrong here.
        print("TypeError: append_element() called with invalid input.\n")
        print("Now try calling append_element() with no input value:")

    try:
        test_list.append_element()
        print(test_list)
    except TypeError:
        #Catch Error resulting from no given input value. This is preferable to
        #Running the function anyway and allowing the user to unknowingly append a series
        #Of placeholders or NoneTypes to her LL
        print("TypeError: append_element() called with invalid input.\n\n")

#TWO: test insert_element_at()
    print("2. Test for insert_element_at():\n")
    print("\tTesting that length attribute of identifier Linked_List\nhas been cleared:\n")
    test_list = Linked_List()
    print(test_list)
    print("length of test_list:", len(test_list)) #make sure all attributes have been reset for this identifier
    nums = [1,2,3,4,5,6,7,8,9,0]
    print("Append elements of nums =", nums, "to test_list:")

    try:
        for num in nums:
            test_list.append_element(num)

        print(test_list)
        print("\n\n")
    except TypeError:
        print("TypeError: append_element() called with invalid input.")

    #Test cases for valid indices
    print("Try inserting at first, last, and intermediate valid indices:")

    try:
        #Index 0
        print("Try inserting '\"Z\"'at index 0:\n")
        test_list.insert_element_at(index = 0, val = "Z")
        print("test_list:")
        print(test_list)
        #test that length has been incremented. We only need to do this once because of
        #the simple structure of this function
        print("length of test_list:", len(test_list), "\n\n")
        #Insert at last valid index
        print("\nTry inserting \"foo\" at last valid index:")
        test_list.insert_element_at(index = len(test_list) - 1, val = "foo")
        print("test_list after insertion:")
        print(test_list)
        print("\n\n")
        #Insert string values at some intermediate indices
        print("insert \"pain\" at index 2:\n")
        test_list.insert_element_at(val = "pain", index = 2)
        print(test_list)
        print("\n")
        print("insert \"joy\" at index 7:\n")
        test_list.insert_element_at(index = 7, val = "joy")
        print(test_list)
        print("\n")
        print("insert \"inertia\" at index 5:")
        test_list.insert_element_at(index = 5, val = "inertia")
        print(test_list, "\n")

    except IndexError:
        print("IndexError: insert_element_at() called with invalid index.")
    #make sure intermediate insertions went to the right places:
    print("If intermediate insertions were correct, below are pain, joy, and inertia, in that order:\n")

    try:
        #Joy is at index 8 now because of insertion at index 5
        print(test_list.get_element_at(2), test_list.get_element_at(8), test_list.get_element_at(5))
    except IndexError:
        print("IndexError in get_element_at(): invalid index.")

    #Test ability to catch invalid indices
    print("Now, we'll try inserting at the following invalid indices:\n")
    print("index < 0; index >= self.__length; index = None; index = test_list\n")


    #insert at negative index

    print("Attempted insertion at -1:")
    print("Length of list is:", len(test_list))

    try:
        test_list.insert_element_at(val = "foo", index = -1)
        #Signal that method has failed the test case.
        print("Test failed. You seem to have inserted a value at a negative index. \nJim doesn't like that.\n So something went wrong.")
        #test that length has remained unchanged:
        print("The length of test_list is,", len(test_list))
    except IndexError:
        print("IndexError: Negative indexing not supported by Linked_List.\n")
    #insert at some out of bounds indices:
    print("Attempted insertion at postion", len(test_list), "which is too large:\n")

    try:
        test_list.insert_element_at("foo", len(test_list))
        print("Error: Test failed. You shouldn't have been able to insert in that location.\n")
    except IndexError:
        print("IndexError: Index out of bounds. This error has been caught successfully.\n")

    print("Attempted insertion at postion", (len(test_list) + 1), "which is too large:\n")

    try:
        test_list.insert_element_at("foo", len(test_list) + 1)
        print("Test failed. Insertion occurred in out of bounds location.\n")
    except IndexError:
        print("IndexError: Insertion index out of bounds. Error caught successfully.\n")
    #insert at index None
    print("Insert at index None:\n")

    try:
        test_list.insert_element_at("foo", None)
        print("Test failed. Insertion at None should not work.\n")
    except IndexError:
        print("IndexError: Index out of bounds. Error caught successfully.\n")
    #test nonsensical index input index = test_list
    print("Call linked list as its own index:")

    try:
        test_list.insert_element_at(index = test_list, val = "foo")
        print("Test failed. That should not have worked.")
    except IndexError:
        print("Caught error successfully. Nonsensical insertion index will not crash program.\n")
    #see if method catches error in call with no parameters.
    print("Call method with no parameters:\n")

    try:
        test_list.insert_element_at()
    except TypeError:
        print("TypeError: error caught successfully for method call with no parameters entered.\n")

    #Simulating a potentially dangerous method call, perhaps by a sleepy person
    #who doesn't remember all the parameters
    print("Attempting to insert at index without entering a value:")

    try:
        test_list.insert_element_at(4)
    except TypeError:
        print("Error caught successfully. Please enter an argument for val\n\n\n")

    print("Attempting to insert into an empty list:")
    test_list = Linked_List()
    print("Empty List: ")
    print(test_list)

    try:
        test_list.insert_element_at("foo", 0)
        #insertion into empty list not supported, because technically this is adding to the end.
        #which is only allowed through append_element().
        print("Test failed. You shouldn't be able to insert into an empty list.\n")
    except IndexError:
        print("IndexError caught successfully. Cannot insert into empty list.\n")
    #NOTE: This function will crash if given a call of the following form:
    #test_list.insert_element_at(index = 6). Testing for val == None would
    #prevent the storage of Nonetypes in the list. I do not know how to account
    #For this particular corner case

#3 Testing remove_element_at:
    print("3. Testing remove_element_at:\n\n")
    print("Initializing test list of integers 0 to 10:\n")
    nums = [k for k in range(0,11)]
    test_list = Linked_List()
    for num in nums:
        test_list.append_element(num)

    #Removing first and last elements:
    print("Removing first and last element; checking that length has been decremented:\n")
    print(test_list)
    print("Length of test_list =", len(test_list))

    try:
        test_list.remove_element_at(0)
        test_list.remove_element_at(len(test_list) - 1)
        print(test_list)
        print("Length: ", len(test_list))
    except IndexError:
        print("IndexError: removal index out of range\n")
    #Removing some intermediate elements:
    #Also use print to test value returning functionality:
    print("Test of removal from intermediate valid indices:")
    print("Initializing new list of integers 0-10\n")
    test_list = Linked_List()
    for num in nums:
        test_list.append_element(num)
    print("Test list:", test_list, "\n")
    print("Length of test_list:", len(test_list))
    print("removing elements at index 9, 7, 4, and 1\n")

    try:
        print(test_list.remove_element_at(9))
        test_list.remove_element_at(7)
        print(test_list.remove_element_at(4))
        test_list.remove_element_at(1)
        print(test_list)
        print("9 and 4 should have been printed.\n")
        print("The length is:", len(test_list), "\n\n")
    except IndexError:
        print("IndexError: invalid index for removal.\n")
    #Now test removing from negative index and positive out of range index
    #Should catch the IndexErrors
    print("Attempting to remove element from negative index and from positive out of range index:\n\n")
    print("\t Removing from index", len(test_list), "which is out of range:\n")

    try:
        test_list.remove_element_at(len(test_list))
        print("Test failed. Invalid operation not handled.")
    except IndexError:
        print("IndexError: Removal index out of range. Error caught successfully.\n")
    print("Attempting to remove from a negative index:\n")

    try:
        test_list.remove_element_at(-1)
        print("Test failed. Invalid operation not handled.\n")
    except IndexError:
        print("IndexError handled successfully. Removal index out of range.\n")
    #Now try to remove from Nonetype index:
    print("Removing from Nonetype index:\n")
    try:
        test_list.remove_element_at(None)
        print("Test failed.")
    except TypeError:
        print("TypeError: removal at Nonetype index. Error caught successfully.\n\n")
    #Now initialize a list of one element and remove that element:
    print("Initializing Linked_List of length 1 and removing the one element in it:\n\n")
    test_list = Linked_List()
    test_list.append_element("foo")

    try:
        print(test_list)
        test_list.remove_element_at(0)
        print(test_list, "\n")
    except IndexError:
        print("IndexError: Index for removal out of range or invalid.\n")
    #Now that the Linked_List has no elements, use it to test
    #What happens when you try to remove from a list with no elements
    print("Removing element from empty Linked_List", test_list)

    try:
        test_list.remove_element_at(0)
        print("Test failed. Invalid removal not handled.\t")
    except IndexError:
        print("IndexError: invalid index for removal. Exception handled successfully.\n\n")

#FOUR: Test get_element_at:
    print("4. Test of get_element_at function:\n")
    test_list = Linked_List()
    for num in nums:
        test_list.append_element(num)
    print("Linked_List test_list of integers 0-10 has been initialized:\n")
    print("Length:", len(test_list))
    print("get 1st and last element in list and print them:\n")

    try:
        print("1st:", test_list.get_element_at(0))
        #Make sure self.__length has remained unchanged
        print("length of test list:", len(test_list))
        print("Last:", test_list.get_element_at(10))
        print("length:", len(test_list))
    except IndexError:
        print("IndexError: invalid index passed to get_element_at().\n")
    #Testing inputs to negative and invalid indices:
    print("Get elements at positions 2, 4, 9\n")

    try:
        print(test_list.get_element_at(2))
        print(test_list.get_element_at(4))
        print(test_list.get_element_at(9), "\n\n")
    except IndexError:
        print("IndexError: invalid index for retrieval in get_element_at().\n")
    print("get elements from invalid indices:\n")
    #Try to get elements at negative index and out of range positive index.
    #Also index == None and index == 'foo'
    print("index == -1")

    try:
        test_list.get_element_at(-1)
        print("Test case failed. Negative index invalid but not handled.")
    except IndexError:
        print("IndexError: negative index out of range. Error caught successfully.\n\n")
    print("index = length\n")

    try:
        test_list.get_element_at(len(test_list))
        print("Test failed. IndexError from retrieval at valid index not caught.\n")
    except IndexError:
        print("IndexError in get_element_at(): index out of range. handled successfully.\n")
    print("Attempting retrieval from index = None:\n")

    try:
        test_list.get_element_at(None)
        print("Test failed.\n")
    except TypeError:
        print("TypeError in get_element_at(): None is not a valid index. Error handled.\n")
    print("Attempting retrieval from index = 'foo'\n")

    try:
        test_list.get_element_at('foo')
        print("Test failed.\n")
    except TypeError:
        print("TypeError: index must be an integer for get_element_at(). Error handled.\n\n")
#FIVE: test rotate_left:
    #print the list and rotate it one time
    #Then rotate it n times
    #Then rotate it 500n times
    #print each test case
    print("List and rotated list")
    print(test_list)
    test_list.rotate_left()
    print(test_list)
    for k in range (0,500*len(test_list)):
        test_list.rotate_left()
    print("Rotated 500 times more:", test_list)
    #__len__, __str__, __next__, and __iter__ all work, I assume
    #Or there would have been serious problems above
    #I apologize for the lack of conciseness. I didn't allow enough time and wrote this quickly.
