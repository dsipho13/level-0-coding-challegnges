def common_letters(x,y):
    common_char = ""
    coma = ","
    for i in range(len(x)):
        if x[i] in y and x[i] not in common_char:
            common_char = common_char + x[i]
    
    print(coma.join(common_char))

common_letters("conduct","sodom")