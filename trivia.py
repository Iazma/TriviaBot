"""
Anime Trivia Bot
Created 6/22
Authored by Iazma & Chihaya
"""
import discord
import logging
from discord.ext import commands
import settings
import asyncio
import time

client = discord.Client()
bot_prefix = '*'
trivia_timeout = 10 #seconds to answer trivia question

"""
isCorrect(guess, question)
guess: str containing guess
question: the question being asked
Returns "True" if answer is right. Can be expanded to do the following:
-check for multiple forms of the same answer
-ignore misspellings
-etc...
I dont know if this is the best way to handle this?
"""
def is_correct(guess, question):
    if guess.lower() == question['a'].lower():
        return True
    else
        return False

@client.event
async def on_message(message):
    """
    Message handler.
    *trivia starts trivia.
    If given a paremeter (*trivia songs) it will only pick from that category.
    """
    #prevent bot from replying to itself
    if message.author == client.user:
        return

    #if trivia command, start a game
    if message.content.startswith(bot_prefix + 'trivia'):
        if trivia_session:
            return #if already in the middle of a trivia session in the channel

        #Questions consist of keys{"Question", "Answer", etc}
        #index Question from database
        ##the trivia question would be fed into this message
        sample_question = {
            "q" : "Which season was Steins;Gate aired during? \"Season YYYY\"",
            "a" : "spring 2011", #can also be a list of valid answers?
            "submitter" : "ihave3chihayas",
            "tags" : ["anime", "season"]
        }
        await client.send_message(message.channel, sample_question['q'])

        trivia_start_time = time.time()

        #def guess_check(): check for valid input(is this necessary?)

        #run this loop for the specified timeout duration
        while time.time() - trivia_start_time < trivia_timeout:
            guess = await client.wait_for_message(author=message.author) # currently the only person who can guess is the message
            if is_correct(guess, sample_question): # This will need to be changed later, current it will only accept EXACT answers
                await client.send_message(message.channel, 'Correct!')
                return
                #add point to person with correct guess
            else:
                #send "try again" and wait for next message
                await client.send_message(message.channel, 'Try Again.')
        #return default after 10 seconds
        mes = 'Time is up! The answer is {}'
        await client.send_message(message.channel, mes.format(answer))
        return


@client.event
def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')

if __name__ == '__main__':
    #client.login(settings.USER, settings.PASS)
    logging.basicConfig(level=logging.INFO)
    client.run('')
