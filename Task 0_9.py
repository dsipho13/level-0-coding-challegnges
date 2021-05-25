def vowels(word):
    vowel = ""
    coma = ", "
    for letter in word:
        letter = letter.lower()
        if letter in (["a", "e", "i", "o", "u"]) and letter not in vowel:
            vowel = vowel + letter
    if vowel == "":
        print("There are no vowels in your word")
    else:
        print(f"Vowels: {coma.join(vowel)}")


def main():
    vowels("yyhreuieasuouioEAOUIIOYOUg")


if __name__ == "__main__":
    main()
