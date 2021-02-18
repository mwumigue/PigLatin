

vowels = ('a', 'e', 'i', 'o', 'u')
new_Word = []
new_Phrase = []


def pig_latinize_one_word_vowel(one_word):
    one_word = one_word.lower()
    return one_word.title() + "yay"


def pig_latinize_one_word_consonant(one_word):
    new_Word.clear()
    one_word = one_word.lower()
    while one_word[0] not in vowels:
        new_Word.append(one_word[0])
        one_word = one_word[1:]
    consonant = "".join(new_Word)
    return one_word.title() + consonant + "ay"


def pig_latinize_one_word(word):
    word = word.lower()
    if word[0] in vowels:
        return pig_latinize_one_word_vowel(word)
    else:
        return pig_latinize_one_word_consonant(word)


def pig_latinize(phrase):
    phrase_list = phrase.split()
    for word in phrase_list:
        new_Phrase.append(pig_latinize_one_word(word))
    pig_latinized_phrase = " ".join(new_Phrase)
    return pig_latinized_phrase

