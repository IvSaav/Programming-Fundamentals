#Given a tuple of n integers, with n > 3, write a Python function triplet(atuple) that finds a
#triplet (a, b, c) such that their sum is zero (i.e., a + b + c = 0)

def triplet(atuple):
    result = ()
    indx_1 = 0
    for item1 in atuple:
        indx_1 += 1
        indx_2 = indx_1
        for item2 in atuple[indx_1:]:
            indx_2 += 1
            for item3 in atuple[indx_2:]:
                if item1 + item2 + item3 == 0:
                    result = (item1, item2, item3)
                    return result
    if result == ():
        return ()
                    