def formal(name):
    idx2 = name.rfind(" ")
    last_name = name[idx2 +1:]
    
    result = ""
    for c in name:
        if c[0].isupper():
            result += c + ". "
    return last_name + ", " + result[:-3]
            
 