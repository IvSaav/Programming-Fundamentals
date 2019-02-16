'''
ISOMORPHIC
O Fpro teste não reconhece newline \n e as inputs não estão em string

'''

def isomorphic(astring1, astring2):
    
    # 
    res_list = []
    for i in range(len(astring1)):
        res_list.append((astring1[i], astring2[i]))
    
    # verifications
    verify = True
    dic3 = {}
    for tup in res_list:                         # key already in dic3?
        if tup[0] in dic3:
            if tup[1] != dic3[tup[0]]:            # cheking value
                verify = False
        else:
            if tup[1] in dic3 and dic3[tup[1]] == tup[1]:
                verify = False
                break
            dic3[tup[0]] = tup[1]
    
    # formating result        
    if verify:
        res_list = []
        result = "'{}' and '{}' are isomorphic because we can map: {}"
        for a in dic3.items():
            res_list.append(a)
        result = result.format(astring1, astring2, res_list)
    else:
        result = "'{}' and '{}' are not isomorphic"
        result = result.format(astring1, astring2)
    
    result = str(result)
    return result       

print(isomorphic("paper", "title"))      