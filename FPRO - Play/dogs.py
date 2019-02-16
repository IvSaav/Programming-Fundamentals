'''
DOG'S AGE IN DOG YEARS
recives human age and returns dog's age
'''


def dogs(h_age):
    
    if h_age <= 2:
        return h_age*10.5
    return (h_age-2)*4 + 21

print(dogs(5))