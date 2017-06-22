import discord
from discord.ext import commands
import random

description = '''Trying a basic bot out

There are a few things to work on.'''

bot = commands.Bot(command_prefix='?', description = description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-----')
    
@bot.command
async def 