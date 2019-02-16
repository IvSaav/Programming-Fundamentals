'''
CALCULATOR
'''


def calculator(expr):
    
    calc = ()
    
    if type(expr) == int:
        return expr
    
    for i in expr:
        if type(i) == tuple:
            return (calculator(i),)
        else:
            calc += (i,)
            if len(calc) == 3:
                if calc[1] == "+":
                    return calc[0] + calc[2]
                elif calc[1] == "*":
                    return calc[0]*calc[2]
                else:
                    return calc[0] - calc[2]

print(calculator((6, '-', (3, '*', 2))))          
