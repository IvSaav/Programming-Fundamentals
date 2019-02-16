def summary(text):
    
    alist = text.split(" ")
    
    count = 0
    for word in alist:
        word = word.lower()
        if "e" in word:
            count += 1
    
    return (len(alist), count)

print(summary("A fool thinks himself to be wise, but a wise man knows himself to be a fool."))
        