# MERGE SORT

# Merge Sort is a really efficient sorting algorithm. It works on Divide and Conquer
# paradigm. It divides the array in two halves (Divide) recursively then sorts and
# merge it into a sorted array (Conquer).

# Function for merging arrays divided using merge_sort function
def merge(arr, start, end):

    # Find the middle Index
    mid = (start + end) // 2

    # declaring a temp array for sorting
    tmp = [0] * len(arr)

    # a pointer at the start of arr
    i = start

    # a pointer at (mid+1) of arr
    j = mid + 1

    # another pointer (used for filling tmp array) which initially points to start of arr
    k = start

    # while i reaches mid and j reaches the end
    while i <= mid and j <= end:

        # for sorted output, we need to pick the smallest between ith and jth
        # (if i is smaller)
        if arr[i] < arr[j]:

            # place the element in tmp array
            tmp[k] = arr[i]

            # advance the pointers by 1
            k += 1
            i += 1
            
        else:
            
            # do the same if j is smaller
            tmp[k] = arr[j]
            k += 1
            j += 1

    # if one of the array is exhausted we need to copy the remaining elements to tmp
    # (if ith part is bigger)
    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1

    # do the same if jth part is bigger
    while j <= end:
        tmp[k] = arr[j]
        k += 1
        j += 1

    # at this point tmp is sorted so copy all the elements of tmp to arr
    for index in range(start, end + 1):
        arr[index] = tmp[index]


# merge_sort function
def merge_sort(arr, start, end):
    
    # if there is only one element then no need to sort
    if start >= end:
        return

    # find the mid index
    mid = (start + end) // 2

    # recursive call to merge_sort for one half of array
    merge_sort(arr, start, mid)

    # recursive call to merge_sort for the other half of the array
    merge_sort(arr, mid + 1, end)

    # merge the arrays
    merge(arr, start, end)


# Driver Code
arr = [5, 3, 23, 12, 46]

# calling merge_sort for the whole array
merge_sort(arr, 0, len(arr) - 1)

# printing the sorted array
for i in range(len(arr)):
    print(arr[i], end=" ")

# Time Complexity : O(n*log(n))
# Space Complexity : O(n)
# Inplace : No
