'''
FIND LOCAL MINIMA

This function receives alist of integers and finds the local minima within a
specified neighborhood "n" and returns a list with all (local minimum, index)
pairs found.

Note: previous_value and previoux_indx were created in order to memorize 
the previous tuple in the result to return only the local minima 
with the lowest index.
'''


def local_minima(alist, n):
    n = n//2
    result = []
    previous_value = -20
    previous_idx = -20
    
    for i in range(len(alist)):
        current = alist[i]
        if (i-n) < 0:                                          # right most
            newlist = alist[i:i+n+1]
            if min(newlist) == current:                      
                result.append((current, i))
                previous_value = current
                previous_idx = i
        else:
            newlist = alist[i-n:i+n+1]                         # middle
            if min(newlist) == current:
                if previous_value == current and previous_idx == i-1:
                    previous_value = current
                    previous_idx = i
                    pass
                else:
                    result.append((current, i))
                    previous_value = current
                    previous_idx = i
    
    return result
                      