def common_letters(string_1, string_2):
    common_char = ""
    coma = ", "
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    for i in range(len(string_1)):
        if string_1[i] in string_2 and string_1[i] not in common_char:
            common_char = common_char + string_1[i]
    print(f"Common letters: {coma.join(common_char)}")


def main():
    common_letters("cOnduct", "sodom")


if __name__ == "__main__":
    main()
