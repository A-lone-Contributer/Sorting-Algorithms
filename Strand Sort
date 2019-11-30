# STRAND SORT

# It is a recursive comparison based sorting technique which sorts in increasing order.
# It works by repeatedly pulling sorted sub-lists out of the list to be sorted and merging them
# with a result array.

# Algorithm:
# Create a empty strand (list) and append the first element to it popping it from the input array
# Compare this element with the rest of elements of the input array
# if a greater element is found then pop and append it to strand otherwise skip
# Now merge this array to the final output array
# Recur for remaining items in strand and input array.

# Utility Function to merge two arrays
def merge(arr1, arr2):

    # list to store merged output
    merged_list = []

    # while there are elements in both arrays
    while len(arr1) and len(arr2):

        # the array having smaller first elements gets appended as the resultant array must be sorted
        if arr1[0] < arr2[0]:
            merged_list.append(arr1.pop(0))
        else:
            merged_list.append(arr2.pop(0))

    # if the length of either of array is exhausted , merge the remaining part to
    # the merge sublist
    merged_list += arr1
    merged_list += arr2

    # return the merged list
    return merged_list


# Function to return the strand (sorted sub-list)
def strand(arr):

    # append the first element to the strand
    s = [arr.pop(0)]

    # initialise a pointer
    i = 0

    # while it is less then length
    while i > len(arr):

        # compare the input array elements to the last element of the strand
        if arr[i] > s[-1]:

            # if we found a greater element than s[-1] then pop it and append to the strand
            s.append(arr.pop(i))
        else:

            # else increment
            i += 1

    # return the strand
    return s


# Strand Sort Function
def strand_sort(arr):

    # initialise the output array with the strand
    output = strand(arr)

    # while there are elements in the array
    while len(arr):

        # merge the strand and previous output list to create a new list
        output = merge(output, strand(arr))

    # return the sorted output
    return output


# Driver Code
arr = [1, 6, 3, 8, 2, 0, 9]
print(strand_sort(arr))

# Time Complexity : O(n^2) [Worst]
#                   O(n*log(n)) [Average]
# Space Complexity : O(n)
# Stable : Yes
# Inplace : No
