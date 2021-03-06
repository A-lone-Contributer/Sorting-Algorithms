# COUNTING SORT

# Counting sort is a non-comparison based sorting algorithm that sorts the elements by
# counting the number of occurrences of each unique element in the array.
# The count is stored in an auxiliary array and the sorting is done by
# mapping the count as an index of the auxiliary array.

# This algorithm sorts in linear time and takes some extra space.

# NOTE : Does not work for negative elements.

# Algorithm:
# Create a auxiliary array of size k+1 where k is the maximum element in array.
# Now store the count corresponding to each distinct element in that array.
# Now update the count array by storing the cumulative count (sum of previous counts).
# Now find the index of every element from count array (how?, see the code) . Place the element at that index.

def counting_Sort(arr, n):

    # variable to store the length of count array
    k = max(arr) + 1

    # create a result array of size n as we don't want to make inplace changes to original array
    result = [0] * n

    # count array of size k to store count of distinct elements
    count = [0] * k

    # store the count of each element
    for i in range(0, n):
        count[arr[i]] += 1

    # update the count array such that now it contains actual position of
    # element from the array
    for i in range(1, k):
        count[i] += count[i - 1]

    # take a pointer at the end ( for stable sort purpose)
    i = n - 1

    # till i is less than or equal to zero
    while i >= 0:
        # update the result array with the count of element at index i after decrementing 1 (as
        # the index is 1 less than actual element)
        result[count[arr[i]] - 1] = arr[i]

        # decrease the count
        count[arr[i]] -= 1

        # decrease the pointer
        i -= 1

    # copy the result array to original array
    for i in range(0, n):
        arr[i] = result[i]


# Driver code
arr = [1, 4, 1, 2, 7, 5, 2]
n = len(arr)
counting_Sort(arr, n)
print(arr)

# Time Complexity : O(n+k)
# Space Complexity : O(n)
