# BUBBLE SORT

# Bubble sort is a very straight forward approach for sorting arrays. In this,
# a single element (the largest of all) is swapped continuously till it reaches its correct position.
# Thus in each pass , the largest element from the unsorted part is being bubbled up to the end thus
# the name bubble sort.


def bubble_sort(arr, n):

    # Traversing through the whole array
    for i in range(0, n - 1):
    
        # keeping a flag to skip the traversal if the elements are already sorted
        # which makes the algorithm more efficient
        is_swapped = False
        
        # another loop to compare the elements but as we want to decrease number of elements
        # because n-i-1 elements are getting sorted in each pass
        for j in range(0, n - i - 1):
        
            # compare the jth and (j+1)th element 
            if arr[j] > arr[j + 1]:
            
                # swap them
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
                # update flag to True
                is_swapped = True
                
        # check if elements are already sorted ,if yes,break the loop
        if not is_swapped:
            break

    # return the sorted array
    return arr


# Driver code
arr = [2, 45, 12, 8, 54, 23]
n = len(arr)
print(bubble_sort(arr, n))

# Time Complexity: O(n^2) 
# Space Complexity : O(1)
# Inplace : Yes
