def print_vowels(x):
    word = str(x)
    vowel_list = [ "A","E","I","O","U","a","e","i","o","u"]
    vowel = ""
    for i in range(len(word)):
        if word[i] in vowel_list and word[i] not in vowel:
            vowel = vowel + word[i]

    if vowel == "":
        print("There are no vowels in your word")
    else:
        print("The vowels are: " + vowel)


print_vowels("yyhreuieasuouioEAOUIIOYOUg")
