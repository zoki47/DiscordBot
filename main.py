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
from gtts import gTTS
import subprocess


##################################################


###################################################
client = discord.Client()
  

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$gpu'):
    import backend
    list1 = "https://replit.com/@zoki47/Zoki-bot#Graficke_Kartice.html"


    
    await message.channel.send(list1)  

my_secret = os.environ['TOKEN']


client.run(my_secret)      
