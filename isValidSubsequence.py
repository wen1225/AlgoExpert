def isValidSubsequence(array, sequence):
# T: O(n) where n is the size of the larger array
# M: O(1) 
    if (len(sequence) == 0):
        return true
    i = 0
    j = 0
    while (i < len(array) and j < len(sequence)):
        if (array[i] == sequence[j]):
            j+=1
        i+=1
    return True if j == len(sequence) else False
