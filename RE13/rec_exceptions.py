'''
RECURSIVE EXCEPTIONS
'''


def rec_exceptions(l):
    
    errors = []
    for f in l:
        try:
            l2 = f()
        except Exception as x:
            errors.append(x)
        else:
            errors += rec_exceptions(l2)
    return errors



print(rec_exceptions([lambda: [lambda: [1,2,3].index(-1), lambda:
''[2]], lambda: [1,2,3][4], lambda: [lambda: [lambda: 1/0]]]))
        
        
        