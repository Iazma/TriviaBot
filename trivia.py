"""
Anime Trivia Bot
Created 6/22
Authored by Iazma & Chihaya
"""
import discord
import logging
import settings
import asyncio
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
    Message handler. 
    *trivia starts trivia. 
    If given a paremeter (*trivia songs) it will only pick from that category.
    """
    
    # *trivia start
    if message.content.startswith('*trivia'):
        yield from client.send_message(message.channel, 'TRIVIA QUESTIONS HERE')
        
        def guess_check():
           
        guess = yield from client.wait_for_message(timeout=10.0, author=message.author, check=guess_check)
        #answer = question.getAnswer
    if guess is None:
        mes = 'Times up! The answer is {}'
        yield from client.send_message(message.channel, mes.format(answer))
        return
    if guess.content == answer: # This will need to be changed later, current it will only accept EXACT answers
        yield from client.send_message(message.channel, 'Correct!')
        #add point to person with correct guess
    else:
        yield from client.send_message(message.channel, 'Incorrect.')



if __name__ == '__main__':
    client.login(settings.USER, settings.PASS)
    logging.basicConfig(level=logging.INFO)
    client.run()