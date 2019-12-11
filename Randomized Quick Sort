# RANDOMISED QUICK SORT

# Quick sort uses Divide and Conquer paradigm but unlike Merge sort,
# it is an inplace Sorting algorithm.

# In randomised quick sort we try to improve the worst case complexity of quick sort O(n^2)
# to O(n*log(n)) by picking a random element as a pivot instead of picking start or end element.
# A pseudo random generator function is used for this purpose

from random import randrange


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


# function for selecting a random pivot
def randomised_partition(arr, Start, End):
    
    # Select a random pivot between start and end index of arr
    random_pivot = randrange(Start, End)

    # swap this pivot with the ending element
    arr[End], arr[random_pivot] = arr[random_pivot], arr[End]

    # call partition with the new array
    return partition(arr, Start, End)


# Quick sort function
def quick_sort(arr, Start, End):
    
    if Start > End:
        return

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


# Time Complexity : O(n*log(n)) [All cases]           
# Space Complexity : O(log(n))
# Inplace : Yes
