import discord  #Use Discord.py API
from discord.ext import commands #Import the commands
from discord.ext.commands import Bot
from discord import Game
import asyncio
from itertools import cycle
import os

TOKEN = open("TOKEN.txt", "r").read() #Gets Bot Token

bot = commands.Bot(command_prefix = "??") #Set prefix
bot.remove_command("help")

@bot.event
async def on_ready():
    print("Bot is initalized. Version 0.0.2.1 lock and loaded.")
    servers = len(bot.guilds)
    print("Active on " + str(servers) + " server")


def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

    self.setbotgame = self.loop.create_task(self.change_status)

@bot.event
async def on_message(message):
    author = message.author
    content = message.content
    print("{}: {}".format(author, content))
    await bot.process_commands(message) #Continues searching for commands after executing this event.

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def spaceforme(ctx, *, args): # * means multiple words given
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)

@bot.command()
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed()

    embed.set_author(name="**Help Information**")
    embed.add_field(name="help", value="Shows this info", inline=False)
    embed.add_field(name="ping", value="Returns Pong!", inline=False)
    embed.add_field(name="spaceforme", value="Spaces out words for you", inline=False)

    await ctx.send(author, embed=embed)

@bot.command()
async def say(ctx, *, args): # * means multiple words given
    output = ''
    for word in args:
        output += word
    await ctx.send(output)

@bot.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    print("{}: {}".format(author, content) + " got deleted") #Send a message to the server defined in variable
    await bot.process_commands(message)


for cog in os.listdir(".\\cogs"):
    if cog.endswith(".py"):
        try:
            cog = f"cogs.{cog.replace('.py', '')}"
            bot.load_extension(cog)
        except Exception as e:
            print(f"{cog} can not be loaded:")
            raise e

async def chng_pr():
    await bot.wait_until_ready()
    servers = len(bot.guilds)

    while not bot.is_closed():

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=str(servers) + " server"))

        await asyncio.sleep(30)

        await bot.change_presence(activity=discord.Game(name="V0.0.2.1"))

        await asyncio.sleep(30)

bot.loop.create_task(chng_pr())
bot.run(TOKEN)