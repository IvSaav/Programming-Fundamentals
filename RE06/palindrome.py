#This program groups the letters of astring into groups of 2, 3, 4 and so on,
# and then checks if those groups, written backwards, read the same as written forwards

def palindrome(astring):
    count = 0
    for indx in range(0, len(astring)):
        for indx_2 in range(indx + 1, len(astring)):
            group = astring[indx:indx_2 + 1]
            if group == group[::-1]:
                count += 1
    return "For string '{}': {} palindrome substrings".format(astring, count)
