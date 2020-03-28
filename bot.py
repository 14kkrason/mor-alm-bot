#import sys, traceback
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '$')

startup_extensions = ['read', 'list']

@bot.event
async def on_ready():
    print('Jesteśmy zalogowani jako {0.user}'.format(bot))


if __name__ == '__main__':
    for extension in startup_extensions:
        bot.load_extension(extension)
    bot.run('NjkyNjYyMDkyMDE2Mzg2MDU5.XnxyDg.MWY0OtqZxm8kOYvlVCgoQHW-r9A', bot=True, reconnect = True)
