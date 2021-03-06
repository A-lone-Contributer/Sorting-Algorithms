# QUICK SORT

# Quick sort uses Divide and Conquer paradigm but unlike Merge sort,
# it is an inplace Sorting algorithm.

# There are a lot of variations of Quick sort but we will discuss the default
# implementation here. Here we don't have to combine the end sorted array like we did in
# Merge Sort.

# High level Description:

# Select an element as pivot. (We have picked last element as pivot)
# Partition (Lomuto partitioning) the array around the pivot (A Utility function partition is used for this)
# After partitioning the pivot element will be at its final sorted position.
# The elements on the left and right are still not sorted.
# Then we pick sub-arrays, elements on the left of pivot and elements on the right
# of pivot, and we perform partitioning on them by choosing a pivot in the sub-arrays.


# Function for partitioning around pivot
def partition(arr, Start, End):

    # index of smaller element
    i = Start - 1

    # pick the last element as pivot
    pivot = arr[End]

    # loop from start to end
    for j in range(Start, End):

        # pivot is greater than current element
        if arr[j] < pivot:

            # increment the index of smaller element
            i += 1

            # swap the smaller and current element
            arr[i], arr[j] = arr[j], arr[i]

    # after the loop ends swap the end and i+1 element
    arr[i + 1], arr[End] = arr[End], arr[i + 1]

    # return the index of pivot
    return i + 1


# Quick sort function
def quick_sort(arr, Start, End):

    # Boundary Case
    if Start > End:
        return

    # if there is only one element no need to sort
    if Start == End:

        # print that element
        print(arr[Start])

    # if start is less than end
    if Start < End:

        # call partition function to get the pivot element index
        pivot = partition(arr, Start, End)

        # call quick_sort recursively for the left side of pivot
        quick_sort(arr, Start, pivot - 1)

        # call quick_sort recursively for the right side of pivot
        quick_sort(arr, pivot + 1, End)


# Driver Code
arr = [14, 1, 23, 56, 12, 8]
n = len(arr)

# call quick_sort
quick_sort(arr, 0, n - 1)

# print the array
for i in range(n):
    print(arr[i], end=" ")


# Time Complexity : O(n*log(n)) [Best and Average]
#                   O(n^2) [Worst Case]
# Space Complexity : O(log(n))
# Inplace : Yes
# Stable : No
