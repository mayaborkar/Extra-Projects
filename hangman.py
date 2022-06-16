import random
from words import words
import string


def get_valid(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = get_valid(words)
    # set gives you the characters of the word
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))

        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word",  ' '.join(word_list))
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You already guessed that letter ")

        else:
            print("Invalid character")


hangman()