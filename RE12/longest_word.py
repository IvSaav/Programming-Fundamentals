'''
LONEST WORD
'''


def longest_word(url):
    

    import urllib.request

    resp = urllib.request.urlopen("https://raw.githubusercontent.com/fpro-admin/recitas/master/words")
    file = resp.read().decode()

    response = urllib.request.urlopen(url)
    html = response.read().decode()
    words_dict = set(file.split())
    words_url = set(html.split())

    wd = words_url.intersection(words_dict)
    
    return max(wd, key = len)



print(longest_word('https://www.w3schools.com/python/python_intro.asp'))
    
    
    
    
    