'''
ROTATING
'''


def rotate_list(l):
    if len(l) % 2 == 0:
        tail = l[len(l)//2:]
        front = l[:len(l)//2]
        return tail + front
    else:
        front = l[:len(l)//2]
        mid = [l[len(l)//2]]
        tail = l[(len(l)//2+1):]
        return tail + mid + front

print(rotate_list([1,2,3]))