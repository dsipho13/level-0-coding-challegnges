def vowels(word):
    vowel_list = [ "A","E","I","O","U","a","e","i","o","u"]
    vowel = ""
    coma =","
    for i in word:
        if i in vowel_list and i not in vowel:
            vowel = vowel + i

    if vowel == "":
        print("There are no vowels in your word")
    else:
        print(f"{coma.join(vowel)}")

vowels("yyhreuieasuouioEAOUIIOYOUg")
