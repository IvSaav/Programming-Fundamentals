'''
FIBONACCI NUMBERS
'''


def fib(n):
    alist = [0, 1]
    if n == 1:
        return [0]
    for i in range(n-2):
        alist.append(alist[i] + alist[i+1])
    
    return alist


print(fib(5))