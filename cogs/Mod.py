import discord
from discord.ext import commands
import json

class Mod (commands.Cog):


    def __init__ (self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="You been kicked for no reason"):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked by {ctx.author.mention} for [{reason}]")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason="You been kicked for no given reason"):
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} was banned by {ctx.author.mention} for [{reason}]")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f"{amount} messages were deleted")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def criticalannounce(self, ctx, *, args):
        e = discord.Embed(title="Critical Announcement", color=0xff0000)
        e.add_field(name=args, value=u"\u200B", inline=False)
        await ctx.send(embed=e)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def announce(self, ctx, *, args):


        message = ctx.message

        with open(r"C:\Users\USER\Desktop\LAB Testing\announcechannel.json", "r") as f:
            annchannel = json.load(f)
            achannel = annchannel[str(message.guild.id)]

        e = discord.Embed(title="Announcement")
        e.add_field(name=args, value=u"\u200B", inline=False)
        await ctx.send(achannel[:1], embed=e)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def friendlyannounce(self, ctx, *, args):
        e = discord.Embed(title="Friendly Announcement", color=0x00FF00)
        e.add_field(name=args, value=u"\u200B", inline=False)
        await ctx.send(embed=e)





def setup(bot):
    bot.add_cog(Mod(bot))

