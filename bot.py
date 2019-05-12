import discord  #Use Discord.py API
from discord.ext import commands #Import the commands
from discord.ext.commands import Bot
from discord import Game
import asyncio
from itertools import cycle
import os
import json


async def get_prefix(bot, message):

    if not message.guild:
        return commands.when_mentioned_or("!!")(bot, message)


    with open("prefixes.json", "r") as f:
        prefixes = json.load(f)


    prefixes[str(message.guild.id)] = "!!"
    guildowner = message.guild.owner


    await bot.wait_until_ready()


    if str(message.guild.id) not in prefixes:  

        guildowner.send("Thanks for inviting LAB! Before you can get started with the bot, please run !!prefix YOURPREFIX first.")

        with open("prefixes.json", "w") as f:
            json.dump(prefixes, f)

        return commands.when_mentioned_or("!!")(bot, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(bot, message)


TOKEN = open("TOKEN.txt", "r").read() #Gets Bot Token
bot = commands.Bot(command_prefix = get_prefix) #Set prefix
bot.remove_command("help")


@bot.event
async def on_guild_join(guild):
    owner = guild.owner

    joinembed=discord.Embed(title="Welcome!", color=0x0000ff)
    joinembed.add_field(name="Getting Started", value="To get the bot running use this command: ", inline=False)
    joinembed.add_field(name="Command", value="!!prefix !! or !!prefix YOURPREFIX", inline=False)

    await owner.send(embed=joinembed)

@bot.event
async def on_ready():
    print("Bot is initalized. Version 0.0.4 lock and loaded.")
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

@bot.event
async def on_join(ctx):
    owner = ctx.guild.owner.id

    infoembed=discord.Embed(title="Starting Information", color=0x00FF00)
    infoembed.add_field(name="Getting Started", value="To get the bot running use this command: ", inline=False)
    infoembed.add_field(name="Command", value="!!prefix YOURPREFIX", inline=False)

    await owner.send(embed=infoembed)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! {0}".format(round(bot.latency, 1)))

@bot.command()
async def spaceforme(ctx, *, args): # * means multiple words given
    output = ''
    for word in args:
        output += word
        output += ' '
    await ctx.send(output)


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
    if cog.endswith(".py") and not cog.startswith("_"):
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

        await bot.change_presence(activity=discord.Game(name="V0.0.4"))

        await asyncio.sleep(30)


async def on_command_error(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("You don't have the permission to do that!")
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("This command is not existing")


    raise error




bot.loop.create_task(chng_pr())
bot.run(TOKEN)
