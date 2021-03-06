# SHELL SORT

# Shell sort is a diminishing increment sort algorithm. On each pass i sets of n/i
# items are sorted, typically with insertion sort. On each succeeding pass, i is
# reduced until it is 1 for the last pass. A good series of i values is important to efficiency.

# It is better as compared to Insertion sort as unlike insertion sort we don't compare adjacent
# elements and put them in their right place which involves a lot of swapping, instead we swap far off elements
# in the array using a gap [choose as h=h*3+1 (knuth formula)]. There a lot of other concrete sequences derived.

# Algorithm:
# Initialize the value of gap
# Divide the list into smaller sub-list of equal interval
# Sort these sub-lists using insertion sort
# Repeat until complete list is sorted

def shell_Sort(arr, n):
    
    # initialise the gap to 1
    gap = 1

    # initialise gap with the highest gap value for arr
    while gap <= n / 3:
    
        # knuth formula
        gap = 3 * gap + 1

    # Do a insertion sort for this gap size.
    # The first gap elements a[0..gap-1] are already in gaped
    # order. keep adding one more element until the entire array
    # is gap sorted
    while gap >= 1:

        # for every sub-array of (gap,n)
        for i in range(gap, n):

            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            key = arr[i]

            # shift earlier gap-sorted elements up until the correct
            # location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                j -= gap

            # put key (the original a[i]) in its correct location
            arr[j] = key

        # decrease the gap size
        gap //= 3

    # return arr
    return arr


# Driver code
arr = [3, 45, 2, 1, 23, 12, 34]
n = len(arr)
print(shell_Sort(arr, n))

# Time Complexity : O(n^(3/2))
# Space Complexity : O(1)
# Inplace : Yes
# Stable : Yes
