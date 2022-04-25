import datetime
import random
import string
import time
from datetime import datetime

import discord
from discord.ext import commands

from lib.CacheHandler import message_cache, full_rank_check, channels, users, check_for_word

'''elif user_id in room_cache["roles"]["user"]:
    role_icon = ""
    color = ""'''


class ChatClass(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.time_cache = {}

    def random_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=8))

    def get_time(self, user_id: int):
        if user_id in self.time_cache:
            return self.time_cache[user_id]

    def edit_time(self, user_id):
        self.time_cache[user_id] = time.time()

    def edit_message(self, token, message_id: dict, author_id: int, author_name: str, timestamp):
        message_cache[token] = {
            'author_id': author_id,
            'author_name': author_name,
            'timestamp': timestamp,
            'messages': message_id
        }

    async def embed_builder(self, message, token):
        print(message.content)
        user_id = message.author.id
        user_cache = full_rank_check()[message.author.id]
        if "banned" in user_cache:
            return
        if "owner" in user_cache:
            role_icon = "👑"
            color = 0x0000FF
        elif "admin" in user_cache:
            role_icon = "🛡"
            color = 0x00FF00
        elif "team" in user_cache:
            role_icon = "🛡"
            color = 0x00FF00
        elif "moderator" in user_cache:
            role_icon = "🛡"
            color = 0x00FF00
        elif "partner" in user_cache:
            role_icon = "🛡"
            color = 0x00FF00
        elif "vip" in user_cache:
            role_icon = "🛡"
            color = 0x00FF00
        else:
            color = 0x808080
            role_icon = "🕯"

        website = ""
        support = "https://discord.gg/ezz6JMxcRz"
        embed = discord.Embed(description="\n" +
                                          message.content[0:800] +
                                          f"\n\n [Support]({support})",
                              color=color)
        if message.guild.icon:
            embed.set_footer(icon_url=message.guild.icon, text=message.guild.name + " | " + token)
        else:
            embed.set_footer(text=message.guild.name + " | " + token)

        embed.set_thumbnail(url=message.author.avatar)
        embed.set_author(name=f"{role_icon} | {message.author}")
        if len(message.attachments) != 0:
            ends = [".jpg", ".jpeg", ".jfif", ".png", ".gif"]
            for pic in message.attachments:
                for end in ends:
                    if pic.filename.endswith(end):
                        embed.set_image(url=pic.url)
        embed.timestamp = datetime.utcnow()
        return embed

    @commands.Cog.listener()
    async def on_message(self, message):
        print(message.content)
        if not message.author.bot:
            room = channels()
            if room:
                if message.author.id not in users():
                    await message.channel.send("Bitte registriere dich mit /register.", delete_after=10)
                else:
                    print(["Sending: " + message.content])
                    await self.sending(message, room)  # system cache ist ne json

    async def sending(self, message):
        token = self.random_id()
        embed = await self.embed_builder(message, token)
        if embed:
            blacklist = check_for_word(message.content.split(" "))

            user_time = self.get_time(message.author.id)
            if user_time:
                try:
                    t = round(time.time() - float(user_time))
                except TypeError:
                    t = channel_cache["spam"]

                if round(t) < channel_cache["spam"]:
                    try:
                        await message.delete()
                    except PermissionError:
                        pass
                    await message.channel.send("Du bist zu schnell", delete_after=5)
                    return
            if blacklist:
                await message.channel.send("Eins deiner Wörter war wohl auf der Blacklist.", delete_after=5)
                return
            else:
                self.edit_time(message.author.id)
                message_list = {}
                for i in channel_cache["channel"]["data"]:
                    channel = self.bot.get_channel(i)
                    if channel:
                        if not channel == message.channel:
                            try:
                                end_message = await channel.send(embed=embed)
                                message_list[i] = end_message.id
                            except PermissionError:
                                pass
                emote = "✅"
                await message.add_reaction(emote)
                self.edit_message(token, message_list, message.author.id, message.author.name,
                                  datetime.utcnow())


def setup(bot):
    bot.add_cog(ChatClass(bot))
