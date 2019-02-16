# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 11:33:10 2018

@author: Ivo Saavedra
"""

def reduce_map_filter(args):
    
    from functools import reduce
     
    if isinstance(args[2], list):
        if args[0] == "map":
            return list(map(args[1], args[2]))
        elif args[0] == "filter":
            return list(filter(args[1], args[2]))
        elif args[0] == "reduce":
            return reduce(args[1], args[2])
        
    temp = reduce_map_filter(args[:2] + tuple([reduce_map_filter(args[2])]))
    return temp

print(reduce_map_filter(("reduce", lambda a,b: a+b,
("map", lambda x: 2*x,
("filter", lambda x: x%2 != 0,
[1,2,3])))))