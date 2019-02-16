'''
PALINDORME INDEX
This function receives a string and return -1 if the string is a palindrome;
otherwise it returns the index of the first letter that if removed causes the 
string to be palindrome.
'''


def palindrome_index(s):
    result = -1
    if s == s[::-1]:
        return -1
    else:
        for i in range(len(s)):
            new = s[:i] + s[i+1:]
            if new == new[::-1]:
                result = i
    return result
