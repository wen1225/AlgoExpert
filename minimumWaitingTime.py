def minimumWaitingTime(queries):
    #T: O(nlogn) where nlogn is the worst case sorting time for the sort algorithm while n is the length of the list
    #M: O(1) because sort function does it in-place
    
    queries.sort()
    currWait = 0
    totalWait = 0
    i = 1    zz
    while i < len(queries):
        currWait += queries[i-1]
        totalWait += currWait
        i += 1
    return totalWait
