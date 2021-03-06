# PIGEONHOLE SORT

# This is a non-comparison based sorting algorithm that works for
# arrays where number of elements and the range of possible key values are approximately the
# same. To perform this sort, we need to make some holes. The number of holes needed is decided
# by the range of numbers. In each hole, items are inserted. Finally deleted from the hole and stored
# into an array for sorted order.

# Algorithm:
# Create a empty set of array i.e pigeonhole. One pigeonhole for each key in through the range of the original array.
# Iterate through the original array and put the elements in the pigeonhole corresponding to its key such that
# each pigeonhole eventually contains a list of all values with that key.
# Iterate over the pigeonhole array in order, and put elements from non-empty pigeonholes back into the original array.

def pigeonhole_sort(arr):

    # calculate the size of pigeonhole
    pig_size = max(arr) - min(arr) + 1

    # create a auxiliary array for the pigeonhole
    hole = [0] * pig_size

    # add elements to the holes at indices arr[i]-min(arr)
    for i in range(len(arr)):
        hole[arr[i] - min(arr)] += 1

    # pointer to iterate over sorted array
    i = 0

    # iterate over hole
    for j in range(pig_size):

        # while there are elements left in hole
        while hole[j]:

            # remove element from hole
            hole[j] -= 1

            # add non-empty holes to the original array
            arr[i] = j + min(arr)

            # increment the pointer
            i += 1


# Driver Code
arr = [8, 3, 2, 7, 4, 6, 8]
pigeonhole_sort(arr)
for i in range(len(arr)):
    print(arr[i], end=" ")


# Time Complexity : O(n+Range)
# Space Complexity : O(n+Range)

# Where n is the number of elements and Range is the range of input array
