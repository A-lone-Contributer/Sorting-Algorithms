# BUCKET SORT

# Bucket sort is a distributed sorting algorithm that works by distributing the
# elements of an array into a number of buckets. Bucket sort can be implemented with comparisons
# and therefore can also be considered a comparison sort algorithm. The computational
# complexity depends on the algorithm used to sort each bucket, the number of buckets to
# use, and whether the input is uniformly distributed.

# Algorithm:
# Create n empty buckets.
# Insert the elements into each bucket.
# Sort each bucket using Insertion sort ( we can use any other sorting algorithm as well) 
# (Insertion sort preferred for small sized array otherwise merge sort or quick sort)
# Join all the buckets to create a final sorted list.


def bucket_sort(arr, n):

    # create n empty buckets
    buckets = [[] for i in range(n)]

    # result array to hold the sorted result
    result = []

    # create buckets by appending array elements to each bucket
    for i in range(n):
        bucket_index = n * arr[i]
        buckets[int(bucket_index)].append(arr[i])

    # sort individual buckets using insertion sort
    for i in range(len(buckets)):
    
        # calling insertion_sort
        insertion_sort(buckets[i], len(buckets[i]))

    # Now append the sorted buckets to the result array
    for i in range(0, len(buckets)):
        while len(buckets[i]) > 0:
            result.append(buckets[i].pop(0))

    # return the result
    return result


# Insertion sort code to sort the buckets
def insertion_sort(arr, n):
    
    # starting from 2 as the 1st element is already sorted
    for j in range(2, n):

        # picking elements one by one for key, if we don't do this step we might overwrite the number
        # while shifting
        key = arr[j]

        # keeping a index before the start for the purpose of comparing
        i = j - 1

        # i should not go beyond the lower bound of array and key must be less than current i element
        while i >= 0 and key < arr[i]:
            # insert ith element to (i+1)th
            arr[i + 1] = arr[i]

            # for the purpose of comparing in the sorted part from the current j to start i.e i>=0
            i -= 1

        # else insert key at (i+1)th index
        arr[i + 1] = key

    return arr


# Driver Code
arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
n = len(arr)
print(bucket_sort(arr, n))


# Time Complexity : O(n+k) [best and average]
# Space Complexity : O(n)
