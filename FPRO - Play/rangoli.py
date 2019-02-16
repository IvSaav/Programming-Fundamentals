'''
ALPHABET RANGOLI
'''


def rangoli(N):
    
    alpha = "abcdefghijklmnopkrstuvxwyz"
    
    # main line
    main = []
    for i in range(N):
        main.append(alpha[i])
    left = sorted(main[1:], reverse=True)
    main = left + main 
    
    # top
    top = []
    line = main.copy()
    for elem in line:
        mid = (len(line)-1)//2
        line = line[:mid] + line[mid+2:]
        top.append(line)
        if len(line) == 1:
            break
    #adding bars (top)
    for j in range(len(top)):
        top[j] = "-".join(top[j])
    top = top[::-1]
    
    main = "-".join(main)
    for x in range(len(top)):
        bars = "-"*((len(main)-len(top[x]))//2)
        top[x] = "{}{}{}{}".format(bars, top[x], bars, "\n")
    
    bottom = top[::-1]
    top = "".join(top)
    main += "\n"
    bottom = "".join(bottom)
    
    return top + main + bottom
    
print(rangoli(20))