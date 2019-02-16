'''
PARSE A TUPLE
'''


def parse(filename):
    
    file = open(filename, "r")
    
    lines = file.readlines()
    cont = "".join(lines).replace(" " , "")
    lines = cont.split("\n")
    
    def new_tup(x, total = 0):
        
        if isinstance(x, tuple):
            total = 3
            return x
        
        tup = []
        for i in x[total:]:
            
            if i == "(":
                x = x[1:]
                tup += [new_tup(x)]
            elif i == ")":
                return new_tup(tuple(tup), 3)
            elif i != "(" and i != ")":
                x = x[1:]
                tup.append(int(i))
            
    res = []
    if lines[0] == "(":
        res.append(new_tup(lines[0:]))
    return tuple(res)[0]
                        
    
#    return alist


print(parse("tuple1.txt"))