import asyncio
import requests
import bs4
import random

async def fetch_definition():      
    task = asyncio.create_task(random_word())
    final_secret_word = await task
    print(final_secret_word)
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{final_secret_word}"
    response = requests.get(url)
    obj = response.json()
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

print(asyncio.run(fetch_definition()))

# async def func():
#     task = asyncio.create_task(func2())
#     await task
#     print('Hello')

# async def func2():
#     await asyncio.sleep(5)
#     print('good bye')

# asyncio.run(func())