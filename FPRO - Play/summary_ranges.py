def summary_ranges(astring):
    alist = astring.split(",")
    lower_bound = int(alist[0])
    mem = lower_bound
    res_list = []
    count = 1
    
    for item in alist[1:]:
        count += 1
        if int(item) != mem + 1:    # item not the same as the last one + 1? 
            result = str(lower_bound) + "->" + str(mem)
            if lower_bound == mem:  # cheking if bounds are the same
                result = str(lower_bound)
            res_list.append(result) #saving into alist
            lower_bound = int(item)
            mem = int(item)
        else:
            mem = int(item)
    return res_list
        
print(summary_ranges("1,3,4,6,7,9,10"))          