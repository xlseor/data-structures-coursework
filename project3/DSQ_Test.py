import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
    def setUp(self):
        self.__deque = get_deque(1)
        self.__stack = Stack()
        self.__queue = Queue()



  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should me in a method whose name begins with test_


#Stack tests:
    def test_is_it_empty(self):
        self.assertEqual(str(self.__stack), "[ ]")

    def test_stack_push_to_empty(self):
        self.__stack.push("a")
        self.assertEqual(str(self.__stack), "[ a ]")

    def test_stack_pop_from_empty(self):
        n = self.__stack.pop()
        self.assertEqual(n, None)
        self.assertEqual(str(self.__stack), "[ ]")

    def test_stack_peek_into_empty(self):
        i = self.__stack.peek()
        self.assertEqual(i, None)

    def test_stack_push_two(self):
        self.__stack.push("a")
        self.__stack.push("b")
        self.assertEqual(str(self.__stack), "[ a, b ]")

    def test_stack_push_three(self):
        self.__stack.push("a")
        self.__stack.push('b')
        self.__stack.push('c')
        self.assertEqual(str(self.__stack), "[ a, b, c ]")

    def test_stack_push_one_pop_one(self):
        self.__stack.push("a")
        k = self.__stack.pop()
        self.assertEqual(str(self.__stack), "[ ]")
        self.assertEqual(k, "a")

    def test_stack_push_two_pop_two(self):
        arr = ['a','b']
        arr2 = ['b','a']
        for item in arr:
            self.__stack.push(item)
        for k in range(0, len(arr)):
            i = self.__stack.pop()
            self.assertEqual(i, arr2[k])
        self.assertEqual(str(self.__stack), "[ ]")

    def test_stack_push_three_pop_three(self):
        arr = ['a','b','c']
        arr2 = ['c','b','a']
        for item in arr:
            self.__stack.push(item)
        for k in range(0, len(arr)):
            i = self.__stack.pop()
            self.assertEqual(i, arr2[k])
        self.assertEqual(str(self.__stack), "[ ]")
#Queue tests:
    def test_is_the_queue_empty(self):
        k = self.__queue.dequeue()
        self.assertEqual(k, None)

    def test_enqueue_one(self):
        self.__queue.enqueue("a")
        self.assertEqual(str(self.__queue), "[ a ]")

    def test_enqueue_two(self):
        self.__queue.enqueue("a")
        self.__queue.enqueue("b")
        self.assertEqual(str(self.__queue), "[ b, a ]")

    def test_enqueue_three(self):
        self.__queue.enqueue("a")
        self.__queue.enqueue("b")
        self.__queue.enqueue("c")
        self.assertEqual(str(self.__queue), "[ c, b, a ]")

    def test_dequeue_from_empty(self):
        k = self.__queue.dequeue()
        self.assertEqual(k, None)

    def test_dequeue_one_from_one(self):
        self.__queue.enqueue("a")
        self.__queue.dequeue()
        self.assertEqual(str(self.__queue), "[ ]")

    def test_dequeue_one_from_two(self):
        self.__queue.enqueue("a")
        self.__queue.enqueue("b")
        k = self.__queue.dequeue()
        self.assertEqual("a", k)
        self.assertEqual(str(self.__queue), "[ b ]")

    def test_dequeue_two_from_two(self):
        self.__queue.enqueue("a")
        self.__queue.enqueue("b")
        k = self.__queue.dequeue()
        l = self.__queue.dequeue()
        self.assertEqual("a", k)
        self.assertEqual("b", l)
        self.assertEqual(str(self.__queue), "[ ]")

    def test_three_from_three(self):
        arr = ["a",'b','c']
        for item in arr:
            self.__queue.enqueue(item)
        for k in range(3):
            i = self.__queue.dequeue()
            self.assertEqual(arr[k], i)
        self.assertEqual(str(self.__queue), "[ ]")


    def test_dequeue_two_from_three(self):
        arr = ["a",'b','c']
        for item in arr:
            self.__queue.enqueue(item)

        self.__queue.dequeue()
        r = self.__queue.dequeue()
        self.assertEqual('b', r)
        self.assertEqual(str(self.__queue), "[ c ]")

    def test_dequeue_one_from_three(self):
        arr = ["a",'b','c']
        for item in arr:
            self.__queue.enqueue(item)
        k = self.__queue.dequeue()
        self.assertEqual("a", k)
        self.assertEqual(str(self.__queue), "[ c, b ]")



