def uppercase(astring):
    for indx in range(3):
        char = astring[indx]
        if char.isupper():
            result = astring.upper()
            break
        else:
            result = astring.lower()   
    return result

       