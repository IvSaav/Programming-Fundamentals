''' 
UNPACKING TUPLES
'''
def unpack_rev(atuple):
    glue = " "
    alist = list(atuple)
    alist.reverse()
    astring = glue.join(alist)
    return astring
