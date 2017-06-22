"""
Anime Trivia Bot
Created 6/22
Authored by Iazma & Chihaya
"""
import discord
import logging
import settings
from actions import commands

client = discord.Client()

@client.event
@asyncio.coroutine on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    
@client.event
@asyncio.coroutine on_message(message):
    """ 
    """



if __name__ == '__main__':
    client.login(settings.USER, settings.PASS)
    logging.basicConfig(level=logging.INFO)
    client.run()