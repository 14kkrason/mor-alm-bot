import os
import discord

client = discord.Client()

dict_PC = {
'Tuto': {'Name': 'Tuto Shakamaka', 'Class': 'Wizard, Evoker', 'Level': '5', 'Birthplace': 'Manganium Isle', 'Type': 'Player Character'},
'Jocko': {'Name': 'Jocko Willink', 'Class': 'Bard, Collage of Lore', 'Level': '5', 'Birthplace': 'Dora, Kałuża', 'Type': 'Player Character'},
'Or': {'Name': 'Or of Burning Fists', 'Class': 'Barbarian, Berserker', 'Level': '5', 'Birthplace': 'Rogh', 'Type': 'Player Character'},
'Marmarel': {'Name': 'Marmarel, son of Maglor', 'Class': 'Ranger, Monster Slayer', 'Level': '5', 'Birthplace': 'Fidhail', 'Type': 'Player Character'}
}

@client.event
async def on_ready():
    print('Jesteśmy zalogowani jako {0.user}'.format(client))

@client.event
async def on_message(message):
    if(message.author == client.user):
        return

    if(message.content.startswith('$read')):
        names = message.content.split()
        if(names[1] == 'PC'):
            if(len(names) > 3):
                await message.channel.send("Invalid syntax. Command contains unexpected syntax")
                return
            elif names[2] in dict_PC:
                character = dict_PC[names[2]]
            else:
                await message.channel.send("{0} has not been found in our database. Check your spelling or request this character added.".format(names[2]))
                return

            for cont in character:
                item = character[cont]
                await message.channel.send(cont + ': ' + item)
        else:
            await message.channel.send('Command incorrect. Maybe you lack a Type?')

    if(message.content.startswith('$help')):
        await message.channel.send('This bot is designed to print basic info about Mor-Alm campaign characters.')
        await message.channel.send('To access info about a character write: $read [type] [name]')
        await message.channel.send('To list items of chosen type, write: $list [type]')
        await message.channel.send('For now, you can only access player characters, so existing types are: PC')
        await message.channel.send('e.g $read PC "name of you character" without quotes or $list PC' )

    if(message.content.startswith('$list')):
        types = message.content.split()
        if(types[1] == 'PC'):
            if(len(types) <= 2):
                for cont in dict_PC:
                    await message.channel.send(cont)
            else:
                await message.channel.send('Invalid syntax. Command contains unexpected syntax.')
        else:
            await message.channel.send('No such type exists.')

client.run('NjkyNjYyMDkyMDE2Mzg2MDU5.XnxyDg.MWY0OtqZxm8kOYvlVCgoQHW-r9A')
