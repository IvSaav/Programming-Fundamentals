'''
GREATEST COMMON DIVISOR
'''


def rec_gcd(n1 ,n2):
    
    div1 = []
    for i in range(1, n1):
        if n1 % i == 0:
            div1.append(i)
            
    div2  = []
    for j in range(1, n2):
        if n2 % j == 0:
            div2.append(j)
            
    for x in div1:
        if x in div2:
            mx = x
            
    return mx
        
    
    
    
    
print(rec_gcd(12, 14))
