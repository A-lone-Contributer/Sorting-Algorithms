# BINARY INSERTION SORT

# It is the most basic algorithm for sorting. It is analogous to how we sort the
# deck of cards. Running time of insertion sort is O(n^2) but we can make the
# average runtime faster using binary search (how?)
# As we know insertion sort requires a lot of comparisons to find the correction position of
# the key in question so we can apply binary search to find the index where the element needs
# to be placed.

# Algorithm:
# Run Insertion sort which partitions the array into sorted and unsorted part on each iteration.
# Now for the sorted part , run binary search to find the correct position of key.
# Repeat till we get sorted array.

def insertion_sort(arr):

    # loop through the array
    for i in range(2, len(arr)):

        # select a key element
        key = arr[i]

        # find the position where the key must be inserted
        pos = binary_search(arr, key, 0, i) + 1

        # loop through the sorted part
        for k in range(i, pos, -1):
        
            # shift all the elements
            arr[k] = arr[k - 1]

        # insert the key at its position
        arr[pos] = key


# Binary Search Sub-routine
def binary_search(arr, key, start, end):

    # if there is only one element in the array
    if end - start <= 1:

        # if less than key
        if key < arr[start]:

            # return previous index
            return start - 1

        else:

            # else return the element
            return start

    # calculate the index of middle element
    mid = (start + end) // 2

    # if the element might be present
    # in right sub-array so update the start and end accordingly
    if arr[mid] < key:

        # recursive call
        return binary_search(arr, key, mid, end)

    # else if element is smaller than mid, then it
    # can only be present in left sub-array so update the start and
    # end accordingly
    elif arr[mid] > key:

        # recursive call
        return binary_search(arr, key, start, mid)

    else:

        # If element to be searched is the middle element
        # return the middle element
        return mid


# Driver code
arr = [2, 34, 12, 1, 65, 5]
insertion_sort(arr)
print('Sorted list: ', end='')
print(arr)

# Time Complexity: O(n*log(n))
# (worst is still O(n^2))
# To run in O(n*log(n)) both insertion sort and binary search should be avg case
# Space Complexity : O(1)
# Inplace : Yes
# Stable : Yes
