'''
SUM OF DIGITS
'''


def rec_sum_digits(n):
#    
#    alist = []
#    while(n > 0):
#        alist.append(n % 10)
#        n = n//10
#    
#    return sum(alist)

    if n == 0:
        return n
    return rec_sum_digits(n // 10) + (n % 10)

print(rec_sum_digits(12))
        