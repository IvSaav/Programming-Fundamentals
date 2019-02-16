'''
PASCAL
'''


def pascal(n):
    
    from math import factorial as fact
    
    res = []
    for i in range(n):
        new_line = []
        for j in range(i+1):
            value = fact(i)/(fact(j)*fact(i-j))
            new_line.append(str(int(value)))
        res.append(new_line)
    
    # formating
    for line in range(len(res)):
        if line == len(res)-1:
            res[line] = " ".join(res[line])
        else:
            res[line] = " ".join(res[line]) + "\n"
    
    return "".join(res)
        

print(pascal(20))