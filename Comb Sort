# COMB SORT

# This algorithm is an improvement over bubble sort. Bubble sort compares the
# adjacent elements thus the gap between elements is 1 but comb sort compares
# elements with gap as 1.3 , thus comb sort removes more than one inversion counts
# and hence performs better than bubble sort and sometimes better than merge sort.

# Algorithm:
# Initialise the gap with the length of array
# keep a flag for checking already swapped elements
# While the gap is greater than 1
# Increase the gap by 1.3 and Compare elements for each gap

def comb_sort(arr, n):
    
    # initialise the gap with the length of array
    gap = n

    # initialise the flag to true
    # We have used flag so that we do not traverse the array if it is
    # already sorted
    swapped = True

    # while the gap is greater than 1 or flag is true
    while gap > 1 or swapped:

        # increase the gap by 1.3
        gap = int(gap / 1.3)

        # if gap becomes less than 1 simply return 1 
        if gap < 1:
            return 1

        # flip the flag
        swapped = False

        # compare the elements for current gap using same logic as bubble sort
        for i in range(n - gap):

            # if the current element is greater than element far by 'gap'
            if arr[i] > arr[i + gap]:
            
                # swap them
                arr[i], arr[i + gap] = arr[i + gap], arr[i]

                # flip the flag as we have swapped
                swapped = True


# Driver Code
arr = [88, 18, 31, 44, 4, 0, 8, 81, 14, 78, 20, 76, 84, 33, 73, 75, 82, 5, 62, 70]
n = len(arr)
comb_sort(arr, n)
for i in range(n):
    print(arr[i], end=" ")


# Time Complexity : O(n*log(n))
# Space Complexity : O(1)
# Inplace : Yes
# Stable : No
