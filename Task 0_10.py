def common_letters(string1,string2):
    common_char = ""
    coma = ", "
    for i in range(len(string1)):
        if string1[i] in string2 and string1[i] not in common_char:
            common_char = common_char + string1[i]
    
    print(coma.join(common_char))

def main():
    common_letters("conduct","sodom")

if __name__ == "__main__":
    main()