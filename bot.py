import discord
from discord.ext import commands
import asyncpg
import asyncio
import json
import pickle


bot = commands.Bot(command_prefix = '$')
startup_extensions = ['read', 'list', 'add']
dane_log = json.load("dane.json")
bot_id = pickle.load(open("id", "rb"))

@bot.event
async def on_ready():
    print('Jesteśmy zalogowani jako {0.user}'.format(bot))


if __name__ == '__main__':
    for extension in startup_extensions:
        bot.load_extension(extension)
    bot.run(bot_id, bot=True, reconnect = True)
