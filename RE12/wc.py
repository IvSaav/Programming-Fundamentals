'''
WC
'''


def wc(filename):
    file = open(filename, "r")
    lines = file.readlines()
    
    n_words = 0
    n_chr = 0
    for line in lines:
        n_chr += len(line)
        n_words += len(line.split())
    
    file.close()
        
    return (len(lines), n_words, n_chr)


print(wc("shakespeare.txt"))
        
