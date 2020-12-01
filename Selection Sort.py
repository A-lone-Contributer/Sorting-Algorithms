# SELECTION SORT

# This algorithm works by repeatedly finding the minimum element from unsorted
# part of array and inserting it at the right place.

def selection(arr, n):

    # traversing the whole array
    for i in range(n):
    
        # setting the first element as the index of min element
        index_of_min = i
        
        # loop to find the minimum element except the ith element as it is taken as min
        for j in range(i + 1, n):
        
            # if min index element less than the encountered element then the current element is
            # new minimum
            if arr[index_of_min] < arr[j]:
            
                # save the index of new minimum
                index_of_min = j
                
        # swap it so that it is in its right place
        arr[i], arr[index_of_min] = arr[index_of_min], arr[i]
        
    # return the sorted array
    return arr


# Driver code
arr = [4, 22, 56, 1, 7]
n = len(arr)
print(selection(arr, n))

# Time Complexity : O(n^2)
# Space Complexity : O(1)
# Inplace : Yes
