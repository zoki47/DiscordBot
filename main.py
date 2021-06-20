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
global listOfCommands
listOfCommands = "$help,$gpu,$fuck Zoki,$wow"
##################################################                                              
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
#if someone writes message that is picked up by bot
@client.event
#if statement below stops function from looping when bot see's his own message
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$help'):
    await message.channel.send(listOfCommands)

  if message.content.startswith('$gpu'):
    list1 = "https://zoki47.github.io/Zoki-bot/"      
    await message.channel.send(list1) 

  if message.content.startswith('zoki'):
    await message.channel.send("<:WICKED:840687370662969364>" + ' ' + 'fuck you too')
  
  if message.content.startswith('black'):
    await message.channel.send("<:WideHard:842838001038262294>")
  
  if message.content.startswith(''):
    await message.channel.send('STFU')
    time.sleep(1000)                                                            
#if someone joins :D
@client.event
async def on_member_join(member):
  #console notification
  print("Recognised that a member called " + member.name + " joined")
  @client.event
  #if statement below stops function from looping when bot see's his own message
  async def on_message(message):
    if message.author == client.user:
        return
    else:
      await message.channel.send("Welcome" + member.mention)
#if someone leaves :(
@client.event
async def on_member_remove(member):
   #console notification
   print("Recognized that " + member.name + " left")
   @client.event
   #if statement below stops function from looping when bot see's his own message
   async def on_message(message):
     if message.author == client.user:
       return
     else: 
       await message.channel.send("Left" + member.mention)
        
client.login("ODQyMDIxNTc0OTExNzIxNTEz.YJvPsw.NTWGwkL68wfB_f2K_QZLyRskmHY")      
