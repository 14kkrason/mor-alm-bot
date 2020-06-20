import discord
from discord.ext import commands
import asyncio
import asyncpg
from bot import dane_log

class Read(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.group()
    async def read(self, ctx):
       ''' '''

    @read.command()
    async def PLACE(self, ctx, _name):
        conn = await asyncpg.connect(**dane_log)
        data_place = await conn.fetchrow('SELECT name, description FROM PLACE WHERE name=$1', _name)
        tags = ('Nazwa: ', 'Opis: ')
        if(data_place is not None):
            for i in range(len(data_place)):
                await ctx.send(tags[i] + data_place[i])
        else:
            await ctx.send(f'{_name} nie jest w bazie danych.')
        await conn.close()

    @read.command()
    async def ORGANIZATION(self, ctx, _name):
        conn = await asyncpg.connect(**dane_log)
        data_org_tup = await conn.fetchrow('SELECT name, origin, description FROM ORGANIZATION WHERE name=$1', _name)
        tags = ('Nazwa: ', 'Miejsce: ' ,'Opis: ')
        val = await conn.fetchval('SELECT place.name FROM place WHERE id=$1', data_org_tup[1]) 
        data_org = (data_org_tup[0], val, data_org_tup[2])
        if(data_org is not None):
            for i in range(len(data_org)):
                await ctx.send(tags[i] + data_org[i])
        else:
            await ctx.send(f'{_name} nie jest w bazie danych.')
        await conn.close()

    @read.command()
    async def PC(self, ctx, _name):
        conn = await asyncpg.connect(**dane_log)
        data_org_tup = await conn.fetchrow('SELECT name, race, class, subclass, level,  origin, description, affiliation FROM pc_npc WHERE name=$1', _name)
        cl_name = await conn.fetchval('SELECT class.name FROM class WHERE id=$1', data_org_tup[2]) 
        scl_name = await conn.fetchval('SELECT class.name FROM class WHERE id=$1', data_org_tup[3])
        origin_name = await conn.fetchval('SELECT place.name FROM place WHERE id=$1', data_org_tup[5])
        aff_name = await conn.fetchval('SELECT organization.name FROM organization WHERE id=$1', data_org_tup[7])
        tags = ('Imie: ', 'Rasa: ', 'Klasa: ', 'Subklasa: ', 'Poziom: ', 'Pochodzenie: ', 'Opis: ', 'Związany z: ')
        data_org = (data_org_tup[0], data_org_tup[1], cl_name, scl_name, str(data_org_tup[4]), origin_name, data_org_tup[6], aff_name)
        if(data_org is not None):
            for i in range(len(data_org)):
                await ctx.send(tags[i] + data_org[i])
        else: 
            await ctx.send(f'{_name} nie jest w bazie danych.')
        await conn.close()


    #wymaga testów
    @read.command()
    async def NPC(self, ctx, _name):
        conn = await asyncpg.connect(**dane_log)
        data_org_tup = await conn.fetchrow('SELECT name, race, origin, description, affiliation FROM pc_npc WHERE name=$1', _name)
        origin_name = await conn.fetchval('SELECT place.name FROM place WHERE id=$1', data_org_tup[2])
        aff_name = await conn.fetchval('SELECT organization.name FROM organization WHERE id=$1', data_org_tup[3])
        data_org = (data_org_tup[0], data_org_tup[1], origin_name, data_org_tup[3], aff_name)
        tags = ('Imie: ', 'Rasa: ', 'Pochodzenie: ', 'Opis: ', 'Związany z: ')

        if(data_org is not None):
            for i in range(len(data_org)):
                await ctx.send(tags[i] + data_org[i])
        else:
            await ctx.send(f'{_name} nie jest w bazie danych.')
        await conn.close()


def setup(bot):
    bot.add_cog(Read(bot))
