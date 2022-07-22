def binarySearch(array, target):
    # Recursive solution
    # T: O(log(n)): where n is the length of the array
    # M: O(log(d)): where d is the depth of the recursive call
    if len(array) == 0:
        return -1
    return function(array, 0, len(array)-1, target)

def function(array, start, end, target):
    if start > end:
        return -1
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return function(array, start, mid-1, target)
    else:
        return function(array, mid+1, end, target)
      
      
#
#
#

def binarySearch(array, target):
    # Iterative solution
    # T: O(log(n)): where n is the length of the array
    # M: O(1)
    if len(array) == 0:
        return -1
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1
