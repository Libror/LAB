import discord  #Use Discord.py API
from discord.ext import commands #Import the commands
from discord.ext.commands import Bot
from discord import Game
import asyncio
from itertools import cycle

TOKEN = "NTcwOTg0NjE0MDY4NDg2MTc2.XMOD1g.mTRxGYkrdPvUz2sQvm1GFXJXXoU" #Gets Bot Token

client = commands.Bot(command_prefix = '!!') #Set prefix

@client.event
async def on_ready():
    print("Bot is initalized. Version 0.0.1 lock and loaded.")


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.setbotgame = self.loop.create_task(self.change_status)

@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print("{}: {}".format(author, content))
    await client.process_commands(message) #Continues searching for commands after executing this event.

@client.command()
async def ping(ctx):
    await ctx.send("Pong!")

@client.command()
async def spaceforme(ctx, *, args): # * means multiple words given
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)

@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    print("{}: {}".format(author, content) + " got deleted") #Send a message to the server defined in variable
    await client.process_commands(message)

client.run(TOKEN)