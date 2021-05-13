import discord
import os
import requests
import json
import hashlib
import hmac
import requests
import time
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from datetime import datetime
import os
import sys
import time
from discord import Status 
import subprocess


##################################################


###################################################
client = discord.Client()
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
#if someone writes message that is picked up by bot
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    listaKomandi = "Lista komandi: $gpu"
    await message.channel.send(listaKomandi)

  if message.content.startswith('$gpu'):
    import backend
    list1 = "https://zoki47.github.io/Zoki-bot/"      
    await message.channel.send(list1)  

@client.event
async def on_member_update(before, after):
    if before.status is discord.Status.offline and after.status is discord.Status.online:
        print('was offline then online')
        channel = client.get_channel(594630843297693706)  # notification channel
        await channel.send(f'{after.name} is now {after.status}')


my_secret = os.environ['TOKEN']


client.run(my_secret)      
