import discord
from discord.ext import commands
import asyncio
import asyncpg
from bot import dane_log


class Add(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def add(self, ctx):
        ''' '''


    #add exception handling - one can get many errors in these functions
    @add.command()
    async def PLACE(self, ctx, _name, _desc):
        conn = await asyncpg.connect(**dane_log)
        check_If_Exists = await conn.fetchval('''SELECT place.name FROM PLACE WHERE name=$1;''', _name)
        if(check_If_Exists is None and _desc is not None):
            await conn.execute('INSERT INTO place(name, description) VALUES($1, $2);', _name, _desc)
            await ctx.send('{0} zostało dodane do bazy danych'.format(_name))
        else:
            await ctx.send('{0} nie zostało dodane do bazy danych, ponieważ już w niej jest (lub nie dałeś opisu!). Chcesz sprawdzić? Wpisz $read PLACE "{0}"'.format(_name))
        await conn.close()

    @add.command()
    async def ORGANIZATION(self, ctx, name, origin, description):
        conn = await asyncpg.connect(**dane_log)
        try:
            id_place = await conn.fetchval('''SELECT place.id FROM PLACE WHERE name=$1;''', origin)
            if(id_place is not None):
                await conn.execute('''INSERT INTO organization(name, origin, description) VALUES ($1, $2, $3);''', name, id_place ,description)
                await ctx.send(f'{name} zostało dodane do bazy danych.')
        except Exception as ex:
            await ctx.send(f'{ex} - spróbuj jeszcze raz lub skontaktuj się z devem.')
            pass
        finally:
            await conn.close()

    @add.command()
    async def PC(self, ctx, _name, _race, class_name, subclass_name, _level, origin, desc, affiliation):
        conn = await asyncpg.connect(**dane_log)
        check_If_Exists_name = await conn.fetchval('''SELECT pc_npc.name FROM PC_NPC WHERE name=$1;''', _name)
        class_id = await conn.fetchval('''SELECT class.id FROM CLASS WHERE name=$1;''', class_name)
        subclass_id = await conn.fetchval('''SELECT class.id FROM CLASS WHERE name=$1;''', subclass_name)
        place_id = await conn.fetchval('''SELECT place.id FROM PLACE WHERE name=$1;''', origin)
        affiliation_id = await conn.fetchval('''SELECT organization.id FROM ORGANIZATION WHERE name=$1''', affiliation)

        if(check_If_Exists_name is None and place_id is not None and affiliation_id is not None):
            await conn.execute('''INSERT INTO pc_npc(is_pc, name, race, class, subclass, level, origin, description, affiliation) VALUES($1, $2, $3, $4, $5, $6, $7, $8, $9)''', True, _name, _race, class_id, subclass_id, int(_level), place_id, desc, affiliation_id)
            await ctx.send(f'{_name} został dodany do bazy danych.')
        else:
            await ctx.send('{0} nie został dodany do bazy danych, ponieważ albo już w niej jest, albo miejsce z którego jest się w niej nie znajduje. Sprawdź to!'.format(_name))
        await conn.close()

    @add.command()
    async def NPC(self, ctx, _name, _race, origin, desc, affiliation):
        conn = await asyncpg.connect(**dane_log)
        is_in_db = await conn.fetchval('''SELECT pc_npc.name FROM PC_NPC WHERE name=$1;''', _name)
        place_id = await conn.fetchval('''SELECT place.id FROM PLACE WHERE name=$1;''', origin)
        affiliation_id = await conn.fetchval('''SELECT organization.id FROM ORGANIZATION WHERE name=$1''', affiliation)
        try:
            if(is_in_db is None):
                await conn.execute('''INSERT INTO pc_npc(is_pc, name, race, origin, description, affiliation) 
                VALUES($1, $2, $3, $4, $5, $6) ''', False, _name, _race, place_id, desc, affiliation_id)
                await ctx.send(f'{_name} został dodany do bazy danych.') 
            else:
                await ctx.send(f'{_name} nie został dodany do bazy danych, ponieważ już w niej jest. Chcesz sprawdzić?')
        except Exception as ex:
            await ctx.send(f'{ex}! Spróbuj jeszcze raz.')
            pass
        finally:
            await conn.close()

    @add.command()
    async def ITEM(self, ctx, _name, desc, who, _where):
        conn = await asyncpg.connect(**dane_log)
        is_in_db = await conn.fetchval(''' SELECT item.name FROM ITEM WHERE name=$1''', _name)
        who_id = await conn.fetchval('''SELECT pc_npc.id FROM PC_NPC WHERE name=$1''', who)
        where_id = await conn.fetchval('''SELECT place.id FROM PLACE WHERE name=$1''', _where)
        try:
            if(is_in_db is None and who_id is not None and where_id is not None):
                await conn.execute('''INSERT INTO ITEM(name, description, id_who, id_where) 
                     VALUES($1, $2, $3, $4)''', _name, desc, int(who_id), int(where_id))
                await ctx.send(f'{_name} został dodany do bazy danych.')
            else:
                await ctx.send(f'{_name} nie został dodany przez złą komendę.')
        except Exception as ex:
            await ctx.send(f'{ex}! Spróbuj jeszcze raz.')
            pass
        finally:
            await conn.close()
            pass

    @add.command()
    async def HELP(self, ctx):
        await ctx.send('Dla add występują następujące subkomendy. Pamiętaj o nawiasach "" przy wpisywaniu danych!')
        await ctx.send('Dodanie miejsca: $add PLACE [nazwa] [opis]')
        await ctx.send('Dodanie organizacji: $add ORGANIZATION [Nazwa] [pochodzenie] [opis]')
        await ctx.send('Dodanie postaci gracza: $add PC [Imie] [Rasa] [Klasa] [Podklasa] [Poziom] [Pochodzenie] [Opis] [Powiązania (opcjonalne, ale wpisz "Brak" jeśli nie ma)]') 
        await ctx.send('Dodanie postaci niezaleznej: $add NPC [Imie] [Rasa] [Pochodzenie] [Opis] [Powiązania - jak wyżej]')
        await ctx.send('Dodanie przedmiotu: $add ITEM [Nazwa] [Opis] [Właściciel] [Pochodzenie]')
        await ctx.send('Pamiętaj o tym, aby wpisy do bazy danych były odpowiednio przypisane. Jest to wersja bota 1.0')



def setup(bot):
    bot.add_cog(Add(bot))
