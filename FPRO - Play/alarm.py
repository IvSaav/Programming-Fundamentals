'''
ALLARM CLOCK
'''


def alarm(hour, minute):
    
    from datetime import timedelta
    result = timedelta(hours = 6, minutes = 51) + timedelta(hours = hour, minutes = minute)
    result = "{}".format(result)
    
    # more then 24 hours
    if len(result) > 8:
        result = result[7:11]
     
    # formating hours
    if result[1] == ":":
        result = "0" + result
    return result[:5]
        
    
print(alarm(24, 10))   