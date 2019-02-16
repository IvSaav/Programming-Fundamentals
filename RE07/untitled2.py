def translate(astring, table):
    (intab, outtab) = zip(*table)
    i=0
    for ch in astring:
        i += 1
        if ch in intab:
            astring = astring.replace(intab[i], str(outtab[i]))
    return astring
  

print(translate("Testing this string...", ((' ', '--'), ('.', '!'), ('i', 'o'), ('t', 'tt'))))      