# Pig Latin

## Warm-up

Pig Latin is a neat variant of English that sounds really funny spoken aloud. Here is the way to turn an english word into its corresponding Pig Latin word:
1. Add "yay" to the end of any word that starts with a vowel. This is probably the easiest place to get started.
2. For words that begin with consonant sounds, all letters before the initial vowel are placed at the end of the word sequence. Then, add "ay".
3. Apply these rules to each word in a longer phrase or sentence.

As an example, the sentence "Speaking Pig Latin is fun." would become "Eakingspay Igpay Atinlay isyay unfay."

## The Goal

While possible approaches to getting to it are varied, the goal is reasonably straightforward: to create a function called pig_latinize that accepts a English message as an argument and returns that message in Pig Latin.

Try writing lines of code to test your function in the testpiglatin.py file.

## Steps

While you can take on this puzzle in any way you please, we would recommend building up to a full solution in the following order:
1. Create a function called pig_latinize_one_word that accepts a single word as an argument and returns it in Pig Latin.
    * You'll likely want to split this into cases for words that start with vowels and those that do not.
    * Also, try to make sure that "speak" goes to "eakspay" and not "peaksay."
2. Next, create the general pig_latinize function that accepts an entire phrase.
    * Make sure to use your pig_latinize_one_word function. It will make this step far easier.
3. Stretches: How does your function handle capital letters? What about punctuation?
