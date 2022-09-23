from ftplib import all_errors
from http.client import responses
from turtle import title
from urllib import response
import requests
import json
import asyncio
import bs4
import random

def blank_list(word):
    new_list = []
    character = ' - '
    for x in word:
        new_list.append(character)
    return new_list

def final_word_list(index,blank_list,letter):
    for x in index:
        blank_list[x] = letter
    return blank_list

def hang_man(count):
    if count == 6:
        print('  +---+  \n  |   |  \n  O   |  \n      |  \n      |  \n      |  \n=========\n')
    if count == 5:
        print('  +---+  \n  |   |  \n  O   |  \n  |   |  \n      |  \n      |  \n=========\n')
    if count == 4:
        print('  +---+  \n  |   |  \n  O   |  \n /|   |  \n      |  \n      |  \n=========\n')
    if count == 3:
        print('  +---+  \n  |   |  \n  O   |  \n /|\  |  \n      |  \n      |  \n=========\n')
    if count == 2:
        print('  +---+  \n  |   |  \n  O   |  \n /|\  |  \n /    |  \n      |  \n=========\n')

def wrong_letter(letter):
    count = 6
    print(f"You guessed {letter}, that's not in the word. You lose a life\n")
    hang_man(count)
    count -= 1
    letter = input('Guess a letter: ')
    return letter

async def fetch_definition():      
    task = asyncio.create_task(random_word())
    final_secret_word = await task
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{final_secret_word}"
    response = requests.get(url)
    obj = response.json()
    while not isinstance(obj,list):
        task = asyncio.create_task(random_word())
        final_secret_word = await task
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{final_secret_word}"
        response = requests.get(url)
        obj = response.json()
    else:
        dictionary = obj[0]
        definition = dictionary['meanings'][0]['definitions'][0]['definition']
        return definition
           
async def random_word():    
    url = requests.get('https://random-word-api.herokuapp.com/all')
    soup = bs4.BeautifulSoup(url.text,'lxml')
    all_words = soup.find('p').text
    list_all_words = all_words.split(',')
    list_all_words.pop(0)
    random_index = random.randint(0,len(list_all_words))
    new_random_word = list_all_words[random_index]
    remove_first_character = new_random_word[1:]
    final_random_word = remove_first_character[:-1]
    return final_random_word
