def vowels(word):
    vowel = ""
    coma = ", "
    for letter in word:
        if (
            letter.lower() in (["a", "e", "i", "o", "u"])
            and letter.lower() not in vowel
        ):
            vowel = vowel + letter.lower()
    if vowel == "":
        print("There are no vowels in your word")
    else:
        print(f"Vowels: {coma.join(vowel)}")


def main():
    vowels("yyhreuieasuouioEAOUIIOYOUg")


if __name__ == "__main__":
    main()
