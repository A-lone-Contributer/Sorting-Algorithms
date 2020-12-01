# COCKTAIL SORT

# This is a variant of bubble sort which compares adjacent elements and swaps largest elements to end by
# traversing from start to end and then from end to start bubbling smaller elements to the start due to
# which it is also known as bidirectional bubble sort. It is less than twice as fast as bubble sort.

# Algorithm:
# Traverse the array from left to right comparing adjacent elements and swapping if left value is
# greater than the element on the right. After each pass, the largest element is at the end.
# The second step is to Traverse the array from right to left comparing adjacent elements and swapping if right value is
# smaller than the element on the right. After each pass, the smallest element is at the start.

def cocktail_sort(arr, n):

    # flag to check whether the array is already sorted or not
    swapped = True

    while swapped:

        # reset the flag it might be true from a previous iteration
        swapped = False

        # loop through all the elements
        for i in range(0, n - 1):

            # compare the adjacent elements and if left is greater than right
            if arr[i] > arr[i + 1]:

                # swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                # set the flag to true
                swapped = True

        # if the previous loop was not run then break as array is already sorted
        if not swapped:
            break

        # reset the swapped for the second pass
        swapped = False

        # loop through the array backwards leaving the least element
        for i in range(n - 2, -1, -1):

            # compare the adjacent elements and if left is smaller than right
            if arr[i] > arr[i + 1]:
                
                # swap them
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # set the flag to true
                swapped = True
                
    # return the sorted array
    return arr


# Driver Code
arr = [25, 12, 43, 67, 33, 1]
n = len(arr)
print(cocktail_sort(arr, n))


# Time Complexity : O(n^2)
# Space Complexity : O(1)
# Inplace : Yes
