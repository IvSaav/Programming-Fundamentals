def adigits(x, y, z):
    x = int(x)
    y = int(y)
    z = int(z)
    sum = 0
    if (x >= y and x >= z):
        sum = x*100
        if (y >= z):
            sum += y*10
            sum += z
        elif (z >= y):
            sum += z*10
            sum += y
    elif (y >= x and y >= z):
        sum = y*100
        if (x >= z):
            sum += x*10
            sum += z
        elif (z >= x):
            sum += z*10
            sum += x
    elif (z >= x and z >= y):
        sum = z*100
        if (x >= y):
            sum += x*10
            sum += y
        elif (y >= x):
            sum += y*10
            sum += x
    return sum


print(adigits("1", "2", "3"))
