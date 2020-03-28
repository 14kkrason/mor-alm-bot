import discord
from discord.ext import commands
from data import dict_PC, dict_NPC, dict_ITEM

class Read(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #read command and it's subcommands with dictionaries
    @commands.group()
    async def read(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Invalid command - no type detected.')

    @read.command()
    async def PC(self, ctx, arg):
        if(arg in dict_PC):
            character = dict_PC[arg]
            for name in character:
                item = character[name]
                await ctx.send(name + ': ' + item)
        else:
            await ctx.send('Invalid command - {0} is not in the database of PCs.'.format(arg))

    @read.command()
    async def NPC(self, ctx, arg):
        if(arg in dict_NPC):
            character = dict_NPC[arg]
            for name in character:
                item = character[name]
                await ctx.send(name + ': ' + item)
        else:
            await ctx.send('Invalid command - {0} is not in the database of NPCs.'.format(arg))

    @read.command()
    async def ITEM(self, ctx, arg):
        if(arg in dict_ITEM):
            items = dict_ITEM[arg]
            for name in items:
                item = items[name]
                await ctx.send(name + ': ' + item)
        else:
            await ctx.send('Invalid command - {0} is not in the database of ITEMs.'.format(arg))

def setup(bot):
    bot.add_cog(Read(bot))
