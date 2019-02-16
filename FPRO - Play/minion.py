'''
MINION GAME
'''


def minion(astring):
    
    v = "aeiou".upper()
    message = "The winner was {} with a total of {} points:\n{}"
    
    kevin = []
    stuart = []
    for i in range(len(astring)):
        if astring[i] in v:
            if astring[i] not in kevin:
                kevin.append(astring[i])
            temp = astring[i+1:]
            for i2 in range(len(temp)+1):
                group = astring[i] + temp[:i2]
                if group not in kevin:
                    kevin.append(group)
        else:
            if astring[i] not in stuart:
                stuart.append(astring[i])
                temp = astring[i+1:]
                for c in range(len(temp)+1):
                    group = astring[i] + temp[:c]
                    if group not in stuart:
                        stuart.append(group)
   
    stuart = sorted(stuart, key = len)
    kevin = sorted(kevin, key = len)
    
    if len(stuart) > len(kevin):
        total = 0
        sub = []
        for item in stuart:
            total += astring.count(item)
            sub.append("- " + item + ": " + str(astring.count(item)))
        return message.format("Stuart", total, "\n".join(sub))
    
    if len(kevin) > len(stuart):
        total = 0
        sub = []
        for item in kevin:
            total += astring.count(item)
            sub.append("- " + item + ": " + str(astring.count(item)))
        return message.format("Kevin", total, "\n".join(sub))
    
    return "It was a draw!"

   
print(minion("KEVIN"))
                
            
    
    
    

