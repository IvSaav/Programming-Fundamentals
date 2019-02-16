def sort_grades(records):
#    Sorts grades based on average, then by ascending order and finally by student number
#    Returns the sorted records as a tuple
    
    def sort_rule(item):
#        Key rule for sorting grades
        avrg = -float(sum(item[2]))/max(len(item[2]), 1)
        return (avrg, item[0], item[1]) 
    
    return tuple(sorted(records, key = sort_rule, reverse = False))
    
    