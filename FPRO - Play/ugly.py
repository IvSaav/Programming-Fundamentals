'''
UGLY NUMBER
This function receives a number "n" and checks if it is an ugly number.
Ugly numbers are positive numbers whose prime facors only include 2, 3, 5.
'''


def ugly(n):
    
    # returns a list with the prime divisors of a number
    def prime_div(x):
        alist = []
        if x == 2:
            return [2]
        if x < 0:
            x = -x
        for i in range(2, x+1):
            if i == 2 and x % 2 == 0:
                alist.append(i)
            if x % i == 0 and i % 2 != 0:
                alist.append(i)
        return alist
    
    ugly = [2, 3, 5]
    divisors = prime_div(n)
    
    for num in divisors:
        if num not in ugly:
            return False
    
    return True
    
print(ugly())   