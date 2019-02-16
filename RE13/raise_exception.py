'''
RAISING YOUR OWN EXCEPTIONS
'''


def raise_exception(alist, value):
    errors = []
    
    for i in alist:
        if i <= value:
            errors.append(ValueError("{} is not greater than {}".format(i, value)))
    
    return errors


print(raise_exception([3], 2))
