import aiohttp
from . local_settings import WORDS_API_URL_RANDOM, WORDS_API_URL_GENDER_ALL, \
    WORDS_API_URL_ALL, WORDS_API_URL_ADD


async def get_random():
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_RANDOM) as response:
            return await response.json()


async def get_next(pk):
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_GENDER_ALL+'/'+str(pk)) as response:
            status = response.status
            if status == 200:
                return await response.json()
            return None


async def get_all():
    async with aiohttp.ClientSession() as session:
        async with session.get(WORDS_API_URL_ALL) as response:
            return await response.json()


async def add_word_to_db(json_data):
    async with aiohttp.ClientSession() as session:
        async with session.post(WORDS_API_URL_ADD, data=json_data) as response:
            status = response.status
