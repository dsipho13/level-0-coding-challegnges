def common_letters(string_1, string_2):
    common_char = ""
    coma = ", "
    for i in range(len(string_1)):
        if string_1[i] in string_2 and string_1[i] not in common_char:
            common_char = common_char + string_1[i]
    print(coma.join(common_char))


def main():
    common_letters("conduct", "sodom")


if __name__ == "__main__":
    main()
