'''
CUT
'''


def cut(filename, delimiter, field):
    
    file = open(filename, "r")
    lines = file.readlines()
    
    if isinstance(field, int):
        tb_line = []
        for line in lines:
            line = line.replace("\n", "")
            tb_line.append(line.split(delimiter)[field-1])
    else:
        tb_line = []
        for line in lines:
            temp = []
            for f in field:
                temp.append(line.split(delimiter)[f-1])
            tb_line.append(delimiter.join(temp)) 
    file.close()

    return "\n".join(tb_line)


print(cut("data.csv", ",", [2,4]))
            
        
        
    