'''
REMOVE LEADING ZEROS
For a given IP adress "ip" the function returns a new ip with all the
leading zeros removed
'''


def remove_leading(ip):
    alist = ip.split(".")
    result_list = []
    glue = "."
    for item in alist:
        item = int(item)
        result_list.append(str(item))
    return glue.join(result_list)
