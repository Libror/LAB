import discord
from discord.ext import commands
import json

async def is_guild_owner(ctx):
    return ctx.author.id == ctx.guild.owner.id


class Events (commands.Cog):
    def __init__ (self, bot):
        self.bot = bot


    @commands.command()
    @commands.check(is_guild_owner)
    async def prefix(self, ctx, *, pre):
        with open(r"C:\Users\USER\Desktop\LAB Testing\prefixes.json", "r") as f:
            prefixes = json.load(f)

        
        prefixes[str(ctx.guild.id)] = pre
        await ctx.send(f"New Prefix is '{pre}'")

        with open(r"C:\Users\USER\Desktop\LAB Testing\prefixes.json", "w") as f:
            json.dump(prefixes, f, indent=4)


    @commands.command()
    @commands.check(is_guild_owner)
    async def setannouncechannel(self, ctx, *, ach):
        with open(r"C:\Users\USER\Desktop\LAB Testing\announcechannel.json", "r") as f:
            annchannel = json.load(f)

        
        annchannel[str(ctx.guild.id)] = ach
        await ctx.send(f"New Announce Channel is '{ach}'")

        with open(r"C:\Users\USER\Desktop\LAB Testing\announcechannel.json", "w") as f:
            json.dump(annchannel, f, indent=4)




def setup(bot):
    bot.add_cog(Events(bot))