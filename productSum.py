# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.

#T: O(n) where n is the length of the array
#M: O(d) where d is the depth of the recursive call
def productSum(array, depth=1):
    sum = 0
    for i in array:
        '''
        if type(array[i]) == int:
           sum += depth * array[i]
        else:
            sum += productSum(i, depth+1)
        '''
        if type(i) is list:
            sum += productSum(i, depth+1)
        else:
            sum += i
    return sum * depth
