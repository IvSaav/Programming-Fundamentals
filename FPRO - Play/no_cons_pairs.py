'''
NO PAIR OF 1S
'''


def no_consecutives1(k):
    def rec_to_base(n, base):
        hexa = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        string = ""
        while(n > 0):
            if base == 16 and n % base >= 10:
                string = hexa[n % base] + string
            else:
                string = str(n % base) + string
            n = n // base    
        return string
    
    binary = []
    for i in range(2**k):
        binary.append(rec_to_base(i, 2))
        
    count = 0    
    for item in binary:
        if "11" not  in item:
            count += 1
    
    return count
    
    
print(no_consecutives1(5))
        


    