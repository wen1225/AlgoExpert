def isPalindrome(string):
    # naive solution. Build string backwards
    # T: O(k), M: O(1) where k is the length of the string
    newString = ""
    i = len(string) - 1
    while i > -1:
        newString += string[i]
        i -= 1

    return string == newString

def isPalindrome(string):
    # use two indices: front and back and compare each time they iterate over the list
    # T: O(N), M: O(1)
    i = 0
    j = len(string) - 1

    while i <= j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True
