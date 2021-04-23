def vowels(word):
    vowel = ""
    coma =","
    for i in word:
        if i.lower() in (["a","e","i","o","u"]) and i.lower() not in vowel:
            vowel = vowel + i.lower()
    if vowel == "":
        print("There are no vowels in your word")
    else:
        print(f"{coma.join(vowel)}")

def main():
    vowels("yyhreuieasuouioEAOUIIOYOUg")

if __name__ == "__main__":
    main()

