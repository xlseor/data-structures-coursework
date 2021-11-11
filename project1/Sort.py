def insertion_sort(arr):
    for k in range(1, len(arr)):
        cur = arr[k]
        j = k
        while j > 0 and arr[j-1] > cur:
            arr[j] = arr[j-1]
            j = j - 1
        arr[j] = cur

def selection_sort(arr):
    for m in range(0, len(arr)-1):
        p = m
        swap_index = m
        swap = arr[m]
        select = arr[m]
        while(p < len(arr)):
            if(arr[p] < select):
                select = arr[p]
                swap_index = p
            p += 1
        arr[m] = select
        arr[swap_index] = swap


if __name__ == '__main__':
    import time
    import random
    gotime = time.time()
    #initialize tuples as iterables for nested loops:
    #iterate across them:
    cell_nums = (1000, 2500, 5000, 7500, 10000)
    order_types = ('inc','dec','rand')

    item = 1
    #This counter makes outputs easier to read

    for cell_num in cell_nums:
        #iterate through each number of cells

        for order_type in order_types:
            #iterate through types of array ordering
            #create the randomly populated arrays here

            array1 = [None]*cell_num
            array1 = [random.randint(-150,151) for k in array1]
            #sort them to the specifications required by this test iteration
            if order_type == 'inc':
                array1.sort()
            elif order_type == 'dec':
                array1.sort(reverse = True)

            #initialize identical array
            array2 = array1.copy()
            start1= time.time()
            selection_sort(array1)
            end1 = time.time()

            start2 = time.time()
            insertion_sort(array2)
            end2 = time.time()


            print("Item:", item) #"item" refers to one array sorted the two different ways
            print("Cells:", cell_num)
            print("Array Order Type:", order_type)
            print("Time to sort by selection:", "{:.20f}".format(end1-start1))
            print("Time to sort by insertion:", "{:.20f}".format(end2-start2))
            print("\n") #skip two lines between items
            item += 1

    stoptime = time.time()

    print("This program took: ","{:.20f}".format(stoptime-gotime), "to execute.")
