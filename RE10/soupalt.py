'''
FILE FINDER
'''


def file_finder(dirs, file_name):
    
    # verifying i is a folder or file
    folder_name = True
    for char in file_name:
        if char == ".":
            folder_name = False
    if folder_name:
        return None
    
    path = dirs[0]
    for i in dirs:
        if type(i) == list and file_name not in i:
            path += "/{}".format(i[0])
            return dirs[0] + "/" + file_finder(i, file_name)
        if type(i) == list and file_name in i:
            path += "/{}/{}".format(i[0], file_name)
            return path
            
    
    
print(file_finder(["home",["Documents",[ "FPRO", "lists.txt", "recursion.pdf", "functions" ],[ "Python", "hello_world.py", "readme.md" ],],["Downloads",[ "Movies",[ "TV Series", "BreakingBad.mp4", "TheBigBangTheory.avi" ],"1.avi", "22", "001.mp4"],],"tmp.txt", "page.html"],"recursion.pdf" ))   