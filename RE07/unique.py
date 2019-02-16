def unique(atuple):
    tresult = ()
    for i in atuple:
        if i not in tresult:
            tresult += (i,)
    return tuple(sorted(tresult))


print(unique((8, 8, 1, 3, 1, 3, 5)))
