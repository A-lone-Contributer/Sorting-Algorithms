# RADIX SORT

# Counting sort technique is not efficient for arrays having bigger elements as the
# size of array to store count becomes very large . For such arrays, Radix sorts works
# well. Radix sort does sorting on the basis of each digit and perform
# sorting using counting sort (used as sub-routine).

# Similar to Counting sort , Radix sort is also a non-comparison based sorting.

# Algorithm:
# For each digit i where i varies from least significant digit to the most significant digit.
# Sort input array using counting sort (or any stable sort) according to the i’th digit.


def radix_sort(arr, n):

    # find the maximum element from the array so that we can know the upper limit of exponent
    maximum = max(arr)

    # initialise the exponent as 1
    exponent = 1

    # while the maximum digit and exponent ratio is greater than 0
    while maximum / exponent > 0:
        
        # call counting sort passing exponent as a parameter
        counting_Sort(arr, n, exponent)

        # increase the exponent
        exponent *= 10


# counting_Sort function modified to work with radix_sort
def counting_Sort(arr, n, exponent):

    # variable to store the length of count array
    k = max(arr) + 1

    # create a result array of size n as we don't want to make inplace changes to original array
    result = [0] * n

    # count array of size k to store count of distinct elements
    count = [0] * k

    # store the count of each element
    for i in range(0, n):
        count[(arr[i] // exponent) % 10] += 1

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
        result[count[(arr[i] // exponent) % 10] - 1] = arr[i]

        # decrease the count
        count[(arr[i] // exponent) % 10] -= 1

        # decrease the pointer
        i -= 1

    # copy the result array to original array
    for i in range(0, n):
        arr[i] = result[i]


# Driver Code
arr = [23,343,121,5534,11,567]
n = len(arr)
radix_sort(arr, n)

for i in range(0, n):
    print(arr[i],end=" ")


# Time Complexity : O(d*(n+k))
# where d denotes the number of digits, n is the number of elements and k is the size of count array
# Space Complexity : O(n)
