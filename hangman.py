import os
from hangman_func import blank_list, final_word_list, hang_man, fetch_definition, random_word
import requests
import random
import json
import bs4
import asyncio

def hangman_game():
    print('Finding word...')
    final_random_word = asyncio.run(random_word())
    definition = asyncio.run(fetch_definition())

    secret_word = final_random_word
    total_characters = len(final_random_word)

    word_list = [x for x in secret_word]
    count = 7
    final_list = []
    first_blank_list = []
    final_secret_word = ''
    print(definition)
    print(' - ' * len(secret_word))
    print(f'The word has {total_characters} letter')
    letter = input('Guess a letter: ')

    def secret_word_index(word,letter,list_):
        if letter in word:
            index_pos_list = [ i for i in range(len(word)) if list_[i] == letter ]  
        return index_pos_list      

    while count != 2 and ''.join(final_list) != secret_word:
        if letter not in secret_word:
            if bool(first_blank_list) == False or final_secret_word == '':
                count -= 1
                os.system('clear')
                first_blank_list = blank_list(secret_word)
                print(definition)
                print(''.join(first_blank_list))
                print(f"You guessed {letter}, that's not in the word. You lose a life\n")
                hang_man(count)
                letter = input('Guess a letter: ')
                
            else:
                count -= 1
                os.system('clear')
                final_secret_word = ' '.join(final_list)
                print(final_secret_word)
                print(definition)
                print(f"You guessed {letter}, that's not in the word. You lose a life\n")
                hang_man(count)
                letter = input('Guess a letter: ')

        elif letter in secret_word and bool(final_list) == False:
            os.system('clear')
            index = secret_word_index(secret_word,letter,word_list)
            new_blank_list = blank_list(secret_word)
            final_list = final_word_list(index,new_blank_list,letter)
            final_secret_word = ' '.join(final_list)
            print(final_secret_word)
            print(definition)
            hang_man(count)
            first_blank_list = new_blank_list
            if ''.join(final_list) == secret_word:
                break
            else:
                letter = input('Guess a letter: ')
        
        elif letter in secret_word and bool(final_list) == True:
                os.system('clear')
                index = secret_word_index(secret_word,letter,word_list)
                final_secret_word = ' '.join(final_word_list(index,final_list,letter))
                print(final_secret_word)
                print(definition)
                hang_man(count)
                if ''.join(final_list) == secret_word:
                    break
                else:
                    letter = input('Guess a letter: ')            
    if count == 2:
        os.system('clear')
        print('  +---+  \n  |   |  \n  O   |  \n /|\  |  \n / \  |  \n      |  \n=========\n')
        print(f'The word was {secret_word}. You lose!')
    else: 
        print(f'The secret word is {secret_word}, you won!')
        
    new_game = input('Want to play again?').upper()
    while new_game not in ['YES','NO']:
        new_game = input('You must select yes or no: ').upper()
    if new_game == 'YES':
        hangman_game()
    else:
        print('Thanks for playing!')   

hangman_game()