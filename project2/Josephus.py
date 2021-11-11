from Linked_List import Linked_List


def Josephus(ll):
    # solve the Josephus problem following the following algorithm:
    # rotate the list to the left by one position circularly,
    # and then delete the first element;
    # repeat it until there is only one element left in the list.
    # print the sequence of survivors after each death,
    # and finally print the survivor’s number.
    # TODO replace pass with your implementation
    while len(ll) > 1:
        ll.rotate_left()
        ll.remove_element_at(0)
        print(ll)
    print("The survivor is:", ll.get_element_at(0))
if __name__ == '__main__':
    n = int(input("Input the total number of people: "))
    # create a new doubly linked list object called ll
    # with n elements named 1 to n.
    ll = Linked_List()
    for n in range(1, n + 1):
        ll.append_element(n)

    print("Initial order:", ll)
    Josephus(ll)
