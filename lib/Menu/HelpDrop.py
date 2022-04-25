import discord
import discord.ui

from Menu.Options import HelpMenuContent as HMC
from lib.CacheHandler import config


class Dropdown(discord.ui.Select):
    def __init__(self):
        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(
                label="Allgemein", description=HMC.normal_desc, emoji="📄"
            ),
            discord.SelectOption(
                label="Setup", description=HMC.setup_desc, emoji="🛠"
            ),
            discord.SelectOption(
                label="Administration", description=HMC.admin_desc, emoji="💻"
            ),
            discord.SelectOption(
                label="Moderation", description=HMC.mod_desc, emoji="🛡"
            ),
            discord.SelectOption(
                label="Anime", description=HMC.anime_desc, emoji="🔬"
            ),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(
            placeholder="Bitte wähle eine Kategorie aus",
            min_values=1,
            max_values=1,
            options=options,
        )

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        output = self.values[0]
        if output == "Allgemein":
            embed = discord.Embed(title="📄 Allgemeine commands", color=discord.Color(config()["color"]))
            embed.add_field(
                name="public_list",
                value="Liste alle öffentlichen Chaträume auf!"
            )
            embed.add_field(
                name="info",
                value="Lasse dir Infos über einen Chatraum ausgeben."
            )
            embed.add_field(
                name="botinfo",
                value="Lasse dir Infos über den Bot anzeigen",
                inline=False
            )
            embed.add_field(
                name="channelinfo",
                value="Lasse dir Infos über einen Channel ausgeben",
                inline=False
            )

        elif output == "Setup":
            embed = discord.Embed(title="🛠 Setup commands", color=discord.Color(config()["color"]))
            embed.add_field(
                name="register",
                value="Registriere dich, um deine Daten in unsere Datenbank eintragen zu lassen\n"
                      "Weitere Infos findest du vorerst auf unserem [Supportserver](https://discord.gg/ezz6JMxcRz)",
                inline=False)
            embed.add_field(
                name="unregister",
                value="coming soon",
                inline=False
            )
            embed.add_field(
                name="create_room",
                value="Erstelle einen Chatraum, den du eigenständig verwalten kannst.",
                inline=False
            )
            embed.add_field(
                name="delete_room",
                value="Lösche deinen Chatraum wieder",
                inline=False
            )
            embed.add_field(
                name="add_channel",
                value="Füge TextChannel zu deinem Chatraum hinzu, um untereinander zu chatten",
                inline=False
            )
            embed.add_field(
                name="remove_channel",
                value="Entferne einen TextChannel aus einem Chatraum.",
                inline=False
            )
        elif output == "Administration":
            embed = discord.Embed(title="/admin commands", description="Benötigt Chatraum Administrations Rechte.",color=discord.Color(config()["color"]))
            embed.add_field(name="add_mod",
                            value="Ernenne Moderatoren für deinen Chatraum",
                            inline=False)
            embed.add_field(name="remove_mod",
                            value="Entferne Moderatoren aus deinem Chatraum",
                            inline=False)
            embed.add_field(name="make_public",
                            value="Öffne deinen Chatraum für jeden, der beitreten will!",
                            inline=True)
            embed.add_field(name="undo_public",
                            value="Stelle deinen Chatraum wieder in den Privaten Modus.",
                            inline=True)
            embed.add_field(name="room_setup",
                            value="Setze ein Thema und eine Beschreibung für deinen Chatraum!",
                            inline=False)
        elif output == "Moderation":
            embed = discord.Embed(title="/mod commands",
                                  description="Benötigt Chatraum Admin oder Moderator Rechte.")

            embed.add_field(
                name="delete",
                value="Lösche eine Chatnachricht",
                inline=False
            )
            embed.add_field(
                name="slowmode",
                value="Stelle den Slowmode für deinen Chatraum ein",
                inline=False
            )
            embed.add_field(
                name="add_word",
                value="Füge ein Wort deiner Chatraum Blacklist hinzu",
                inline=False
            )
            embed.add_field(
                name="remove_word",
                value="Entferne ein Wort aus deiner Chatraum Blacklist",
                inline=False
            )
            embed.add_field(
                name="blacklist",
                value="Lasse dir die Blacklist deines Chatraums zukommen",
                inline=False
            )
            embed.add_field(
                name="ban",
                value="Banne Leute aus deinem Chatraum",
                inline=False
            )
            embed.add_field(
                name="unban",
                value="Hebe banns wieder auf",
                inline=False
            )
            embed.add_field(
                name="banlist",
                value="Lasse dir eine Liste von Leuten geben, die aus deinem Chatraum gebannt worden sind.",
                inline=False
            )
        elif output == "Anime":
            embed = discord.Embed(title="/anime commands", color=discord.Color(config()["color"]))
            embed.add_field(
                name="kiss",
                value="Verteile deine Zuneigung",
                inline=False
            )
            embed.add_field(
                name="hug",
                value="Umarme jemanden",
                inline=False
            )
            embed.add_field(
                name="bite",
                value="Knabbere deine Mitmenschen an",
                inline=False
            )
            embed.add_field(
                name="pat",
                value="Verteile Streicheleinheiten",
                inline=False
            )
            embed.add_field(
                name="slap",
                value="Hau drauf!",
                inline=False
            )
            embed.add_field(
                name="purr",
                value="Sei eine Katze!",
                inline=False
            )
        else:
            embed = discord.Embed(title="anderes", color=discord.Color(config()["color"]))
        await interaction.message.edit(embed=embed)


class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(Dropdown())
