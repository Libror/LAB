import discord
from discord.ext import commands

class Mod (commands.Cog):
    def __init__ (self, client):
        self.client = client


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

def setup(client):
    client.add_cog(Mod(client))