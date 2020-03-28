import discord
from discord.ext import commands
from data import dict_PC, dict_NPC, dict_ITEM

class List(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #list command and it's subcommands with dictionaries
    @commands.group()
    async def list(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid command - no type detected.')

    @list.command()
    async def PC(self, ctx):
        for item in dict_PC:
            await ctx.send(item)

    @list.command()
    async def NPC(self, ctx):
        for item in dict_NPC:
            await ctx.send(item)

    @list.command()
    async def ITEM(self, ctx):
        for item in dict_ITEM:
            await ctx.send(item)

def setup(bot):
    bot.add_cog(List(bot))
