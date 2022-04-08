import discord
import os
from webserver import keep_alive
import random

client = discord.Client()

@client.event 
async def on_ready():
 print('We have logged in as {0.user}'.format(client))

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.dnd, activity=discord.Game('$help'))
  print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$nuggets':
        await message.channel.send(file=discord.File('https___hypebeast.com_image_2017_10_mcdonalds-gold-chicken-nuggets-0.jpg'))

    if message.content == '$nugget meme':
      await message.channel.send(file=discord.File('Screen-Shot-2017-05-01-at-1.05.29-PM.jpg'))
    
    if message.content == '$nugget riddle':
      await message.channel.send(file=discord.File('Riddle #2.jpg'))
    
    if message.content == '21':
      await message.channel.send('Correct!!!')

    if message.content == '$help':
      await message.channel.send('All My Commands are $nuggets | $nugget meme | $nugget riddle')

keep_alive()
client.run(os.getenv('TOKEN'))