'''
Anime Trivia Bot
Created 6/22
Authored by Iazma & Chihaya
'''
import discord
from discord.ext import commands
import random

client = discord.Client()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    
@bot.command
async def 



if __name__ == '__main__':
    client.login(settings.USER, settings.PASS)
    logging.basicConfig(level=logging.INFO)
    client.run()