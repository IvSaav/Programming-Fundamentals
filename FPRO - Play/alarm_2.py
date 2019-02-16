'''
ALLARM CLOCK
'''


def alarm(hour, minutes):
    
    alarm = 6.85
    minutes = minutes/60
    delt = hour + minutes + alarm
    
    
    return delt//23, (delt % 23) * 60

print(alarm(5, 10))
    
    
    