#imports>>>>>>>>>>>>>>>>>>>>>>>>>
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
from discord import Embed
import subprocess
import asyncio
import logging
from discord.ext import commands
##################################################
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
###################################################
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
#if someone joins :D
@client.event
async def on_member_join(member):
  print("Recognised that a member called " + member.name + " joined")
  @client.event
  async def on_message(message):
    if message.author == client.user:
        return
    else:
      await message.channel.send("Welcome" + member.mention)
#if someone leaves :(
@client.event
async def on_member_remove(member):
    print("Recognized that " + member.name + " left")
    @client.event
    async def on_message(message):
      if message.author == client.user:
        return
      else: 
        await message.channel.send("Left" + member.mention)

my_secret = os.environ['TOKEN']


client.run(my_secret)      
