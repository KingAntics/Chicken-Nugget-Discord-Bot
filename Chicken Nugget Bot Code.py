import discord
import os
from webserver import keep_alive
import random

client = discord.Client()

@client.event 
async def on_ready():
 print('We have logged in as {0.user}'.format(client))

@client.event
async def on_connect():
  await client.change_presence(activity = discord.Streaming(name = "Nuggets", url = "https://twitch.tv/kokodownunder"))
  print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '$nugget meme':
      await message.channel.send(file=discord.File(random.choice(['Screen-Shot-2017-05-01-at-1.05.29-PM.jpg', 'download(9).jpg', 'download(10).jpg', 'd39b446b798cc675230445ca03753d58.jpg', 'images(4).jpg', 'f1df90193ee9ef7c1af80ef3bfb2742c.jpg', 'thumb_i-dont-have-enough-money-for-chicken-nuggets-lets-start-50083605.png'])))
    
    if message.content == '$nugget riddle':
      await message.channel.send(file=discord.File(random.choice(['Riddle #2.jpg', 'Chicken Nugget Equation #1.png'])))
    
    if message.content == 'ewhhurweiufhweuihfhuiwe':
      await message.channel.send('Correct!!!')

    if message.content == '$help':
      await message.channel.send('All My Commands are $nuggets | $nugget meme | $nugget riddle | Use $status if you want to see the current status of the bot')

    if message.content == '$status':
      await message.channel.send('Use this link to see if the bot is online and working properly ---> https://tinyurl.com/nugget-status')

    if message.content == '$nuggets':
        await message.channel.send(file=discord.File(random.choice(['https___hypebeast.com_image_2017_10_mcdonalds-gold-chicken-nuggets-0.jpg', 'chicken-nuggets.jpg', 'cvv3s3k8b5x51.jpg', 'Mcnugget6lg.jpg', 'unnamed.jpg', 'chicken-nugget-meme.jpg'])))

keep_alive()
client.run(os.getenv('TOKEN'))
