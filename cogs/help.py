import discord
from discord.ext import commands
import json


class Help (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx):

        author = ctx.message.author
        channel = ctx.message.channel
        message = ctx.message
        emoji = "\U0001F4EC"

        with open(r"C:\Users\USER\Desktop\LAB Testing\prefixes.json", "r") as f:
            prefixes = json.load(f)
            prefix = prefixes[str(message.guild.id)]

        helpembed1=discord.Embed(title="Help Page 1", color=0xff0000)
        helpembed1.add_field(name=str(prefix) + "help", value="Opens this page", inline=False)
        helpembed1.add_field(name=str(prefix) + "ping", value="Sends a message with 'pong!' and the latency to the bot", inline=False)
        helpembed1.add_field(name=str(prefix) + "kick <player> <reason>", value="Kicks a player with given reason", inline=False)
        helpembed1.add_field(name=str(prefix) + "ban <player> <reason>", value="Bans a player with given reason", inline=False)
        helpembed1.add_field(name=str(prefix) + "clear <amount>", value="Deletes <amount> chat messages", inline=False)
        helpembed1.add_field(name=str(prefix) + "prefix <newprefix>", value="Sets the new prefix to <newprefix>", inline=False)

        await channel.send(ctx.message.author.mention + " PM sent!")
        await message.add_reaction(emoji)
        await author.send(embed=helpembed1)



def setup(bot):
    bot.add_cog(Help(bot))