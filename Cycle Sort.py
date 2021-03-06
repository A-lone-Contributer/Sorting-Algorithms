# CYCLE SORT

# It is a comparison based unstable sorting algorithm which is theoretically efficient in the sense
# that it has less number of writes. Cycle sort forces the array to be factored into number
# of cycles and then rotate it to get the sorted output.

# Algorithm:
# Loop through the array and find the pos by counting number of elements less than the current element
# if there is no such element leave it as it is.
# Now swap the element with its correct index and now this element which is moved needs to be
# moved to its correct position which is done by rotating the array.

def cycle_Sort(arr, n):

    # Loop through the array
    for cycleStart in range(0, n - 1):

        # store the element that will be compared with the rest for swapping
        ele = arr[cycleStart]

        # stores the correct index of ele
        loc = cycleStart

        # Find the correct index for ele
        for i in range(cycleStart + 1, n):

            # increment the loc till we encounter a greater element than ele
            if arr[i] < ele:
                loc += 1

        # If item is at its correct position then leave it as it is
        if loc == cycleStart:
            continue

        # Otherwise, put the item there or right after any duplicates.
        while ele == arr[loc]:
            loc += 1

        # swap the element with the loc found
        arr[loc], ele = ele, arr[loc]

        # Now the element from which ele is swapped is at incorrect position
        # so this code moves that element to its correct position by rotating the array
        while loc != cycleStart:

            loc = cycleStart

            # Find the correct index for ele
            for i in range(cycleStart + 1, n):

                # increment the loc till we encounter a greater element than ele
                if arr[i] < ele:
                    loc += 1

            # Take care of duplicates
            while ele == arr[loc]:
                loc += 1
            
            # swap the elements
            arr[loc], ele = ele, arr[loc]


# Driver Code
arr = [1, 9, 3, 4, 21, 10, 45, 2]
n = len(arr)
cycle_Sort(arr, n)
for i in range(n):
    print(arr[i], end=" ")


# Time Complexity : O(n^2)
# Space Complexity : O(1)
# Inplace : Yes
