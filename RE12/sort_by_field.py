'''
SORT BY FIELD
'''

def sort_by_field(filename, field):
    
    emails = open(filename, "r")
#    dest = open("emails_by_{}.txt".format(field), "w")
#    email_out = open("emails_by_surname.txt", "w")
    
    srt = emails.readline()
    srt = srt.replace("\n", "")

    lines = emails.readlines()
    alist = []
    for line in lines:
        line = line.replace("\n", "")
        alist.append(line.split(","))
    
    def sort_rule(x):
        idx = srt.split(",").index(field)
        return x[idx]
    
    lines = sorted(alist, key = sort_rule)
    for i in range(len(lines)):
        lines[i] = ",".join(lines[i])

    lines = [srt] + lines
    emails.close()
    return "\n".join(lines) + "\n"
    
    
        
        
        
    
    
#print(sort_by_field("emails.txt", "surname"))


