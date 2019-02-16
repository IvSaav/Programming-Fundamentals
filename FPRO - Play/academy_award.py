'''
ACADEMY AWARDS
'''


def academy_awards(alist):
    
    dic = {}
    for tup in alist:
        if tup[1] in dic:
            dic[tup[1]] += 1
        else:
            dic[tup[1]] = 1
    return dic

print(academy_awards([("Best Picture", "Moonlight"), ("Best Director", "La La Land"), ("Best Actor", "Manchester by the Sea"), ("Best Actress", "La La Land"), ("Best Supporting Actor", "Moonlight"),  ("Best Supporting Actress", "Fences"), ("Best Original Screenplay", "Manchester by the Sea"), ("Best Original Score", "La La Land")]))