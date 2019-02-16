'''
FLATTEN
'''


def flatten(alist):
    
    new_list = []
    for i in alist:
        if type(i) == list:
            new_list += flatten(i)
        else:
            new_list.append(i)  
            
    return new_list
