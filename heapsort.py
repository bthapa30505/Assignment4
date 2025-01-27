import random
import time


#    This below method is used to make sure the heap property is 
#    correct for a part of the tree.
def heapify(numbers_list, heap_size, root_index):
    # Iterative implementation of heapify to maintain the heap property.
    # Avoiding recursive implementation in order to put less strain on the memory
    # :param numbers_list: The list of numbers representing the heap.
    # :param heap_size: The number of elements in the heap.
    # :param root_index: The index of the current root of the subtree.
    while True:
        largest_value_index = root_index
        left_child_index = 2 * root_index + 1
        right_child_index = 2 * root_index + 2

        # Check if the left child exists and is larger than the root
        if left_child_index < heap_size and numbers_list[left_child_index] > numbers_list[largest_value_index]:
            largest_value_index = left_child_index

        # Check if the right child exists and is larger than the largest so far
        if right_child_index < heap_size and numbers_list[right_child_index] > numbers_list[largest_value_index]:
            largest_value_index = right_child_index

        # If the largest is not the root, swap them
        if largest_value_index != root_index:
            numbers_list[root_index], numbers_list[largest_value_index] = numbers_list[largest_value_index], numbers_list[root_index]
            # Update root_index to continue heapifying the affected subtree
            root_index = largest_value_index
        else:
            # If the heap property is satisfied, break the loop
            break


#convert the list into a valid maxheap
def make_max_heap(numbers_list):
    total_items = len(numbers_list)
    # Start from the last parent node and go up to the root
    # The range(total_items // 2 - 1, -1, -1) iterates from the last non-leaf node to the 
    # root in reverse order. This ensures smaller subtrees are heapified first, 
    # maintaining the max-heap property. The loop starts at total_items // 2 - 1, 
    # stops before -1, and steps backward by -1.
    for i in range(total_items // 2 - 1, -1, -1):
        heapify(numbers_list, total_items, i)


#sort and return the list.
def heapsort(numbers_list):
    total_items = len(numbers_list)

    # Step 1: Make the list into a max-heap
    make_max_heap(numbers_list)

    # Step 2: Swap the largest item with the last item, and reduce the heap size
    for i in range(total_items - 1, 0, -1):
        # Move the largest value (at the root) to the end of the list
        numbers_list[0], numbers_list[i] = numbers_list[i], numbers_list[0]
        # Fix the reduced heap
        heapify(numbers_list, i, 0)

    return numbers_list

def print_difference(start_time, end_time, data_type):
    print(f"Time taken for {data_type}: {end_time - start_time:.6f} seconds")


#changed the values here to generate different sample of input size.
sorted = list(range(1, 20001))

#This is an array going from 10000 to 1.
sorted_descending = list(range(20000, 0, -1))

#This is a random array of 10000 number. No duplicates allowed.
random_data = random.sample(range(1, 20001), 20000)

#This is a random array of 10000 numbers. They can range from 0 to 10000 but can have duplicates.
random_data_duplicate = random.choices(range(1, 20001), k=20000)

#The below code is used to call heapsort method and record the time required to call 
# each type of data.
# Sorted data.
start_time = time.time()
heapsort(sorted)
end_time = time.time()
print_difference(start_time, end_time, "sorted data for heap sort")

#Reverse sorted data
start_time = time.time()
heapsort(sorted_descending)
end_time = time.time()
print_difference(start_time, end_time, "reverse sorted data for heap sort")

#Random data.
start_time = time.time()
heapsort(random_data)
end_time = time.time()
print_difference(start_time, end_time, "random data for heap sort")

#Random data with duplicates
start_time = time.time()
heapsort(random_data_duplicate)
end_time = time.time()
print_difference(start_time, end_time, "random data with duplicates for heap sort")