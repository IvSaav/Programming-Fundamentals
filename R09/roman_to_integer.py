'''
ROMAN INTEGER

'''


def roman_to_integer(astring):
    
    symbols = {"I":1, "V":5, "X":10, "L":50, "C": 100, "D": 500, "M":1000}

    # separating digits
    alist = []
    for symb in astring:
        alist.append(symb)
    
    # fetching the values from the dictionary
    values = []
    for item in alist:
        value = symbols[item]
        values.append(value)
    
    # addition of the values
    total = 0 
    for i in range(len(values)):
        if i == len(values)-1:
            total += values[i]
        elif values[i] >= values[i+1]:
            total += values[i]
        else:
            total -= values[i]
    
    return total
        