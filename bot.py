import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '$')

@bot.event
async def on_ready():
    print('Jesteśmy zalogowani jako {0.user}'.format(bot))

#list command and it's subcommands with dictionaries
@bot.group()
async def list(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid command - no type detected.')

@list.command()
async def PC(ctx):
    for item in dict_PC:
        await ctx.send(item)

@list.command()
async def NPC(ctx):
    for item in dict_NPC:
        await ctx.send(item)

#read command and it's subcommands with dictionaries
@bot.group()
async def read(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Invalid command - no type detected.')

@read.command()
async def PC(ctx, arg):
    if(arg in dict_PC):
        character = dict_PC[arg]
        for name in character:
            item = character[name]
            await ctx.send(name + ': ' + item)
    else:
        await ctx.send('Invalid command - {0} is not in the database.'.format(arg))

@read.command()
async def NPC(ctx, arg):
    if(arg in dict_NPC):
        character = dict_NPC[arg]
        for name in character:
            item = character[name]
            await ctx.send(name + ': ' + item)
    else:
        await ctx.send('Invalid command - {0} is not in the database of NPCs.'.format(arg))

dict_PC = {
'Tuto': {'Name': 'Tuto Shakamaka','Race': 'Human (islander)' , 'Class': 'Wizard, Evoker', 'Level': '5', 'Birthplace': 'Manganium Isle', 'Type': 'Player Character'},
'Jocko': {'Name': 'Jocko Willink','Race': 'Lighfoot Halfling', 'Class': 'Bard, Collage of Lore', 'Level': '5', 'Birthplace': 'Dora, Kałuża', 'Type': 'Player Character'},
'Or': {'Name': 'Or of Burning Fists', 'Class': 'Barbarian, Berserker', 'Level': '5', 'Birthplace': 'Rogh', 'Type': 'Player Character'},
'Marmarel': {'Name': 'Marmarel, son of Maglor', 'Class': 'Ranger, Monster Slayer', 'Level': '5', 'Birthplace': 'Fidhail', 'Type': 'Player Character'}
}

dict_NPC = {
'Kazamakuz': {'Name': 'Kazamakuz','Race': 'Cat (cursed)' ,'Profesion': 'Wizard (archmage), shopkeeper', 'Origin': 'Mor-Alm','Status': 'Alive', 'Type': 'NPC'},
'Snigbat': {'Name': 'Snigbat', 'Race': 'Goblin', 'Profesion': 'Rogue, Scout, Guide', 'Origin': 'Synn Gwaetal', 'Status': 'Alive','Type': 'NPC'},
'Gahnir': {'Name': 'Gahnir Toriar', 'Race': 'Dragonborn', 'Profesion': 'Eldritch Knight, House of Dragons chief warrior', 'Origin': 'Mor-Alm', 'Status': 'Alive' ,'Type': 'NPC'},
'Feice': {'Name': 'Feice Abeilar', 'Race': 'Human (Mor-Almian)', 'Profesion': 'Wizard (prearchmage)', 'Origin': 'Mor-Alm','Status': 'Alive' , 'Type': 'NPC'},
'Azaelia': {'Name': 'Azaelia Harthimar', 'Race': 'Succubus', 'Profesion': 'Unknown, sorcerer', 'Origin': 'Probably Nine Hells', 'Status': 'Deceased - physical form destroyed by Marmarel in Lop Gollos' ,'Type': 'NPC'},
'Iankur': {'Name': 'Iankur Getzbech', 'Race': 'Gnome', 'Profesion': 'Artificer, inventor', 'Origin': 'Free City of Digrorn', 'Status': 'Deceased - killed by falling rocks while fighting chieftain of The Blood Of The Forest orc tribe' ,'Type': 'NPC'},
'Yungrek': {'Name': 'Yungrek (reffered to)', 'Race': 'Dragon (color unknown)', 'Profesion': 'unknown', 'Origin': 'Unknown', 'Status': 'Alive'},
'Marvin': {'Name': 'Marvin Buyoe', 'Race': 'Half-orc', 'Profesion': 'Cartographer', 'Origin': 'Unknown, lived in Liliangaard', 'Status': 'Deceased - killed by Marmarel in Lop Gollos' ,'Type': 'NPC'}
}

bot.run('NjkyNjYyMDkyMDE2Mzg2MDU5.XnxyDg.MWY0OtqZxm8kOYvlVCgoQHW-r9A')
