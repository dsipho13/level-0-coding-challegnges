def common_letters(x,y):
    """ a function that returns common letters
    """
    x = str(x)
    y = str(y)
    common_char = ""
    for i in range(len(x)):
        if x[i] in y and x[i] not in common_char:
            common_char = common_char + x[i] + ", "
    
    print(common_char[:-2])

common_letters("common","column")