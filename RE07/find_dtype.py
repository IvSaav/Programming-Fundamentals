def find_dtype(atuple, data_type):
    tresult = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            tresult += (i,)
    return tuple(tresult)


print(find_dtype((1, 2, 3), "int"))
