def vowels(word):
    vowel = ""
    coma =","
    for i in word:
        if i in ([ "A","E","I","O","U","a","e","i","o","u"]) and i not in vowel:

            vowel = vowel + i
    if vowel == "":

        print("There are no vowels in your word")
    else:

        print(f"{coma.join(vowel)}")


vowels("yyhreuieasuouioEAOUIIOYOUg")

