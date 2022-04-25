import discord
from discord.ui import InputText, Modal

from lib.CacheHandler import room, SomeFreeSpace
from lib.RoomHandler import RoomDecorator


class MyModal(Modal):
    def __init__(self, name):
        super().__init__(f"Willkommen im Setup für \n{name}")
        self.name = name
        self.add_item(
            InputText(
                label="Thema deines Chatraums:",
                value=SomeFreeSpace(self.name).get_topic(),
                placeholder="Gaming, WWO, WOW, Chatten"
            )
        )

        self.add_item(
            InputText(
                label="Sprache in deinem Chatraum:",
                value=SomeFreeSpace(self.name).get_language(),
                placeholder="Deutsch, Englisch, Klingonisch"
            )
        )

        self.add_item(
            InputText(
                label="Beschreibung deines Chatraums:",
                value=SomeFreeSpace(self.name).get_description(),
                placeholder="Wir chatten und essen Kekse",
                style=discord.InputTextStyle.short,
            )
        )

    async def callback(self, interaction: discord.Interaction):
        RoomDecorator(self.name, self.children[0].value).edit_topic()
        RoomDecorator(self.name, self.children[1].value).edit_language()
        RoomDecorator(self.name, self.children[2].value).edit_description()
        room.cache_clear()
        embed = discord.Embed(title=f"Infos über: {self.name}", color=0x00FF00)
        embed.add_field(name="Sprache:", value=self.children[1].value, inline=False)
        embed.add_field(name="Thema deines Chatraums:", value=self.children[0].value, inline=False)
        embed.add_field(name="Beschreibung:", value=self.children[2].value)
        await interaction.response.send_message(embeds=[embed])
