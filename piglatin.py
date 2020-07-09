# Write your code here

from string import ascii_lowercase
from string import ascii_uppercase

vowels = ['a', 'e', 'i', 'o', 'u']


def pig_latinize_one_word_vowel(string):
    if string.lower.startswith(vowels):
        return string + "yay"


def pig_latinize_one_word_single_consonant(string):
    for c in ascii_lowercase:
        if string.lower.find(c) == 0:
            return string.replace(c, "") + "-" + c + "ay"
            break
        break


def pig_latinize_one_word_multiple_consonant(string):
    for c.lower.find("a") | c.lower.find("e") | c.lower.find("i") | c.lower.find("o") | c.lower.find("u"):


