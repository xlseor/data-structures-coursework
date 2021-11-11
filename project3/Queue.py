from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()

  def __str__(self):
    # TODO replace pass with your implementation.
    return str(self.__dq)

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    # We enqueue at the front and dequeue at the back
    self.__dq.push_front(val)

  def dequeue(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_back()


# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
