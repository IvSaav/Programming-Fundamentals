'''
LIST MANIPULATION
This function receives a list with commands and alters another given list
accordingly
(Tentar usar eval)
'''


def manipulator(l, cmds):
    result = ""
    for cmd in cmds:
        cmd = cmd.split(" ")
        if cmd[0] == "insert":
            l.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == "print":
            result += str(l) + " "
        elif cmd[0] == "remove":
            l.remove(int(cmd[1]))
        elif cmd[0] == "append":
            l.append(int(cmd[1]))
        elif cmd[0] == "sort":
            l.sort()
        elif cmd[0] == "pop":
            del l[len(l)-1]
        elif cmd[0] == "reverse":
            l.reverse()
    return result
