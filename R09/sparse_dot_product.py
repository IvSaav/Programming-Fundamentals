'''
SPARSE DOT PRODUCT

'''

def sparse_dot_product(dict1, dict2):
    
    key_list = list(dict1.keys())
    prod = 0
    for key in key_list:
        if key in dict2:
            prod += dict1[key] * dict2[key]
    
    return prod
