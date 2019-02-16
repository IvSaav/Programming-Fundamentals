def summary_ranges(astring):
    alist = astring.split(",")
    lower_bound = int(alist[0])
    res_list = []
    upper_bound = int(alist[0])
    glue = ","
    
    for i in range(len(alist)):

        current = int(alist[i])
        if (i + 1) > (len(alist)-1):  # fix
            if lower_bound == upper_bound:  # number is the same (7->7)
                result = str(lower_bound)
                res_list.append(result)
            else:
                result = str(lower_bound) + "->" + str(upper_bound)
                res_list.append(result)
            break
        else:
            nxt = int(alist[i + 1])
        
        if current == (nxt -1):             # next number in list is current +1?
            upper_bound = nxt
        else:                               # sequence not verified (1,2,5)

            if lower_bound == upper_bound:  # number is the same (7->7)
                result = str(lower_bound)
                res_list.append(result)
                lower_bound = nxt
            else:
                result = str(lower_bound) + "->" + str(upper_bound)
                res_list.append(result)
                lower_bound = nxt
    return glue.join(res_list)
                
            
print(summary_ranges("1,3,4,6,7,9,10"))
                
            
print(summary_ranges("0,1,2,3,4,5,7,10,11,20,21")) 