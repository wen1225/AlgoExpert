def sortedSquaredArray(array):
    # T: O(n) where n is the length of the array
    # M: O(n) where n is the length of the array
    headPtr = 0
    tailPtr = len(array) - 1
    posPtr = len(array) - 1
    newArray = [0] * len(array)
    for i in array:
        if abs(array[headPtr]) > abs(array[tailPtr]):
            newArray[posPtr] = pow(array[headPtr], 2)
            headPtr += 1
        else:
            newArray[posPtr] = pow(array[tailPtr], 2)
            tailPtr -= 1
        posPtr -= 1
    return newArray
