from check import is_dev
from check import get_credits
from check import user_add_credits
from check import user_remove_credits
import discord
from discord.ext import commands
import asyncio
import sys
import random
from discord.ext.commands import CommandNotFound
from datetime import datetime
import json
import os


os.chdir(r'/home/niko/bot/rankdata')

bot = commands.Bot(command_prefix='ng!')

botcolor = 0x000ffc

bot.remove_command('help')

class minigames(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(3, 30, commands.BucketType.user)
    async def slots(self, ctx, money:int):
        try:
            credits = get_credits(str(ctx.author.id))
            if money > credits:
                await ctx.channel.send('{} haven´t enough Credits to do that.'.format(ctx.author.mention))
            elif money > 501:
                await ctx.channel.send('{} 500 Credits as deployment is limit for that game'.format(ctx.author.mention))
            else:
                await ctx.channel.send('If two emoijs are the same you win....\n')
                await asyncio.sleep(0.5)
		    
                slots =['bus', 'train', 'horse', 'tiger', 'monkey', 'cow', 'sailboat', 'blue_car', 'goat']
                slot1 = slots[random.randint(0, 8)]
                slot2 = slots[random.randint(0, 8)]
                slot3 = slots[random.randint(0, 8)]
		    
                slotOutput = '| :{}: | :{}: | :{}: |\n'.format(slot1, slot2, slot3)
		    
                if slot1 == slot2 == slot3:
                    await asyncio.sleep(2)
                    win = money*3
                    await ctx.channel.send("{}\n Jackpot!!!!, You won {} Credits.".format(slotOutput, win)) #(bei X würd ich das geld einsetzten)
                    user_add_credits(str(ctx.author.id), win)
		    
                elif slot1 == slot2:
                    await asyncio.sleep(2)
                    win = money*2
                    await ctx.channel.send("{}\nYou won {} Credits.".format(slotOutput, win)) #Hier auch
                    user_add_credits(str(ctx.author.id), win)
		    
                elif slot2 == slot3:
                    await asyncio.sleep(2)
                    win = money*2
                    await ctx.channel.send("{}\nYou won {} Credits.".format(slotOutput, win)) #Hier auch
                    user_add_credits(str(ctx.author.id), win)
		    
                elif slot1 == slot3:
                    await asyncio.sleep(2)
                    win = money*2
                    await ctx.channel.send("{}\nYou won {} Credits.".format(slotOutput, win)) #Hier auch
                    user_add_credits(str(ctx.author.id), win)
		    
                else:
                    await asyncio.sleep(2)
                    await ctx.channel.send("{}\nYou lost {} Credits".format(slotOutput, money)) #Hier auch
                    user_remove_credits(str(ctx.author.id), money)
        except KeyError:
            await ctx.send("Ops you are not in the Database :O")

    @commands.command()
    @is_dev()
    async def give_credits(self, ctx, user:discord.User, money:int):
        user_add_credits(str(user.id), money)
        await ctx.channel.send("Hey{}, {} give you {} Credits.".format(user.mention, ctx.author.name, money))
				
			
			

def setup(bot):
    bot.add_cog(minigames(bot))