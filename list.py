import discord
from discord.ext import commands
import asyncio
import asyncpg
from bot import dane_log



class List(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    #grupa komend
    @commands.group()
    async def list(self, ctx):
        ''' '''

     #komendy 
    @list.command()
    async def PC(self, ctx):
        conn = await asyncpg.connect(**dane_log)
        


def setup(bot):
    bot.add_cog(List(bot))
