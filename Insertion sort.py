# INSERTION SORT

# It is the most basic algorithm for sorting. It is analogous to how we sort the
# deck of cards.
# It is a stable and inplace sorting algorithm.

# It iterates the input elements by growing the sorted array at each iteration
# and compares the current element with the largest value in the sorted array.
# If the current element is greater, then it leaves the element in its place and moves on to the next element
# else it finds its correct position in the sorted array and moves it to that position.
# This is done by shifting all the elements, which are larger than the current element,
# in the sorted array to one position ahead.

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


# Driver code
arr = [10, 43, 67, 2, 6, 14]
n = len(arr)
print(insertion_sort(arr, n))

# Time Complexity: O(n^2)
# Auxiliary Space: O(1)


