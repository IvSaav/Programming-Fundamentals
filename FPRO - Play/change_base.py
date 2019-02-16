'''
CHANGE TO BASE
'''


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

#
#    if n < base:
#        return str(n)
#    if base == 16 and n % base >= 10:
#        return rec_to_base(n//base, base) + hexa[n % base]
#    return rec_to_base(n//base, base) + str(n % base)

print(rec_to_base(142,16))