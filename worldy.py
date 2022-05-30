from inspect import CORO_CREATED
import random

def word_list():
    words = []
    with open("5_letter_words.txt", "r") as file:
        for line in file:
            line = line.strip()
            words += [line]
    return words

def random_word(words):
    word = random.choice(words)
    return word

def binarysearsh(guess, wl):
    wl.sort()
    start = 0
    end = len(wl) - 1
    while start <= end:
        middle = int((start + end)/ 2)
        midpoint = wl[middle]
        if midpoint > guess:
            end = middle - 1
        elif midpoint < guess:
            start = middle + 1
        else:
            return midpoint

def is_real_word(guess, wl):
    fw = binarysearsh(guess, wl)
    if fw == guess:
        return True
    else:
        return False

def check_guess(guess, guessed):
    hint = []
    hint.clear()
    hint = ['_', '_', '_', '_', '_']
    exclude = []
    exclude.clear()
    for chcnt, char in enumerate(guess):
        FL = 0
        for chcnt2, char2 in enumerate(guessed):
            if char == char2 and chcnt2 == chcnt:
                hint[chcnt] = 'X'
                exclude.append(chcnt2)
            elif char == char2 and chcnt2 != chcnt and chcnt2 not in exclude and FL == 0:
                if hint[chcnt] != 'X':
                    hint[chcnt] = 'O'
                    FL = 1
                exclude.append(chcnt2)
    return "".join(hint)

def next_guess(wl):
    isExist = False
    while isExist is False:
        guess = input("Please enter a guess: ")
        guess = guess.lower()
        isExist = is_real_word(guess, wl)
        if isExist is False:
            print("That's not a real word!")
    return guess
    
        
def play():
    wl = word_list()
    guessed = random_word(wl)
    cnt = 0
    while cnt < 6:
        guess = next_guess(wl)
        hint = check_guess(guess, guessed)
        print(hint)
        if hint == 'XXXXX':
            print("You won!")
            break
        cnt += 1
    if cnt >= 6:
        print("You lost!")
        print("The word was: " + guessed)

play()
