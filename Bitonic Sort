# BITONIC SORT

# Bitonic sort is a comparison based parallel sorting algorithm. It performs efficiently when
# implemented in hardware and parallel processor array.
# So what is a bitonic sequence?
# If a sequence is increasing and then decreasing. A rotation of Bitonic Sequence is also bitonic.

# Algorithm for constructing bitonic sequence :
# Construct a bitonic sequence from the given array. How?
# (Consider a sequence n elements. First start constructing Bitonic sequence
# by using 4 elements of the sequence. Sort the first 2 elements in ascending order and
# the last 2 elements in descending order, concatenate this pair to form a Bitonic
# sequence of 4 elements. Repeat this process for the remaining pairs of element until we find a Bitonic sequence)

# Algorithm for performing bitonic sort:
# Form bitonic sequence from the given array. After this step, the first part is sorted in ascending order and
# other half in descending order
# Compare the first element of first half,second element of second half and so on till the end and swap if
# element in the second half is found to be smaller.
# After this step, the elements in first half are smaller than the elements in the second half. The above step
# resulted in a sequence of n/2 length each so now repeat the process(second step) recursively for every sequence
# till we get a sorted array

# function to compare elements for creating bitonic sequence
def bitonic_comparator(arr, n, flag):

    # take a gap in gaps of 2
    dist = n // 2

    # run a loop for that much elements
    for i in range(dist):

        # comparison is done between the elements and is then compared with flag
        # If the flag is True then it sorts in ascending order else descending
        if (arr[i] > arr[i + dist]) == flag:
            arr[i], arr[i + dist] = arr[i + dist], arr[i]

# function to recursively sort bitonic sequences
def bitonic_merge(arr, flag):

    n = len(arr)

    # if length of array is 1 then no need to sort, just return that element
    if n == 1:
        return arr

    else:

        # compare the elements
        bitonic_comparator(arr, n, flag)

        # recursively call bitonic sort for the first part and sort according to the flag
        first = bitonic_sort(arr[:n // 2], flag)

        # recursively call bitonic sort for the second part and sort according to the flag
        second = bitonic_sort(arr[n // 2:], flag)

        # return the merged sequence
        return first + second

# function to produce a bitonic sequence
def bitonic_sort(arr, flag):

    n = len(arr)

    # if length of array is less than or equal to 1 then no need to sort
    if n <= 1:
        return arr

    else:

        # Produces a bitonic sequence by recursively sorting its two halves in opposite
        # sorting orders, and then calls bitonic_merge to make them in the same order
        first = bitonic_sort(arr[:n // 2], True)
        second = bitonic_sort(arr[n // 2:], False)
        return bitonic_merge(first + second, flag)


# Driver Code
arr = [40, 50, 11, 20, 4, 30, 21, 90]
print(bitonic_sort(arr, True))


# Time Complexity : O(n*log(n)^2)
# Space Complexity : O(n*log(n)^2)
