'''
EXCEPTION STRING
'''


def exception_str(f):
    try:
        f()
    except Exception as x:
        return x
    return "No exception was raised"
    
    
print(exception_str(lambda:1/0))