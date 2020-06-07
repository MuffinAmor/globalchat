import discord
from discord.ext import commands
import asyncio
import sys
import aiohttp
from datetime import datetime

TOKEN = ''

bot = commands.Bot(command_prefix='ng!')

botcolor = 0xffffff

bot.remove_command('help')
########################################################################################################################

extensions = ['commands.help', 'commands.auto', 'commands.chat', 'commands.cmd', 'commands.owner', 'commands.servers', 'commands.ping', 'commands.game', 'commands.target', 'commands.mod', 'commands.warn']

@bot.event
async def on_ready():
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------------------------------')
    bot.loop.create_task(status_task())
########################################################################################################################			
async def status_task():
    while True:
        user = sum(len(s.members) for s in bot.guilds)
        servers = list(bot.guilds)
        await bot.change_presence(activity=discord.Game('ng!help | Lucy'), status=discord.Status.online)
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game('On Tour', type=3), status=discord.Status.do_not_disturb)
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game('ng!help | Lucy'), status=discord.Status.online)
        await asyncio.sleep(15)
        await bot.change_presence(activity=discord.Game('with {0} server'.format(str(len(servers))), type=3), status=discord.Status.do_not_disturb)
        await asyncio.sleep(15)
       
########################################################################################################################
@bot.command(pass_context=True)
async def goodnight(ctx):
    if ctx.author.id==474947907913515019:  
        await ctx.channel.send("Sleep well")
        await bot.logout()

		
@bot.command(pass_context=True)
async def load(ctx, extension):
    if ctx.author.id==474947907913515019:
        try:
            bot.load_extension(extension)
            print('{} wurde geladen.'.format(extension))
            embed = discord.Embed(
                title='{} wurde geladen.'.format(extension),
                color=botcolor
            )
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))
            embed = discord.Embed(
                title='{} konnte nicht geladen werden. [{}]'.format(extension, error),
                color=botcolor
            )
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()
    else:
        await ctx.channel.send('Sorry, but only the Botowner can use this command')
########################################################################################################################
@bot.command(pass_context=True)
async def unload(ctx, extension):
    if ctx.author.id==474947907913515019:
        try:
            bot.unload_extension(extension)
            print('{} wurde deaktiviert.'.format(extension))
            embed = discord.Embed(
                title='{} wurde deaktiviert.'.format(extension),
            color=botcolor
            )
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()
        except Exception as error:
            print('{} konnte nich deaktiviert werden. [{}]'.format(extension, error))
            embed = discord.Embed(
                title='{} konnte nicht deaktiviert werden. [{}]'.format(extension, error),
            color=botcolor
            )
            msg = await ctx.channel.send(embed=embed)
            await asyncio.sleep(5)
            await msg.delete()
    else:
        await ctx.channel.send('Sorry, but only the Botowner can use this command')
########################################################################################################################
@bot.command(pass_context=True)
async def reload(ctx, extension):
    if ctx.author.id==474947907913515019:
        try:
            bot.unload_extension(extension)
            bot.load_extension(extension)
            await ctx.channel.send('{} wurde neu geladen.'.format(extension))
        except Exception as error:
            await ctx.channel.send('{} konnte nicht geladen werden. [{}]'.format(extension, error))
    else:
        await ctx.channel.send('Sorry, but only the Botowner can use this command')
########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))

bot.run(TOKEN)

