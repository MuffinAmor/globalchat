import asyncio
import json
import os

import discord
from discord.ext import commands

from lib.CacheHandler import channels, full_rank_check

default_prefix = "l!"

intents = discord.Intents()
intents.message_content = True
intents.guild_messages = True
intents.messages = True
intents.guilds = True
with open("config.json") as fp:
    data = json.load(fp)


def Lol(bot, message):
    if os.path.isfile("prefix.json"):
        with open("prefix.json") as f:
            prefixes = json.load(f)
        try:
            return prefixes.get(str(message.guild.id), default_prefix)
        except KeyError:
            return default_prefix

    else:
        prefixes = {}
        with open("prefix.json", "w") as f:
            json.dump(prefixes, f, indent=4)
        return default_prefix


bot = commands.Bot(command_prefix=Lol, intents=intents)

TOKEN = data["token"]

botcolor = 0xffffff

bot.remove_command('help')
########################################################################################################################

extensions = ['commands.AdminCommands', 'commands.RoleCommands', 'commands.UserCommands',
              'commands.ModerationCommands', 'commands.Commands', 'commands.chat']


# ['commands.clean']


@bot.event
async def on_ready():
    if bot.auto_sync_commands:
        await bot.sync_commands()
    print('--------------------------------------')
    print('Bot is ready.')
    print('Eingeloggt als')
    print(bot.user.name)
    print(bot.user.id)
    channels()
    full_rank_check()
    await status_task()


########################################################################################################################
async def status_task():
    await bot.change_presence(
        activity=discord.Activity(name='everbody do the flop!', type=discord.ActivityType.watching))


########################################################################################################################
@bot.command()
@commands.has_permissions(administrator=True)
async def prefix(ctx, prefix):
    with open("prefix.json", "r") as f:
        prefixes = json.load(f)
    try:
        del prefixes[str(ctx.guild.id)]
    except KeyError:
        pass
    prefixes[ctx.guild.id] = prefix
    with open("prefix.json", "w") as f:
        json.dump(prefixes, f, indent=4)
    await ctx.send("Your Prefix has been changed to {}".format(prefix))


@bot.command()
@commands.is_owner()
async def reloadall(ctx):
    for extension in extensions:
        try:
            bot.unload_extension(extension)
            bot.load_extension(extension)
            await ctx.send("{} has been reloaded".format(extension))
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))


@bot.command()
@commands.is_owner()
async def goodnight(ctx):
    await ctx.channel.send("Sleep well")
    await bot.close()


@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    try:
        bot.load_extension(extension)
        print('{} wurde geladen.'.format(extension))
        embed = discord.Embed(
            title='{} wurde geladen.'.format(extension),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nicht geladen werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht geladen werden. [{}]'.format(extension, error),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


########################################################################################################################
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    try:
        bot.unload_extension(extension)
        print('{} wurde deaktiviert.'.format(extension))
        embed = discord.Embed(
            title='{} wurde deaktiviert.'.format(extension),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()
    except Exception as error:
        print('{} konnte nich deaktiviert werden. [{}]'.format(extension, error))
        embed = discord.Embed(
            title='{} konnte nicht deaktiviert werden. [{}]'.format(extension, error),
            color=ctx.author.color
        )
        msg = await ctx.channel.send(embed=embed)
        await asyncio.sleep(5)
        await msg.delete()


########################################################################################################################
@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    try:
        bot.unload_extension(extension)
        bot.load_extension(extension)
        await ctx.channel.send('{} wurde neu geladen.'.format(extension))
    except Exception as error:
        await ctx.channel.send('{} konnte nicht geladen werden. [{}]'.format(extension, error))


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))
        else:
            print(f"{extension} wurde geladen")
    # asyncio.run(ApplicationCommandMixin().sync_commands())

    bot.run(TOKEN)