#Deque tests:
    def test_pop_front_from_empty(self):
        k = self.__deque.pop_front()
        self.assertEqual(str(self.__deque), "[ ]")
        self.assertEqual(k, None)
        self.assertEqual(len(self.__deque), 0)

    def test_pop_back_from_empty(self):
        k = self.__deque.pop_back()
        self.assertEqual(str(self.__deque), "[ ]")
        self.assertEqual(k, None)
        self.assertEqual(len(self.__deque), 0)

    def test_peek_back_empty(self):
        k = self.__deque.peek_back()
        self.assertEqual(k, None)
        self.assertEqual(str(self.__deque), "[ ]")

    def test_peek_front_empty(self):
        k = self.__deque.peek_front()
        self.assertEqual(k, None)
        self.assertEqual(str(self.__deque), "[ ]")

    def test_push_one_back_empty(self):
        self.__deque.push_back("a")
        self.assertEqual(str(self.__deque), "[ a ]")
        self.assertEqual(len(self.__deque), 1)

    def test_push_one_front_empty(self):
        self.__deque.push_front("a")
        self.assertEqual(str(self.__deque), "[ a ]")
        self.assertEqual(len(self.__deque), 1)

    def test_push_two_front(self):
        self.__deque.push_front("a")
        self.__deque.push_front("b")
        self.assertEqual(str(self.__deque), "[ b, a ]")
        self.assertEqual(len(self.__deque), 2)

    def test_push_two_back(self):
        self.__deque.push_back("a")
        self.__deque.push_back("b")
        self.assertEqual(str(self.__deque), "[ a, b ]")
        self.assertEqual(len(self.__deque), 2)

    def test_push_back_then_front(self):
        self.__deque.push_back("b")
        self.__deque.push_front("a")
        self.assertEqual(str(self.__deque), "[ a, b ]")
        self.assertEqual(len(self.__deque), 2)

    def test_push_front_then_back(self):
        self.__deque.push_front("a")
        self.__deque.push_back("b")
        self.assertEqual(str(self.__deque), "[ a, b ]")
        self.assertEqual(len(self.__deque), 2)

    def test_push_front_then_back_to_one(self):
        self.__deque.push_front("b")
        self.__deque.push_front("a")
        self.__deque.push_back("c")
        self.assertEqual(str(self.__deque), "[ a, b, c ]")
        self.assertEqual(len(self.__deque), 3)

    def test_push_back_then_front_to_one(self):
        self.__deque.push_back("b")
        self.__deque.push_back("c")
        self.__deque.push_front("a")
        self.assertEqual(str(self.__deque), "[ a, b, c ]")
        self.assertEqual(len(self.__deque), 3)

    def test_pop_two_front(self):
        self.__deque.push_front("b")
        self.__deque.push_front("a")
        n = self.__deque.pop_front()
        i = self.__deque.pop_front()
        self.assertEqual(n, "a")
        self.assertEqual(i, "b")

    def test_pop_two_back(self):
        self.__deque.push_front("b")
        self.__deque.push_front("a")
        n = self.__deque.pop_back()
        i = self.__deque.pop_back()
        self.assertEqual(n, "b")
        self.assertEqual(i, "a")


    def test_pop_front_then_back(self):
        self.__deque.push_front("b")
        self.__deque.push_front("a")
        n = self.__deque.pop_front()
        i = self.__deque.pop_back()
        self.assertEqual(n, "a")
        self.assertEqual(i, "b")

    def test_pop_back_then_front(self):
        self.__deque.push_front("b")
        self.__deque.push_front("a")
        n = self.__deque.pop_back()
        i = self.__deque.pop_front()
        self.assertEqual(n, "b")
        self.assertEqual(i, "a")

    def test_pop_front_then_back_from_three(self):
        arr = ["a", "b", "c"]
        for k in arr:
            self.__deque.push_back(k)
        a = self.__deque.pop_front()
        b = self.__deque.pop_back()
        self.assertEqual(a, "a")
        self.assertEqual(b, "c")
        self.assertEqual(str(self.__deque), "[ b ]")

    def test_pop_back_then_front_from_three(self):
        arr = ["a", "b", "c"]
        for k in arr:
            self.__deque.push_back(k)
        c = self.__deque.pop_back()
        a = self.__deque.pop_front()
        self.assertEqual(a, "a")
        self.assertEqual(c, "c")
        self.assertEqual(str(self.__deque), "[ b ]")
        self.assertEqual(len(self.__deque), 1)

if __name__ == '__main__':
  unittest.main()
