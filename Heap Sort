# HEAP SORT

# A Binary Heap is a Complete Binary Tree where items are stored in a special order such
# that value in a parent node is greater(or smaller) than the values in its two children
# nodes. The former is called as max heap and the latter is called min heap. The heap can be
# represented by binary tree or array.

# Heapsort (comparison based sort) is similar to selection sort as we're repeatedly choosing the largest item and
# moving it to the end of our array. The main difference is that instead of scanning
# through the entire array to find the largest item, we convert the array into a max heap to speed things up.

# Algorithm:
# Our first step is to transform the input array into a max heap ("heapify" it).
# Max heap stores the largest element at the root so replace the root with the last item
# following by decrease-key() which reduces the size of heap by 1. Heapify the root.
# Repeat the steps till we have a heap of size>1.

from math import floor

# heap_sort function
def heap_sort(arr, n):
    
    # build a max_heap
    build_max_heap(arr, n)

    # find the last element index
    last_element = n - 1

    # as long as there is a last element in heap
    while last_element:
        # call swap to swap root and last_element
        swap(arr, 0, last_element)

        # heapify the rest of the tree after swapping
        heapify(arr, 0, last_element)

        # decrease the last element index
        last_element -= 1


# function to build_max_heap
def build_max_heap(arr, n):
    
    # find the index to place the root
    i = floor(n / 2 - 1)

    # while there are elements in the array
    while i >= 0:
        
        # heapify them to build max_heap
        heapify(arr, i, n)

        # decrease the index
        i -= 1


# utility function for swapping root and last element
def swap(arr, root, last_element):
    
    # swap the root and last_element
    arr[root], arr[last_element] = arr[last_element], arr[root]


# heapify the heap
def heapify(arr, i, max_len):
    
    # while the index is greater than the maximum length of heap yet created
    while i < max_len:

        # make i as root_index
        root_index = i

        # assign value to left_child_index
        left_child_index = 2 * i + 1

        # assign value to right_child_index
        right_child_index = 2 * i + 2

        # check if the heap is full or not and if the root is less than left index make it the new root
        if left_child_index < max_len and arr[root_index] < arr[left_child_index]:
            root_index = left_child_index

        # check if the heap is full or not and if the root is less than right index make it the new root
        if right_child_index < max_len and arr[root_index] < arr[right_child_index]:
            root_index = right_child_index

        # if there is only one node
        if root_index == i:
            
            # simply return
            return

        # swap elements
        swap(arr, i, root_index)

        # store root index in i
        i = root_index


# Driver Code
arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
heap_sort(arr, n)

# printing the array
for i in range(n):
    print(arr[i])


# Time Complexity:
# build_max_heap() - O(n)
# heapify() - O(log(n))
# heap_sort() - O(n*log(n))

# Space Complexity : O(1)
# Inplace : Yes
# Stable : No
