'''
ADD ITEM
This function receives a tupple and inserts an item at a designated index
'''


def add_item(tup, idx, item):
    if idx == (len(tup) - 1):   # insert item in last position
        result = tup[:idx] + (item, )
    elif idx == 0:
        result = (item, ) + tup[idx:]   # insert item in first position
    else:
        result = tup[:idx] + (item, ) + tup[idx:]
    return result
