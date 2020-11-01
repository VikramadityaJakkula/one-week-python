"""In computer science, binary search, also known as half-interval search, 
logarithmic search, or binary chop, is a search algorithm 
that finds the position of a target value within a sorted array. 
Binary search compares the target value to the middle element 
of the array.
Class: Search algorithm
Data structure: Array
Worst-case space complexity: O(1)
Worst-case performance: O(log n)
"""

def binarysearchiterative(A,key):
    low = 0
    high = len(A) - 1
    while (low <= high):
        mid = int((low + high) / 2)
        if (A[mid]== key):
            return "Found"
        elif (key < A[mid]):
            high = mid - 1
        else:
            low = mid + 1
    return "not found"

def binarysearchrecursive(A,key,low,high):
    if (low >= high):
        return "Not found error in params"
    else:
        mid = ((low + high) // 2)
        if (key == A[mid]):
            return "found"
        elif (key < A[mid]):
            binarysearchrecursive(A,Key,low,mid-1)
        else:
            binarysearchrecursive(A,Key,mid+1,high)
        #return "not found"


A = [10,20,30,40,50]
Key = 36
Found = binarysearchiterative(A,Key)
print("Iterative Binary Search element is", Found)
A = [10,20,30,40,50]
Key = 10
RFound = binarysearchrecursive(A,Key,0,5)
print("Recursive binary search element is",RFound)





