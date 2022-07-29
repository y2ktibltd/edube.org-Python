#!/bin/python3
user_word=input("Enter a word to eat vowels from: ")
for letter in user_word:
    if letter.upper() in "AEIOU":
        continue
    else:
        print(letter.upper())
