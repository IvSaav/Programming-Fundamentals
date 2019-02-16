def translate(astring, table):
#  translates a given string 'astring' using a translation table  
    for char in astring:
        for atuple in table:
            if atuple[0] == char:
                result = astring.replace((atuple[0]), str(atuple[1]))
    return result



