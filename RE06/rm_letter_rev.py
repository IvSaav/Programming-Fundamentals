def rm_letter_rev(l, astr):
    result = ""
    for c in astr:
        if c != l:
            result = c + result
    return result

