def countv (word):
    vowelsa = word.count("a")
    vowelse = word.count("e")
    vowelsi = word.count("i")
    vowelso = word.count("o")
    vowelsu = word.count("u")
    vowels = vowelsa + vowelse + vowelsi + vowelso + vowelsu
    return vowels
word = input("\n\nType a word\n\n")
print (f"\n\nThe word '{word}' has {countv(word)} vowels.\n\n")